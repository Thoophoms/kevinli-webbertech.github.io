# Ubuntu System Commands

## systemd-analyze

The following commands will address the computer slowness issue.

`systemd-analyze critical-chain`

`systemd-analyze blame`

## Optimize the restart speed

* Stop all these services

`systemctl disable docker.service`

`systemctl disable mysql.service`

`systemctl disable NetworkManager-wait-online.service`

* Remove Snap

`sudo apt purge snap`

`sudo apt autoremove`

* Inspect the following [TODO]

```
55.619s plymouth-quit-wait.service
46.580s e2scrub_reap.service
33.979s podman-restart.service
```

* Frozen Terminal

Get `Activity Monitor` and kill `Gnome-shell`, it is like windows explorer and it will restart.

**Solution**: It was fixed by changing from XWayland to X11.

## Visualize the service

`systemd-analyze plot > ~/SystemdAnalyzePlot.svg`

## Variables to check your Desktop Manager

"$XDG_CURRENT_DESKTOP" "$GDMSESSION"

```shell
Ubuntu 18.04 and 20.04 (Ubuntu on GNOME)
XDG_CURRENT_DESKTOP=ubuntu:GNOME
GDMSESSION=ubuntu
Ubuntu 18.04 (Ubuntu on Wayland)
XDG_CURRENT_DESKTOP=ubuntu:GNOME
GDMSESSION=ubuntu-wayland
```

## Recover Ubuntu Desktop

If you have any wierdness and do not know how to fix it,

`sudo apt autoremove gdm3 ubuntu-desktop`
`sudo apt purge gdm3 ubuntu-desktop`
`sudo apt-get install gdm3 ubuntu-desktop`
`sudo /etc/init.d/gdm restart`

## Fix login window and gnome-shell issue

`sudo apt install --reinstall gdm3 ubuntu-desktop gnome-shell`
`sudo systemctl reboot`

## Change Wayland to X11 Window Manager

* If you wish to do it permanently, edit `/etc/gdm3/custom.conf` and uncomment the line:

`#WaylandEnable=false`

* Save and reboot

## Change Screen Resolution

```shell
xiaofengli@xiaofenglx:~$ xrandr -q
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 16384 x 16384
VGA-1 disconnected (normal left inverted right x axis y axis)
HDMI-1 connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 598mm x 336mm
   1920x1080     60.00*+  74.97    50.00    59.94  
   1920x1080i    60.00    50.00    59.94  
   1680x1050     59.88  
   1280x1024     75.02    60.02  
   1440x900      59.90  
   1280x960      60.00  
   1280x720      60.00    50.00    59.94  
   1024x768      75.03    70.07    60.00  
   832x624       74.55  
   800x600       72.19    75.00    60.32    56.25  
   720x576       50.00  
   720x480       60.00    59.94  
   640x480       75.00    72.81    66.67    60.00    59.94  
   720x400       70.08  
HDMI-2 disconnected (normal left inverted right x axis y axis)
```

ref: https://askubuntu.com/questions/425628/how-do-i-resolve-desktop-larger-than-screen

### startx command

The startx command in Linux starts an X session and has several uses, including:

**Starting an X session.**

The `startx` command starts an X session on a single computer.

**Booting Linux**

The startx command can boot Linux into runlevel 3 mode, which enables X11, multiuser, and networking.

**Passing options**

The startx command can pass command-line options to the X server, such as starting color-depth information.
Finding client commands

The startx command can find client commands or options to run for the session.

The startx command is a shell script that acts as a front end to xinit(1). It's often run without any arguments.

By default, the startx command sends errors to the .xerrors file in the user's home directory.

## Remote Desktop to the Xserver

`sudo apt install rdesktop`

`rdesktop -u host -p password ip/dns`

Then we see the connection like the following,

![alt text](../../../images/linux/rdesktop1.png)
![alt text](../../../images/linux/rdesktop2.png)
![alt text](../../../images/linux/rdesktop3.png)

Note: I have observed some slowess. Not sure this would be thing.

## Enable *.desktop file in ubuntu

```shell
xiaofengli@xiaofenglx:~$ gio set ~/Desktop/thinkorswim.desktop metadata::trusted true
chmod a+x ~/Desktop/app.desktop
```

## MYSQL Installation

**Reinstallation**

First, remove MySQL:

```shell
sudo apt purge mysql-server mysql-client mysql-common
sudo apt autoremove
sudo mv -iv /var/lib/mysql /var/tmp/mysql-backup
sudo rm -rf /var/lib/mysql*
Then reinstall:

sudo apt update
sudo apt install mysql-server
mysqld --initialize
sudo /usr/bin/mysql_secure_installation
```

Login and reset root password to something,

`sudo mysql -uroot -p`

No password,

Then run the following,

`ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'yourpasswd';`

## EDIMAX BT8500 Driver Installation on Ubuntu

First of all, please make sure the "Secure boot" is disabled in BIOS.  If the Secure Boot is enabled, the installed driver will not work for you.

[1.]  Make sure your system is able to access the Internet.

[2.] Open a Terminal program from your Ubuntu OS.

[3.] Verify the kernel version in your Ubuntu Linux.

`$ uname –r`

If your kernel is newer than the supported kernel, stop here.  This instruction may not work for you.

[4] Update system.  This step is optional but recommended.

`$ sudo apt update`

`$ sudo apt upgrade`

`$ sudo reboot`

 [5] Install Linux headers

` $ sudo apt install linux-headers-$(uname –r)`

[6] Install the necessary package for compiling drivers

`$ sudo apt install build-essential make`

[7] Download Linux driver from Edimax website.

Open your web browser.

Go to http://www.edimax.com site.

Look for the model number BT-8500.

Select BT-8500 to get into the product page.

Click on Download.

Locate the Linux driver.

Pay attention to the supported kernel of the Linux driver before you download it.

Download the Linux driver.

Usually the zip driver will be saved in your Downloads folder.  

We have BT-8500_Linux_Bluetooth_Driver_1_0_0_3.zip in this instruction.

The driver filename can be updated without notification.  You will need to perform below commands according to the newer filename.

[8] Extract the download driver.

Locate the zipped file in Downloads folder.

Right-click on the zip file and select Extract Here.  

You will see a new folder "BT-8500_Linux_Bluetooth_Driver_1.0.0.3".

Right-click on the new folder. elect Open in Terminal Window.


[9] Install the driver

`$ sudo make install INTERFACE=usb`

Please note the command is case sensitive.

[10]  Reboot your system

`$ sudo reboot`

[11]  Plug in BT-8500 adapter if the adapter is not plugged in yet.

[12]  Find Bluetooth option on the top right menu bar.  Or you can go to Settings >> Bluetooth.  Search for available bluetooth devices.

Congratulations!  The setup is complete.

For removal,

`$ cd ~/Downloads/BT-8500_Linux_Bluetooth_Driver_1.0.0.3`

`$ sudo make uninstall`

### Ref

- https://support.system76.com/articles/login-loop-ubuntu/
- https://superuser.com/questions/65185/when-i-start-ubuntu-it-enters-tty1-6-instead-of-my-desktop-how-do-i-get-to-de