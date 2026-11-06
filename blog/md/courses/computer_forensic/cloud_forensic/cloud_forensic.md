# **📊 Visualizing Logs with ELK Stack (Elasticsearch, Logstash, Kibana)**
The **ELK Stack** (**Elasticsearch, Logstash, Kibana**) is a powerful toolset for **log analysis, monitoring, and visualization**. It allows you to centralize, process, and analyze logs from multiple sources, including **Syslog, application logs, and security logs**.

---

## **🛠 Step 1: Install the ELK Stack**
ELK runs on **Linux**, and we will install it on **Ubuntu/Debian**. 

### **1️⃣ Add the Elasticsearch Repository**
```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo apt install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
sudo apt update
```

### **2️⃣ Install Elasticsearch**
```bash
sudo apt install elasticsearch
```
Start and enable the service:
```bash
sudo systemctl enable --now elasticsearch
```
Verify Elasticsearch is running:
```bash
curl -X GET "localhost:9200"
```

---

## **📂 Step 2: Install Logstash (Log Processing)**
Logstash collects logs from **Syslog, applications, and other sources**.

```bash
sudo apt install logstash
```

### **🔧 Configure Logstash to Process Syslog**
Create a **Logstash configuration file**:
```bash
sudo nano /etc/logstash/conf.d/syslog.conf
```
Add:
```ini
input {
  file {
    path => "/var/log/syslog"
    start_position => "beginning"
  }
}

filter {
  grok {
    match => { "message" => "%{SYSLOGLINE}" }
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "syslog-%{+YYYY.MM.dd}"
  }
  stdout { codec => rubydebug }
}
```
Save and restart Logstash:
```bash
sudo systemctl restart logstash
sudo systemctl enable logstash
```

---

## **📊 Step 3: Install Kibana (Visualization)**
```bash
sudo apt install kibana
```
Start Kibana:
```bash
sudo systemctl enable --now kibana
```

### **Access Kibana Web UI**
Open **`http://localhost:5601`** in your browser.

To set up **index patterns** for logs:
1. Go to **Management > Index Patterns**.
2. Create an index called **`syslog-*`**.
3. Set `@timestamp` as the time filter.

---

## **🚀 Step 4: Forward Logs from Remote Machines**
To collect logs from multiple servers, **use Filebeat**.

### **1️⃣ Install Filebeat on Remote Server**
```bash
sudo apt install filebeat
```
### **2️⃣ Configure Filebeat to Send Logs to Logstash**
Edit the Filebeat configuration:
```bash
sudo nano /etc/filebeat/filebeat.yml
```
Add:
```yaml
filebeat.inputs:
- type: log
  paths:
    - /var/log/syslog

output.logstash:
  hosts: ["192.168.1.100:5044"]
```
🔹 **Replace `192.168.1.100` with your ELK server’s IP.**

Restart Filebeat:
```bash
sudo systemctl restart filebeat
```

---

## **📡 Step 5: Visualizing Logs in Kibana**
Once logs are flowing into Elasticsearch, use Kibana to:
- **Search logs** with the **Discover** tab.
- **Create visualizations** (e.g., failed logins, network traffic).
- **Build security dashboards**.

Example Kibana Query:
```kibana
message: "Failed password"
```
🔹 Finds **all failed SSH logins**.

---

## Ref

- ChatGPT