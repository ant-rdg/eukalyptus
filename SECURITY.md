# Politique de sécurité

*English version at the [bottom of this page](#english-version).*

La sécurité d'Eukalyptus compte beaucoup, surtout pour une application qui manipule des accès à vos serveurs. Si vous pensez avoir
trouvé une faille, merci de la signaler **en privé**, comme expliqué ci-dessous.

## Versions prises en charge

Seule la **dernière version publiée** de chaque plateforme reçoit les correctifs de sécurité. Quand un correctif est urgent, l'auteur peut
déclarer une version précédente « périmée » : l'application demande alors de se mettre à jour avant de continuer.

| Plateforme | Version prise en charge |
|---|---|
| macOS (14 et plus, Apple silicon) | la dernière version publiée |
| Windows (10 et 11) | la dernière version publiée |

La dernière version est indiquée sur [eukalyptus.app/telecharger](https://eukalyptus.app/telecharger) et dans le [journal des versions](CHANGELOG.md).
L'application vérifie les mises à jour à chaque lancement.

## Signaler une faille

**Ne publiez pas une faille dans une issue, une discussion ou une pull request** : tout y est public.

Deux moyens, au choix :

1. **Signalement privé GitHub** (recommandé) : onglet *Security* de ce dépôt, puis
   [*Report a vulnerability*](https://github.com/ant-rdg/eukalyptus/security/advisories/new). Seul l'auteur voit votre message, et vous
   pouvez échanger avec lui en privé.
2. **E-mail** : [contact@eukalyptus.app](mailto:contact@eukalyptus.app), avec « Sécurité » dans l'objet.

Dans votre message, indiquez si possible :

- la version d'Eukalyptus et le système (macOS ou Windows, avec sa version) ;
- ce que la faille permet (lire un secret, exécuter une commande, contourner une vérification…) ;
- les étapes pour la reproduire, avec si besoin un fichier de session ou un serveur d'essai ;
- votre avis sur la gravité, et si vous souhaitez être cité dans les remerciements.

Ne joignez pas de vrais mots de passe, de clés privées ou de données de production : un exemple minimal suffit.

## Ce que vous pouvez attendre

Eukalyptus est développé par une seule personne. Les délais ci-dessous sont **indicatifs** :

| Étape | Délai visé |
|---|---|
| Accusé de réception | sous 7 jours |
| Première évaluation (faille confirmée ou non, gravité) | sous 14 jours |
| Correctif | selon la gravité : le plus vite possible pour une faille grave, dans une version ordinaire sinon |

Vous êtes tenu informé de l'avancement. Une fois le correctif publié, la faille est mentionnée dans les notes de version, et vous êtes
remercié publiquement si vous le souhaitez.

Nous vous demandons de **ne pas divulguer la faille avant la publication d'un correctif**, et de ne pas accéder aux données d'autres
personnes ni perturber le service pour la démontrer. De bonne foi, un chercheur qui respecte ces règles n'a rien à craindre.

Les failles du **site eukalyptus.app** (formulaires, API, paiement) se signalent de la même façon.

## Ce qui est documenté publiquement

La page [eukalyptus.app/securite](https://eukalyptus.app/securite) (et son [équivalent anglais](https://eukalyptus.app/en/security)) décrit,
de façon vérifiable, ce qu'Eukalyptus fait et ne fait pas, en particulier :

- **la liste complète des connexions de l'application** vers le site d'Eukalyptus (compteur d'installations, liste des versions,
  mises à jour, activation d'Eukalyptus+, synchronisation) : qui parle à qui, quand, avec quoi, et ce qui le protège ;
- l'installation et les mises à jour (liste des versions signée, empreinte SHA-256 vérifiée avant toute installation) ;
- le stockage des secrets (Trousseau macOS, coffre chiffré sous Windows, jamais de mot de passe dans un export) ;
- les protections par protocole (SSH, SFTP, FTP, RDP, VNC, S3), contre les serveurs et les fichiers hostiles, et dans le terminal ;
- la synchronisation et le coffre d'équipe (Eukalyptus+) : chiffrement de bout en bout, relais temporaire qui ne peut rien lire ;
- les **limites connues**, dites franchement.

La même information est dans l'application, menu Aide › Sécurité et confidentialité.

### Principes en bref

- **Aucun suivi** : pas de compte, de statistiques d'usage ni de publicité. Les seules connexions vers le site d'Eukalyptus sont celles de
  la page de sécurité ; les autres sont celles que vous demandez (vos serveurs, les pages ouvertes dans le navigateur intégré).
- **Secrets protégés** : mots de passe dans le Trousseau macOS ou le coffre chiffré de Windows ; un export `.eukalyptus` n'en contient aucun.
- **Peu de code, peu de risques** : les bibliothèques sont compilées depuis les sources officielles à empreintes vérifiées ; aucun
  composant GPL ou LGPL.
- **Données reçues traitées comme hostiles** : noms d'hôtes, fichiers de session reçus ou noms de fichiers renvoyés par un serveur sont
  contrôlés ; les options qui agissent sans votre accord (transfert d'agent, X11, options ssh libres, commande locale, macro de démarrage)
  sont désactivées à l'import d'une session ou à sa réception par la synchronisation.
- **Terminal** : le presse-papiers (OSC 52) et le rapport de titre sont désactivés ; un lien qui n'est pas une page web demande confirmation.
- **RDP** : TLS et NLA seulement, certificat vérifié par empreinte, aucune redirection de disques entiers, d'imprimantes, de ports ni d'USB.
- **Identité des serveurs** : si la clé d'un serveur change, la connexion reste bloquée et une alerte l'explique.
- **Synchronisation et coffre d'équipe** (Eukalyptus+) : chiffrés de bout en bout ; le serveur relais ne peut ni lire ni modifier les
  données sans que l'application le détecte, et les efface au plus tard 365 jours après leur dernière écriture.

### Limites connues, en bref

- Sur Mac, l'application est signée avec le certificat de son auteur, sans certificat Developer ID d'Apple : elle n'est pas notarisée, et
  macOS demande une confirmation au premier lancement. Sous Windows, l'installateur n'est pas encore signé : SmartScreen peut avertir.
  L'empreinte SHA-256 de chaque installateur est publiée pour vérification.
- Elle n'est pas dans le bac à sable (elle lance un terminal local et OpenSSH) : elle agit avec les droits de l'utilisateur.
- Le FTP simple n'est pas chiffré (limite du protocole), ni une session S3 en http : à réserver à un réseau de confiance.
- Qui détient la clé de synchronisation peut lire les données du relais : à garder comme un mot de passe.
- Dans le coffre d'équipe, le rôle « se connecte sans voir les mots de passe » est une protection de confort, pas une barrière : l'app
  doit déchiffrer le mot de passe pour se connecter.

Pour tout détail, la page [eukalyptus.app/securite](https://eukalyptus.app/securite) fait foi.

---

## English version

**Supported versions.** Only the latest published version of each platform (macOS 14+ on Apple silicon, Windows 10/11) receives security
fixes. For an urgent fix, an older version can be declared obsolete and the app then asks for an update.

**Reporting a vulnerability.** Please report it **privately**; do not post it in an issue, a discussion or a pull request. Either use
GitHub's private reporting ([Report a vulnerability](https://github.com/ant-rdg/eukalyptus/security/advisories/new) in the Security tab)
or write to [contact@eukalyptus.app](mailto:contact@eukalyptus.app) with "Security" in the subject. Include the version, the system, what the
flaw allows and the steps to reproduce it; do not attach real passwords, private keys or production data. You may write in English.

**What to expect.** Eukalyptus is developed by one person, so these times are indicative: acknowledgement within 7 days, first assessment
within 14 days, and a fix as fast as possible for a serious flaw (otherwise in a regular release). You are kept informed, and credited in
the release notes if you wish. Please do not disclose the flaw before a fix is published, and do not access other people's data or disrupt
the service to demonstrate it.

**What is documented publicly.** [eukalyptus.app/en/security](https://eukalyptus.app/en/security) lists every network connection the app
makes, how updates are verified, how secrets are stored, the protections for each protocol, how encrypted sync and the team vault work,
and the known limitations. The same information is in the app (Help › Security and privacy).
