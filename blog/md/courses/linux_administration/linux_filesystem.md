# **Linux File Systems Overview**


# Linux File System

## What is the Linux File System?

The Linux File System is a structured way to store and organize files on a storage device, such as a hard drive or SSD, in a Linux operating system. It dictates how files are named, stored, and retrieved. Unlike some other operating systems, Linux treats everything as a file, including hardware devices and processes.

## Key Concepts and Structure

### Hierarchical Directory Structure

The Linux file system is organized in a hierarchical structure, often referred to as a tree. The top level of this hierarchy is the root directory, denoted by a forward slash (`/`). All other directories and files branch off from this root.

### Important Directories

Here are some of the key directories in the Linux file system:

- **/** : The root directory.
- **/bin** : Contains essential binary executables.
- **/boot** : Contains boot loader files.
- **/dev** : Contains device files.
- **/etc** : Contains system configuration files.
- **/home** : Contains personal directories for users.
- **/lib** : Contains essential shared libraries and kernel modules.
- **/media** : Mount point for removable media (CD-ROMs, USB drives, etc.).
- **/mnt** : Temporary mount point for filesystems.
- **/opt** : Contains add-on application software packages.
- **/proc** : Virtual filesystem providing process and kernel information.
- **/root** : Home directory for the root user.
- **/sbin** : Contains essential system binaries.
- **/srv** : Contains data for services provided by the system.
- **/tmp** : Temporary files.
- **/usr** : Secondary hierarchy for read-only user data.
- **/var** : Variable data like logs and databases.

### File Permissions

Linux file permissions determine who can read, write, and execute a file. Each file and directory has three types of permissions:

- **Read (r)** : View the contents of the file.
- **Write (w)** : Modify the contents of the file.
- **Execute (x)** : Run the file as a program.

Permissions are set for three categories of users:

- **Owner** : The user who owns the file.
- **Group** : The group that owns the file.
- **Others** : All other users.

Permissions can be viewed and modified using commands like `ls -l` and `chmod`.

### File Types

In Linux, files can be of various types, including:

- **Regular file (-)** : Ordinary files like text and binary files.
- **Directory (d)** : A folder containing files and other directories.
- **Symbolic link (l)** : A link pointing to another file.
- **Socket (s)** : Used for inter-process communication.
- **Pipe (p)** : A special file for FIFO (first-in, first-out) communication.
- **Block device (b)** : A file that represents a block device.
- **Character device (c)** : A file that represents a character device.

### Inodes

An inode is a data structure on a filesystem on Linux that stores information about a file or a directory except its name and its actual data. This information includes file metadata such as user and group ownership, access mode (read, write, execute permissions), and type of file.

### Mounting and Unmounting Filesystems

To access the contents of a filesystem, it must be mounted to a directory. The `mount` command is used to attach a filesystem, and the `umount` command is used to detach it.

### Filesystem Types

Linux supports various filesystem types, including:

- **ext4** : The most commonly used Linux filesystem.
- **ext3** : Older version of ext4 with less features.
- **xfs** : High-performance filesystem.
- **btrfs** : Filesystem with advanced features like snapshots.
- **vfat** : For compatibility with Windows filesystems.

## Best Practices

- **Regular Backups** : Regularly back up important data to prevent loss.
- **Permission Management** : Carefully manage file permissions to enhance security.
- **Disk Usage Monitoring** : Monitor disk space usage using tools like `df` and `du`.
- **Filesystem Checks** : Periodically check and repair filesystems using tools like `fsck`.
- **Use Appropriate Filesystem** : Choose the right filesystem based on your use case (e.g., ext4 for general use, xfs for performance).

___

## Additional Concepts and Tools

### Filesystem Hierarchy Standard (FHS)

The Filesystem Hierarchy Standard (FHS) defines the directory structure and directory contents in Unix-like operating systems. It is important to understand FHS to ensure compatibility and standardization across different distributions.

### File and Directory Commands

Here are some commonly used commands to manage files and directories:

- **ls** : List directory contents.
- **cd** : Change the current directory.
- **pwd** : Print the current working directory.
- **cp** : Copy files and directories.
- **mv** : Move or rename files and directories.
- **rm** : Remove files or directories.
- **mkdir** : Create directories.
- **rmdir** : Remove empty directories.
- **touch** : Create an empty file or update the timestamp of an existing file.
- **ln** : Create links between files.

### Disk Usage and Quotas

