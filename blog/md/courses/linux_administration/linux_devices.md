# **Linux Device Files**

Linux represents hardware devices as special files located in the `/dev/` directory. These **device files** serve as interfaces between user applications and hardware.

#### **Types of Device Files**

1. **Character Devices (`c`)**  
   - Read and write operations occur one character at a time.
   - Examples: `/dev/tty`, `/dev/null`, `/dev/random`
   
2. **Block Devices (`b`)**  
   - Data is read/written in fixed-size blocks.
   - Examples: `/dev/sda` (Hard Drive), `/dev/mmcblk0` (SD Card)

3. **Special Devices**  
   - **Named Pipes (`p`)**: Used for inter-process communication.  
   - **Sockets (`s`)**: Used for network communication.  
   - **Symbolic Links (`l`)**: Pointers to other device files.

#### **Types of Hardware Supported by Linux**
1. **Storage Devices**: HDD, SSD, USB drives (`/dev/sda`, `/dev/nvme0n1`)  
2. **Input Devices**: Keyboards (`/dev/input/eventX`), Mice  
3. **Display Devices**: GPUs (`/dev/dri/card0`)  
4. **Network Devices**: Ethernet (`eth0`), WiFi (`wlan0`)  
5. **Sound Devices**: Microphones, Speakers (`/dev/snd/`)  
6. **Printers and Scanners**: (`/dev/lp0`)  
7. **Embedded Systems & IoT**: GPIO, I2C, SPI (`/dev/gpiochip0`)  

## A breakdown

### **Linux Storage Device Naming Schemas**
Linux follows specific naming conventions for storage devices. The most common naming schemas are:

#### **1. Traditional HDDs and SSDs (`/dev/sdX`)**
- **Format:** `/dev/sd[a-z]`
- **Example:** `/dev/sda`, `/dev/sdb`
- Used for **SCSI, SATA, and USB drives**.
- Partitions are named `/dev/sda1`, `/dev/sda2`, etc.

#### **2. NVMe SSDs (`/dev/nvmeXnY`)**
- **Format:** `/dev/nvmeXnYpZ`
- **Example:** `/dev/nvme0n1`, `/dev/nvme0n1p1`
- Used for **NVMe-based SSDs** (faster than SATA).
- `X` → Controller number, `Y` → Namespace, `Z` → Partition.

#### **3. eMMC Storage (`/dev/mmcblkX`)**
- **Format:** `/dev/mmcblkX`
- **Example:** `/dev/mmcblk0`, `/dev/mmcblk0p1`
- Used in **embedded systems and mobile devices**.

#### **4. Loopback Devices (`/dev/loopX`)**
- **Format:** `/dev/loopX`
- **Example:** `/dev/loop0`, `/dev/loop1`
- Used for **mounting disk images**.

#### **5. RAM Disks (`/dev/ramX`)**
- **Format:** `/dev/ramX`
- **Example:** `/dev/ram0`, `/dev/ram1`
- Used for **temporary storage in RAM**.

## **Understanding `/dev/sd[a-z]` in Linux**

In Linux, storage devices like **SATA, SCSI, and USB drives** are represented as `/dev/sdX`, where `X` is a letter assigned to each detected device.

### Naming Convention**

- `/dev/sda`: First detected disk  
- `/dev/sdb`: Second detected disk  
- `/dev/sdc`: Third detected disk  
- **Partitions** are numbered as `/dev/sda1`, `/dev/sda2`, etc.

#### **2. Example Use Cases**
- **List all disks:**  
  ```bash
  lsblk
  ```
- **Check disk information:**  
  ```bash
  sudo fdisk -l
  ```
- **Mount a partition:**  
  ```bash
  sudo mount /dev/sdb1 /mnt
  ```
- **Format a disk to ext4:**  
  ```bash
  sudo mkfs.ext4 /dev/sdb1
  ```

#### **3. Difference from Other Storage Naming Schemes**
- **NVMe Drives:** `/dev/nvme0n1`
- **MMC/eMMC Storage:** `/dev/mmcblk0`
- **RAID Arrays:** `/dev/md0`
### **Managing Storage Devices in Linux**

