# **🔔 Real-Time Log Alerts with Logwatch & Fail2Ban**
For **real-time security monitoring**, **Logwatch** and **Fail2Ban** can send alerts when suspicious activity occurs. Here’s how to configure both for **automated log analysis and security response**.

---

## **📜 Option 1: Logwatch - Daily Log Summaries**
Logwatch is a system log analyzer that provides **daily email reports** summarizing system activity.

### **🛠 Step 1: Install Logwatch**
#### **Debian/Ubuntu**
```bash
sudo apt update
sudo apt install logwatch
```
#### **RHEL/CentOS**
```bash
sudo yum install logwatch
```

### **📂 Step 2: Configure Logwatch**
Edit the **main configuration file**:
```bash
sudo nano /etc/logwatch/conf/logwatch.conf
```
Set:
```
Output = mail
Format = text
MailTo = admin@example.com
Detail = High
```
🔹 This **sends daily reports** to `admin@example.com`.

### **📊 Step 3: Generate Manual Log Reports**
To test Logwatch:
```bash
sudo logwatch --detail High --mailto admin@example.com --range yesterday
```
🔹 This generates a **summary of logs from yesterday**.

---

## **🛡️ Option 2: Fail2Ban - Real-Time Security Alerts**
Fail2Ban **monitors log files** and **automatically bans IPs** showing suspicious behavior (e.g., repeated failed SSH logins).

### **🛠 Step 1: Install Fail2Ban**
#### **Debian/Ubuntu**
```bash
sudo apt install fail2ban
```
#### **RHEL/CentOS**
```bash
sudo yum install epel-release
sudo yum install fail2ban
```

### **🔧 Step 2: Configure Fail2Ban**
Edit the **main configuration file**:
```bash
sudo nano /etc/fail2ban/jail.local
```
Add:
```
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 3
destemail = admin@example.com
sender = fail2ban@example.com
mta = sendmail
action = %(action_mwl)s

[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log
maxretry = 3
```
🔹 **Bans IPs for 1 hour** (`bantime = 3600`) if there are **3 failed login attempts** within **10 minutes** (`findtime = 600`).

### **🚀 Step 3: Restart Fail2Ban**
```bash
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban
```

### **🔍 Step 4: Check Banned IPs**
```bash
sudo fail2ban-client status sshd
```
🔹 **Lists currently banned IPs**.

### **🔔 Step 5: Enable Email Alerts**
To get real-time alerts, ensure the `action` includes `mwl` (mail, whois, log):
```
action = %(action_mwl)s
```
🔹 Sends an email **with details** whenever an IP is banned.

---

## **🚀 Next Steps**
✅ Need help **customizing Fail2Ban for web servers** (Apache, Nginx)?  
✅ Want **Logwatch & Fail2Ban to work together**? 🚨