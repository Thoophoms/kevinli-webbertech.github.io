# Linux Desktop Environment

## Outline

* Window Display Manager
    * GDM
    * KDE
    * Xfce

* Display protocol
    * Wayland
    * X11/X Server

## GNOME

GNOME is used both by Fedora and Ubuntu.
Nautilus offers a simple and integrated way of managing files and browsing the file system.

- Activities overview
- GNOME Software Center- GNOME Commander: a free open source graphic file manager for linux desktop.
- GNOME Display Manager (GDM): A display manager (a graphical login manager) for the windowing systems X11 and Wayland
- Mutter:A portmanteau of "Metacity" and "Clutter", Mutter can function as a standalone window manager for GNOME-like desktops

### Nautilus

Files, also known as Nautilus, is the default file manager of the GNOME desktop. It provides a simple and integrated way of managing your files and browsing your file system.

Nautilus supports all the basic functions of a file manager and more. It can search and manage your files and folders, both locally and on a network, read and write data to and from removable media, run scripts, and launch apps. It has three views: Icon Grid, Icon List, and Tree List. Its functions can be extended with plugins and scripts.

More information can be found here,

https://apps.gnome.org/Nautilus/#:~:text=Files%2C%20also%20known%20as%20Nautilus,a%20file%20manager%20and%20more

### GDM

GNOME Display Manager (GDM) is a display manager (a graphical login manager) for the windowing systems X11 and Wayland. GDM was written from scratch and does not contain any XDM or X Consortium code.

The X Window System by default uses the XDM display manager. However, resolving XDM configuration issues typically involves editing a configuration file. GDM allows users to customize or troubleshoot settings without having to resort to a command line. 

GDM comprises the following components:

- Chooser – a program used to select a remote host as the source for a remote display on the attached display (gdm-host-chooser)
- Greeter – the graphical login window (provided by GNOME Shell)
- Pluggable authentication module (PAM)
- X Display Manager Control Protocol (XDMCP)

#### PAM

A pluggable authentication module (PAM) is a mechanism to integrate multiple low-level authentication schemes into a high-level application programming interface (API).

PAM allows programs that rely on authentication to be written independently of the underlying authentication scheme.

