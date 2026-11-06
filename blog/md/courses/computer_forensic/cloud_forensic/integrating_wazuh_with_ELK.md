integrating Wazuh with ELK

# **🔗 Integrating Wazuh with ELK (Elasticsearch, Logstash, Kibana)**
Integrating **Wazuh with ELK** (Elasticsearch, Logstash, and Kibana) enhances security monitoring by **centralizing log analysis, threat detection, and compliance auditing**.

---

## **🛠 Step 1: Install Wazuh on the ELK Server**
Run the **Wazuh installation script** to set up Wazuh and ELK on the same server.

### **1️⃣ Download and Install Wazuh**
```bash
curl -sO https://packages.wazuh.com/4.x/wazuh-install.sh
sudo bash wazuh-install.sh --wazuh-server --elastic-stack
```
This installs:
✔ **Wazuh Manager** (Log collection & threat detection)  
✔ **Filebeat** (Sends logs to Elasticsearch)  
✔ **Elasticsearch** (Stores logs)  
✔ **Kibana** (Visualizes security events)  

---

## **📂 Step 2: Configure Wazuh to Send Logs to ELK**
### **1️⃣ Configure Wazuh Manager**
Edit Wazuh's configuration:
```bash
sudo nano /var/ossec/etc/ossec.conf
```
Add the following inside the `<global>` section:
```xml
<remote>
  <connection>secure</connection>
  <port>1514</port>
</remote>
```
Restart Wazuh:
```bash
sudo systemctl restart wazuh-manager
```

### **2️⃣ Configure Filebeat to Send Wazuh Logs to Elasticsearch**
Edit the **Filebeat configuration**:
```bash
sudo nano /etc/filebeat/filebeat.yml
```
Modify the output section:
```yaml
output.elasticsearch:
  hosts: ["http://localhost:9200"]
  username: "elastic"
  password: "your_password"
```
Enable Wazuh module:
```bash
sudo filebeat modules enable wazuh
```
Restart Filebeat:
```bash
sudo systemctl restart filebeat
```

---

## **📊 Step 3: Enable Wazuh Dashboards in Kibana**
1. Open Kibana at:  
   ```
   http://YOUR_SERVER_IP:5601
   ```
2. Navigate to **"Stack Management" → "Saved Objects"**.
3. Import the **Wazuh dashboard templates**:
   ```bash
   curl -X POST "localhost:9200/_bulk" -H "Content-Type: application/json" -d @/usr/share/kibana/data/wazuh_templates.json
   ```

---

## **🚨 Step 4: Visualizing Wazuh Security Events**
### **1️⃣ View Security Logs in Kibana**
1. Go to **"Discover"**.
2. Select the **`wazuh-*` index pattern**.
3. Filter logs for:
   ```kibana
   event.module: wazuh
   ```

### **2️⃣ Create a Dashboard for Threat Monitoring**
1. Navigate to **Dashboards → Create New Dashboard**.
2. Add visualizations for:
   - **Failed SSH logins**.
   - **Brute force attacks**.
   - **Unauthorized sudo attempts**.

---

## **🚀 Step 5: Automate Threat Response**
### **1️⃣ Enable Active Response for Auto-Banning Attackers**
Edit Wazuh's configuration:
```bash
sudo nano /var/ossec/etc/ossec.conf
```
Enable IP banning:
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
🔹 **Now, attackers will be automatically banned!**

---

## Ref

- ChatGPT