# Logcheck - Linux Log 

`Logcheck` is a tool that helps identify suspicious entries in Linux log files by filtering out routine messages and highlighting potential security issues.

## Key Features:

* Log monitoring: Automatically checks and sends reports of suspicious log activity.
* Customizable: Allows users to set custom thresholds for alerting based on log contents.

## Use Cases:

Analyzing logs for unauthorized login attempts, privilege escalation, or suspicious activity.


# **📜 Logcheck - Linux Log Monitoring Tool**
Logcheck is a **Linux log monitoring** tool that scans system logs and reports anomalies or security events. It is useful for **system administrators** and **security analysts** to detect unauthorized access, system errors, or suspicious activities.

---

## **🛠 Step 1: Install Logcheck**
Logcheck is available in most Linux distributions.

### **Debian/Ubuntu**
```bash
sudo apt update
sudo apt install logcheck
```

### **CentOS/RHEL (Install via EPEL)**
```bash
sudo yum install epel-release
sudo yum install logcheck
```

### **Verify Installation**
```bash
logcheck -h
```

---

## **📂 Step 2: Configure Logcheck**
The configuration files are located at:
- **Main config file**: `/etc/logcheck/logcheck.conf`
- **Rules directory**: `/etc/logcheck/ignore.d/`

### **1️⃣ Edit Configuration File**
```bash
sudo nano /etc/logcheck/logcheck.conf
```
Modify these parameters:
```ini
REPORTLEVEL="server"   # Options: workstation, server, paranoid
LOGFILE="/var/log/syslog"   # Change if needed
SENDMAILTO="admin@example.com"
```
🔹 **REPORTLEVEL**:
   - `workstation` (less strict, normal logs ignored)
   - `server` (moderate security alerts)
   - `paranoid` (very strict, reports all anomalies)

---

## **🔍 Step 3: Run Logcheck Manually**
To analyze logs immediately:
```bash
sudo logcheck
```
This will scan system logs and output a **summary of security events**.

To scan a specific log file:
```bash
sudo logcheck -l /var/log/auth.log
```

---

## **📊 Step 4: Automate Log Monitoring**
You can schedule Logcheck to run periodically using **cron**.

### **1️⃣ Edit Cron Job**
```bash
sudo nano /etc/cron.d/logcheck
```
Add:
```
0 * * * * logcheck /usr/sbin/logcheck
```
🔹 This runs Logcheck **every hour**.

---

## **🔑 Step 5: Customizing Logcheck Rules**
### **1️⃣ Ignore Unwanted Log Entries**
To prevent false alerts, add rules to **ignore.d.server**:
```bash
sudo nano /etc/logcheck/ignore.d.server/custom.rules
```
Example rule to ignore SSH login from a trusted IP:
```
^\w{3} [ :0-9]{11} myserver sshd\[[0-9]+\]: Accepted password for root from 192.168.1.10 port [0-9]+
```
Save and reload Logcheck.

---

## **🕵️ Step 6: Analyze Logcheck Reports**
Logcheck sends reports via **email** or **console output**.

### **View Latest Report**
```bash
sudo cat /var/log/logcheck/logcheck.log
```

### **Search for Suspicious Activity**
```bash
sudo grep "Possible Attack" /var/log/logcheck/logcheck.log
```
🔹 This helps find **failed logins, brute force attacks, and system errors**.

---

## **📄 Example Logcheck Report**
```
System Events Summary - 2024-03-01 12:00:00

🚨 Security Warnings:
- [SSH] 10 Failed login attempts from 192.168.1.50
- [Sudo] Unauthorized sudo attempt by user 'hacker'
- [Kernel] Unusual CPU spikes detected

📂 System Errors:
- [Disk] /dev/sda1 reaching 95% capacity
- [Service] Apache crashed unexpectedly

🎯 Recommendations:
- Block 192.168.1.50 in the firewall.
- Investigate unauthorized sudo attempt.
- Check Apache logs for crash reasons.
```

---
