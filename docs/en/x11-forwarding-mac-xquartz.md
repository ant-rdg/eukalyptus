---
title: "X11 forwarding on a Mac: show a server’s application with XQuartz"
description: "Show a Linux server’s graphical application on your Mac: install XQuartz, enable X11 forwarding and fix the common errors."
category: Tutorial
date: 2026-10-28
updated: 2026-10-29
reading_time: 7 min read
source: https://eukalyptus.app/en/blog/x11-forwarding-mac-xquartz
---

# X11 forwarding on a Mac: show a server’s application with XQuartz

A Java installer, a graphical admin tool, an Oracle database: some server programs only come with a window. X11 forwarding displays them on your Mac, through the SSH connection. Here is how to set it up with XQuartz and Eukalyptus, and what to do when it fails.

> **In short**
>
> - X11 forwarding sends the windows of a program running on the server to your Mac, over SSH.
> - You need XQuartz on the Mac (free) and xauth on the server.
> - In Eukalyptus: tick "X11 forwarding" in the SSH session's settings.
> - The most frequent errors come from a missing xauth or X11Forwarding turned off.

**In this article**

1. [How X11 forwarding works](#how-x11-forwarding-works)
2. [Install XQuartz on the Mac](#install-xquartz-on-the-mac)
3. [Prepare the server](#prepare-the-server)
4. [Turn it on in Eukalyptus](#turn-it-on-in-eukalyptus)
5. [Test with a small app](#test-with-a-small-app)
6. [Fix the common errors](#fix-the-common-errors)
7. [A security precaution](#a-security-precaution)
8. [Frequently asked questions](#frequently-asked-questions)

## How X11 forwarding works

On Linux, graphical applications talk to an "X server" that draws their windows. With X11 forwarding, the program runs on the remote server, but its display is sent through the [SSH](./ssh-client-mac.md) connection to the X server on your Mac: the window appears next to your other apps, while nothing but the program itself runs on the server.

*Diagram: X11 forwarding: a program runs on the server, its display goes through the SSH connection and appears on the Mac through XQuartz.*

| Your Mac |  | SSH connection |  | The server |
|---|---|---|---|---|
| XQuartz<br>shows the window | ← windows | encrypted<br>port 22 | ← display | runs the program<br>(xeyes, installer…) |

macOS no longer ships an X server. **XQuartz**, an open-source project, plays that role on the Mac. Eukalyptus doesn't bundle it: it relies on it.

## Install XQuartz on the Mac

The simplest way: in Eukalyptus (since version 0.8.1), **Settings › General › XQuartz › Install XQuartz…**. The same button appears if you open an X11 session without XQuartz. Eukalyptus downloads the official installer (XQuartz 2.8.6, from github.com), verifies its SHA-256 checksum and opens it in the macOS Installer, which in turn checks Apple's signature and notarization. Otherwise:

1. Download XQuartz from **xquartz.org** and install it, or run the command below if you use Homebrew.
2. Log out of macOS and log back in (or restart): the XQuartz installer asks for it, because it sets up the system's display variable.

*With Homebrew*

```sh
brew install --cask xquartz
```

## Prepare the server

Two things are needed on the server side, and they explain almost every failure:

- **X11 forwarding is allowed** in the sshd configuration: the line `X11Forwarding yes` in `/etc/ssh/sshd_config`, then a reload of the SSH service.
- **The `xauth` tool is installed**, because SSH uses it to create the display's authentication cookie.

*Install xauth (Debian, Ubuntu)*

```sh
sudo apt install xauth
```

*Install xauth (RHEL, Rocky, Fedora)*

```sh
sudo dnf install xorg-x11-xauth
```

## Turn it on in Eukalyptus

1. Open your server's **Session Settings** (SSH type).
2. Tick **"X11 forwarding (-Y, requires XQuartz)"** in the SSH options, then save.
3. Open the session: graphical programs started from the terminal are displayed in XQuartz.

Eukalyptus finds XQuartz's display by itself (the `DISPLAY` variable, launchd or the XQuartz socket). If XQuartz isn't installed, it offers to install it, instead of ssh's "X11 forwarding request failed".

On the command line, the equivalent is the `-Y` option. If the display is slow, also turn on **compression** (`-C`) in the same options: it helps on low-bandwidth connections.

*Command-line equivalent*

```sh
ssh -Y user@server.example.com
```

## Test with a small app

Once connected, first check that the display is forwarded, then run a simple program:

```sh
echo $DISPLAY      # should print something like localhost:10.0
xeyes &             # a pair of eyes should appear on your Mac
```

If `xeyes` isn't installed, `xclock` or `xterm` do the same job. Once the test works, run your real program, for example a graphical Java installer.

## Fix the common errors

### "X11 forwarding request failed on channel 0"

The server refused the request. Check that `X11Forwarding yes` is really active (and that sshd was reloaded) and that `xauth` is installed on the server.

### "Error: Can't open display" or "cannot connect to X server"

The `DISPLAY` variable is empty: the session didn't get display forwarding. Check that the X11 box is ticked, that XQuartz is installed, and that you logged out of macOS and back in after installing it. After `sudo -i` or `su`, the `DISPLAY` variable and the `xauth` cookie don't follow: run the program as the user you logged in with.

### The window opens but the display is very slow

Graphical applications send a lot of data. Turn on compression (`-C`), make the window smaller and, if the program allows it, turn off animations and 3D rendering.

## A security precaution

The `-Y` option is the "trusted" mode: the server's programs can, technically, observe what happens in your X server (for example keyboard input in the other windows shown by XQuartz). So keep X11 forwarding for servers whose administration you control, and leave it off for the others. It is a per-session option: you turn it on server by server.

For the rest of your day-to-day server work, see [the SFTP client](./sftp-client-mac.md), [SSH tunnels](./ssh-tunnel-mac.md) and [our comparison of Mac tools](./best-mobaxterm-alternative-mac.md).

## Frequently asked questions

<details>
<summary>Why doesn't macOS handle X11 by itself?</summary>

Apple no longer ships an X server with macOS. XQuartz, an open-source project, plays that role: it is what displays the windows sent by the server.

</details>

<details>
<summary>Does Eukalyptus bundle XQuartz?</summary>

No. XQuartz is free and installed separately: in one click from the Eukalyptus settings (version 0.8.1 and later), from xquartz.org or with Homebrew.

</details>

<details>
<summary>What is the difference between -X and -Y?</summary>

Both forward the display. -X applies security restrictions that sometimes make programs fail; -Y ("trusted") is more permissive and more compatible. Eukalyptus uses -Y.

</details>

<details>
<summary>Do I need to install a desktop environment on the server?</summary>

No. Only the graphical program you want to run (and its libraries) is needed, along with the xauth tool.

</details>
