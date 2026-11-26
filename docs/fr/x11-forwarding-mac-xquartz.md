---
title: "X11 forwarding sur Mac : afficher une application d'un serveur avec XQuartz"
description: "Afficher sur votre Mac une application graphique d'un serveur Linux : installer XQuartz, activer le X11 forwarding et corriger les erreurs courantes."
category: Tutoriel
date: 2026-10-28
updated: 2026-10-29
reading_time: 7 min
source: https://eukalyptus.app/blog/x11-forwarding-mac-xquartz
---

# X11 forwarding sur Mac : afficher une application d'un serveur avec XQuartz

Un installateur Java, un outil d'administration graphique, une base Oracle : certains programmes d'un serveur n'existent qu'avec une fenêtre. Le X11 forwarding les affiche sur votre Mac, à travers la connexion SSH. Voici comment le mettre en place avec XQuartz et Eukalyptus, et quoi faire quand ça échoue.

> **En bref**
>
> - Le X11 forwarding envoie les fenêtres d'un programme du serveur vers votre Mac, par SSH.
> - Il faut XQuartz sur le Mac (gratuit) et xauth sur le serveur.
> - Dans Eukalyptus : cocher « X11 forwarding » dans les paramètres de la session SSH.
> - Les erreurs les plus fréquentes viennent de xauth manquant ou de X11Forwarding désactivé.

**Dans cet article**