Monitoring disk usage and setting quotas can help manage storage efficiently:

- **df** : Report filesystem disk space usage.
- **du** : Estimate file space usage.
- **quota** : Display user and group quotas.
- **edquota** : Edit user and group quotas.

### Advanced Filesystem Features

- **LVM (Logical Volume Manager)** : LVM provides a more flexible way to manage disk space by allowing you to create, resize, and delete logical volumes.
- **RAID (Redundant Array of Independent Disks)** : RAID combines multiple physical disks into a single logical unit for redundancy and performance improvement.
- **Swap Space** : Swap space is used as virtual memory when the physical RAM is full. It can be a dedicated swap partition or a swap file.

### Filesystem Tuning and Optimization

- **tune2fs** : Adjust tunable filesystem parameters on ext2/ext3/ext4 filesystems.
- **xfs_admin** : Manage and tune XFS filesystems.

### Filesystem Security

- **ACL (Access Control Lists)** : ACLs provide a more flexible permission mechanism than the traditional Unix permissions, allowing you to set permissions for individual users or groups.
- **SELinux (Security-Enhanced Linux)** : A security architecture integrated into the kernel that provides a mechanism for supporting access control security policies.
- **AppArmor** : Another Linux security module that protects the operating system and applications from security threats.

### Backup and Recovery

Regular backups and a recovery plan are crucial:

- **rsync** : A fast and versatile file copying tool for local and remote backups.
- **tar** : An archiving utility to create tarball files (archives).
- **dd** : Low-level copying and conversion tool useful for disk cloning and backups.

### Filesystem Integrity and Checking

- **fsck** : Filesystem consistency check and repair tool.
- **badblocks** : Check for bad blocks on a storage device.

### Network File Systems

- **NFS (Network File System)** : Allows a system to share directories and files with others over a network.
- **Samba** : Provides SMB/CIFS protocol support, enabling file and print sharing between Unix/Linux and Windows systems.
- **SSHFS** : Filesystem client based on SSH, enabling access to remote filesystems via SSH.

### Journaling Filesystems

Journaling filesystems like ext4, XFS, and btrfs keep track of changes not yet committed to the main filesystem, helping to prevent corruption and improve recovery times after a crash.

### Case Sensitivity

Linux filesystems are case-sensitive. This means that `File.txt` and `file.txt` are considered different files. This is an important consideration when working with files and directories.

### Hidden Files

Files and directories starting with a dot (`.`) are considered hidden in Linux. These are often configuration files or directories. You can view them using the `ls -a` command.

### Pathnames

There are two types of pathnames in Linux:

- **Absolute pathname** : Begins with the root directory (`/`), e.g., `/home/user/file.txt`.
- **Relative pathname** : Does not begin with the root directory, relative to the current working directory, e.g., `file.txt` or `../file.txt`.

### Hard Links and Symbolic Links

- **Hard Link** : A direct pointer to the data on the disk. Multiple hard links to a file share the same inode and data blocks.
- **Symbolic Link** : A pointer to another file or directory. Unlike hard links, symbolic links can cross filesystem boundaries and can link to directories.

### File System Errors

Understanding and troubleshooting filesystem errors is crucial for maintaining system health. Common commands and logs to inspect include `dmesg`, `journalctl`, and specific filesystem repair tools like `e2fsck` for ext filesystems.
___

## Takeaway

* Linux top directoreis
* Linux file system
* Automounting and /etc/fstab

## Top directories

It looks like you have a Python script with Huffman encoding, Red-Black tree implementation, and LVM/RAID automation. Here’s how you can add **Linux top-level directories and their uses** into your script:

### **Linux Top-Level Directories and Their Uses**

| **Directory** | **Description** |
|--------------|----------------|
| `/` | Root directory, base of the file system. |
| `/bin` | Essential binary executables (e.g., `ls`, `cp`). |
| `/sbin` | System binaries (e.g., `fdisk`, `reboot`), typically for root. |
| `/etc` | Configuration files for the system and applications. |
| `/home` | Home directories for users (e.g., `/home/user`). |
| `/var` | Variable data (logs, databases, mail, etc.). |
| `/usr` | User-related programs, libraries (`/usr/bin`, `/usr/lib`). |
| `/opt` | Optional software installed manually. |
| `/tmp` | Temporary files (cleared on reboot). |
| `/dev` | Device files (e.g., `/dev/sda1` for a disk). |
| `/mnt` | Mount point for external storage. |
| `/media` | Automounted removable media (USB, CD-ROM). |
| `/proc` | Virtual file system for process and kernel information. |
| `/sys` | System information, kernel parameters. |
| `/boot` | Bootloader files (e.g., `vmlinuz`, `initrd`). |
| `/root` | Home directory of the root user. |
| `/lib` | Shared system libraries required for binaries in `/bin` and `/sbin`. |

