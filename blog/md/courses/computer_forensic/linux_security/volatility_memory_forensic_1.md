# Volatility Memory Forensics Tutorial

Volatility is a powerful **memory forensics** tool used to analyze **RAM dumps** and extract digital evidence, such as running processes, network connections, open files, and even passwords.

---

## **🛠 Step 1: Install Volatility**
### **Linux (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install volatility
```
### **Windows**
- Download **Volatility 2** from: [Volatility GitHub](https://github.com/volatilityfoundation/volatility)
- Install Python 2.7 (for Volatility 2) or Python 3 (for Volatility 3)

### **macOS**
```bash
brew install volatility
```

To check if Volatility is installed:
```bash
volatility -h
```

---

## **📥 Step 2: Get a Sample Memory Dump**
To analyze a real RAM dump, you need a memory image (`.raw`, `.bin`, `.mem`).  
### 📥 **Download Sample Memory Dumps**
- **Digital Corpora**: [Download here](https://digitalcorpora.org/corpora/memory-images)
- **Volatility Foundation**: [Test Images](https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples)

Or capture your own:
```bash
sudo ./winpmem-3.3.rc3.exe --output memory_dump.raw
```
_(For Windows, use **WinPMEM** to create a memory image)_

---

## **🔍 Step 3: Identify Memory Profile**
Before analysis, determine the OS profile:
```bash
volatility -f memory_dump.raw imageinfo
```
Example Output:
```
Suggested Profiles: Win10x64_19041, Win10x64_1809
```
🔹 **Note the suggested profile** (`Win10x64_19041` in this case).

---

## **📊 Step 4: List Running Processes**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 pslist
```
Example Output:
```
Offset(V) Name          PID    PPID    Threads Handles
0x823b3d98 explorer.exe 2844   1384    32      454
0x823b3c00 cmd.exe      3444   2844    2       31
```
🔹 Shows all **running processes**, parent processes, and IDs.

To see **hidden/malicious processes**, use:
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 psscan
```

---

## **🌐 Step 5: Check Network Connections**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 netscan
```
Example Output:
```
Proto Local Address  Foreign Address State       PID
TCP   192.168.1.10:50234  45.33.32.156:80  ESTABLISHED 1234
```
🔹 Suspicious connections? Look up the IP address.

---

## **📂 Step 6: List Open Files**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 filescan
```
🔹 Helps find **files open by malware**.

To dump a file:
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 dumpfiles -Q 0x823b3d98 -D output/
```
_(Replace `0x823b3d98` with the file offset)_

---

## **🕵️ Step 7: Extract Passwords**
🔹 **Dump Windows Hashes (for password cracking)**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 hashdump
```
🔹 **Find plaintext passwords**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 mimikatz
```
_(Mimikatz extracts credentials from Windows memory.)_

---

## **📸 Step 8: Dump & Analyze Process Memory**
🔹 **Extract process memory to find hidden commands or malware**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 memdump -p 3444 -D output/
```
_(Dumps `cmd.exe` memory to `output/`)_

Analyze the memory dump:
```bash
strings output/3444.dmp | grep "password"
```
_(Search for passwords in dumped process memory)_

---

## **🛠 Step 9: Detecting Malware**
🔹 **Find suspicious DLLs loaded by processes**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 dlllist
```
🔹 **Scan for hidden or injected code**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 malfind
```
🔹 **Detect anomalies in kernel memory**
```bash
volatility -f memory_dump.raw --profile=Win10x64_19041 apihooks
```

---

## **📊 Step 10: Generate a Forensic Report**
### Sample Report:
```
**Case ID**: 2024-DFIR-002
**Investigator**: [Your Name]
**Date**: [Date of Analysis]
**Memory Image**: memory_dump.raw
**Findings**:
- Suspicious process `cmd.exe` (PID: 3444) running under `explorer.exe`
- Network connection to `45.33.32.156:80` (potential malicious server)
- Extracted credentials using `mimikatz`
- Dumped process memory revealing hardcoded passwords
**Conclusion**:
- `cmd.exe` might be a malicious backdoor
- Further investigation needed on remote connections
```

---
## Ref

- ChatGPT