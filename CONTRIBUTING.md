# Contribuer à Eukalyptus

[English](CONTRIBUTING.en.md) · Français

Merci de votre intérêt. Eukalyptus est un logiciel **gratuit à code fermé** : ce dépôt ne contient pas son code source, donc pas de
pull request de code. Il sert à recueillir vos **retours** et à publier ce qui peut l'être : la documentation et les fichiers de langue.
Voici ce que vous pouvez faire, et comment.

*You can write in English, everywhere: issues, discussions and pull requests. French is the default language of this repository.*

Avant de participer, lisez le [code de conduite](CODE_OF_CONDUCT.md).

## Sommaire

- [Signaler un bug](#signaler-un-bug)
- [Proposer une idée](#proposer-une-idée)
- [Poser une question](#poser-une-question)
- [Corriger la documentation](#corriger-la-documentation)
- [Traduire l'application](#traduire-lapplication)
- [Signaler une faille de sécurité](#signaler-une-faille-de-sécurité)
- [Ce qui n'est pas accepté](#ce-qui-nest-pas-accepté)

## Signaler un bug

1. **Mettez l'application à jour** : le bug est peut-être déjà corrigé. Les versions sont dans le [journal des versions](CHANGELOG.md).
2. **Cherchez dans les [issues](https://github.com/ant-rdg/eukalyptus/issues)** (ouvertes et fermées) : si le problème existe déjà, ajoutez
   un 👍 et, si vous avez un détail de plus, un commentaire.
3. Sinon, **[ouvrez une issue](https://github.com/ant-rdg/eukalyptus/issues/new?template=bug.yml)** avec le formulaire « Bug ». Indiquez :
   - **La version d'Eukalyptus** : Réglages › Crédits › À propos (sur Mac, aussi le menu Eukalyptus › À propos d'Eukalyptus).
   - **Le système** : version de macOS (menu Pomme › À propos de ce Mac) ou de Windows (Paramètres › Système › À propos de), et le type de processeur.
   - **Les étapes pour reproduire** le problème, une par ligne.
   - **Ce que vous attendiez**, et **ce qui s'est passé** (le message d'erreur exact, une capture d'écran si elle aide).
   - **Le type de serveur** concerné quand c'est utile (Linux, Windows, NAS, version d'OpenSSH…).
4. **Masquez les informations sensibles** avant de publier : mots de passe, clés, jetons, adresses IP et noms de serveurs privés. Une issue
   est publique.

Une issue = un problème. Si vous en avez plusieurs, ouvrez-en plusieurs.

## Proposer une idée

Les idées se discutent dans les **[Discussions, catégorie « Idées »](https://github.com/ant-rdg/eukalyptus/discussions/new?category=idees)**,
pas dans les issues.

- **Cherchez d'abord** une idée proche : votez avec 👍 plutôt que d'ouvrir un doublon. Les votes aident à choisir ce qui vient ensuite.
- **Décrivez le besoin avant la solution** : ce que vous essayez de faire, ce qui vous gêne aujourd'hui, avec quel type de serveur ou de
  flux de travail. Une idée accompagnée de son contexte est bien plus utile qu'une fonction réclamée seule.
- Consultez la [feuille de route](ROADMAP.md) : l'idée y est peut-être déjà.

Proposer une idée n'oblige pas l'auteur à la réaliser, et aucune date n'est promise.

## Poser une question

Une question d'utilisation, de configuration ou de compatibilité : **[Discussions, catégorie « Questions »](https://github.com/ant-rdg/eukalyptus/discussions/new?category=questions)**.
Regardez d'abord les [guides](README.md#guides) : la réponse y est peut-être. Pour une question sur un achat Eukalyptus+ ou sur vos
données personnelles, écrivez à contact@eukalyptus.app plutôt qu'en public.

## Corriger la documentation

Les guides sont dans [`docs/fr/`](docs/fr/) (français) et [`docs/en/`](docs/en/) (anglais). Une faute, une commande inexacte, une
information devenue fausse, une explication confuse : **les pull requests sont les bienvenues**.

1. Créez un fork du dépôt et modifiez directement le fichier Markdown (le bouton « Modifier » de GitHub suffit).
2. Gardez le style du guide : **vouvoiement**, ton direct, commandes dans des blocs de code, pas d'emoji dans les titres.
3. Ne modifiez qu'un sujet par pull request.
4. Si vous corrigez le français, corrigez aussi l'anglais (ou signalez-le dans la description) : les deux versions doivent dire la même chose.
5. Ne collez aucune information privée (adresses, mots de passe, noms de machines).

Ouvrez la pull request avec le modèle proposé : une courte description suffit. L'auteur relit et fusionne.

Pour une erreur que vous ne savez pas corriger, ouvrez une issue en précisant le guide et le passage concernés.

## Traduire l'application

L'application suit la langue du système. Elle existe en **français** et en **anglais**, et les fichiers de langue sont publiés dans
[`translations/`](translations/) : vous pouvez corriger l'anglais ou proposer une **nouvelle langue**. La marche à suivre complète est dans
[`translations/README.md`](translations/README.md). En résumé :

- Les fichiers sont au format **`.strings`** d'Apple (`"clé" = "valeur";`). Les deux applications (macOS et Windows) lisent les mêmes fichiers.
- **Ne changez jamais les clés** (la partie à gauche du signe `=`) : elles sont le texte français d'origine, et l'application les retrouve
  grâce à elles. Seule la valeur (à droite) se traduit.
- **Gardez les marqueurs** (`%@`, `%lld`, `\n`…) tels quels, en même nombre.
- **Pas de texte plus long que nécessaire** : les boutons, les menus et les onglets ont une largeur limitée. Choisissez le terme le plus court
  qui reste clair.
- **Vouvoiement** pour le français, et l'équivalent poli dans votre langue (jamais familier).
- **Une traduction ne se teste pas sans compiler l'application**, qui n'est pas fournie : vous ne pourrez donc pas la voir à l'écran avant
  qu'elle soit intégrée. L'auteur relit votre pull request, l'intègre à une version, et vous pouvez ensuite signaler tout texte coupé ou mal placé
  dans une issue.

Une traduction se propose par **pull request sur `translations/`**. Si vous n'êtes pas à l'aise avec Git, ouvrez une issue ou une
discussion et joignez le fichier.

## Signaler une faille de sécurité

**Ne publiez jamais une faille dans une issue, une discussion ou une pull request.** Utilisez le signalement privé de GitHub
(« Report a vulnerability » dans l'onglet Security) ou écrivez à l'auteur. Tout est expliqué dans [SECURITY.md](SECURITY.md).

## Ce qui n'est pas accepté

- **Les pull requests de code** : il n'y a pas de code ici. Une pull request qui ajoute ou modifie du code sera fermée.
- **Les demandes de fonction sans contexte** (« ajoutez X »). Expliquez le besoin dans les Discussions, avec votre cas d'usage.
- **Les doublons** d'issues ou d'idées déjà ouvertes : votez ou commentez sur l'existant.
- **Les demandes de support par e-mail ou par X** qui devraient être publiques : les réponses aident les autres utilisateurs.
- **Les messages hors sujet, promotionnels ou irrespectueux** : voir le [code de conduite](CODE_OF_CONDUCT.md).

Merci d'aider Eukalyptus à s'améliorer.
