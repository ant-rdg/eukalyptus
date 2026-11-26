# Journal des versions

Ce fichier est généré par [`scripts/changelog.py`](scripts/changelog.py) à partir de la liste des versions publiée par
[eukalyptus.app](https://eukalyptus.app/notes-de-version) ; il ne se modifie pas à la main. Les notes sont celles des versions,
telles que publiées (en français). Le site reste la source de vérité des mises à jour de l'app.

- Téléchargement : [eukalyptus.app/telecharger](https://eukalyptus.app/telecharger) ou les [Releases](https://github.com/ant-rdg/eukalyptus/releases) de ce dépôt.
- Le site ne garde que le dernier installateur de chaque plateforme : pour une version plus ancienne, les empreintes SHA-256 ci-dessous
  permettent de vérifier un fichier que vous auriez déjà.
- Vérifier une empreinte : `shasum -a 256 <fichier>` (macOS) ou `Get-FileHash <fichier>` (Windows PowerShell).
- Les numéros de version de macOS et de Windows avancent chacun de leur côté : une même version peut ne pas exister sur les deux.
- English readers: the release notes are written in French; see [README.en.md](README.en.md).

## 0.9.5

### Windows (2026-11-08)

**Transferts de fichiers**

- Plusieurs transferts en même temps : jusqu'à 4 fichiers à la fois, les suivants attendent leur tour.
- Nouvelle zone « Transferts » : pour chaque fichier, le pourcentage, la taille transférée, le débit et le temps restant, avec un bouton pour annuler.
- Transferts bien plus rapides avec un serveur éloigné : jusqu'à 10 fois plus rapides en téléchargement.

**Bugs**

- Corrections de plusieurs bugs mineurs.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `3ec6d49831859a9238e73364da9b1acb23e2c25e0d735bc7cfd4710407b32371`

## 0.9.4

### Windows (2026-11-06)

**Terminal**

- Le terminal n'affiche plus que votre serveur : les messages d'Eukalyptus (connexion, reconnexion, session terminée) passent dans un bandeau au-dessus, avec ses boutons.
- Le panneau Fichiers peut suivre le dossier du terminal sans rien écrire sur le serveur : menu « … » › Suivre le dossier du terminal.
- Un message s'affiche pendant que Bitwarden ou 1Password attend votre accord.

**Tunnels SSH**

- Ils acceptent maintenant un mot de passe, en plus d'une clé. Interface du tunnel plus claire.

**Interface**

- Les onglets portent le nom de vos sessions.
- « Fichiers » n'apparaît que lorsqu'il y a des fichiers à montrer.
- Réglages allégés, barre d'état plus discrète.

**Bugs**

- Corrections de plusieurs bugs mineurs.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `6f425214f19c85e57b756f7b8bb709ab627eeb3cbf4d8cb51982f2dd9a2eccb6`

## 0.9.3

### Windows (2026-11-05)

**Coffre**

- Il reste ouvert jusqu'au redémarrage de l'ordinateur, pour tous à cette mise à jour : plus de mot de passe à chaque lancement, au verrouillage de Windows ni en veille. Réglages › Général › « Verrouiller le coffre » : Jamais, au redémarrage de l'app, ou après une inactivité comme avant.
- Un coffre disparu se restaure depuis sa copie de sauvegarde.

**Fichiers**

- Envoyer sur un nom déjà pris demande d'abord : Garder les deux, Remplacer ou Annuler. Un envoi annulé ne perd plus l'ancien fichier.
- FTP fiable en rafale ; une sélection de fichiers se télécharge bien plus vite ; la liste suit les commandes du terminal.

**Terminal**

- Drapeaux en couleurs. Ctrl+Retour arrière efface un mot, Ctrl+_ annule.
- htop, vim et tmux reçoivent le clic droit quand ils suivent la souris.

**Onglets**

- Les onglets Bureau à distance et page web se détachent dans une fenêtre.
- Imports, arbre des sessions et messages corrigés ; Réglages rangés par utilité.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `ebd472fa14df34702747e9ee2d444c9fcdb98445f4361308c6c05ec66e755cff`

## 0.9.2

### macOS (2026-11-04)

**Connexions**

- Serveurs SSH anciens ou très durcis : la connexion se fait sans aucun réglage. Eukalyptus s'adapte aux algorithmes du serveur, s'en souvient pour ce serveur et le signale d'un ⓘ sur l'onglet.

**Sécurité**

- Fichier téléchargé : une question avant d'ouvrir tout type de fichier qui n'est pas connu pour être inoffensif.
- Liens du terminal : une adresse longue est abrégée au milieu, le nom du serveur reste toujours entier.
- Sessions importées ou reçues : les options de rebond SSH sont vérifiées, et un fichier de clé sur un partage réseau est signalé.
- Le texte envoyé par un serveur est nettoyé avant d'être affiché (surveillance, capture réseau).
- Listages SFTP et FTP géants bornés : l'app reste fluide.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `28148680538661716448f3a99e277875ebdea2b3ed7c7c011a64b3c8b1822579`  
> SHA-256 de l'archive de mise à jour : `03fbb88b054ad72eec7c910ac332e0dbbd50ca85f7d4f0b09d7b5c293b29d739`

### Windows (2026-11-04)

**Connexions**

- Serveurs SSH très durcis (CIS, ANSSI, FIPS) : la connexion se fait sans réglage.
- Serveurs SSH anciens : Eukalyptus se reconnecte avec leurs algorithmes, retient ce choix pour ce serveur et le signale d'un cadenas sur l'onglet. Terminal, SFTP, tunnels et passerelle RDP compris.

**Terminal**

- La touche Tab va au shell : l'autocomplétion du serveur fonctionne.
- Suggestions de commande désactivées par défaut (Réglages › Terminal pour les activer).

**Sécurité (audit de l'app Windows)**

- Coffre d'équipe : une session Bureau à distance partagée ne peut plus monter vos dossiers ou imprimantes, ni lancer un programme.
- Une clé SSH sur un partage réseau n'est plus lue d'office ; un rebond SSH piégé est refusé.
- Une question avant d'ouvrir un fichier téléchargé qui pourrait lancer quelque chose. Liens du terminal : la vraie adresse visible.
- Messages des serveurs et capture réseau nettoyés ; VNC en lecture seule ne touche plus à votre presse-papiers.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `c63350fafdb1388c948c006a99c14dcce9080f80571933d80a60d1d452703871`

## 0.9.1

### macOS (2026-11-03)

**Version de sécurité**

- Synchro : la clé d'un serveur SSH ou une macro modifiée sur un autre Mac attend votre accord.
- Sessions reçues ou partagées : les options qui agissent sans votre accord sont retirées.
- Un serveur hostile ne peut plus faire planter l'app ni saturer sa mémoire.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `386e01056ff16b6113f0af0f7d9e2f59ce505770847ebd1ac8f0b0e895e61fab`  
> SHA-256 de l'archive de mise à jour : `7ad6a70f6f71fa6d46e7aa6d134691669ac702794e96e40a24fec54c42f51870`

## 0.9.0

### macOS (2026-11-03)

**Recherche et navigation**

- Palette de commandes ⌘K : une session, une action, un réglage, ou utilisateur@hôte pour se connecter sans créer de session.
- Nouveau panneau de gauche : favoris, Mes sessions, et un point qui dit si chaque serveur répond. Nouvel accueil (Reprendre, Favoris, À regarder).

**Sécurité**

- Alerte si l'identité d'un serveur change ; vérification des clés SSH ; clés physiques (YubiKey) en option.
- Signature stable « Eukalyptus Signature » : une seule demande d'accès au Trousseau, plus à chaque mise à jour.

**Eukalyptus+**

- Synchronisation chiffrée entre vos Mac et coffre d'équipe, via un relais temporaire d'Eukalyptus (365 jours, illisible par nous).
- Messages d'erreur plus clairs. RDP : une session fermée par le serveur n'est plus un échec.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `3616793b82cb250b145f2f7c743849c331bab279155c8eba5ddabf0853c179cb`  
> SHA-256 de l'archive de mise à jour : `bc9fd56f9d9020a39096fd4d214e4f59b6237326b41f06437b1ed423356bb29a`

### Windows (2026-11-03)

Toute première version de Windows.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `d5d330c56a6ea94742897f064d1f5984edadee9af573636159e8f48a23adb3db`

## 0.8.2

### macOS (2026-10-29)

**News**

- L'application est traduite en anglais. Elle suit la langue du Mac
- La licence et l'installateur existent aussi en anglais.

**Patch**

- Connexion SSH : le mot de passe enregistré est aussi tapé quand le serveur le demande sous la forme « (compte@hôte) Password: » (PAM, double authentification).
- Capture du réseau : en anglais, les tailles (MB, kB) et le résumé en bas de la fenêtre sont traduits.
- Monitoring et S3 : la durée de fonctionnement du serveur et la durée des liens présignés sont traduites en anglais.
- Navigateur de fichiers : la colonne des tailles n'est plus coupée (« 734 octets » s'affiche en entier).
- Installateur : les pages d'accueil et de fin indiquent la bonne version.

**Optimisation**

- Le lien de téléchargement mène à la page du site dans la langue de l'app.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `8c6c722174def92a5dfd6be7438192bcf6577ab2a2c2f746e991f5cab08a0503`  
> SHA-256 de l'archive de mise à jour : `510e92833e1dd4b7d2a7b171a34c7ba9844a3341d1ba280fe62144943ed9b348`

## 0.8

### macOS (2026-10-28)

**News**

- RDP : Eukalyptus ne dépend plus de Windows App, tout s'ouvre dans l'onglet.
- RDP : Refonte complète de la gestion RDP
- Import : reprenez vos sessions RDP depuis des fichiers .rdp, un dossier ou un .zip.
- Macros : une session peut lancer une macro toute seule à son ouverture, avec le délai de votre choix.
- Terminal : nouvelle option « Colorer les mots-clés » (Réglages › Général) : erreurs en rouge, alertes en jaune, réussites en vert, adresses IP en cyan.
- Outils : « Capture du réseau » montre qui parle à qui, avec un résumé en

**Patch**

- X11 : l'affichage est retrouvé tout seul, même si XQuartz vient d'être installé.
- X11 : sans XQuartz, Eukalyptus explique quoi installer au lieu d'une erreur de ssh.

**Optimisation**

- RDP : graphismes RDPGFX activés pour un affichage plus fluide (réglage « Affichage fluide » par session).
- RDP : option « Écran Retina » pour un texte plus net.
- RDP : reconnexion automatique après une coupure réseau.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `40b792073c2da010bac99807328a2a5c1afb647a0dc222cd2af0580970f97a06`  
> SHA-256 de l'archive de mise à jour : `dbc7d033a6cc3b5d01435a1fb39fa8b0d342f6b63d673231324bf71115adefe0`

## 0.7

### macOS (2026-10-27)

_Pas de notes publiées pour cette version._

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `5455262b9defa5c1a1a9522379ecb98f515b3257bd909111fdee1b4fd9de7e81`  
> SHA-256 de l'archive de mise à jour : `a6db08dd8b65e730e1b10ab4055decc223d8555adcebe37ea6ffc9a2d028c131`

## 0.6

### macOS (2026-10-27)

**News**

- Ajout d'un onboarding
- S3 : AWS S3, MinIO, Cloudflare R2, Backblaze B2 et autres services compatibles, envoi, téléchargement, renommage, suppression, glisser-déposer et liens présignés.

**Patch**

Surveillance : les serveurs macOS sont pris en charge.

Import : Termius, et clic droit pour MobaXterm.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `d1f26a40c6af9f9cf8d72b0c2246bed0842304cf4ca9c8b8d3d486a6a0b394fc`  
> SHA-256 de l'archive de mise à jour : `9c051ca6122b0fcb3f96f4657adabe2a2b329cd9d63aea8c9cbf25a3902978de`

## 0.5

### macOS (2026-10-26)

Eukalyptus 0.5 fiabilise la mise à jour automatique.

- Correction : la mise à jour automatique fonctionne désormais aussi lorsque l'application a été installée avec le fichier .pkg.
- Si une mise à jour ne peut pas être installée, Eukalyptus le signale clairement et conserve votre version actuelle, au lieu de se rouvrir sans explication.
- Si vous êtes en 0.3 ou 0.4 et que la mise à jour automatique échoue, installez cette version avec le .pkg : c'est nécessaire une seule fois.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `dd6639e9c6a392517aef486f4682c51c769136ee8b2957c20e13f98cfa99891c`  
> SHA-256 de l'archive de mise à jour : `b6ecf403c9d05f18780b58bbada5ee15d66eba823fe68399047503639b8f952c`

## 0.4

### macOS (2026-10-26)

Eukalyptus 0.4 facilite l'arrivée depuis MobaXterm.

- Un écran de bienvenue s'ouvre au tout premier lancement et propose d'importer vos sessions MobaXterm (fichier MobaXterm.ini ou export .mxtsessions)

- L'import est désormais à portée de clic : bouton « Importer depuis MobaXterm » sur l'accueil, et Aide › Bienvenue pour rouvrir l'écran.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `aedd08571940373761130e299e7d7e9ade3be593f2032f15398d5400576496b1`  
> SHA-256 de l'archive de mise à jour : `3f4a5ba3911ca2ca1552a34eeb992a16e1fccaec708e2c9c0c9e6e7e76501afb`

## 0.3

### macOS (2026-10-26)

Ajout d'un compteur d'installations anonyme, conçu pour respecter votre vie privée.

- Au tout premier lancement, l'app signale une seule fois qu'un Mac de plus l'utilise. Seul le numéro de version est transmis : aucun identifiant, aucun nom de Mac, aucune licence, aucune adresse conservée.
- Le site n'en retient que le total par jour et par version, afin de mesurer l'adoption et d'orienter les prochaines versions. Aucune statistique d'usage n'est collectée.
- En toute transparence, cet envoi est décrit dans les Réglages, dans Aide › Sécurité et confidentialité et dans la licence.

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `a9bea1c28f2a1f7b631384dd5d76aa02059c46bb8723b56c6aa3c243e630220f`  
> SHA-256 de l'archive de mise à jour : `d9af67a9bf9d126921dde66df03c26d319a2dfa9f5ccab08118e27adc6a34da9`

## 0.2

### macOS (2026-10-26)

Toute première version de l'application Eukalyptus <3

> Téléchargement : <https://eukalyptus.app/telecharger>  
> SHA-256 de l'installateur : `179c9cc93e11b1ed4b4b2fe742515e8e6dde838682792dc480be76bbf3f86942`  
> SHA-256 de l'archive de mise à jour : `e71298f3ea16c9c888b32d5afc535968262976dc08cee1c35843ede7113e4a12`
