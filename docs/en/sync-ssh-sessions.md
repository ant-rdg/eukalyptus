---
title: "Sync your SSH sessions between Mac and Windows, end-to-end encrypted"
description: "Session sync is available since version 0.9.0 on Mac, with Eukalyptus+: end-to-end encrypted on your devices, through a temporary relay on the Eukalyptus server that cannot read anything. With Windows once its version is out. The principle and how to check it."
category: Guide
date: 2026-11-01
updated: 2026-11-03
reading_time: 7 min read
source: https://eukalyptus.app/en/blog/sync-ssh-sessions
---

# Sync your SSH sessions between Mac and Windows, end-to-end encrypted

If you manage servers from a Mac and a Windows PC, you end up copying your sessions by hand. Eukalyptus sync, available since version 0.9.0, keeps them up to date on all your devices: everything is encrypted on the device before it leaves, and the Eukalyptus server is only a temporary relay that cannot read anything. It is reserved for Eukalyptus+. Here is how it works, and how to check it.

> **In short**
>
> - It is available since version 0.9.0, between your Macs, and it is reserved for Eukalyptus+, like the team vault. With Windows, it will work once the Windows version is out.
> - No account. The files go through the Eukalyptus server, a simple temporary relay, and are deleted from it at the latest 365 days after their last modification. No iCloud, no Dropbox, no OneDrive, no SFTP.
> - Everything is end-to-end encrypted on your devices, with a key only your devices have: the server cannot read the files.
> - An administrator or an attacker of the server can hold back or delete files, never read them or modify them without detection. If you lose the key and all your devices, nobody can recover the data.

**In this article**

