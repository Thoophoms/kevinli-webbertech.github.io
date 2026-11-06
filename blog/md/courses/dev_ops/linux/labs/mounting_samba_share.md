In-class Tutorial: Setup Samba Client to access the shared folder

## Goal:
In the previous tutorial: setup_samba_server.pdf, we learn how to set up a samba server, it is similar to other web server(apache2/apached), or ssh server (sshd). It is providing a shared directory for other machines to access. See this a file server like google dropbox or box.com services. 

Now in this tutorial, we teach you how to set up a client that is in your client machine, a second VM possibly to access the shared directory that we set up in the first VM.


## Use mount/unmount to do one-off mounting

* Step 1 To mount a Samba (SMB/CIFS) share in Linux, follow these steps 

1/ Install cifs-utils: This package provides the necessary tools for mounting CIFS shares. 
  
    `sudo apt-get install cifs-utils` # For Debian/Ubuntu-based systems
 
or 

    `sudo yum install cifs-utils` # For RHEL/CentOS-based systems

or

    `sudo pacman -S cifs-utils` # For Arch Linux

2/ Create a mount point: This is the local directory where the Samba share will be accessible. 
  
    `sudo mkdir /mnt/smb_share`

3/ Use `mount` command,

    * Mount the Samba share: You can mount the share temporarily or permanently. 
    * Temporary mount (unmounts on reboot): 
    * The following command is in one-line, make sure you pay attention to that.

     `sudo mount -t cifs //SERVER_IP_OR_HOSTNAME/SHARE_NAME /mnt/smb_share -o username=YOUR_USERNAME,password=YOUR_PASSWORD`

* Replace `/mnt/smb_share` with your desired mount point.
* Replace SERVER_IP_OR_HOSTNAME, SHARE_NAME, YOUR_USERNAME, and YOUR_PASSWORD with the appropriate values for your Samba share. If your password contains special characters, it might be necessary to escape them or use a credentials file (see below). Permanent mount (using /etc/fstab). 

## Mount with /etc/fstab

This would mount it permanently. You will see the folder available whenever you reboot your linux,

a. Create a credentials file (optional but recommended for security): This prevents storing your password directly in /etc/fstab.  (use vim or nano editor, skipped here)

            `vim ~/.smbcredentials`

Add the following content, replacing with your actual credentials: 

```
            username=YOUR_USERNAME
            password=YOUR_PASSWORD
```

Set appropriate permissions for the file to protect your credentials: 

            sudo chown YOUR_USERNAME:YOUR_USERNAME ~/.smbcredentials
            sudo chmod 600 ~/.smbcredentials

b. Edit /etc/fstab: Add a line to automatically mount the share at boot. 

            sudo vi /etc/fstab

Add the following line, adjusting the paths and options as needed: (one-liner)

`//SERVER_IP_OR_HOSTNAME/SHARE_NAME /mnt/smb_share cifs credentials=/home/YOUR_USERNAME/.smbcredentials,iocharset=utf8,file_mode=0777 ,dir_mode=0777 0 0`

If you are not using a credentials file, you can include username=YOUR_USERNAME,password=YOUR_PASSWORD directly in the options, but this is less secure. 
Verify the mount. 

    mount -t cifs

This command will list all currently mounted CIFS shares. You can also navigate to your mount point and list its contents to confirm access: 

    cd /mnt/smb_share
    ls
