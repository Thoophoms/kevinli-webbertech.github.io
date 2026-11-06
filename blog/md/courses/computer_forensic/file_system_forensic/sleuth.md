# Sleuth Kit (TSK) Tutorial

The **Sleuth Kit (TSK)** is an open-source digital forensics toolkit used for analyzing disk images, file systems, and extracting digital evidence. It includes command-line tools for examining and recovering deleted files, listing file system metadata, and inspecting file structures.
It is a suite of commands/executables/tools provided.

## Key Takeaway

Sleuth Kit provides powerful tools for digital forensics, including:
- **File System Analysis** (`fsstat`, `fls`)
- **Metadata Extraction** (`istat`)
- **File Recovery** (`icat`, `ils`)
- **Timeline Creation** (`mactime`)

## Installation

### **Linux (Ubuntu/Debian)**

```bash
sudo apt update
sudo apt install sleuthkit
```

### **macOS (using Homebrew)**

```bash
brew install sleuthkit
```

### **Windows**

Download the binaries from the [official website](https://www.sleuthkit.org/) and install.

---

## **Basic Commands**

Once installed, you can use TSK commands to analyze disk images and file systems.

### **List Partitions in a Disk Image**

```bash
mmls disk.img
```

- `disk.img` is a forensic disk image.
- This command outputs the partition table, showing partition start/end sectors.

### **Analyze a Specific Partition**

```bash
fsstat disk.img -o 2048
```

- `-o 2048` specifies the sector offset found using `mmls`.

### **List Files in a Partition**

```bash
fls -o 2048 disk.img
```

- Lists files and directories in the partition.

### **Extract a File**

```bash
icat -o 2048 disk.img 12345 > recovered_file.jpg
```

- Extracts file with inode `12345` and saves it as `recovered_file.jpg`.

### **Find Deleted Files**

```bash
ils -o 2048 disk.img
```

- Lists inodes of deleted files.

### **Recover Deleted Files**

```bash
icat -o 2048 disk.img 67890 > recovered.txt
```

- If `67890` is the inode of a deleted file, this command recovers it.

---

## **3. Case Study: Recovering Deleted Files from a Disk Image**
### **Step 1: Identify Partitions**

```bash
mmls disk.img
```

_Output Example:_

```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot    Start        End          Length       Description
000:  0000000000   0000002047   0000002048   Primary Table (#1)
001:  0000002048   0001048575   0001046528   NTFS (0x07)
```

_The partition starts at sector `2048`._

### **Step 2: List Files**

```bash
fls -o 2048 disk.img
```

_Output Example:_

```
r/r 5-128-3: $AttrDef
r/r 6-144-3: $Bitmap
d/d 11-128-3: Documents
r/r 20-160-4: photo.jpg (deleted)
```

_The deleted file `photo.jpg` has inode `20`._

### **Step 3: Recover Deleted File**

```bash
icat -o 2048 disk.img 20 > recovered_photo.jpg
```

_Check the file to confirm recovery._

---

## **4. File System Analysis**
### **Check File System Type**

```bash
fsstat disk.img -o 2048
```
- Provides details about the file system type, size, and structures.

### **View Metadata of a Specific File**

```bash
istat disk.img -o 2048 20
```
- Shows metadata, including timestamps and size.

---

## **5. Searching for Specific Files**
### **Search for a Specific File Name**

```bash
ffind -o 2048 disk.img "confidential.txt"
```
- Returns inode of the file.

### **Find Files by Content**

```bash
blkls -o 2048 disk.img | strings | grep "password"
```
- Searches for the keyword "password" in unallocated space.

---

## **6. Timeline Analysis**

Create a forensic timeline to track file activities.

### **Step 1: Generate File System Metadata**

```bash
fls -r -o 2048 disk.img > filelist.txt
```

### **Step 2: Extract Timestamps**

```bash
mactime -b filelist.txt -d > timeline.csv
```
- The timeline contains **MAC times** (Modified, Accessed, Created).

---

## Addtional Example

Here’s an example of how the `mmls` command might be used and what its output could look like. Let’s assume you’re working with a disk image file named `disk_image.dd` in a forensic investigation or system analysis scenario.

### Command

You’d run:
```
mmls disk_image.dd
```

### Sample Output

The output might look something like this (this is a simplified example based on typical `mmls` behavior):
```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

     Slot      Start        End          Length       Description
00:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
01:  -----     0000000000   0000000062   0000000063   Unallocated
02:  00:00     0000000063   0001028159   0001028097   NTFS (0x07)
03:  00:01     0001028160   0002056319   0001028160   FAT32 (0x0c)
04:  -----     0002056320   0002097151   0000040832   Unallocated
```

### Explanation of the Output

- **Slot**: Indicates the partition entry (e.g., "00:00" is the first partition, "00:01" is the second). "Meta" refers to metadata like the partition table itself, and "-----" marks unallocated space.
- **Start**: The starting sector of the partition or space.
- **End**: The ending sector.
- **Length**: The size of the partition or space in sectors (e.g., 1,028,097 sectors for the NTFS partition).
- **Description**: The type of partition or area (e.g., NTFS, FAT32, or unallocated). The hex code (like 0x07) corresponds to the partition type in the partition table.

### What This Tells Us

- The disk has two partitions: one NTFS starting at sector 63 and one FAT32 starting at sector 1,028,160.
- There’s unallocated space before and after the partitions.
- Each sector is 512 bytes, so you could calculate sizes (e.g., NTFS partition size = 1,028,097 × 512 = ~526 MB).

### Practical Use

If you’re analyzing `disk_image.dd` for forensics, you might use this output to:
1. Identify where file systems start (e.g., sector 63 for NTFS).
2. Extract a partition with another tool like `dd` (e.g., `dd if=disk_image.dd bs=512 skip=63 count=1028097 of=ntfs_partition.img`).
3. Check for hidden data in unallocated spaces.

If you want a different example (e.g., with specific options like `-b` for byte offsets or a real-world scenario), or if you’re working with a particular disk image you’d like me to tailor this to, just let me know!

Since you asked about `mmls` earlier and now `fsstat`, it seems like you’re exploring tools from the Sleuth Kit for disk and file system analysis. The `fsstat` command is used to display detailed information about a file system within a partition or image. It’s often used after `mmls` to dig into the specifics of a file system identified in a partition.

Let’s assume you’re working with the same `disk_image.dd` from the `mmls` example, where we found an NTFS partition starting at sector 63. I’ll walk you through an `fsstat` example based on that.

### Step 1: Identify the Offset

From the `mmls` output:
- NTFS partition starts at sector 63.
- Sector size is 512 bytes, so the byte offset is 63 × 512 = 32,256 bytes.

### Command

You’d run `fsstat` on the disk image, specifying the offset of the NTFS partition:
```
fsstat -o 63 disk_image.dd
```
The `-o` option tells `fsstat` where the file system starts (in sectors).

### Sample Output

Here’s what the output might look like for an NTFS file system (simplified for clarity):
```
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: NTFS
Volume Serial Number: 1A2B-3C4D
OEM ID: NTFS
Version: Windows XP

METADATA INFORMATION
--------------------------------------------
Root Directory: 5
Cluster Size: 4096 bytes
Sector Size: 512 bytes

CONTENT INFORMATION
--------------------------------------------
Cluster Area Start: 63
Cluster Area End: 1028159
Total Cluster Range: 0 - 255024
$MFT Start Cluster: 42668
$MFT Mirror Start Cluster: 2

FAT INFORMATION
--------------------------------------------
Not Applicable (NTFS does not use a FAT)
```

### Explanation of the Output

1. **File System Information**:
   - Confirms it’s an NTFS file system.
   - Provides the volume serial number and version info (e.g., compatible with Windows XP).

2. **Metadata Information**:
   - Root directory is at cluster 5.
   - Cluster size is 4 KB (8 sectors), which is typical for NTFS.
   - Sector size matches the disk’s 512 bytes.

3. **Content Information**:
   - Cluster area aligns with the partition boundaries from `mmls` (adjusted for clusters).
   - `$MFT` (Master File Table) is the core metadata structure in NTFS, starting at cluster 42,668.
   - `$MFTMirr` is a backup, starting at cluster 2.

4. **FAT Information**:
   - Not relevant here since this is NTFS, not a FAT-based file system.

### Practical Use

- **Forensics**: You could use the `$MFT` location (cluster 42,668) to extract it with a tool like `icat` (`icat -o 63 disk_image.dd 5 > mft_output`) to analyze file metadata.
- **Recovery**: The cluster size and layout help determine how data is stored, aiding in file carving from unallocated clusters.
- **Validation**: Confirms the file system type matches what `mmls` reported (NTFS, 0x07).

### Another Example: FAT32

If you ran `fsstat` on the FAT32 partition from the `mmls` example (offset 1,028,160 sectors):
```
fsstat -o 1028160 disk_image.dd
```
Output might include:
```
FILE SYSTEM INFORMATION
--------------------------------------------
File System Type: FAT32
Number of FATs: 2
Cluster Size: 16384 bytes

CONTENT INFORMATION
--------------------------------------------
Cluster Area Start: 1028224
Total Cluster Range: 2 - 63998
```

This would show FAT-specific details like the number of File Allocation Tables and a larger cluster size.

### Your Next Step

If you’ve got a specific image or scenario in mind, I can tweak the example further. Want to analyze a real output, pair this with another tool, or explore a different file system? Let me know!

Since you’ve asked about `mmls` and `fsstat` earlier, it’s clear you’re diving into the Sleuth Kit tools for forensic analysis. The `fls` command (file list) is another key tool in this suite, used to list files and directories in a file system, including deleted ones, based on metadata like the NTFS `$MFT` or FAT directory entries. It’s a natural follow-up to `fsstat`, which gives you file system details, as `fls` lets you explore the contents.

Let’s build on the previous examples with `disk_image.dd`, where we identified an NTFS partition at sector 63 and a FAT32 partition at sector 1,028,160. I’ll provide an `fls` example for the NTFS partition.

### Command

To list files in the NTFS partition starting at sector 63:
```
fls -o 63 disk_image.dd
```
- `-o 63` specifies the offset in sectors where the NTFS file system begins (from the `mmls` output).

### Sample Output

Here’s what the output might look like (simplified):
```
r/r 5-128-1:    $MFT
r/r 6-128-1:    $MFTMirr
r/r 7-128-1:    $LogFile
d/d 8-144-4:    $Recycle.Bin
r/r * 9-128-3:  secret.txt (deleted)
d/d 10-144-2:   Documents
r/r 11-128-1:   Documents/note.txt
r/r 12-128-5:   Documents/photo.jpg
```

### Explanation of the Output

- **File Type**:
  - `r/r`: Regular file (allocated).
  - `d/d`: Directory (allocated).
  - `*`: Indicates the file is deleted but still has metadata (e.g., `secret.txt`).
- **Inode/Metadata Entry**:
  - The number before the colon (e.g., `5-128-1`) is the inode or metadata entry in a format like `inode-metadata_type-sequence`. For NTFS, this often ties to `$MFT` entries.
- **Name**:
  - The file or directory name. System files like `$MFT` are NTFS-specific metadata files.
- **Examples**:
  - `$MFT` (entry 5) is the Master File Table.
  - `secret.txt` (entry 9) is a deleted file.
  - `Documents/note.txt` (entry 11) is an allocated file in the `Documents` directory.

### Practical Use

- **Recover Deleted Files**: The deleted `secret.txt` (marked with `*`) could be extracted using `icat`:
  ```
  icat -o 63 disk_image.dd 9 > secret.txt
  ```
- **Directory Exploration**: To list only the contents of the `Documents` directory (inode 10):
  ```
  fls -o 63 disk_image.dd 10
  ```
  Output might be:
  ```
  r/r 11-128-1:   note.txt
  r/r 12-128-5:   photo.jpg
  ```
- **Full Paths**: Add the `-r` (recursive) and `-p` (full path) options for a detailed tree:
  ```
  fls -r -p -o 63 disk_image.dd
  ```
  Output might include:
  ```
  /$MFT
  /$Recycle.Bin
  /Documents/note.txt
  /Documents/photo.jpg
  ```

### FAT32 Example

For the FAT32 partition at offset 1,028,160:
```
fls -o 1028160 disk_image.dd
```
Output might look like:
```
d/d 2:          .
r/r 3:          BOOTSECT.BAK
d/d 4:          PHOTOS
r/r * 5:        oldfile.doc (deleted)
r/r 6:          PHOTOS/vacation.jpg
```
- FAT uses simpler inode numbers (e.g., 2, 3).
- Deleted files like `oldfile.doc` are still recoverable if the clusters haven’t been overwritten.

### Options to Enhance

- `-l`: Long format (shows timestamps, sizes).
- `-u`: Show only unallocated (deleted) entries.
- `-f ntfs`: Explicitly specify the file system type (e.g., `fls -f ntfs -o 63 disk_image.dd`).

### Your Move

If you’ve got a specific image, a file you want to focus on, or need help interpreting real `fls` output, let me know! I can also tie this back to `mmls` or `fsstat` results or suggest next steps like file recovery. What’s your goal here?

## Ref

- ChatGPT
