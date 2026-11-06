# **📊 Advanced Log Filtering with Logcheck**

By default, **Logcheck** scans system logs and reports unusual events. However, **false positives** and **irrelevant logs** can overwhelm administrators. To make Logcheck more useful, we need **custom filtering rules**.

---

## **🔧 Step 1: Understanding Logcheck Rule Files**
Logcheck uses **rule sets** to filter log messages. The rules are stored in:
- `/etc/logcheck/ignore.d.workstation/`
- `/etc/logcheck/ignore.d.server/`
- `/etc/logcheck/ignore.d.paranoid/`

Each directory corresponds to a **report level**:
- **Workstation** → Low sensitivity (basic filtering)
- **Server** → Medium sensitivity (recommended for sysadmins)
- **Paranoid** → High sensitivity (for security-critical systems)

---

## **📝 Step 2: Creating Custom Ignore Rules**
To ignore unwanted log entries, create a new rule file.

### **1️⃣ Create a Custom Rule File**
```bash
sudo nano /etc/logcheck/ignore.d.server/custom.rules
```
_Add rules based on log patterns._

### **2️⃣ Example: Ignore SSH Successful Logins**
To prevent Logcheck from reporting normal SSH logins:
```
^\w{3} [ :0-9]{11} myserver sshd\[[0-9]+\]: Accepted password for .* from [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ port [0-9]+
```
🔹 This regex pattern **ignores successful SSH logins**.

### **3️⃣ Example: Ignore Systemd Service Restarts**
```
^\w{3} [ :0-9]{11} myserver systemd\[[0-9]+\]: Starting .* service
```
🔹 **Prevents false alerts** when services restart.

---

## **🔍 Step 3: Filtering Out Noisy Logs**
Some services generate logs that are **not security-related** but clutter reports.

### **1️⃣ Ignore Common Kernel Messages**
To filter out standard kernel messages:
```bash
sudo nano /etc/logcheck/ignore.d.server/kernel.rules
```
Add:
```
^\w{3} [ :0-9]{11} myserver kernel: \[.*\] ata[0-9]: SATA link down
^\w{3} [ :0-9]{11} myserver kernel: \[.*\] usb [0-9]-[0-9]: reset full-speed USB device
```
🔹 These **ignore SATA and USB device resets**.

### **2️⃣ Ignore Periodic Cron Job Logs**
Create a rule to ignore cron jobs:
```bash
sudo nano /etc/logcheck/ignore.d.server/cron.rules
```
Add:
```
^\w{3} [ :0-9]{11} myserver CRON\[[0-9]+\]: \(root\) CMD \(/usr/bin/updatedb\)
```
🔹 **Prevents false alerts from cron jobs**.

---

## **🚨 Step 4: Custom Alerts for Critical Events**
Instead of ignoring everything, we can **prioritize** important logs.

### **1️⃣ Alert on Multiple SSH Failures (Possible Brute Force)**
Create an alert rule:
```bash
sudo nano /etc/logcheck/violations.d/bruteforce.rules
```
Add:
```
^\w{3} [ :0-9]{11} myserver sshd\[[0-9]+\]: Failed password for invalid user .*
^\w{3} [ :0-9]{11} myserver sshd\[[0-9]+\]: Failed password for root from .*
```
🔹 **This ensures failed SSH attempts are reported.**

### **2️⃣ Alert on Unauthorized Sudo Attempts**
Create a rule:
```bash
sudo nano /etc/logcheck/violations.d/sudo.rules
```
Add:
```
^\w{3} [ :0-9]{11} myserver sudo\[[0-9]+\]: .* authentication failure; user=.* tty=.* ruser=.* rhost=.*
```
🔹 Reports **failed sudo attempts**.

---

## **🛠 Step 5: Test Log Filtering**
To check if Logcheck ignores rules correctly, run:
```bash
sudo logcheck -t
```
If **filtered logs still appear**, adjust the **regex patterns** in `ignore.d.server`.

---

## **📄 Step 6: Review Logcheck Reports**
Filtered logs appear in:
```bash
sudo cat /var/log/logcheck/logcheck.log
```
Or receive reports via email:
```bash
cat /var/mail/root
```
🔹 **Review logs daily** to detect anomalies.

---

## **🚀 Next Steps**
✅ Need help **optimizing regex filters**?  
✅ Want to **integrate Logcheck with Fail2Ban** for automatic blocking? 🚨