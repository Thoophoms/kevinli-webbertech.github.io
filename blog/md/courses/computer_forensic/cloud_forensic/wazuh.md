# Wazuh SIEM Tutorial – Open-Source Security Monitoring

Wazuh is an **open-source SIEM** that provides **log collection, threat detection, compliance monitoring, and incident response**. It integrates with **Elasticsearch and Kibana** to visualize security events.

---

## **🛠 Step 1: Install Wazuh SIEM**
Wazuh can be installed on **Ubuntu/Debian**, **CentOS/RHEL**, or **Docker**.

### **1️⃣ Install Wazuh Server on Ubuntu/Debian**
```bash
curl -sO https://packages.wazuh.com/4.x/wazuh-install.sh
sudo bash wazuh-install.sh --wazuh-server
```

### **2️⃣ Install Wazuh Agent on Client Machines**
To monitor logs from **remote servers**:
```bash
sudo apt install wazuh-agent
sudo systemctl start wazuh-agent
```
🔹 The **agent sends logs to the Wazuh server**.

---

## **📂 Step 2: Configure Wazuh for Log Monitoring**
### **1️⃣ Configure the Wazuh Agent**
Edit the agent configuration:
```bash
sudo nano /var/ossec/etc/ossec.conf
```
Set:
```xml
<server>
  <address>WAZUH_SERVER_IP</address>
  <port>1514</port>
</server>
```
Restart the agent:
```bash
sudo systemctl restart wazuh-agent
```

### **2️⃣ Enable Log Collection**
To monitor **authentication logs**:
```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/auth.log</location>
</localfile>
```
Restart Wazuh:
```bash
sudo systemctl restart wazuh-manager
```
🔹 **Now, Wazuh is collecting logs from `/var/log/auth.log`.**

---

## **📊 Step 3: Visualize Security Events in Kibana**
1. Open **Kibana**:  
   ```
   http://YOUR-WAZUH-SERVER:5601
   ```
2. Go to **Wazuh → Security Events**.
3. View logs for **failed SSH logins, brute force attacks, and malware detection**.

---

## **🚨 Step 4: Detect and Block Threats**
### **1️⃣ Brute-Force Attack Detection**
To **detect multiple failed SSH logins**, add a rule:
```xml
<rule id="100001" level="8">
  <decoded_as>syslog</decoded_as>
  <field name="message">Failed password for</field>
  <description>Brute-force SSH attack detected</description>
</rule>
```

### **2️⃣ Automatically Block Attackers**
Enable **active response** to ban IPs:
```xml
<active-response>
  <command>firewalld</command>
  <location>local</location>
</active-response>
```
Restart Wazuh:
```bash
sudo systemctl restart wazuh-manager
```
🔹 **Now, Wazuh will block IPs after multiple failed logins.**

---

## **📜 Step 5: Compliance Auditing**
Wazuh supports **PCI-DSS, HIPAA, GDPR compliance monitoring**.

1. Go to **Wazuh → Compliance**.
2. Enable rules for **file integrity monitoring, unauthorized access, and audit logs**.
3. Generate **compliance reports**.

---

## Ref

- ChatGPT