1. [Comment fonctionne le X11 forwarding](#comment-fonctionne-le-x11-forwarding)
2. [Installer XQuartz sur le Mac](#installer-xquartz-sur-le-mac)
3. [Préparer le serveur](#préparer-le-serveur)
4. [L'activer dans Eukalyptus](#lactiver-dans-eukalyptus)
5. [Tester avec une petite application](#tester-avec-une-petite-application)
6. [Résoudre les erreurs courantes](#résoudre-les-erreurs-courantes)
7. [Une précaution de sécurité](#une-précaution-de-sécurité)
8. [Questions fréquentes](#questions-fréquentes)

## Comment fonctionne le X11 forwarding

Sous Linux, les applications graphiques parlent à un « serveur X » qui dessine leurs fenêtres. Avec le X11 forwarding, le programme tourne sur le serveur distant, mais son affichage est envoyé à travers la connexion [SSH](./client-ssh-mac.md) jusqu'au serveur X de votre Mac : la fenêtre apparaît à côté de vos autres applications, alors que rien d'autre que le programme n'est exécuté sur le serveur.

*Schéma : X11 forwarding : un programme tourne sur le serveur, son affichage traverse la connexion SSH et s'affiche via XQuartz sur le Mac.*

| Votre Mac |  | Connexion SSH |  | Le serveur |
|---|---|---|---|---|
| XQuartz<br>affiche la fenêtre | ← fenêtres | chiffrée<br>port 22 | ← affichage | lance le programme<br>(xeyes, installateur…) |

macOS ne livre plus de serveur X. C'est **XQuartz**, un projet libre, qui joue ce rôle sur Mac. Eukalyptus ne l'embarque pas : il s'appuie dessus.

## Installer XQuartz sur le Mac

Le plus simple : dans Eukalyptus (depuis la version 0.8.1), **Réglages › Général › XQuartz › Installer XQuartz…**. Le même bouton apparaît si vous ouvrez une session X11 sans XQuartz. Eukalyptus télécharge l'installateur officiel (XQuartz 2.8.6, sur github.com), vérifie son empreinte SHA-256 et l'ouvre dans l'Installateur de macOS, qui contrôle à son tour la signature et la notarisation d'Apple. Sinon :

1. Téléchargez XQuartz sur **xquartz.org** et installez-le, ou lancez la commande ci-dessous si vous utilisez Homebrew.
2. Fermez votre session macOS puis rouvrez-la (ou redémarrez) : l'installateur de XQuartz le demande, car il met en place la variable d'affichage du système.

*Avec Homebrew*

```sh
brew install --cask xquartz
```

## Préparer le serveur

Deux choses sont nécessaires côté serveur, et elles expliquent presque tous les échecs :

- **Le transfert X11 est autorisé** dans la configuration de sshd : la ligne `X11Forwarding yes` dans `/etc/ssh/sshd_config`, puis un rechargement du service SSH.
- **L'outil `xauth` est installé**, car SSH s'en sert pour créer le cookie d'authentification de l'affichage.

*Installer xauth (Debian, Ubuntu)*

```sh
sudo apt install xauth
```

*Installer xauth (RHEL, Rocky, Fedora)*

```sh
sudo dnf install xorg-x11-xauth
```

## L'activer dans Eukalyptus

1. Ouvrez les **Paramètres de la session** de votre serveur (type SSH).
2. Cochez **« X11 forwarding (-Y, nécessite XQuartz) »** dans les options SSH, puis enregistrez.
3. Ouvrez la session : les programmes graphiques lancés depuis le terminal s'affichent dans XQuartz.

Eukalyptus retrouve lui-même l'affichage de XQuartz (variable `DISPLAY`, launchd ou socket de XQuartz). Si XQuartz n'est pas installé, il propose de l'installer, au lieu du « X11 forwarding request failed » de ssh.

En ligne de commande, l'équivalent est l'option `-Y`. Si l'affichage est lent, activez aussi la **compression** (`-C`) dans les mêmes options : elle aide sur les connexions à faible débit.

*Équivalent en ligne de commande*

```sh
ssh -Y utilisateur@serveur.exemple.fr
```

## Tester avec une petite application

Une fois connecté, vérifiez d'abord que l'affichage est bien transmis, puis lancez un programme simple :

```sh
echo $DISPLAY      # doit afficher quelque chose comme localhost:10.0
xeyes &             # une paire d'yeux doit apparaître sur votre Mac
```

Si `xeyes` n'est pas installé, `xclock` ou `xterm` font le même office. Une fois le test réussi, lancez votre vrai programme, par exemple un installateur Java graphique.

## Résoudre les erreurs courantes

### « X11 forwarding request failed on channel 0 »

Le serveur a refusé la demande. Vérifiez que `X11Forwarding yes` est bien actif (et que sshd a été rechargé) et que `xauth` est installé sur le serveur.

### « Error: Can't open display » ou « cannot connect to X server »

La variable `DISPLAY` est vide : la session n'a pas reçu le transfert d'affichage. Vérifiez que la case X11 est cochée, que XQuartz est installé, et que vous avez bien fermé puis rouvert votre session macOS après son installation. Après `sudo -i` ou `su`, la variable `DISPLAY` et le cookie `xauth` ne suivent pas : lancez le programme avec votre utilisateur de connexion.

### La fenêtre s'ouvre mais l'affichage est très lent

Les applications graphiques envoient beaucoup de données. Activez la compression (`-C`), réduisez la taille de la fenêtre et, si le programme le permet, désactivez les animations et le rendu 3D.

## Une précaution de sécurité

L'option `-Y` est le mode « de confiance » : les programmes du serveur peuvent, techniquement, observer ce qui se passe dans votre serveur X (par exemple la saisie clavier dans les autres fenêtres affichées par XQuartz). Réservez donc le X11 forwarding aux serveurs dont vous maîtrisez l'administration, et laissez-le désactivé pour les autres. C'est une option de chaque session : vous l'activez serveur par serveur.

Pour le reste de votre quotidien de serveur, voir [le client SFTP](./client-sftp-mac.md), [les tunnels SSH](./tunnel-ssh-mac.md) et [notre comparatif des outils pour Mac](./meilleure-alternative-mobaxterm-mac.md).

## Questions fréquentes

<details>
<summary>Pourquoi macOS ne gère-t-il pas X11 tout seul ?</summary>

Apple ne livre plus de serveur X avec macOS. XQuartz, un projet libre, joue ce rôle : c'est lui qui affiche les fenêtres envoyées par le serveur.

</details>

<details>
<summary>Eukalyptus embarque-t-il XQuartz ?</summary>

Non. XQuartz est gratuit et s'installe séparément : d'un clic depuis les réglages d'Eukalyptus (version 0.8.1 et suivantes), depuis xquartz.org ou avec Homebrew.

</details>

<details>
<summary>Quelle est la différence entre -X et -Y ?</summary>

Les deux transfèrent l'affichage. -X applique des restrictions de sécurité qui font parfois échouer des programmes ; -Y (« trusted ») est plus permissif et plus compatible. Eukalyptus utilise -Y.

</details>

<details>
<summary>Faut-il installer un environnement de bureau sur le serveur ?</summary>

Non. Seul le programme graphique que vous voulez lancer (et ses bibliothèques) est nécessaire, ainsi que l'outil xauth.

</details>
