# LIEF - Evidence Extractor Tutorial

LIEF (**Library to Instrument Executable Formats**) is a powerful framework for **parsing, modifying, and analyzing executable files** like PE (Windows), ELF (Linux), and Mach-O (macOS). It is widely used in **reverse engineering** and **malware analysis**.

## **🛠 Step 1: Install LIEF**

LIEF can be installed using Python's package manager.

### **Linux/macOS**
```bash
pip install lief
```

### **Windows**
```bash
pip install lief
```
To verify installation:
```python
import lief
print(lief.__version__)
```

---

## **📂 Step 2: Load an Executable File**
LIEF supports **PE, ELF, and Mach-O** formats.

```python
import lief

# Load a Windows PE file
binary = lief.parse("malware.exe")

# Display general info
print(binary)
```

---

## **🔍 Step 3: Extract Evidence from a PE File**
### **1️⃣ Extract Sections of the Executable**
```python
for section in binary.sections:
    print(f"Name: {section.name}, Size: {section.size}")
```
🔹 This identifies sections like `.text`, `.data`, and `.rdata`, which may contain malicious code.

### **2️⃣ List Imported DLLs & Functions**
```python
for imp in binary.imports:
    print(f"Imported DLL: {imp.name}")
    for entry in imp.entries:
        print(f"  Function: {entry.name}")
```
🔹 Identifies **suspicious DLL imports** (e.g., `kernel32.dll`, `advapi32.dll`).

### **3️⃣ Extract Exported Functions**
```python
for exp in binary.exported_functions:
    print(f"Exported function: {exp}")
```
🔹 Useful for analyzing **malicious payloads**.

---

## **🦠 Step 4: Detect Malware Indicators**
### **1️⃣ Check for Packed Binaries**
Packed malware often has a small `.text` section but a large `.data` section.
```python
text_size = binary.get_section(".text").size
data_size = binary.get_section(".data").size

if text_size < 500 and data_size > 100000:
    print("🚨 Suspicious: Possible packed malware detected!")
```

### **2️⃣ Identify Suspicious Strings**
```python
import re

suspicious_patterns = ["http", "cmd.exe", "powershell"]
for section in binary.sections:
    content = section.content.tobytes().decode(errors='ignore')
    for pattern in suspicious_patterns:
        if re.search(pattern, content):
            print(f"🚨 Found suspicious string '{pattern}' in {section.name}")
```
🔹 Extracts strings like **URLs, commands, or encoded payloads**.

---

## **🕵️ Step 5: Modify & Reconstruct Executables**
### **1️⃣ Remove a Dangerous Import (Evasion)**
```python
binary.remove_library("wininet.dll")
binary.write("cleaned.exe")
print("🚀 Cleaned executable saved!")
```
🔹 Removes **malicious imports** from the binary.

### **2️⃣ Inject a New Import**
```python
binary.add_library("user32.dll")
binary.write("modified.exe")
```
🔹 Injects **new DLLs** into the executable.

## **📊 Step 6: Generate a Forensic Report**
```python
report = f"""
🔍 LIEF Malware Analysis Report
----------------------------------
File: {binary.name}
Machine: {binary.header.machine}
Number of Sections: {len(binary.sections)}

📂 Sections:
"""
for section in binary.sections:
    report += f"  - {section.name}: {section.size} bytes\n"

report += "\n🔗 Imported DLLs:\n"
for imp in binary.imports:
    report += f"  - {imp.name}\n"

with open("forensic_report.txt", "w") as f:
    f.write(report)

print("📄 Report saved as forensic_report.txt!")
```

## Ref

- ChatGPT
- https://github.com/lief-project/LIEF
- https://lief.re/doc/latest/tutorials/01_play_with_formats.html