### **File System Forensics**

**File System Forensics** is a critical aspect of **digital forensics**, which involves the analysis and investigation of file systems to extract, recover, and analyze data for legal or investigative purposes. The goal is to examine a file system (whether on a hard drive, SSD, or any other storage medium) to uncover evidence of actions, such as file deletion, unauthorized access, malware activity, or data manipulation.

### **Core Concepts in File System Forensics**

1. **File System Overview**:
   - A **file system** is a method of organizing and storing data on a storage device (such as a hard drive or SSD). It defines how files are named, stored, and retrieved.
   - Common file systems include:
     - **FAT32 (File Allocation Table)**: Older, commonly used in flash drives and external drives.
     - **NTFS (New Technology File System)**: Used primarily in Windows operating systems.
     - **EXT4 (Fourth Extended File System)**: Common in Linux-based systems.
     - **APFS (Apple File System)**: Used in macOS and iOS devices.
     - **exFAT (Extended File Allocation Table)**: Used in large drives or flash drives, particularly with Windows and macOS.

2. **File System Forensics**:
   - File system forensics involves recovering and analyzing the contents of a file system to detect criminal or unauthorized activity, investigate data breaches, or verify compliance.
   - A forensic examiner can use specialized tools to examine file system structures, recover deleted files, and identify abnormal file access patterns.

### **Key Elements of File System Forensics**

1. **File Metadata**:
   - **Metadata** refers to the additional information about a file, such as:
     - **File name**: The name of the file.
     - **File size**: The size of the file in bytes.
     - **Timestamps**: Time-related data such as **creation time**, **last modified time**, and **last accessed time**.
     - **File permissions**: Who has access to the file (read, write, execute permissions).
     - **File ownership**: Information about who owns the file.
     - **Location**: The physical location of the file's data blocks on the storage device.

   - **Timestamps** are critical in forensic investigations because they can show when a file was created, modified, or accessed, which is valuable for establishing timelines.

2. **Deleted Files and Data Recovery**:
   - Even if a file is deleted, its data might not be completely erased from the storage medium. The file's metadata may be removed, but the actual data can remain in the sectors of the disk until it is overwritten.
   - **File carving** is a technique used to recover deleted files by scanning the raw data of the disk and identifying file headers and footers.
   - Tools such as **EnCase**, **FTK Imager**, or **Autopsy** can help recover deleted files or fragments of files.

3. **Slack Space**:
   - **Slack space** is unused space between the end of a file's data and the end of the allocated block on the disk. The space can contain remnants of deleted or previously written files.
   - Investigators may analyze slack space to find leftover data from deleted files or fragments of files that may be relevant to an investigation.

4. **File System Structures**:
   - **File Allocation Table (FAT)**: In FAT file systems, the FAT keeps track of the clusters that belong to each file. Forensics can track how files were allocated and deleted by examining the FAT.
   - **Master File Table (MFT)**: In **NTFS**, the MFT stores records for each file and directory. Forensics can analyze the MFT for details about the file, including metadata and previous file versions.
   - **Inodes**: In **Linux file systems** like EXT4, inodes contain metadata about files and directories, including ownership, permissions, and timestamps.

5. **Volume Shadow Copies**:
   - In Windows systems, **Volume Shadow Copies** are automatic backups that Windows creates periodically or during certain system events.
   - These copies can provide forensic investigators with snapshots of file systems at specific times, helping to recover files or track changes over time.

### **File System Forensic Process**

1. **Identification and Preservation**:
   - The first step in a forensic investigation is to identify and preserve the data from the target storage device. This often involves creating a **forensic image** of the storage medium to ensure the original evidence is not altered.
   - This image is an exact bit-by-bit copy of the drive, including unallocated space, file slack, and deleted files.

2. **Analysis of File System Structures**:
   - The forensic investigator examines the file system's structure, including metadata, directory structure, and file allocation table, to understand how the data was stored and how files might have been deleted or modified.
   - Investigators can look for anomalies, such as **unexpected timestamps** or **file access patterns** that might suggest malicious activity.

3. **Recover Deleted Files**:
   - The examiner attempts to recover deleted files using **file carving** tools or by searching for unallocated space where the file data may still exist. Forensic tools like **Recuva**, **Photorec**, or **X1 Search** can help recover deleted files.

4. **Examine Timestamps and Logs**:
   - Timestamps, such as **last accessed** or **last modified** times, can provide critical information for establishing a timeline of activities.
   - Log files from the operating system, applications, or security software can also provide insight into actions that occurred on the file system.

