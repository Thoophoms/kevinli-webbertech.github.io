# **🔗 Integrating Logcheck with Fail2Ban for Real-Time Security Response**
By integrating **Logcheck** with **Fail2Ban**, we can **automatically detect suspicious activity** from system logs and **ban offending IPs** in real-time.

---

## **🔍 Step 1: Identify Suspicious Log Entries**
Logcheck scans logs and generates alerts for potential security threats. These alerts are stored in:
```bash
/var/log/logcheck/logcheck.log
```
To see recent alerts:
```bash
sudo tail -f /var/log/logcheck/logcheck.log
```
Look for patterns like:
```
Possible Attack: Failed SSH login attempts from 192.168.1.100
```
We will use these patterns to **trigger Fail2Ban bans**.

---

## **🛠 Step 2: Create a Custom Fail2Ban Jail for Logcheck**
We need to configure **Fail2Ban** to monitor Logcheck logs and ban attackers.

### **1️⃣ Create a New Fail2Ban Jail**
Edit the Fail2Ban configuration:
```bash
sudo nano /etc/fail2ban/jail.local
```
Add the following jail configuration:
```
[logcheck]
enabled = true
port = all
filter = logcheck
logpath = /var/log/logcheck/logcheck.log
maxretry = 3
bantime = 3600
findtime = 600
```
🔹 **Explanation:**
- **`logpath = /var/log/logcheck/logcheck.log`** → Monitors Logcheck alerts.
- **`maxretry = 3`** → If an IP is flagged 3 times, it's banned.
- **`bantime = 3600`** → Bans IP for **1 hour**.
- **`port = all`** → Bans the attacker from **all services**.

---

## **🔎 Step 3: Define Fail2Ban Filter for Logcheck**
We need to **extract IPs from Logcheck logs**.

### **1️⃣ Create a Fail2Ban Filter**
```bash
sudo nano /etc/fail2ban/filter.d/logcheck.conf
```
Add the following regex rule to detect attacks:
```
[Definition]
failregex = .*Possible Attack: .* from <HOST>
ignoreregex =
```
🔹 This **matches failed logins, brute-force attempts, or suspicious behavior**.

---

## **🚀 Step 4: Restart Services & Test**
### **1️⃣ Restart Fail2Ban**
```bash
sudo systemctl restart fail2ban
```

### **2️⃣ Check Logcheck & Fail2Ban Integration**
```bash
sudo fail2ban-client status logcheck
```
🔹 This should show **banned IPs** detected by Logcheck.

### **3️⃣ Simulate a Brute-Force Attack**
To test, try **multiple failed SSH logins**:
```bash
ssh user@your-server
```
Enter the wrong password **3 times**, then check Fail2Ban:
```bash
sudo fail2ban-client status logcheck
```
If configured correctly, Fail2Ban will **ban your IP**.

---

## **📊 Step 5: Set Up Email Alerts for Bans**
To receive an email when an IP is banned, edit `jail.local`:
```bash
sudo nano /etc/fail2ban/jail.local
```
Change:
```
action = %(action_mwl)s
destemail = admin@example.com
sender = fail2ban@example.com
```
Restart Fail2Ban:
```bash
sudo systemctl restart fail2ban
```
🔹 You will now **receive email alerts when Fail2Ban blocks an IP**.

---

## Ref

- ChatGPT