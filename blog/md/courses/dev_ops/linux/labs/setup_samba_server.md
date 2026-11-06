#  Setting up a Samba Server

## Goal

In linux world, HTTP server (Web server), Samba server (File sharing server), SSH server and Email servers are a couple of important businesses and skills.
In our devOps, we would be able to only introduce you a couple of them, but the mindset is the same, that is, to get hands dirty and get very handson.

## What is Samba?

Samba is a free, open-source software suite that provides file and print services to SMB/CIFS clients, allowing interoperability between Unix/Linux and Windows machines. Here are some key aspects of Samba:

File and Print Sharing: Samba allows Unix/Linux systems to share files and printers with Windows clients and vice versa. It uses the SMB (Server Message Block) protocol, which is also known as CIFS (Common Internet File System).

Interoperability: Samba makes it possible for Unix/Linux systems to appear as Windows servers on a network, allowing seamless file sharing between different operating systems.

Domain Controller: Samba can function as a Primary Domain Controller (PDC) or a Backup Domain Controller (BDC) in a Windows NT domain. It can also join Active Directory as a member.

Authentication and Authorization: Samba can handle user authentication and authorization, integrating with various backend systems such as LDAP, Active Directory, and local Unix/Linux password files.

Network Browsing: Samba allows Unix/Linux machines to participate in Windows network browsing, making them visible in the Network Neighborhood or My Network Places on Windows machines.

Key Components of Samba smbd: The SMB/CIFS server daemon that provides file and print services to SMB/CIFS clients.

nmbd: The NetBIOS name server daemon that handles NetBIOS name resolution and browsing.

winbindd: This service allows for the integration of Unix/Linux systems with Windows NT-based systems, enabling domain authentication.

Common Use Cases Home Networks: Sharing files and printers between different operating systems within a home network. Office Networks: Centralized file and print services in mixed OS environments, often replacing or supplementing Windows servers. Domain Services: Acting as a domain controller in small to medium-sized networks.

## Installation

To start a Samba server (also known as a Samba "driver") on a Linux system, you need to install the Samba package, configure it, and then start the Samba services. Here's a step-by-step guide:

```
sudo apt update
sudo apt install samba
```

## Configuration
Configure Samba:
Edit the Samba configuration file `/etc/samba/smb.conf` to define your shared directories and settings. 

For example:

```
[shared]
path = /srv/samba/shared
read only = no
browsable = yes
```

## Create the Shared Directory

```
sudo mkdir -p /srv/samba/shared
sudo chown nobody:nogroup /srv/samba/shared
sudo chmod 0775 /srv/samba/shared
```

## Add Samba Users

Add a user to Samba (the user must already exist on the system):

```
sudo smbpasswd -a username
```

## Start the Samba Services

```
sudo systemctl restart smbd
sudo systemctl enable smbd
sudo systemctl restart nmbd
sudo systemctl enable nmbd
```

## Verify the Samba Configuration

Check the Samba configuration for any syntax errors, testparm.

## Access the Share
From a Windows machine or another Samba client, you can access the share by navigating to \\hostname\shared where hostname is the name of your Samba server.
for Example, from Mac, you can do this,

`smb://xiaofengli@192.168.0.105`

## Check logs

If you encounter any issues, checking the Samba logs can be helpful. They are usually located in `/var/log/samba/`
