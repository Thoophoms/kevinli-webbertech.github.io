# In-class Lab Mounting NTFS Disk in Linux

## Abstract

In this lab, we will show you how to mount a harddisk of Microsoft NTFS into Linux server.
This is often used in data center of companies or schools.

## Permanently mounting the disk partition

### Step 1 Identify the disk and partitions that were added to the linux machine

First I use `sudo fdisk -l` to view all the partitions and hard drive on my linux system.

![fdisk.png](/blog/images/dev_ops/linux/labs/fdisk.png)

### Step 2 view the partition UUID 

In order to mount my NTFS hard drive taken from an old windows server, I need to mount the disk/partition into my linux machine using /etc/fstab. However, we might need to take the partition or disk’s UUID, and we need another command,
The other command I use is the `blkid`, and it allows me to see all the UUID of the system.

![blkid.png](/blog/images/dev_ops/linux/labs/blkid.png)

Now I am getting the UUID of that partition of /dev/sdb1,

```
/dev/sdb1: LABEL="New Volume" BLOCK_SIZE="512" UUID="1074F6E274F6CA0C" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="fb7c74c5-3854-483c-b91d-21a3f24965a7"
```

### Step 3 Create a mounting directory

And we want to make sure that, we did create a folder before we reboot or let this fstab file to take effect.

`sudo mkdir /mnt/ntfs`

### Step 4 Mounting the disk to a directory using /etc/fstab

You can learn VIM editor commands in latter of the class, but when you first time to modify the /etc/fstab, I would recommend you to backup this file before you modify it,
You can use `sudo` and `cp` to make another copy.

![fstab_bk.png](/blog/images/dev_ops/linux/labs/fstab_bk.png)

To permanently mount the partition into the linux machine, so next time, when we boot up the machine, the drive is always good for use.

We will use the `mount` command to add a line of instruction into `/etc/fstab` and we need to use `sudo` which is a root permission to modify this file and save it.
So here I use the `vim` editor to add this line,

![fstab.png](/blog/images/dev_ops/linux/labs/fstab.png)

Once we open the /etc/fstab, we will add the last line there [you see the UUID], 

![fstab_edit.png](/blog/images/dev_ops/linux/labs/fstab_edit.png)

## One-off mounting with `mount` command

Or you can run the following command to simplify the process so that you might not need to grab the UUID of the partition.

`sudo mount -t ntfs-3g /dev/sdb1 /mnt/ntfs`


>> Side-notes:
    As you can see in the /etc/fstab, there is a ntfs-3g, this is a unity that we might need to install, the command is like the follow, but in most cases, you might have had it already. sudo apt install ntfs-3g