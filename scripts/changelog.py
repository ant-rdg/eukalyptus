#!/usr/bin/env python3
"""Régénère CHANGELOG.md à partir de la liste publique des versions d'Eukalyptus.

Sources (publiques, sans compte) :
  https://eukalyptus.app/api/v1/updates                    macOS
  https://eukalyptus.app/api/v1/updates?platform=windows   Windows

Usage (depuis la racine du dépôt) :
  python3 -I scripts/changelog.py              écrit CHANGELOG.md
  python3 -I scripts/changelog.py --stdout     affiche le résultat sans écrire de fichier

Les notes sont reprises telles que publiées (en français). Seule la mise en page change : une ligne
sans tiret devient un intertitre en gras, et des lignes vides sont ajoutées pour que Markdown affiche
correctement les listes. La liste publiée par le site ne contient que les versions rendues publiques.
"""

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://eukalyptus.app/api/v1/updates"
SOURCES = [("macOS", BASE), ("Windows", BASE + "?platform=windows")]
DOWNLOAD_PAGE = "https://eukalyptus.app/telecharger"
OUTPUT = Path(__file__).resolve().parent.parent / "CHANGELOG.md"

HEADER = """# Journal des versions

Ce fichier est généré par [`scripts/changelog.py`](scripts/changelog.py) à partir de la liste des versions publiée par
[eukalyptus.app](https://eukalyptus.app/notes-de-version) ; il ne se modifie pas à la main. Les notes sont celles des versions,
telles que publiées (en français). Le site reste la source de vérité des mises à jour de l'app.

- Téléchargement : [eukalyptus.app/telecharger](https://eukalyptus.app/telecharger) ou les [Releases](https://github.com/ant-rdg/eukalyptus/releases) de ce dépôt.
- Le site ne garde que le dernier installateur de chaque plateforme : pour une version plus ancienne, les empreintes SHA-256 ci-dessous
  permettent de vérifier un fichier que vous auriez déjà.
- Vérifier une empreinte : `shasum -a 256 <fichier>` (macOS) ou `Get-FileHash <fichier>` (Windows PowerShell).
- Les numéros de version de macOS et de Windows avancent chacun de leur côté : une même version peut ne pas exister sur les deux.
- English readers: the release notes are written in French; see [README.en.md](README.en.md).

"""


def fetch(url: str) -> list[dict]:
    request = urllib.request.Request(url, headers={"User-Agent": "eukalyptus-changelog/1", "Accept": "application/json"})
    try:
        response = urllib.request.urlopen(request, timeout=30)  # URL fixe, https, certificat vérifié
    except urllib.error.URLError as error:
        # Python installé depuis python.org n'a pas toujours de certificats racine : repli sur ceux du système (macOS, Linux).
        cafile = next((c for c in ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt") if Path(c).exists()), None)
        if not isinstance(error.reason, ssl.SSLCertVerificationError) or cafile is None:
            raise
        response = urllib.request.urlopen(request, timeout=30, context=ssl.create_default_context(cafile=cafile))
    with response:
        data = json.load(response)
    releases = data.get("releases")
    if not isinstance(releases, list):
        raise ValueError(f"réponse inattendue de {url}")
    return releases


def version_key(version: str) -> tuple:
    return tuple(int(part) if part.isdigit() else 0 for part in re.split(r"[.\-]", version))


def date_of(release: dict) -> str:
    stamp = release.get("publishedAt", "")
    try:
        return datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(timezone.utc).strftime("%Y-%m-%d")
    except ValueError:
        return stamp[:10]


def format_notes(notes: str) -> str:
    """Notes telles quelles ; seules les lignes vides et les intertitres en gras sont ajoutés pour Markdown."""
    lines = [line.rstrip() for line in notes.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    out: list[str] = []
    for line in lines:
        if not line.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        is_bullet = line.lstrip().startswith(("- ", "* "))
        if is_bullet:
            out.append(line)
        else:
            if out and out[-1] != "":
                out.append("")
            # Intertitre court (« Sécurité », « News : ») : en gras ; phrase : paragraphe.
            title = line.strip().rstrip(":").strip()
            out.append(f"**{title}**" if len(title) <= 40 and not title.endswith((".", "!", "?")) else line.strip())
            out.append("")
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


def render(by_version: dict[str, dict[str, dict]]) -> str:
    parts = [HEADER.rstrip() + "\n"]
    for version in sorted(by_version, key=version_key, reverse=True):
        platforms = by_version[version]
        parts.append(f"## {version}\n")
        for platform in ("macOS", "Windows"):
            release = platforms.get(platform)
            if release is None:
                continue
            parts.append(f"### {platform} ({date_of(release)})\n")
            notes = (release.get("notes") or "").strip()
            parts.append((format_notes(notes) if notes else "_Pas de notes publiées pour cette version._") + "\n")
            lines = [f"> Téléchargement : <{release.get('url') or DOWNLOAD_PAGE}>"]
            if release.get("sha256"):
                lines.append(f"> SHA-256 de l'installateur : `{release['sha256']}`")
            archive = release.get("archiveSHA256")
            if archive and archive != release.get("sha256"):
                lines.append(f"> SHA-256 de l'archive de mise à jour : `{archive}`")
            parts.append("  \n".join(lines) + "\n")
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Régénère CHANGELOG.md depuis l'API publique des versions.")
    parser.add_argument("--stdout", action="store_true", help="affiche le résultat au lieu d'écrire CHANGELOG.md")
    args = parser.parse_args()
    by_version: dict[str, dict[str, dict]] = {}
    for platform, url in SOURCES:
        for release in fetch(url):
            by_version.setdefault(str(release["version"]), {})[platform] = release
    text = render(by_version)
    if args.stdout:
        sys.stdout.write(text)
    else:
        OUTPUT.write_text(text, encoding="utf-8")
        print(f"{OUTPUT} écrit : {len(by_version)} versions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
