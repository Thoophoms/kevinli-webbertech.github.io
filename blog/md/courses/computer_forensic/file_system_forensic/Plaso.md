# Plaso (log2timeline) Tutorial – Digital Forensics & Incident Response (DFIR)

Plaso (**Pluggable Log Output Format**) is a powerful tool used for **timeline generation** from various **log sources** such as system logs, browser history, event logs, registry files, and more. It is widely used in **digital forensics and incident response (DFIR)**.

---

## **🛠 Step 1: Install Plaso (log2timeline)**
Plaso requires **Python 3** and can be installed on **Linux** or **Windows**.

### **Linux (Ubuntu/Debian)**
```bash
sudo add-apt-repository ppa:gift/stable
sudo apt update
sudo apt install plaso-tools
```

### **Windows**
- Install [Plaso Windows Package](https://github.com/log2timeline/plaso/releases)
- Add **Plaso** to the system’s `PATH` variable.

### **Verify Installation**
```bash
log2timeline.py --version
```

---

## **📂 Step 2: Collect Timeline from Logs**
Plaso processes logs and stores data in a **Plaso storage file (`.plaso`)**.

### **Extract Timeline from a Disk Image**
```bash
log2timeline.py timeline.plaso /mnt/evidence/disk_image.dd
```
🔹 This extracts **artifacts** (event logs, browser history, registry keys, etc.).

### **Extract from a Windows Directory**
```bash
log2timeline.py timeline.plaso /mnt/evidence/windows_drive/
```
🔹 Useful for live forensics where a disk image isn't available.

---

## **🔍 Step 3: View Extracted Artifacts**
Before full timeline analysis, verify extracted sources:
```bash
psort.py -o dynamic --analysis list timeline.plaso
```
🔹 This lists **available artifacts** in `timeline.plaso`.

---

## **📊 Step 4: Analyze Timeline**
### **1️⃣ Search for Events in a Date Range**
```bash
psort.py -o dynamic -w timeline.csv timeline.plaso --timestamp-filter "2024-02-01 00:00:00,2024-02-28 23:59:59"
```
🔹 Filters events between **February 1, 2024, and February 28, 2024**.

### **2️⃣ Find Suspicious User Activity**
```bash
psort.py -o dynamic timeline.plaso | grep "cmd.exe"
```
🔹 Looks for **command execution activity**.

### **3️⃣ Search for Deleted Files**
```bash
psort.py -o dynamic timeline.plaso | grep "Recycle Bin"
```
🔹 Shows files deleted by users.

---

## **🕵️ Step 5: Generate a Forensic Report**
### **1️⃣ Create a CSV Report**
```bash
psort.py -o l2tcsv -w forensic_report.csv timeline.plaso
```
🔹 Saves a **detailed forensic timeline** in `forensic_report.csv`.

### **2️⃣ Create a JSON Report (for further analysis)**
```bash
psort.py -o json -w forensic_timeline.json timeline.plaso
```
🔹 Can be imported into **Splunk or Kibana** for visualization.

---

## **🔑 Step 6: Find Key Evidence**
### **1️⃣ Extract Browser History**
```bash
psort.py -o dynamic timeline.plaso | grep "Chrome"
```
🔹 Finds **web browsing activity**.

### **2️⃣ Identify Suspicious USB Insertions**
```bash
psort.py -o dynamic timeline.plaso | grep "USBStor"
```
🔹 Checks if **USB devices were connected**.

### **3️⃣ Detect Logins & Logouts**
```bash
psort.py -o dynamic timeline.plaso | grep "Logon"
```
🔹 Shows **user login history**.

---

## **📄 Step 7: Final Report**
### **Forensic Report Example**
```
🔍 Plaso Timeline Analysis Report
----------------------------------------
📅 Date Range: 2024-02-01 to 2024-02-28
📂 Log Source: /mnt/evidence/windows_drive/
🖥️ System: Windows 10

🛠 Key Findings:
- 📌 User `john.doe` executed `cmd.exe` at 2024-02-10 14:32:10.
- 🔗 Suspicious website visited: `hacker-site.com`
- 🗑️ Files deleted in `C:\Users\john\Desktop\Sensitive.docx`
- 🔌 USB Device inserted: `SanDisk USB` at 2024-02-15 09:20:00.

🎯 Conclusion:
- The user attempted to delete and cover up activity.
- External storage was used, indicating **possible data exfiltration**.

✅ Recommendations:
- **Recover deleted files** from `C:\Users\john\Desktop\`
- **Check USB logs** for transferred data.
- **Block unauthorized USB devices** in Group Policy.
```

---

## Ref

- ChatGPT
- https://plaso.readthedocs.io/en/latest/