# Analyzing Malware in Memory with Volatility

When investigating **malware in RAM dumps**, Volatility provides several plugins to detect hidden processes, injected code, and rootkits. This guide will walk you through **malware detection and analysis**.

---

## **Step 1: Identify the Memory Profile**
First, determine the OS version of the memory image:
```bash
volatility -f memory_dump.raw imageinfo
```
Example Output:
```
Suggested Profiles: Win7SP1x64, Win10x64_19041
```
🔹 **Select the most accurate profile** for later analysis.

---

## **Step 2: Identify Suspicious Processes**

### **List Running Processes**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 pslist
```
🔹 Look for unusual processes (e.g., randomly named executables).

### **Find Hidden or Terminated Processes**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 psscan
```
🔹 This scans for processes that may not appear in `pslist` (possible rootkits).

### **Compare Process Lists**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 pstree
```
🔹 Displays parent-child relationships to check for **orphaned/malicious processes**.

#### **Example Suspicious Process**
```
Name         PID   PPID  Threads  Handles
cmd.exe      3444  2844  2        31
svchost.exe  9999  0     1        5  (Hidden)
```
🔹 `svchost.exe` **with no parent process (PPID = 0)** is suspicious.

---

## **Step 3: Check Process DLLs & Handles**
### **Check DLLs Loaded by a Process**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 dlllist -p 3444
```
🔹 Malware often loads **unusual DLLs** or injects into system processes.

### **Check Open Files by a Process**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 handles -p 3444
```
🔹 Identifies files being accessed by a **suspicious process**.

---

## **Step 4: Detect Code Injection**
### **Scan for Injected Code**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 malfind -p 3444 -D output/
```
🔹 This detects **hidden or injected code** inside legitimate processes.

#### **Example Output**
```
Process: svchost.exe Pid 9999
Injected Code: 0x01ff2300
```
🔹 Possible **malware injection detected in svchost.exe**.

### **Dump the Injected Code**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 procdump -p 9999 -D output/
```
🔹 Extracts the **entire process memory** for further analysis.

---

## **Step 5: Investigate Network Connections**
### **List Active Network Connections**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 netscan
```
🔹 Identifies **remote IPs** and malware **C2 (Command & Control) servers**.

#### **Example Suspicious Connection**
```
Proto Local Address  Foreign Address   State       PID
TCP   192.168.1.10:50234  45.33.32.156:80  ESTABLISHED 3444
```
🔹 Malware **connecting to an external IP**.

### **Reverse Lookup the IP**
```bash
whois 45.33.32.156
```
🔹 Check if it's a known **malicious server**.

---

## **Step 6: Extract Malware Artifacts**
### **Find Dropped Files**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 filescan
```
🔹 Lists **all files** in memory.

### ** Dump a Suspicious File**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 dumpfiles -Q 0x823b3d98 -D output/
```
🔹 Extracts a **malware executable** from memory.

### ** Analyze Extracted Files**
Run `strings` to check for readable content:
```bash
strings output/malware.exe | less
```
🔹 Look for **C2 domains, IPs, passwords, or encoded payloads**.

---

## **Step 7: Scan for Rootkits**
### **Check for API Hooking (Malware Modifications)**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 apihooks
```
🔹 Finds **hooked Windows APIs** (signs of malware hiding itself).

### **Scan for Kernel Rootkits**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 modscan
```
🔹 Checks for **suspicious kernel drivers**.

### **Dump a Malicious Kernel Driver**
```bash
volatility -f memory_dump.raw --profile=Win7SP1x64 moddump -D output/
```
🔹 Extracts a **rootkit driver** for analysis.

---

## **Step 8: Forensic Report**

### **Sample Report:**
```
**Case ID**: 2024-MALWARE-ANALYSIS
**Investigator**: [Your Name]
**Date**: [Date of Analysis]
**Memory Image**: memory_dump.raw

**Findings:**
1. **Malicious Process Identified**:
   - Process: `svchost.exe`
   - Injected Code at: `0x01ff2300`
   - Parent Process: `N/A (Hidden)`

2. **Suspicious Network Connection**:
   - Remote IP: `45.33.32.156`
   - Port: `80 (HTTP)`
   - Potential C2 Server

3. **Extracted Malware**:
   - Filename: `malware.exe`
   - Strings Analysis: Contains `C2 URL: hacker-server.com`
   - MD5 Hash: `b6f9a3f5d4e5671a3a99c9b731b0f3e7`

**Conclusion:**
- `svchost.exe` is likely compromised via **code injection**.
- The malware is communicating with `45.33.32.156` (C2 Server).
- Extracted malware sample requires further **sandbox analysis**.

**Recommendations:**
- **Block IP 45.33.32.156** in the firewall.
- Submit `malware.exe` to **VirusTotal** for scanning.
- Isolate the affected system for further analysis.
```

## Ref

- ChatGPT