5. **Investigate Metadata**:
   - Investigators examine file metadata to determine whether files were tampered with or copied. For example, if a file’s **modified date** is suspiciously recent or inconsistent with other data, it could indicate tampering.

6. **Reporting**:
   - Once analysis is complete, a forensic report is generated, summarizing findings such as recovered files, anomalies, timeline of events, and potential evidence of illegal activities.

### **Forensic Tools for File System Analysis**

Several specialized forensic tools are available for examining file systems, recovering data, and analyzing disk images:

1. **EnCase**:
   - A comprehensive digital forensics tool used for disk imaging, file system analysis, and evidence recovery. EnCase can examine NTFS, FAT, EXT, and other file systems.

2. **FTK Imager**:
   - A forensic tool used to create disk images, recover deleted files, and analyze file systems. It can examine both Windows and Unix-based file systems.

3. **Autopsy**:
   - An open-source forensic analysis tool that can analyze file systems, recover deleted files, and create timeline reports. It supports FAT, NTFS, and EXT file systems.

4. **X1 Search**:
   - A tool used for indexing and searching large volumes of data, particularly useful in finding files or emails that match specific keywords or patterns.

5. **The Sleuth Kit (TSK)**:
   - A collection of command-line tools used for file system forensic analysis, including file and directory discovery, recovering deleted files, and more. It also includes **Autopsy** as a graphical user interface.

6. **Recuva**:
   - A simple tool used for recovering deleted files from FAT and NTFS file systems. It is useful for smaller-scale investigations where rapid recovery of lost files is needed.

### **File System Forensics in Legal Context**

File system forensics is often used in legal investigations, such as:
- **Cybercrime investigations**: To uncover evidence of hacking, data theft, or unauthorized access to systems.
- **Corporate investigations**: To verify compliance with security policies, identify insider threats, or detect fraudulent activity.
- **Civil litigation**: To recover documents, emails, or other electronic evidence for use in court.
  
Forensics must adhere to strict protocols to ensure that the evidence collected is **admissible** in court, including:
- Properly **documenting** the evidence collection process.
- Ensuring the **chain of custody** is maintained (tracking the evidence from the crime scene to the final report).
- Using forensic tools that comply with standards and can generate reports that are understandable and reliable in a legal setting.

**File system forensics** is a crucial part of digital forensics, allowing investigators to recover, analyze, and preserve digital evidence stored on file systems. By examining file metadata, timestamps, deleted files, and file system structures, forensic experts can uncover significant evidence, whether in criminal investigations, corporate fraud, or regulatory compliance.

## **File System Forensics on Windows**

In **Windows environments**, **file system forensics** plays a critical role in the investigation of incidents, breaches, or unauthorized activities. The Windows operating system uses several types of file systems, with the most common being **NTFS (New Technology File System)**, but older versions of Windows also support **FAT (File Allocation Table)**. Modern Windows systems use **NTFS** for its security features, support for large files, and efficient data management.

Windows-specific file system forensics involves recovering, analyzing, and preserving digital evidence from Windows-based file systems, including **NTFS**, **FAT**, and **exFAT** (for external drives and flash storage). Investigators use a variety of specialized tools to explore Windows file systems and retrieve valuable evidence.

---

### **Key Concepts in Windows File System Forensics**

#### **1. NTFS (New Technology File System)**

- **NTFS** is the primary file system used in modern Windows operating systems. It offers several features that are important for forensic investigations:
  - **Master File Table (MFT)**: The MFT stores information about all files and directories on the disk. It includes metadata like file names, sizes, timestamps, and locations of file data.
  - **File Timestamps**: NTFS tracks the **Creation**, **Last Modified**, and **Last Accessed** times for each file.
  - **Alternate Data Streams (ADS)**: NTFS allows files to have multiple streams, which can be used for hidden data storage.
  - **File System Journaling**: NTFS includes a transaction log (journal) that tracks changes to the file system, making it useful for recovering data after crashes or shutdowns.

#### **2. FAT (File Allocation Table)**

- **FAT** is an older file system used in legacy Windows systems and often found in flash drives and external drives.
  - **FAT32** is the most common version of FAT used for external storage devices, but it has limitations on file size and partition size (supports up to 4GB files).
  - **FAT File Structure**: FAT keeps track of clusters on a disk and allocates clusters to files. Forensics can use the **FAT table** to determine where files were located and to recover deleted files by identifying clusters that were previously allocated but are not overwritten.

#### **3. Windows Volume Shadow Copies**

