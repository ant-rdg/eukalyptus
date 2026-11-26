---
title: "Synchroniser ses sessions SSH entre Mac et Windows, chiffrées de bout en bout"
description: "La synchronisation des sessions est disponible depuis la version 0.9.0 sur Mac, avec Eukalyptus+ : chiffrée de bout en bout sur vos appareils, par un relais temporaire du serveur d'Eukalyptus qui ne peut rien lire. Avec Windows, quand sa version sortira. Le principe et comment le vérifier."
category: Guide
date: 2026-11-01
updated: 2026-11-03
reading_time: 7 min
source: https://eukalyptus.app/blog/synchroniser-sessions-ssh
---

# Synchroniser ses sessions SSH entre Mac et Windows, chiffrées de bout en bout

Quand on administre des serveurs depuis un Mac et un PC Windows, on finit par recopier ses sessions à la main. La synchronisation d'Eukalyptus, disponible depuis la version 0.9.0, les garde à jour sur tous vos appareils : tout est chiffré sur l'appareil avant de partir, et le serveur d'Eukalyptus ne sert que de relais temporaire, sans pouvoir rien lire. Elle est réservée à Eukalyptus+. Voici comment elle fonctionne, et comment la vérifier.

> **En bref**
>
> - Elle est disponible depuis la version 0.9.0, entre vos Mac, et elle est réservée à Eukalyptus+, comme le coffre d'équipe. Avec Windows, elle fonctionnera quand la version Windows sortira.
> - Pas de compte. Les fichiers passent par le serveur d'Eukalyptus, simple relais temporaire, et y sont effacés au plus tard 365 jours après leur dernière modification. Ni iCloud, ni Dropbox, ni OneDrive, ni SFTP.
> - Tout est chiffré de bout en bout sur vos appareils, avec une clé que seuls vos appareils possèdent : le serveur ne peut pas lire les fichiers.
> - Un administrateur ou un attaquant du serveur peut retenir ou effacer des fichiers, jamais les lire ni les modifier sans détection. Si vous perdez la clé et tous vos appareils, personne ne peut récupérer les données.

**Dans cet article**

