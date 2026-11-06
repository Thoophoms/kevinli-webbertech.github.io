# dd command

## Introduction

The dd command is an extremely powerful Linux utility. It is commonly referred to as the "disk destroyer", “data definition”, “disk dump”, or "disk duplicator" due to its immense power and ability to directly interact with block devices. In this beginner's guide, we will explore the dd command, its syntax, and various use cases, highlighting its role in file copying, disk partition backup, and restoration, and creating bootable USB drives.

## dd Command Syntax

The syntax of the dd command is simple. It reads from standard input and writes to standard output by default. Here is the basic syntax of the dd command:

```
$ dd [OPTION]...
```

It's worth noting that dd deviates from the standard convention of using the -- or - syntax for options, distinguishing it from most Linux shell commands.

## dd command common options

The dd command accepts several options to customize its behavior and achieve specific tasks. Here are some of the most commonly used options:

![dd](../../../../images/computer_forensic/introduction/dd.png)

## How to copy files in Linux

To make a simple copy of a file, you can use the dd command with the if and of options. For example, to copy a file named source.txt to a new file named destination.txt, run the following command:

`$ dd if=source.txt of=destination.txt`

## Prevent overwriting destination file

When using the dd command, if there is already a file with the same name at the destination, it will be replaced by default. This means that the existing file will be overwritten. Use the conv=notrunc option to prevent overwriting an existing file while using the dd command. This option ensures that the destination file is not truncated during the write process. For example:

`$ dd if=source.txt of=destination.txt conv=notrunc`

## Appending Data to a File

In addition to avoiding overwriting, you can also append data to an existing file by using the conv=append option. Let's consider an example where we want to append the contents of users.txt to newusers.txt:

`$ dd if=users.txt of=newusers.txt conv=append`

With this command, the dd command reads the data from users.txt and appends it to the end of newusers.txt.

## Converting text case

The dd command can also be used to perform text conversions. For instance, to convert all the text in a file from lowercase to uppercase, use the conv option with the lcase and ucase conversion parameters. Consider the following example:

`$ dd if=lowercase.txt of=uppercase.txt conv=ucase`

This command reads the contents of lowercase.txt, converts all lowercase characters to uppercase, and saves the result in uppercase.txt.

Similarly, you can convert text from uppercase to lowercase using the conv option with the ucase and lcase conversion parameters. Here's an example:

`$ dd if=uppercase.txt of=lowercase.txt conv=lcase`

## Creating a Backup of a Linux Disk Partition

One of the powerful use cases of the dd command is creating backups of disk partitions. This can be particularly useful for system administrators or users who want to preserve the state of their disk partitions. To back up a disk partition, you need to identify the block device associated with the partition, usually represented by a device file in the /dev directory.

For example, to back up the first partition of the disk located at /dev/sda, you would use the following command:

`$ dd if=/dev/sda1 of=partition_backup.img`

This command reads the content of /dev/sda1, the first partition of the disk, and saves it to a file named partition_backup.img.

To do this lab properly, first let us find a small drive, I used `df -m` to show the disk size
in megabytes, and then I figured out that `/dev/sda1` is indeed just around 500M, which is a perfect size for backup example, so you can follow this method to find a small partition on your harddrive and do a backup and the file would be in your current directory.

```shell
xiaofengli@xiaofenglx:~/git/assembly$ df -m
Filesystem     1M-blocks    Used Available Use% Mounted on
tmpfs               3195       4      3191   1% /run
/dev/sda2         467851  319108    124906  72% /
tmpfs              15972     154     15818   1% /dev/shm
tmpfs                  5       1         5   1% /run/lock
efivarfs               1       1         1  84% /sys/firmware/efi/efivars
/dev/sdb1       11444094 1801543   9642552  16% /mnt/ntfs
/dev/sda1            511       7       505   2% /boot/efi
tmpfs               3195       1      3195   1% /run/user/1000
xiaofengli@xiaofenglx:~/git/assembly$ dd if=/dev/sda1 of=sda1_backup.img
dd: failed to open '/dev/sda1': Permission denied
xiaofengli@xiaofenglx:~/git/assembly$ sudo dd if=/dev/sda1 of=sda1_backup.img
1048576+0 records in
1048576+0 records out
536870912 bytes (537 MB, 512 MiB) copied, 5.25431 s, 102 MB/s
xiaofengli@xiaofenglx:~/git/assembly$ ls
hello  hello.o	hello.s  input.txt  loop  loop.o  loop.s  output.txt  sda1_backup.img
```

Once you have a backup of a disk partition, you can use the dd command to restore it when needed. To restore a disk partition, you would reverse the input and output files in the command. Here's an example: (DONOT DO THIS, BECAUSE it can damage your file system partitions.)

`$ dd if=partition_backup.img of=/dev/sda1`

This command reads the content from the partition_backup.img file and writes it to the /dev/sda1 partition, effectively restoring the partition to its previous state.

## Creating a Backup of the Entire Linux Hard Drive

In addition to backing up individual partitions, you can use the dd command to create a backup of the entire Linux hard drive. This allows you to capture the complete state of the disk, including all partitions, boot records, and file systems.

To back up the entire hard drive, you would specify the hard drive's block device as the input file. For instance, to back up the hard drive located at /dev/sda, run the following command:

`$ dd if=/dev/sda of=hard_drive_backup.img`

This command reads the entire content of /dev/sda and saves it to a file named hard_drive_backup.img.