![pam architecture](https://kevinli-webbertech.github.io/blog/images/linux/pam.png)

History,

* 1995: It was first proposed by Sun Microsystems in an Open Software Foundation Request for Comments (RFC) 86.0 dated October 1995.

* 1996: It was adopted as the authentication framework of the Common Desktop Environment. As a stand-alone open-source infrastructure, PAM first appeared in Red Hat Linux 3.0.4 in August 1996 in the Linux PAM project. 

* X/Open Single Sign-on (XSSO) 
Since no central standard of PAM behavior exists, there was a later attempt to standardize PAM as part of the X/Open UNIX standardization process, resulting in the X/Open Single Sign-on (XSSO) standard.

* OpenPAM
This standard was not ratified, but the standard draft has served as a reference point for later PAM implementations (for example, OpenPAM).

#### X Display Manager Control Protocol (XDMCP)

* In X window System, the X server runs.

* The X window display manager offers a graphics login manager to start a login session to ask users for username and password.

* The X window display manager acts to do the same functionality as the getty and login on character-mode terminals.

* The X window display manager can connect remotely, then it acts like a telnet server.

* The XDM (the X Window Display Manager) originated in X11R3.

It only reads from Xservers file thus every time a user switched a terminal off and on, it will not know. In X11R4, with XDMCP, the X server must actively request a display manager connection from the host. An X server using XDMCP therefore no longer requires an entry in Xservers.

1988: X11 Release 3 introduced display managers in October 1988 with the aim of supporting the standalone X terminals, just coming onto the market.

1989: X11R4 introduced the X Display Manager Control Protocol (XDMCP) in December 1989 to fix problems in the X11R3 implementation.

* The X Display Manager Control Protocol (XDMCP) uses UDP port 177.

And it keeps a secret key and have a hand-shake package with the X server to authenticate itself. When the session is established, during the session, the server can send KeepAlive packets to the display manager at intervals.  If the display manager fails to respond with an Alive packet within a certain time, the X server presumes that the display manager has ceased running, and can terminate the connection.

* XDMCP security concern.

One problem with XDMCP is that, similarly to telnet, the authentication takes place unencrypted.

### ref

- https://www.gnome.org/
- https://apps.gnome.org/Nautilus/#:~:text=Files%2C%20also%20known%20as%20Nautilus,a%20file%20manager%20and%20more.
- https://extensions.gnome.org/
- https://en.wikipedia.org/wiki/Pluggable_authentication_module

## KDE

KDE is an international free software community that develops free and open-source software. As a central development hub, it provides tools and resources that allow collaborative work on this kind of software. Well-known products include the Plasma Desktop, KDE Frameworks, and a range of cross-platform applications such as Amarok, digiKam, and Krita that are designed to run on Unix and Unix-like operating systems, Microsoft Windows, and Android.

KDE was founded in 1996 by Matthias Ettrich, a student at the University of Tübingen.
In the beginning Matthias Ettrich chose to use Trolltech's Qt framework for the KDE project. Other programmers quickly started developing KDE/Qt applications, and by early 1997, a few applications were being released. On 12 July 1998 the first version of the desktop environment, called KDE 1.0, was released. The original GPL licensed version of this toolkit only existed for platforms which used the X11 display server, but with the release of Qt 4, LGPL licensed versions are available for more platforms. This allowed KDE software based on Qt 4 or newer versions to theoretically be distributed to Microsoft Windows and OS X.

The KDE Marketing Team announced a rebranding of the KDE project components on 24 November 2009. Motivated by the perceived shift in objectives, the rebranding focused on emphasizing both the community of software creators and the various tools supplied by the KDE, rather than just the desktop environment.

What was previously known as KDE 4 was split into KDE Plasma Workspaces, KDE Applications, and KDE Platform (now KDE Frameworks) bundled as KDE Software Compilation 4. Since 2009, the name KDE no longer stands for K Desktop Environment, but for the community that produces the software.

### ref

- https://en.wikipedia.org/wiki/KDE
- https://kde.org/
- https://kdeconnect.kde.org/
- https://neon.kde.org/
- https://kde.org/plasma-desktop/

## xfce

### ref
- https://www.vpsserver.com/gnome-vs-xfce-vs-kde/#:~:text=KDE%2C%20GNOME%2C%20and%20Xfce%20are,of%20the%20Unix%20operating%20system.

- https://1gbits.com/blog/best-linux-desktop-environment/#:~:text=The%20most%20well%2Dknown%20Linux,be%20user%2Dfriendly%20and%20adaptable.

- https://www.vpsserver.com/gnome-vs-xfce-vs-kde/#:~:text=Xfce%20is%20faster%20than%20KDE,quicker%20desktop%20environment%20than%20GNOME.

- https://cloudzy.com/blog/linux-mint-cinnamon-vs-mate-vs-xfce/#:~:text=Unlike%20Linux%20Mint%20Cinnamon%20and,but%20has%20its%20own%20libraries.

- https://alternativeto.net/software/gnome/

## Common XDM

* GDM, GNOME implemation
* KDM, KDE implementation
* SDDM, KDE Plasma 5 and LXQt. Successor to KDM.
* LightDM, a lightweight, modular, cross-desktop, fully themeable desktop display manager by Canonical Ltd.
* TWin, the TDE window manager
* dtlogin (shipped with CDE)
* xlogin display manager, a lightweight, secure and login like console display manager for X, written in C.

Note: `Source coming from Wikipedia`

#### ref
- https://en.wikipedia.org/wiki/X_display_manager#XDMCP

## X11/X Server

The X Window System (X11, or simply X) is a windowing system for bitmap displays, common on Unix-like operating systems.

X originated as part of Project Athena at Massachusetts Institute of Technology (MIT) in 1984. The *X protocol* has been at version 11 (hence "X11") since September 1987. The X.Org Foundation leads the X project, with the current reference implementation, X.Org Server, available as free and open-source software under the MIT License and similar permissive licenses.

![x server](https://kevinli-webbertech.github.io/blog/images/linux/xserver.png)

### ref

- https://www.x.org/releases/X11R7.6/doc/man/man1/Xserver.1.xhtml


## Wayland

Wayland is a communication protocol that specifies the communication between a display server and its clients, as well as a C library implementation of that protocol. A display server using the Wayland protocol is called a Wayland compositor, because it additionally performs the task of a compositing window manager.

Wayland is developed by a group of volunteers initially led by Kristian Høgsberg as a free and open-source community-driven project with the aim of replacing the X Window System with a secure and simpler windowing system for Linux and other Unix-like operating systems. The project's source code is published under the terms of the MIT License, a permissive free software licence.

As part of its efforts, the Wayland project also develops a reference implementation of a Wayland compositor called Weston.

### Check the XDM

- Display Environment Variable: `echo $DISPLAY` and `echo $XDG_SESSION_TYPE`
- Check process: `ps aux | grep [X]` or `ps aux | grep [w]ayland`
- Using loginctl Command: `$ loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type`

```shell
xiaofengli@xiaofenglx:~$ wmctrl -m
Name: GNOME Shell
Class: N/A
PID: N/A
Window manager's "showing the desktop" mode: OFF
xiaofengli@xiaofenglx:~$ echo $XDG_SESSION_TYPE
wayland
```

### Troubleshooting UI issues

Try resetting gdm to the default values

Disable screen magnifier in GDM:

`sudo -u gdm gconftool-2 --recursive-unset /desktop`

Disable on-screen keyboard in GDM:

`sudo -u gdm gconftool-2 /desktop/gnome/applications/at/screen_magnifier_enabled --type bool --set false`


## Switch from Wayland to X11

If you wish to do it permanently, edit /etc/gdm3/custom.conf and uncomment the line:

`#WaylandEnable=false`

#### ref

https://askubuntu.com/questions/6217/disabling-assistive-technologies-during-login