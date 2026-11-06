# Forensic analysis using Sleuth (solution and lab)

This hands-on exercise will guide you through a real-world forensic analysis scenario using The Sleuth Kit (TSK).

---

## ** Scenario**

A company suspects that an employee deleted sensitive files from a **USB drive** before quitting. Your job as a forensic investigator is to:
1. Identify the partitions on the disk image.
2. List existing and deleted files.
3. Recover a deleted file.
4. Analyze file timestamps to create a timeline.

---

## **🔹 Step 1: Download a Sample Disk Image**
Download a sample forensic disk image from **Digital Corpora** or use the one below:

📥 **Download Sample Image:**  
👉 [Forensic Disk Image](https://dftt.sourceforge.net/test8.tar.gz)

Extract the `.tar.gz` file:
```bash
tar -xvzf test8.tar.gz
cd test8
```

---

## **🔹 Step 2: Identify Partitions**
Run the `mmls` command to check the disk image structure.
```bash
mmls test8.E01
```
**Example Output:**
```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot    Start        End        Length       Description
000:  0000000000   0000002047   0000002048   Primary Table (#1)
001:  0000002048   0001048575   0001046528   NTFS (0x07)
```
**Observation:**  
The NTFS partition starts at **sector 2048**.

---

## **🔹 Step 3: List Files**
Use `fls` to list files in the NTFS partition:
```bash
fls -o 2048 test8.E01
```
Example Output:
```
r/r 5-128-3: $AttrDef
r/r 6-144-3: $Bitmap
d/d 11-128-3: Documents
r/r 20-160-4: secret.pdf (deleted)
```
**Observation:**  
The file **secret.pdf** has been deleted but can be recovered. Its inode is **20**.

---

## **🔹 Step 4: Recover Deleted File**
Use `icat` to recover the deleted file:
```bash
icat -o 2048 test8.E01 20 > recovered_secret.pdf
```
Verify the recovered file:
```bash
ls -lh recovered_secret.pdf
file recovered_secret.pdf
```
If the file opens successfully, it means we successfully recovered it.

---

## **🔹 Step 5: Extract Metadata**
Use `istat` to analyze the recovered file:
```bash
istat test8.E01 -o 2048 20
```
Example Output:
```
M: 2023-01-10 14:35:22
A: 2023-01-10 14:40:15
C: 2023-01-10 14:30:50
D: 2023-01-11 09:45:00
```
**Observation:**  
- The file was last **modified** on January 10, 2023.
- It was **deleted** on January 11, 2023, at 09:45 AM.

---

## **🔹 Step 6: Generate a Timeline**
1. Extract file system metadata:
```bash
fls -r -o 2048 test8.E01 > filelist.txt
```
2. Generate a timeline CSV:
```bash
mactime -b filelist.txt -d > forensic_timeline.csv
```
3. Open `forensic_timeline.csv` in Excel or a text editor to analyze **who modified, accessed, or deleted files**.

---

## **🎯 Summary of Findings**
✅ Identified that **secret.pdf** was deleted.  
✅ Successfully recovered the deleted file.  
✅ Extracted timestamps showing when it was modified and deleted.  
✅ Created a forensic timeline for investigation.

## **🛠️ Additional Exercises**

- Try finding **other deleted files** using `ils`:

  ```bash
  ils -o 2048 test8.E01
  ```
- Search for **specific keywords** in the unallocated space:

  ```bash
  blkls -o 2048 test8.E01 | strings | grep "password"
  ```

## Ref

- ChatGPT
- https://corp.digitalcorpora.org/corpora/drives/nps-2009-ntfs1/