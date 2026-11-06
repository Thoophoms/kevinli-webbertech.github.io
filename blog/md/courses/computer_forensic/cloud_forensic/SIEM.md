# SIEM

# **🔍 Security Information and Event Management (SIEM) Overview**
A **SIEM (Security Information and Event Management)** system collects, analyzes, and correlates logs from multiple sources to detect security threats in real time.

---

## **🛠 Key Functions of SIEM**
✔️ **Log Management** – Collects logs from network devices, endpoints, and applications.  
✔️ **Threat Detection** – Identifies anomalies and suspicious activity.  
✔️ **Real-Time Alerts** – Notifies security teams of incidents (e.g., failed SSH logins, malware).  
✔️ **Incident Response** – Automates actions (e.g., block IPs, disable accounts).  
✔️ **Compliance Reporting** – Helps meet PCI-DSS, HIPAA, GDPR, and other regulations.  

---

## **📡 Popular SIEM Solutions**
### 🔹 **Open-Source SIEMs**
- **Wazuh** – Based on ELK, provides threat detection and compliance.
- **Security Onion** – Full SIEM with IDS, packet capture, and threat hunting.
- **Graylog** – Log management SIEM with security modules.

### 🔹 **Enterprise SIEMs**
- **Splunk Enterprise Security** – Advanced analytics, real-time detection.
- **IBM QRadar** – AI-powered threat intelligence.
- **Microsoft Sentinel** – Cloud-based SIEM on Azure.

---

## **📂 SIEM Architecture**
### **1️⃣ Data Collection**
- Logs from **servers, firewalls, applications, databases**.
- Captured using **Filebeat, Syslog, or Logstash**.

### **2️⃣ Data Analysis & Correlation**
- **Rule-based alerts** (e.g., "Detect more than 5 failed SSH logins in 10 minutes").
- **Behavioral analytics** (detects anomalies).

### **3️⃣ Automated Threat Response**
- Blocks **malicious IPs** via **Fail2Ban**.
- Disables **compromised user accounts**.

---

## **🛠 Deploying an Open-Source SIEM (Wazuh)**
### **1️⃣ Install Wazuh on a Server**
```bash
curl -sO https://packages.wazuh.com/4.x/wazuh-install.sh
sudo bash wazuh-install.sh --wazuh-server
```

### **2️⃣ Install Wazuh Agents on Endpoints**
```bash
sudo apt install wazuh-agent
sudo systemctl start wazuh-agent
```

### **3️⃣ Visualize Security Events in Kibana**
1. Open **Wazuh Dashboard** (`http://YOUR-SIEM-IP:5601`).
2. Go to **Security Events**.
3. View logs from **firewalls, web servers, authentication logs**.

---

## **🚨 SIEM Use Cases**
### 🔹 **Brute-Force Detection**
- **Rule:** More than 10 failed SSH logins in 5 minutes.
- **Response:** Block IP via **Fail2Ban**.

### 🔹 **Malware Detection**
- **Rule:** Suspicious file hashes detected in logs.
- **Response:** Alert security team, quarantine the file.

### 🔹 **Unauthorized Data Access**
- **Rule:** A non-admin user accesses `/etc/passwd`.
- **Response:** Log and alert the SOC team.

---

## Ref

- ChatGPT