Similarly, you can use the dd command to restore a previously created backup of the entire Linux hard drive. This can be extremely useful in situations where you need to recover the whole system from a backup.

To restore the hard drive, you would reverse the input and output files in the command. For example:

`$ dd if=hard_drive_backup.img of=/dev/sda`

This command reads the content from the hard_drive_backup.img file and writes it back to the /dev/sda hard drive, effectively restoring the entire system.

## Creating a Backup of the Master Boot Record

The Master Boot Record (MBR) is a crucial component of a disk that contains the boot loader and partition table. By using the dd command, you can create a backup of the MBR, ensuring that you can recover the boot sector if it gets corrupted or overwritten.

To back up the MBR, you can use the dd command to copy the first 512 bytes of the disk. Here's an example:

`$ dd if=/dev/sda of=mbr_backup.img bs=512 count=1`

In this command, if=/dev/sda specifies the disk from which to read the MBR, of=mbr_backup.img specifies the output file to save the backup, bs=512 sets the block size to 512 bytes (the size of the MBR), and count=1 specifies that only one block should be copied.

If you need to restore the MBR from a backup, you can use the dd command to write the contents of the backup file back to the disk. Here's an example:

`$ dd if=mbr_backup.img of=/dev/sda bs=512 count=1`

This command reads the content from the mbr_backup.img file and writes it back to the /dev/sda disk, effectively restoring the MBR.

## Copying Content from a CD/DVD Drive

The dd command can also be used to create a bit-by-bit copy of a CD or DVD. This can be useful when you want to create an exact replica of the disc, including its file system and bootable properties.

To copy the contents of a CD/DVD drive, you would specify the CD/DVD drive as the input file (if) and an output file to save the copy. 

Here's an example:

`$ dd if=/dev/cdrom of=disk_copy.iso`

In this command, /dev/cdrom represents the CD/DVD drive, and disk_copy.iso is the output file where the copied data will be saved.

## Compressing Data Read by dd

As mentioned earlier, one common use of the dd command is disk cloning. By copying block devices byte by byte, dd creates an exact replica of a disk. When cloning a disk to a file, we can enhance the result and reduce the file size by piping the data read by dd through compression utilities like gzip. For example, to create a clone of the entire /dev/sda block device, we can execute the following command:

`$ sudo dd if=/dev/sda bs=1M | gzip -c -9 > sda.dd.gz`

In this example, we specify that dd should read from the /dev/sda device and adjust the block size to 1M for improved performance. We then pipe the data to the gzip program, utilizing the -c option to output to stdout and the -9 option for maximum compression. Finally, we redirect the output to the "sda.dd.gz" file.

## Skipping Bytes or Characters When Reading the Input File

The dd command provides the skip option, which allows you to skip a specific number of bytes or characters while reading the input file. This can be useful when you need to exclude certain parts of the file. Here's an example:

`$ dd if=user.txt of=newusers.txt skip=100`

In this command, the dd command skips the first 100 bytes of data in users.txt and writes the remaining content to newusers.txt.

## Wiping a Block Device (don't try this on your computer, DONOT!!!)

Another valuable use case for dd is wiping a device. There are various situations where such an operation becomes necessary, such as preparing a disk for sale to ensure the previous data has been completely erased for privacy reasons or wiping data before setting up encryption. In the former case, overwriting the disk with zeros is sufficient:

`$ sudo dd if=/dev/zero bs=1M of=/dev/sda`

With this command, dd reads from the /dev/zero device, which provides null characters, and writes them to the target device until it is completely filled.

When setting up an encryption layer on our system, it is advisable to fill the disk with random data instead. This step renders the sectors that will contain data indistinguishable from the empty ones, thus preventing potential metadata leaks. In this scenario, we can read data from either the /dev/random or /dev/urandom devices:

`$ sudo dd if=/dev/urandom bs=1M of=/dev/sda`

Both commands will require a significant amount of time to complete, depending on the size and type of the block device and the source of random data used. It's worth noting that /dev/random is slower as it blocks until it gathers sufficient environmental noise, but it produces higher-quality random data compared to /dev/urandom.

Both commands will require a significant amount of time to complete, depending on the size and type of the block device and the source of random data used. It's worth noting that /dev/random is slower as it blocks until it gathers sufficient environmental noise, but it produces higher-quality random data compared to /dev/urandom.

## Creating a Bootable USB Drive

The dd command is widely used for creating bootable USB drives from ISO images. This is particularly useful when installing or booting operating systems or live distributions from a USB device.

To create a bootable USB drive, you would specify the ISO file as the input file (if) and the USB drive as the output file (of). Here's an example:

`$ dd if=linux_distro.iso of=/dev/sdX bs=4M status=progress`

In this command, linux_distro.iso represents the ISO image of the Linux distribution, /dev/sdX is the USB drive (replace X with the appropriate drive letter), bs=4M sets the block size to 4 megabytes for faster copying, and status=progress displays the progress of the dd command.

## Displaying the Progress Bar

By using the status=progress option with the dd command, you can display a progress bar that indicates the completion percentage of the ongoing operation. This can be helpful, especially when dealing with large files or lengthy processes.

For example, to copy a file and show the progress bar, use the following command:

`$ dd if=source_file of=destination_file status=progress`

This command reads the content from the source_file and writes it to the destination_file, while displaying a progress bar.


## ref

https://blog.kubesimplify.com/the-complete-guide-to-the-dd-command-in-linux