### **Exploring `/proc` in Linux**

The `/proc` directory is a **virtual file system** that provides real-time system information. It doesn’t store actual files but contains dynamic system data.

---

### **Common `/proc` Files and Their Uses**

| **File/Directory** | **Description** |
|------------------|----------------|
| `/proc/cpuinfo` | Information about the CPU (model, cores, speed). |
| `/proc/meminfo` | Memory usage details (total, free, buffers, swap). |
| `/proc/uptime` | System uptime in seconds. |
| `/proc/loadavg` | System load averages. |
| `/proc/version` | Kernel version and compiler details. |
| `/proc/filesystems` | Supported file systems in the kernel. |
| `/proc/mounts` | Mounted file systems. |
| `/proc/[PID]` | Directory for each running process with details (e.g., `/proc/1` for init). |
| `/proc/net` | Network-related information. |

>Hint: The above are all files. As a matter of fact. `File` is a key in learning linux system.

#### **Automation with Python**

```python
def read_proc_file(file):
    """Reads and displays content from a /proc file."""
    try:
        with open(file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File {file} not found."

def system_info():
    """Displays key system information from /proc."""
    print("\nCPU Info:")
    print(read_proc_file("/proc/cpuinfo").split("\n")[0])  # Show only first line

    print("\nMemory Info:")
    print(read_proc_file("/proc/meminfo").split("\n")[0:5])  # Show first 5 lines

    print("\nUptime:")
    print(read_proc_file("/proc/uptime"))

    print("\nKernel Version:")
    print(read_proc_file("/proc/version"))

# Call system_info() to print details
if __name__ == "__main__":
    system_info()
```

## File Systems

Linux supports multiple file systems, each designed for different use cases. Here are some common ones:

| **File System** | **Description** | **Use Case** |
|---------------|---------------|------------|
| **ext4** | Default Linux file system with journaling and large file support. | General-purpose use (desktops, servers). |
| **XFS** | High-performance journaling file system, scalable. | Large-scale storage, enterprise servers. |
| **Btrfs** | Advanced features like snapshots and checksumming. | Modern storage solutions, data integrity. |
| **ZFS** | RAID, snapshots, and compression built-in. | Enterprise storage, data protection. |
| **F2FS** | Optimized for NAND flash storage (SSDs). | Mobile devices, SSD-based systems. |
| **NTFS** | Microsoft file system with journaling. | Used for Windows partitions in Linux. |
| **VFAT/exFAT** | Microsoft-compatible file systems for removable media. | USB drives, SD cards. |

## **Check and Manage File Systems**

- **List available file systems**

  ```bash
  cat /proc/filesystems
  ```

- **Check file system type of a partition**

  ```bash
  lsblk -f
  ```

- **Format a partition with ext4**

  ```bash
  sudo mkfs.ext4 /dev/sdX
  ```

- **Mount a file system**

  ```bash
  sudo mount /dev/sdX /mnt
  ```

- **Check disk usage**

  ```bash
  df -h
  ```

## **Automounting File Systems in Linux**

To automatically mount a file system at boot, follow these steps:

### **1. Find the Disk UUID**

```bash
blkid
```

- Note the UUID of the partition you want to mount.

### **2. Edit `/etc/fstab`**

```bash
sudo nano /etc/fstab
```

- Add an entry like this:

  ```
  UUID=your-uuid /mnt/your-mount-point ext4 defaults 0 2
  ```

  *(Replace `your-uuid` with the actual UUID and `/mnt/your-mount-point` with your desired mount location.)*

### **3. Create the Mount Point**

```bash
sudo mkdir -p /mnt/your-mount-point
```

### **4. Test the Mount**

```bash
sudo mount -a
```

- If no errors appear, the setup is correct.

Now, the partition will mount automatically at startup!

## Appendix - My mount in my linux

- **Example 1**

```shell
xiaofengli@xiaofenglx:~$ mount |grep ntfs
/dev/sdb1 on /mnt/ntfs type fuseblk (rw,relatime,user_id=0,group_id=0,allow_other,blksize=4096)
```