1. [What version 0.9.0 brings](#what-version-090-brings)
2. [The problem: two machines, one set of sessions](#the-problem-two-machines-one-set-of-sessions)
3. [The principle: a temporary relay, unreadable to us](#the-principle-a-temporary-relay-unreadable-to-us)
4. [Encrypted before it leaves, with a key only you have](#encrypted-before-it-leaves-with-a-key-only-you-have)
5. [What each party sees, and what an attacker can do](#what-each-party-sees-and-what-an-attacker-can-do)
6. [If you lose the key](#if-you-lose-the-key)
7. [Check it yourself](#check-it-yourself)
8. [The team vault, through the same relay](#the-team-vault-through-the-same-relay)
9. [Without sync: export and import](#without-sync-export-and-import)
10. [What is decided, what is still open](#what-is-decided-what-is-still-open)
11. [Frequently asked questions](#frequently-asked-questions)

## What version 0.9.0 brings

A clarification first, so there is no doubt: **session sync is available since version 0.9.0 for Mac**, and it is reserved for Eukalyptus+. Between a Mac and a Windows PC, it will work with the Windows version, which is not out yet. This article describes the chosen principle, so that you can judge it before trusting it with anything.

## The problem: two machines, one set of sessions

A Mac at the office, a Windows PC at home, a spare laptop: for every new server you have to recreate the session elsewhere, or export and import a file. Typical sync services solve this by storing your data, readable, with their publisher. For a list of servers, sometimes with credentials, that is a lot of trust to place in a third party, and a prime target for an attacker.

Eukalyptus takes another road: the files are encrypted on your devices before they leave, with a key the server never has. The Eukalyptus server is only a temporary mailbox, and it cannot read what it keeps.

## The principle: a temporary relay, unreadable to us

Your devices exchange files through the Eukalyptus server. For each group of devices, it keeps the latest encrypted file of each device, and the other devices come and fetch it. The mailbox and its access right are computed from the sync key, which only your devices have: there is no account to create.

*Diagram: Sync: a Mac encrypts its sessions and sends them to the Eukalyptus server, a simple temporary relay where they stay unreadable; your other device (another Mac, then a Windows PC with the Windows version) fetches them and decrypts them with the same key.*

| Your Mac |  | Eukalyptus server |  | Your other device |
|---|---|---|---|---|
| encrypts before<br>sending | encrypted files → | temporary relay,<br>unreadable files | encrypted files → | decrypts with<br>the same key |

What this means:

- **A limited lifetime.** Each file is deleted from the server at the latest 365 days after its last modification. An active device rewrites it at every change, and at least every 7 days.
- **Your data stays on your devices.** The relay is only a place to pass through: if it is empty, the first device to come back republishes its file.
- **No third-party storage.** No iCloud, no Dropbox, no OneDrive, no SFTP: the Eukalyptus server is the only transport.
- **Reserved for Eukalyptus+.** Writing to the relay requires a valid Eukalyptus+ license; without one, the app explains it. The team vault is in the same case.

The Eukalyptus website is contacted for updates, the license, the install counter (once) and, since version 0.9.0, for the relay if you turn sync on: the exact list is on the [Security](https://eukalyptus.app/en/security) page.

## Encrypted before it leaves, with a key only you have

Encryption happens **on the device**, before a single byte goes to the server. The key exists only on your devices: the server and Eukalyptus don't have it. That is what end-to-end encryption means.

It relies on libsodium, a well-regarded cryptography library. Eukalyptus invents no algorithm.

To add a new device, you give it the same key: it is what lets it read what the others put there. Without it, the device only sees unreadable data.

## What each party sees, and what an attacker can do

In practice, here is what each party can see:

- **The Eukalyptus server** sees a random mailbox identifier, the number of devices, the size and date of the files, and the IP address of the requests (in its logs, 60 days at most). It never sees a server name, a session or a password.
- **Cloudflare**, through which all the website's traffic goes, sees the IP address and the size of the requests, as for any page, and nothing readable in the files.
- **Your devices** decrypt with the key and get the sessions back.

And if the server were compromised, or its administrator malicious? They could **hold back or delete files**. Your devices keep their data: nothing is lost, and they republish their files. They could **neither read them nor modify them without detection**: each file is authenticated, and a device refuses any file that was modified, forged or rolled back to an older version.

## If you lose the key

This is the other side of encryption where nobody else holds the key: **if you lose the key and all your devices, nobody can recover the data**. Not you, not the publisher, who has nothing to open. As long as one device is left, nothing is lost. When you turn sync on, the app tells you so clearly: keep the key somewhere safe, such as your password manager.

## Check it yourself

End-to-end encryption shouldn't be taken on faith. Here is how to check it without trusting us:

1. **Watch the network.** An application firewall such as Little Snitch on Mac, or simplewall on Windows, shows who the app talks to. It contacts the Eukalyptus website only for updates, the license, the install counter and, if you turn it on, the relay: everything is listed on the [Security](https://eukalyptus.app/en/security) page. What it sends there is an unreadable series of bytes.
2. **Read the format.** It will be published, with sample files: anyone will be able to write a small program that decrypts them, and check that the key is really needed, and that a modified file is refused.
3. **Check the building blocks.** libsodium, a well-regarded library, and no home-made cryptography.

## The team vault, through the same relay

The team vault also goes through the Eukalyptus server, with the same guarantees. Each team file is encrypted and signed by its author on their device, with one key per shared folder, and the server reads none of them. It deletes them at the latest 365 days after their last write; an active member resends, unchanged, the ones nearing their end, which keeps them on the relay. The publisher has no more access to a team's data than to a single person's. Like sync, it is reserved for Eukalyptus+: writing to the vault requires a license.

## Without sync: export and import

Without Eukalyptus+, or to move to a Windows PC until its version is out, you can move between machines by hand: export your sessions to an **.eukalyptus** file, then import it on the other device. That export contains no password. Your SSH keys stay in your agent or your **.ssh** folder, as with any client: see the [SSH keys guide](./ssh-keys-mac.md).

## What is decided, what is still open

What is settled:

- no account; the files go through the Eukalyptus server, a simple temporary relay, end-to-end encrypted, and the server cannot read them;
- files deleted at the latest 365 days after their last modification, and no third-party storage (no iCloud, no Dropbox, no OneDrive, no SFTP);
- sync and the team vault are reserved for Eukalyptus+, whose price does not change;
- the sync key is generated at random by the app (not a password you make up); it is shown once, as a QR code and in groups of characters, to print or keep in your password manager, and you scan or type it on the new device;
- passwords are synced by default, and you choose what is synced, category by category;
- a published format you can check.

**Our servers only pass things along.** Everything that goes through them is end-to-end encrypted on your devices before it leaves: the server only sees unreadable data, without the key to open it. Nothing is kept there more than 365 days after its last change, and your data stays on your devices. Still open: sync with Windows, which waits for the Windows version to be out. The principle is also summarized on the [Security](https://eukalyptus.app/en/security#sync) page.

## Frequently asked questions

<details>
<summary>Is sync available?</summary>

Yes, since version 0.9.0 of Eukalyptus for Mac, with Eukalyptus+. Between a Mac and a Windows PC, it will work with the Windows version, which is not out yet.

</details>

<details>
<summary>Do I need Eukalyptus+?</summary>

Yes, for sync and for the team vault: writing to the relay requires an Eukalyptus+ license. The rest of Eukalyptus stays free. The price of Eukalyptus+ does not change.

</details>

<details>
<summary>Do I need a Eukalyptus account?</summary>

No. There is no account: the relay mailbox and its access right are computed from the sync key, which only your devices have.

</details>

<details>
<summary>Do my files go through a Eukalyptus server?</summary>

Yes, through a simple temporary relay. The files arrive already end-to-end encrypted, the server cannot read them, and it deletes them at the latest 365 days after their last modification.

</details>

<details>
<summary>Can Eukalyptus's publisher read my sessions?</summary>

No. The server only keeps files encrypted with a key it doesn't have. It sees a random mailbox identifier, the number of devices, the size and date of the files, and the IP address of the requests. It never sees a server name, a session or a password.

</details>

<details>
<summary>What can an attacker who takes control of the server do?</summary>

Hold back or delete files. They cannot read them or modify them without detection: your devices keep their data and refuse any modified or forged file.

</details>

<details>
<summary>What happens if I don't open Eukalyptus for more than 365 days?</summary>

The device's file is deleted from the relay, but nothing is lost: your data is on your devices, and the first one to come back republishes its file.

</details>

<details>
<summary>What happens if I lose my key and all my devices?</summary>

Nobody can recover your data: not you, not the publisher. That is the other side of real end-to-end encryption. Keep the key somewhere safe, for example in your password manager.

</details>

<details>
<summary>Are my passwords synced?</summary>

Yes, by default, since they are end-to-end encrypted like everything else. You choose what is synced, category by category. Your private SSH keys are never synced.

</details>
