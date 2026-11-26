# Traductions

Ce dossier contient les **fichiers de langue d'Eukalyptus**. Vous pouvez corriger la traduction anglaise ou en proposer une nouvelle, par
pull request. Le principe général est dans [CONTRIBUTING.md](../CONTRIBUTING.md#traduire-lapplication).

*English: this folder holds the app's language files. You can fix the English or propose a new language by pull request; the rules
below apply (keep the keys, keep the placeholders, keep texts short). You can write your pull request in English.*

## Ce qu'il y a ici

```text
translations/
├── fr.lproj/
│   ├── Localizable.strings   français : voir « Le français » plus bas
│   └── InfoPlist.strings     texte système (accès au réseau local)
└── en.lproj/
    ├── Localizable.strings   anglais : environ 2 800 textes
    └── InfoPlist.strings
```

Les applications macOS et Windows lisent **les mêmes fichiers**. Une version publiée contient la traduction telle qu'elle était au
moment de la compilation : une pull request fusionnée ici est intégrée dans une **version suivante**, pas tout de suite.

## Le format `.strings`

Un fichier est une suite de lignes `"clé" = "valeur";`, éventuellement séparées par des commentaires `/* ... */` :

```text
/* Menu Aide */
"Aide" = "Help";
"Télécharger la version %@" = "Download Version %@";
"« %@ » existe déjà dans %@." = "“%@” already exists in %@.";
```

- La **clé** (à gauche) est **le texte français d'origine**, tel qu'il est écrit dans l'application. L'application s'en sert pour trouver
  la traduction : **ne la modifiez jamais**, pas même une faute de frappe ou une apostrophe.
- La **valeur** (à droite) est la seule chose à traduire.
- Chaque ligne se termine par `;`. Les guillemets droits `"` délimitent le texte ; un guillemet dans le texte s'écrit `\"`. Les
  guillemets typographiques (« », “ ”) sont autorisés tels quels dans la valeur.
- Le fichier est en **UTF-8**.

## Règles de traduction

1. **Clés inchangées**, une entrée traduite pour chaque clé (ne supprimez ni n'ajoutez de clé).
2. **Marqueurs conservés** : `%@` (texte), `%lld` ou `%d` (nombre), `%%` (un signe %) doivent rester **en même nombre et dans le même
   ordre** que dans la clé. Si votre langue exige un autre ordre, dites-le dans la pull request : ne réordonnez pas de votre propre chef.
3. **Séquences spéciales conservées** : `\n` (retour à la ligne), `\r`, et les séquences de terminal comme `\U001B[1;33m` (couleurs) ne se
   traduisent pas et ne se déplacent pas.
4. **Pas de texte plus long que nécessaire.** Les boutons, menus, onglets, info-bulles et barres d'état ont une largeur limitée, et un
   texte trop long est coupé. Prenez le terme le plus court qui reste clair, surtout pour les boutons et les menus. Comparez avec la longueur
   de la clé française et de la valeur anglaise.
5. **Ton** : poli et direct, sans familiarité, avec l'équivalent du vouvoiement dans votre langue. Une phrase d'erreur dit ce qui s'est
   passé et ce qu'on peut faire.
6. **Noms propres inchangés** : Eukalyptus, Eukalyptus+, SSH, SFTP, FTP, S3, RDP, VNC, Telnet, Mosh, X11, XQuartz, Wake-on-LAN, MultiExec,
   noms de commandes et de fichiers (`~/.ssh/config`, `known_hosts`…). Pour Trousseau, Touch ID, Finder, Explorateur de fichiers et les
   autres termes du système, reprenez **le terme officiel de macOS ou de Windows dans votre langue**.
7. **Cohérence** : un même mot français = un même mot dans votre langue (« session », « onglet », « identifiant », « empreinte »…).
8. Les deux textes les plus longs (licence abrégée et « ce que fait Eukalyptus, et ne fait pas ») engagent l'auteur : traduisez-les fidèlement,
   sans rien ajouter ni retirer ; l'auteur les relit avec une attention particulière.

## Corriger l'anglais

1. Faites un fork du dépôt et ouvrez `translations/en.lproj/Localizable.strings` (le bouton « Modifier » de GitHub suffit pour quelques
   corrections).
2. Corrigez la **valeur** de l'entrée concernée. Ne touchez pas la clé.
3. Ouvrez une pull request en citant, si vous le pouvez, l'endroit de l'application où le texte apparaît.

## Proposer une nouvelle langue

1. Faites un fork du dépôt.
2. Choisissez le code de la langue : code ISO 639-1 sur deux lettres (`de`, `es`, `it`, `nl`, `pt`…), éventuellement suivi de la région
   (`pt-BR`, `zh-Hans`). Le dossier s'appelle `<code>.lproj`.
3. **Copiez** `en.lproj/Localizable.strings` dans `translations/<code>.lproj/Localizable.strings`, et `en.lproj/InfoPlist.strings` dans
   `translations/<code>.lproj/InfoPlist.strings`. Partez de la version anglaise : la clé française et la valeur anglaise vous donnent
   deux points de repère.
4. **Remplacez chaque valeur anglaise** par votre traduction, en suivant les règles ci-dessus. Gardez les commentaires `/* ... */` tels quels ou
   supprimez-les, mais ne changez aucune clé.
5. **Vérifiez le fichier** :
   - sur Mac : `plutil -lint translations/<code>.lproj/Localizable.strings` doit répondre `OK` ;
   - le nombre d'entrées doit être le même que dans `en.lproj` (environ 2 800 lignes `"clé" = "valeur";`) :
     `grep -c '^"' translations/<code>.lproj/Localizable.strings`.
6. Ouvrez une pull request intitulée « Traduction : <langue> » avec le modèle proposé. Indiquez votre niveau (langue maternelle ou non) et
   si vous voulez rester créditée ou crédité.

Une traduction partielle est acceptable : une entrée absente retombe normalement sur le texte français d'origine. Mais un fichier complet donne une
application cohérente.

### Ce qui se passe ensuite

Une traduction ne peut pas être testée sans compiler l'application, qui n'est pas publiée : **c'est donc l'auteur qui la relit et
l'essaie**. Il vérifie le fichier, ajoute la langue à l'application (macOS et Windows), puis l'intègre à une version. Les textes coupés
ou mal placés qui apparaissent à ce moment-là peuvent demander un raccourcissement : il vous le dira dans la pull request. Cela peut
prendre du temps, une langue n'est ajoutée qu'avec une version de l'application.

Après la sortie, ouvrez une [issue](https://github.com/ant-rdg/eukalyptus/issues/new/choose) si vous voyez un texte coupé, mal traduit
ou resté en français.

## Le français

Le français est la **langue du code** : ses textes sont écrits en français dans l'application, donc `fr.lproj/Localizable.strings` ne
contient qu'un commentaire qui déclare la langue. Il n'y a pas de texte français à modifier ici.

Pour corriger un texte français (faute, tutoiement au lieu du vouvoiement, formulation ambiguë), **ouvrez une issue** qui cite le texte
exact et l'endroit où il apparaît : l'auteur le corrige dans le code. La clé d'une entrée étant ce texte français, il n'est pas possible de
le corriger par pull request sans casser la traduction.

## Licence

Ces fichiers sont publiés pour permettre la traduction. En proposant une traduction, vous acceptez qu'elle soit intégrée à Eukalyptus et
distribuée avec lui, selon la [licence d'utilisation](../LICENSE.txt) du logiciel.
