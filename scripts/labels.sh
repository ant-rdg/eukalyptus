#!/usr/bin/env bash
# Crée (ou met à jour) les étiquettes décrites dans .github/labels.yml, via l'API GitHub.
#
# Usage :
#   read -rs GITHUB_TOKEN && export GITHUB_TOKEN     # saisie masquée, jamais écrite dans un fichier
#   scripts/labels.sh                                # dépôt ant-rdg/eukalyptus
#   scripts/labels.sh --dry-run                      # affiche ce qui serait fait, sans appeler l'API ni lire le jeton
#   GITHUB_REPO=autre/depot scripts/labels.sh
#
# Le jeton (variable GITHUB_TOKEN) doit avoir le droit d'écrire sur les issues du dépôt (jeton à granularité fine :
# « Issues : lecture et écriture » ; jeton classique : portée « public_repo »).
# Rien n'est jamais supprimé : une étiquette absente de labels.yml reste en place.

set -euo pipefail

REPO="${GITHUB_REPO:-ant-rdg/eukalyptus}"
API="https://api.github.com/repos/${REPO}/labels"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILE="${DIR}/../.github/labels.yml"
DRY=0
[[ "${1:-}" == "--dry-run" ]] && DRY=1

[[ -f "$FILE" ]] || { echo "Fichier introuvable : $FILE" >&2; exit 1; }
if [[ $DRY -eq 0 && -z "${GITHUB_TOKEN:-}" ]]; then
  echo "La variable GITHUB_TOKEN est vide. Saisissez-la sans l'afficher : read -rs GITHUB_TOKEN && export GITHUB_TOKEN" >&2
  exit 1
fi

json_escape() { printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g'; }
url_encode() { python3 -I -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1], safe=""))' "$1"; }

call() { # méthode, URL, corps JSON : écrit le code HTTP sur la sortie standard
  curl -sS -o /dev/null -w '%{http_code}' -X "$1" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    -H "Authorization: Bearer ${GITHUB_TOKEN}" \
    -H "Content-Type: application/json" \
    --data "$3" "$2"
}

apply() {
  local name="$1" color="$2" description="$3" body status
  body="{\"name\":\"$(json_escape "$name")\",\"color\":\"$color\",\"description\":\"$(json_escape "$description")\"}"
  if [[ $DRY -eq 1 ]]; then
    echo "[essai] $name  #$color  $description"
    return
  fi
  status="$(call POST "$API" "$body")"
  case "$status" in
    201) echo "créée      : $name" ;;
    422) # existe déjà : mise à jour
      status="$(call PATCH "${API}/$(url_encode "$name")" "$body")"
      if [[ "$status" == "200" ]]; then echo "mise à jour : $name"; else echo "ÉCHEC ($status) : $name" >&2; return 1; fi ;;
    401|403) echo "Accès refusé ($status) : vérifiez le jeton et ses droits." >&2; exit 1 ;;
    404) echo "Dépôt introuvable ($REPO), ou jeton sans accès." >&2; exit 1 ;;
    *) echo "ÉCHEC ($status) : $name" >&2; return 1 ;;
  esac
}

name="" color="" description=""
flush() {
  if [[ -n "$name" ]]; then apply "$name" "$color" "$description"; fi
  name="" color="" description=""
}

while IFS= read -r line || [[ -n "$line" ]]; do
  case "$line" in
    "#"*|"") ;;
    "- name: "*) flush; name="${line#- name: }" ;;
    "  color: "*) color="${line#  color: }"; color="${color//\"/}" ;;
    "  description: "*) description="${line#  description: }" ;;
  esac
done < "$FILE"
flush