1. [Ce qu'apporte la version 0.9.0](#ce-quapporte-la-version-090)
2. [Le problème : deux machines, un seul jeu de sessions](#le-problème--deux-machines-un-seul-jeu-de-sessions)
3. [Le principe : un relais temporaire, illisible pour nous](#le-principe--un-relais-temporaire-illisible-pour-nous)
4. [Chiffré avant de partir, avec une clé que vous seul avez](#chiffré-avant-de-partir-avec-une-clé-que-vous-seul-avez)
5. [Ce que chacun voit, et ce qu'un attaquant peut faire](#ce-que-chacun-voit-et-ce-quun-attaquant-peut-faire)
6. [Si vous perdez la clé](#si-vous-perdez-la-clé)
7. [Le vérifier par vous-même](#le-vérifier-par-vous-même)
8. [Le coffre d'équipe, par le même relais](#le-coffre-déquipe-par-le-même-relais)
9. [Sans synchronisation : exporter et importer](#sans-synchronisation--exporter-et-importer)
10. [Ce qui est décidé, ce qui reste ouvert](#ce-qui-est-décidé-ce-qui-reste-ouvert)
11. [Questions fréquentes](#questions-fréquentes)

## Ce qu'apporte la version 0.9.0

Une précision d'abord, pour ne laisser aucun doute : **la synchronisation des sessions est disponible depuis la version 0.9.0 pour Mac**, et elle est réservée à Eukalyptus+. Entre un Mac et un PC Windows, elle fonctionnera avec la version Windows, qui n'est pas encore sortie. Cet article décrit le principe retenu, pour que vous puissiez le juger avant d'y confier quoi que ce soit.

## Le problème : deux machines, un seul jeu de sessions

Un Mac au bureau, un PC Windows à la maison, un portable de dépannage : à chaque nouveau serveur, il faut recréer la session ailleurs, ou exporter puis importer un fichier. Les services de synchronisation classiques règlent cela en stockant vos données, lisibles, chez leur éditeur. Pour une liste de serveurs, avec parfois des identifiants, c'est beaucoup de confiance à accorder à un tiers, et une cible de choix pour un attaquant.

Eukalyptus prend un autre chemin : les fichiers sont chiffrés sur vos appareils avant de partir, avec une clé que le serveur n'a jamais. Le serveur d'Eukalyptus n'est qu'une boîte aux lettres temporaire, et il ne peut pas lire ce qu'il garde.

## Le principe : un relais temporaire, illisible pour nous

Vos appareils échangent des fichiers à travers le serveur d'Eukalyptus. Pour chaque groupe d'appareils, il garde le dernier fichier chiffré de chaque appareil, et les autres appareils viennent le récupérer. La boîte et son droit d'accès sont calculés à partir de la clé de synchronisation, que seuls vos appareils possèdent : il n'y a pas de compte à créer.

*Schéma : Synchronisation : un Mac chiffre ses sessions et les envoie au serveur d'Eukalyptus, simple relais temporaire où elles restent illisibles ; votre autre appareil (un autre Mac, puis un PC Windows avec la version Windows) les récupère et les déchiffre avec la même clé.*

| Votre Mac |  | Serveur Eukalyptus |  | Votre autre appareil |
|---|---|---|---|---|
| chiffre avant<br>l'envoi | fichiers chiffrés → | relais temporaire,<br>fichiers illisibles | fichiers chiffrés → | déchiffre avec<br>la même clé |

Ce que cela implique :

- **Une durée de vie limitée.** Chaque fichier est effacé du serveur au plus tard 365 jours après sa dernière modification. Un appareil actif le réécrit à chaque changement, et au moins tous les 7 jours.
- **Vos données restent sur vos appareils.** Le relais n'est qu'un lieu de passage : s'il est vide, le premier appareil qui revient republie son fichier.
- **Aucun stockage tiers.** Ni iCloud, ni Dropbox, ni OneDrive, ni SFTP : le serveur d'Eukalyptus est le seul transport.
- **Réservée à Eukalyptus+.** Écrire sur le relais demande une licence Eukalyptus+ valide ; sans licence, l'application l'explique. Le coffre d'équipe est dans le même cas.

Le site d'Eukalyptus est contacté pour les mises à jour, la licence, le compteur d'installations (une seule fois) et, depuis la version 0.9.0, pour le relais si vous activez la synchronisation : la liste exacte est sur la page [Sécurité](https://eukalyptus.app/securite).

## Chiffré avant de partir, avec une clé que vous seul avez

Le chiffrement se fait **sur l'appareil**, avant que le moindre octet ne parte vers le serveur. La clé n'existe que sur vos appareils : le serveur et Eukalyptus n'en ont pas. C'est ce qu'on appelle le chiffrement de bout en bout.

Il repose sur libsodium, une bibliothèque de cryptographie reconnue. Eukalyptus n'invente aucun algorithme.

Pour ajouter un nouvel appareil, vous lui donnez la même clé : c'est elle qui lui permet de lire ce que les autres déposent. Sans elle, il ne voit que des données illisibles.

## Ce que chacun voit, et ce qu'un attaquant peut faire

Concrètement, voici ce que chacun peut voir :

- **Le serveur d'Eukalyptus** voit un identifiant de boîte aléatoire, le nombre d'appareils, la taille et la date des fichiers, et l'adresse IP des requêtes (dans ses journaux, 60 jours au plus). Il ne voit jamais un nom de serveur, une session ou un mot de passe.
- **Cloudflare**, par lequel passe tout le trafic du site, voit l'adresse IP et la taille des requêtes, comme pour n'importe quelle page, et rien de lisible dans les fichiers.
- **Vos appareils** déchiffrent avec la clé et retrouvent les sessions.

Et si le serveur était compromis, ou si son administrateur était malveillant ? Il pourrait **retenir ou effacer des fichiers**. Vos appareils gardent leurs données : rien n'est perdu, et ils republient leurs fichiers. Il ne pourrait **ni les lire, ni les modifier sans détection** : chaque fichier est authentifié, et l'appareil refuse tout fichier modifié, fabriqué ou ramené à une version plus ancienne.

## Si vous perdez la clé

C'est la contrepartie d'un chiffrement dont personne d'autre ne détient la clé : **si vous perdez la clé et tous vos appareils, personne ne peut récupérer les données**. Ni vous, ni l'éditeur, qui n'a rien à ouvrir. Tant qu'il vous reste un appareil, rien n'est perdu. À l'activation, l'application vous le dit clairement : conservez la clé à un endroit sûr, comme votre gestionnaire de mots de passe.

## Le vérifier par vous-même

Un chiffrement de bout en bout ne doit pas se croire sur parole. Voici de quoi le contrôler, sans nous faire confiance :

1. **Observez le réseau.** Un pare-feu d'application comme Little Snitch sur Mac, ou simplewall sous Windows, montre à qui l'application parle. Elle ne contacte le site d'Eukalyptus que pour les mises à jour, la licence, le compteur d'installations et, si vous l'activez, le relais : tout est listé sur la page [Sécurité](https://eukalyptus.app/securite). Ce qu'elle y envoie est une suite d'octets illisible.
2. **Lisez le format.** Il sera publié, avec des fichiers d'exemple : n'importe qui pourra écrire un petit programme qui les déchiffre, et vérifier qu'il faut bien la clé, et qu'un fichier modifié est refusé.
3. **Vérifiez les briques.** libsodium, une bibliothèque reconnue, et aucune cryptographie maison.

## Le coffre d'équipe, par le même relais

Le coffre d'équipe passe lui aussi par le serveur d'Eukalyptus, avec les mêmes garanties. Chaque fichier de l'équipe est chiffré et signé par son auteur sur son appareil, avec une clé par dossier partagé, et le serveur n'en lit aucun. Il les efface au plus tard 365 jours après leur dernière écriture ; un membre actif renvoie à l'identique ceux qui approchent de leur fin, ce qui les garde sur le relais. L'éditeur n'a pas plus accès aux données d'une équipe qu'à celles d'une personne seule. Comme la synchronisation, il est réservé à Eukalyptus+ : écrire dans le coffre demande une licence.

## Sans synchronisation : exporter et importer

Sans Eukalyptus+, ou pour passer à un PC Windows tant que sa version n'est pas sortie, vous pouvez passer d'une machine à l'autre à la main : exportez vos sessions dans un fichier **.eukalyptus**, puis importez-le sur l'autre appareil. Cet export ne contient aucun mot de passe. Vos clés SSH, elles, restent dans votre agent ou votre dossier **.ssh**, comme avec n'importe quel client : voir [le guide des clés SSH](./cles-ssh-mac.md).

## Ce qui est décidé, ce qui reste ouvert

Ce qui est arrêté :

- pas de compte ; les fichiers passent par le serveur d'Eukalyptus, simple relais temporaire, chiffrés de bout en bout, et le serveur ne peut pas les lire ;
- des fichiers effacés au plus tard 365 jours après leur dernière modification, et aucun stockage tiers (ni iCloud, ni Dropbox, ni OneDrive, ni SFTP) ;
- la synchronisation et le coffre d'équipe sont réservés à Eukalyptus+, dont le prix ne change pas ;
- la clé de synchronisation est créée au hasard par l'app (ce n'est pas un mot de passe à inventer) ; elle s'affiche une seule fois, en QR code et en groupes de caractères, à imprimer ou à ranger dans votre gestionnaire de mots de passe, et se scanne ou se tape sur le nouvel appareil ;
- les mots de passe sont synchronisés par défaut, et vous choisissez ce qui l'est, catégorie par catégorie ;
- un format publié, qui se vérifie.

**Nos serveurs ne font que transmettre.** Ce qui y passe est chiffré de bout en bout sur vos appareils avant de partir : le serveur ne voit que des données illisibles, sans la clé pour les ouvrir. Rien n'y est gardé plus de 365 jours après sa dernière modification, et vos données, elles, restent sur vos appareils. Ce qui reste ouvert : la synchronisation avec Windows, qui attend la sortie de la version Windows. Ce principe est aussi résumé sur la page [Sécurité](https://eukalyptus.app/securite#synchronisation).

## Questions fréquentes

<details>
<summary>La synchronisation est-elle disponible ?</summary>

Oui, depuis la version 0.9.0 d'Eukalyptus pour Mac, avec Eukalyptus+. Entre un Mac et un PC Windows, elle fonctionnera avec la version Windows, qui n'est pas encore sortie.

</details>

<details>
<summary>Faut-il Eukalyptus+ ?</summary>

Oui, pour la synchronisation et pour le coffre d'équipe : écrire sur le relais demande une licence Eukalyptus+. Le reste d'Eukalyptus reste gratuit. Le prix d'Eukalyptus+ ne change pas.

</details>

<details>
<summary>Faut-il créer un compte Eukalyptus ?</summary>

Non. Il n'y a pas de compte : la boîte du relais et son droit d'accès sont calculés à partir de la clé de synchronisation, que seuls vos appareils possèdent.

</details>

<details>
<summary>Mes fichiers passent-ils par un serveur d'Eukalyptus ?</summary>

Oui, par un simple relais temporaire. Les fichiers y arrivent déjà chiffrés de bout en bout, le serveur ne peut pas les lire, et il les efface au plus tard 365 jours après leur dernière modification.

</details>

<details>
<summary>L'éditeur d'Eukalyptus peut-il lire mes sessions ?</summary>

Non. Le serveur ne garde que des fichiers chiffrés avec une clé qu'il n'a pas. Il voit un identifiant de boîte aléatoire, le nombre d'appareils, la taille et la date des fichiers, et l'adresse IP des requêtes. Il ne voit jamais un nom de serveur, une session ou un mot de passe.

</details>

<details>
<summary>Que peut faire un attaquant qui prendrait le contrôle du serveur ?</summary>

Retenir ou effacer des fichiers. Il ne peut ni les lire ni les modifier sans que ce soit détecté : vos appareils gardent leurs données et refusent tout fichier modifié ou fabriqué.

</details>

<details>
<summary>Que se passe-t-il si je n'ouvre pas Eukalyptus pendant plus de 365 jours ?</summary>

Le fichier de l'appareil est effacé du relais, mais rien n'est perdu : vos données sont sur vos appareils, et le premier qui revient republie son fichier.

</details>

<details>
<summary>Que se passe-t-il si je perds ma clé et tous mes appareils ?</summary>

Personne ne peut récupérer vos données : ni vous, ni l'éditeur. C'est la contrepartie d'un vrai chiffrement de bout en bout. Gardez la clé en lieu sûr, par exemple dans votre gestionnaire de mots de passe.

</details>

<details>
<summary>Mes mots de passe sont-ils synchronisés ?</summary>

Oui, par défaut, puisqu'ils sont chiffrés de bout en bout comme le reste. Vous choisissez ce qui est synchronisé, catégorie par catégorie. Vos clés SSH privées ne sont jamais synchronisées.

</details>