Linux provides several commands to **list, mount, format, and manage** storage devices like `/dev/sdX`. Below are common tasks you might need to perform.

---

### **1. Listing Storage Devices**
Check which storage devices are available on your system.

- **List all block devices** (HDDs, SSDs, USBs, etc.):
  ```bash
  lsblk
  ```
- **View detailed disk partitions**:
  ```bash
  sudo fdisk -l
  ```
- **List mounted devices**:
  ```bash
  df -h
  ```

---

### **2. Mounting and Unmounting Devices**
To access a storage device, you need to mount it.

- **Manually mount a partition**:
  ```bash
  sudo mount /dev/sdb1 /mnt
  ```
- **Unmount a device**:
  ```bash
  sudo umount /mnt
  ```

---

### **3. Formatting Storage Devices**
Before using a new drive, you may need to format it.

- **Format as ext4 (Linux Filesystem)**:
  ```bash
  sudo mkfs.ext4 /dev/sdb1
  ```
- **Format as NTFS (Windows-compatible)**:
  ```bash
  sudo mkfs.ntfs /dev/sdb1
  ```
- **Format as FAT32 (Universal Compatibility)**:
  ```bash
  sudo mkfs.vfat -F 32 /dev/sdb1
  ```

---

### **4. Checking and Repairing Filesystems**
If a disk has issues, you can check and fix it.

- **Check filesystem for errors**:
  ```bash
  sudo fsck /dev/sdb1
  ```
- **Repair filesystem**:
  ```bash
  sudo fsck -y /dev/sdb1
  ```

---

### **5. Managing Partitions**
Use **`fdisk`** or **`parted`** to manage partitions.

- **Start partitioning a new disk**:
  ```bash
  sudo fdisk /dev/sdb
  ```
  - Press `n` to create a new partition.
  - Press `w` to write changes.

- **Create partitions using `parted`**:
  ```bash
  sudo parted /dev/sdb
  ```

---

### **6. Automount a Device at Boot**
To mount a device automatically at startup, add it to `/etc/fstab`.

1. Find the UUID of the device:
   ```bash
   sudo blkid /dev/sdb1
   ```
2. Add an entry to `/etc/fstab`:
   ```
   UUID=XXXX-XXXX  /mnt/mydrive  ext4  defaults  0  2
   ```
3. Apply the changes:
   ```bash
   sudo mount -a
   ```

Now, let's cover **LVM (Logical Volume Management)** and **RAID (Redundant Array of Independent Disks)** in Linux.

---

## **1. LVM (Logical Volume Management)**
LVM allows flexible disk management by creating **Logical Volumes (LVs)** instead of directly using physical partitions.

### **LVM Structure**
1. **Physical Volume (PV)** – Raw disks/partitions (`/dev/sdb`, `/dev/sdc`).
2. **Volume Group (VG)** – A pool of one or more PVs.
3. **Logical Volume (LV)** – A partition-like segment inside a VG.

### **LVM Commands**
- **Initialize a disk as a Physical Volume (PV):**
  ```bash
  sudo pvcreate /dev/sdb
  ```
- **Create a Volume Group (VG):**
  ```bash
  sudo vgcreate my_vg /dev/sdb
  ```
- **Create a Logical Volume (LV) of 10GB:**
  ```bash
  sudo lvcreate -L 10G -n my_lv my_vg
  ```
- **Format and mount LV:**
  ```bash
  sudo mkfs.ext4 /dev/my_vg/my_lv
  sudo mount /dev/my_vg/my_lv /mnt
  ```

---

## **2. RAID (Redundant Array of Independent Disks)**
RAID provides disk redundancy and performance improvements.

### **Common RAID Levels**
1. **RAID 0 (Striping)** – Faster, no redundancy.
2. **RAID 1 (Mirroring)** – Full redundancy, slower.
3. **RAID 5 (Striping + Parity)** – Efficient redundancy.
4. **RAID 10 (Mirrored Striping)** – Best of RAID 1 & 0.

### **RAID Setup Using `mdadm`**
- **Create a RAID 1 array from two disks:**
  ```bash
  sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
  ```
- **Check RAID status:**
  ```bash
  cat /proc/mdstat
  ```