- **Volume Shadow Copies** are **backups** of the file system taken at specific points in time. Windows automatically creates these copies for system restore and backup purposes.
  - Shadow copies can contain versions of files that have been deleted or modified.
  - Investigators can recover files or examine previous versions of files using **Volume Shadow Copies**. This is particularly useful when trying to retrieve deleted or altered files that were previously backed up.

#### **4. File Timestamps in Windows**

- **Timestamps** are vital in forensics for tracking file activities, such as creation, modification, and access times. The main timestamps are:
  - **Creation Time**: When the file was created.
  - **Last Accessed Time**: The last time the file was accessed (read).
  - **Last Modified Time**: The last time the file content was modified.

- These timestamps are stored in the **MFT (for NTFS)** or **FAT Table** (for FAT file systems), and they are essential for establishing a timeline of events in forensic investigations.

#### **5. Slack Space and Unallocated Space**

- **Slack Space**: This is the unused space between the end of a file and the end of its allocated cluster. Even though the file may appear to be fully written, the slack space can contain remnants of deleted or modified files.
- **Unallocated Space**: This refers to the areas on the disk that are not currently assigned to any files. These areas can still contain traces of deleted files and are often recovered using specialized tools.

---

### **File System Forensics Process in Windows**

#### **1. Collection and Preservation of Evidence**
The first step in forensic analysis is to preserve the integrity of the evidence:
- **Create a forensic image** of the Windows system drive using tools such as **FTK Imager**, **dd**, or **Guymager**. This image is a bit-for-bit copy of the disk and is used for further analysis, preserving the original evidence.
- Ensure the **chain of custody** is maintained. Document the acquisition process thoroughly to ensure the evidence is admissible in court.

#### **2. Analyzing File System Structures**

- **MFT Analysis**: In **NTFS**, the Master File Table (MFT) contains essential file metadata, including timestamps, file locations, file names, and access permissions. MFT entries for deleted files might still exist, allowing forensic investigators to recover these files.
- Use forensic tools such as **The Sleuth Kit (TSK)** or **Autopsy** to examine MFT records and uncover evidence related to file access, modification, and deletion.
- **FAT Table Analysis**: In FAT file systems, the FAT table maps out clusters allocated to files. By examining the FAT, investigators can determine file locations, recover deleted files, and check if data has been overwritten.

#### **3. Recovering Deleted Files**

- **Deleted Files Recovery**: Even though files are deleted, the data may still reside on the disk in unallocated clusters until they are overwritten. Forensic tools can recover this data using methods like:
  - **File carving**: Searching the raw disk for file signatures and reconstructing files.
  - **NTFS $LogFile**: NTFS maintains a transaction log, and forensic investigators can analyze it to recover deleted file data or uncover any file system anomalies.
  
- Tools like **Recuva**, **EnCase**, **FTK Imager**, and **Autopsy** can recover deleted files and even provide insights into the file system's state prior to deletion.

#### **4. Investigating Alternate Data Streams (ADS)**

- **Alternate Data Streams (ADS)** in NTFS allow files to have hidden metadata or data, which can be used by malware or attackers to conceal data.
- Use forensic tools like **Streams** (from the Sysinternals suite) to identify and analyze any hidden data within alternate data streams.

#### **5. Investigating Windows Event Logs**

- **Windows Event Logs** (Application, Security, System logs) can provide vital information about user activities, file access, authentication attempts, and system errors.
- **Event Log Analysis** can uncover critical evidence such as:
  - **User logins/logouts**
  - **File access and modifications**
  - **Malicious activity, such as failed login attempts or privilege escalation attempts**

- **Event Viewer** and tools like **LogParser** or **X1 Search** are used to analyze Windows event logs.

#### **6. Timeline Analysis**

- Timeline analysis involves creating a chronological sequence of events (e.g., file creation, access, modification, deletion, login activities) based on timestamps and other file system data.
- This can be done using tools such as **Plaso** or **Timeline Explorer**, which help build timelines for digital investigations by analyzing file metadata, logs, and other artifacts.

#### **7. Investigating Volume Shadow Copies**

- **Volume Shadow Copies** contain previous versions of files and can help recover files that were deleted or modified.
- Use tools like **ShadowExplorer** or **VShadow** to examine and recover files from volume shadow copies.

#### **8. Reporting Findings**

- After performing the analysis, the forensic examiner will prepare a detailed report that includes:
  - A description of the tools and methods used.
  - The chain of custody and how evidence was handled.
  - Findings and conclusions regarding deleted files, timestamps, and any potential criminal activity.
  - Screenshots or data extracts to support findings.



