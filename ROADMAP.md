# Feuille de route

[English summary at the bottom](#english-summary)

Cette page dit où en est Eukalyptus : ce qui est fait, ce qui est en cours, ce qui est prévu, et ce qui reste à discuter avec vous.
**Aucune date n'est promise** : Eukalyptus est développé par une seule personne, et un ordre de passage peut changer selon vos retours.
Le détail de chaque version publiée est dans le [journal des versions](CHANGELOG.md).

Pour donner votre avis, votez ou proposez une idée dans les [Discussions, catégorie « Idées »](https://github.com/ant-rdg/eukalyptus/discussions/categories/idees) :
les votes (👍) pèsent dans le choix de la suite.

## Fait

**Mac et Windows**

- Application native pour **macOS** (14 et plus, Apple silicon) et pour **Windows** (10 et 11), sans Electron : terminal, SSH, SFTP, FTP,
  FTPS, S3, RDP, VNC, Telnet, tunnels, macros, monitoring, outils réseau, éditeur intégré, import MobaXterm, Termius et `.rdp`.
- Bureau à distance **RDP** intégré dans l'onglet, avec passerelle SSH ; **VNC** intégré dans l'onglet.
- Application en **français et en anglais**, selon la langue du système (0.8.2).
- Palette de commandes (⌘K), nouveau panneau de gauche, nouvel accueil (0.9.0).
- Sécurité : alerte quand l'identité d'un serveur change, vérification des clés SSH, clés de sécurité physiques (YubiKey, FIDO2) en option
  (0.9.0) ; connexion aux serveurs SSH anciens ou très durcis sans réglage (0.9.2).
- **Eukalyptus+** : synchronisation chiffrée de bout en bout entre vos ordinateurs et coffre d'équipe (0.9.0).
- Versions de sécurité : 0.9.1 et 0.9.2 (Mac), 0.9.2 (Windows).

**Windows**

- Première version publiée le 3 novembre 2026 (0.9.0), avec un coffre chiffré par mot de passe maître ; serveur X11 intégré pour le X11 forwarding.
- Coffre qui reste ouvert jusqu'au redémarrage (0.9.3) ; tunnels SSH par mot de passe et bandeau d'état de la connexion (0.9.4).
- Plusieurs transferts de fichiers en même temps, avec progression, débit et temps restant, et des téléchargements bien plus rapides
  avec un serveur éloigné (0.9.5).

## En cours

- **Mac 0.9.5** : reprend, après la 0.9.2, ce qui a été fait côté Windows et d'autres améliorations : tunnels SSH par mot de passe, bandeau
  d'état de la connexion au-dessus du terminal, navigateur de fichiers qui suit le dossier du terminal sans rien taper dans le shell,
  sélection de plusieurs sessions, onglets réordonnables, option RDP « Rester actif », plusieurs transferts de fichiers en même temps avec
  progression lisible, demande avant d'écraser un fichier.
- **Consolider** ce qui a été moins éprouvé en conditions réelles, en particulier sous Windows (RDP pour les entreprises, Entra ID,
  clés de sécurité physiques) : vos retours y comptent beaucoup.

## Prévu

Ce qui est identifié comme restant à faire, sans date.

- **Windows** : Mosh, réglage d'apparence de l'application (clair, sombre ou système), sélection de plusieurs sessions à la fois.
- **Windows** : signature de code de l'installateur, pour supprimer l'avertissement SmartScreen (le site indique « pas encore »).
- **RDP** (Mac et Windows) : micro, caméra, USB, ports série, RemoteApp, Kerberos, H.264. Le client RDP actuel ne les gère pas.
- **Mac** : bandeau « serveur silencieux », déjà présent sous Windows.

## Idées à discuter

Des sujets ouverts, sur lesquels votre avis aide à décider. Ouvrez ou rejoignez une discussion :

- **Attente de l'agent SSH sur Mac** : afficher un message pendant que Bitwarden ou 1Password attend votre approbation (c'est le cas sous
  Windows). Le faire sur Mac demande un relais local de l'agent, avec des effets de bord à peser.
- **Mosh sous Windows** : l'utilisez-vous, et pour quels serveurs ?
- **Autres plateformes** : Linux et les Mac à processeur Intel ne sont pas pris en charge aujourd'hui. Votre besoin, avec votre contexte,
  nous intéresse.
- **Ce qui manque** : une fonction que vous cherchez dans un autre outil et que vous ne trouvez pas ici. Décrivez le besoin, pas
  seulement la fonction.

## Ce qui a été retiré, volontairement

- L'indicateur de joignabilité des serveurs favoris et récents (point « répond / ne répond pas » dans le panneau de gauche) a été retiré
  de la 0.9.x à la demande de l'auteur.

---

## English summary

This page says where Eukalyptus stands: done, in progress, planned, and open topics. **No date is promised.** Eukalyptus is built by one
person, and the order can change with your feedback. Vote or suggest ideas in
[Discussions, "Idées" category](https://github.com/ant-rdg/eukalyptus/discussions/categories/idees). Per-version details are in the
[changelog](CHANGELOG.md) (notes in French).

**Done.** Native apps for macOS (14+, Apple silicon) and Windows (10/11): terminal, SSH, SFTP, FTP/FTPS, S3, RDP and VNC in tabs, tunnels,
macros, monitoring, network tools, built-in editor, MobaXterm/Termius/.rdp import; French and English interface; command palette; server
identity change alert, SSH key checks, optional physical security keys; encrypted sync and team vault (Eukalyptus+); Windows 0.9.0 to 0.9.5
(encrypted vault, built-in X server, parallel transfers with progress).

**In progress.** Mac 0.9.5 (SSH tunnels with a password, connection status banner, file browser following the terminal's folder, multiple
session selection, parallel transfers). Hardening features that have seen less real-world testing, especially on Windows.

**Planned (no dates).** Windows: Mosh, an appearance setting, multiple session selection, code-signed installer. RDP: microphone, camera,
USB, serial ports, RemoteApp, Kerberos, H.264. Mac: a "silent server" banner.

**Ideas to discuss.** Waiting-for-agent hint on Mac, Mosh on Windows, other platforms (Linux, Intel Macs: not supported today), and
whatever you find missing: describe the need, not only the feature.
