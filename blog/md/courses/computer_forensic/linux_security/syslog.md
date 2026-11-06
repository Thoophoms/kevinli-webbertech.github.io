# Syslog

Syslog is a standard logging system used in many Linux distributions.
Logs are stored in `/var/log/`, and common logs include /var/log/syslog (system logs), /var/log/auth.log (authentication logs), and /var/log/messages (system messages).

## Key Features:

* System and application logs: Analyze logs for any signs of unauthorized access or system errors.
* Centralized logging: Syslog can forward logs to remote servers for centralized logging.

## Use Cases:

* Reviewing system events and network access.
* Detecting unauthorized logins, system reboots, or application failures.

# **📜 Syslog – Centralized Log Management in Linux**
Syslog is a **logging system** used in Linux to **capture system events** and forward logs to local or remote locations. It is essential for **monitoring, debugging, and security auditing**.

---

## **🛠 Step 1: Check if Syslog is Installed**
Most Linux distributions use **syslog variants** like:
- `rsyslog` (modern syslog, default in Ubuntu/Debian)
- `syslog-ng` (more advanced, flexible alternative)
- `journalctl` (for systemd-based logs)

Check if Syslog is running:
```bash
systemctl status rsyslog
```
If it's not installed, install it:
```bash
sudo apt install rsyslog    # Debian/Ubuntu
sudo yum install rsyslog    # RHEL/CentOS
```

---

## **📂 Step 2: Locate Syslog Logs**
Common syslog files:
```bash
/var/log/syslog         # General system logs (Ubuntu/Debian)
/var/log/messages       # General logs (RHEL/CentOS)
/var/log/auth.log       # Authentication logs
/var/log/kern.log       # Kernel messages
/var/log/mail.log       # Mail server logs
/var/log/secure         # Security logs (RedHat-based)
```

---

## **🔍 Step 3: Viewing Syslog Logs**
### **1️⃣ View the Latest Logs**
```bash
sudo tail -f /var/log/syslog
```
🔹 **`-f` (follow mode)** updates logs in real-time.

### **2️⃣ Filter Logs by Keyword**
```bash
sudo grep "error" /var/log/syslog
```
🔹 Searches for the keyword **"error"** in the logs.

### **3️⃣ View Logs for a Specific Service**
```bash
sudo journalctl -u sshd --since "1 hour ago"
```
🔹 **Shows logs for SSH service in the last hour**.

---

## **🛠 Step 4: Configuring Syslog (`rsyslog.conf`)**
Syslog settings are stored in:
```bash
/etc/rsyslog.conf
```
### **1️⃣ Customize Log Rules**
Edit the configuration:
```bash
sudo nano /etc/rsyslog.conf
```
To **log all authentication failures to a custom file**, add:
```
auth,authpriv.*  /var/log/authentication.log
```
Then restart Syslog:
```bash
sudo systemctl restart rsyslog
```

### **2️⃣ Forward Logs to a Remote Syslog Server**
To send logs to a **centralized Syslog server**:
```bash
*.* @192.168.1.100:514
```
🔹 **Replace `192.168.1.100` with your Syslog server’s IP**.

Restart Syslog:
```bash
sudo systemctl restart rsyslog
```

---

## **🚨 Step 5: Set Up Log Rotation**
Log files can become **too large** over time. Linux automatically rotates logs using **logrotate**.

To check rotation settings:
```bash
cat /etc/logrotate.conf
```

To **rotate syslog logs daily**, create a custom rule:
```bash
sudo nano /etc/logrotate.d/syslog
```
Add:
```
/var/log/syslog {
    daily
    rotate 7
    compress
    missingok
    notifempty
}
```
🔹 This **keeps logs for 7 days and compresses old logs**.

---

## **📊 Step 6: Analyze Syslog for Security**
### **1️⃣ Detect Failed SSH Logins**
```bash
sudo grep "Failed password" /var/log/auth.log
```

### **2️⃣ Monitor System Reboots**
```bash
sudo last reboot
```

### **3️⃣ Detect Unauthorized Sudo Attempts**
```bash
sudo grep "sudo:" /var/log/auth.log | grep "authentication failure"
```

---

## Ref

- ChatGPT