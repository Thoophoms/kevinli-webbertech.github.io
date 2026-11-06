# Integrating Wazuh with AWS for Cloud Security Monitoring

Wazuh can be integrated with **AWS services** like **CloudTrail, GuardDuty, VPC Flow Logs, and Security Groups** to enhance **threat detection, log monitoring, and compliance auditing**.

---

## **🛠 Step 1: Deploy Wazuh on AWS**
You can deploy **Wazuh** in AWS in two ways:
1. **Using an AWS EC2 Instance** (Recommended for centralized log collection).
2. **Using AWS Marketplace AMI** (Preconfigured Wazuh instance).

### **Option 1: Install Wazuh on an AWS EC2 Instance**
1️⃣ Launch an **Ubuntu 20.04** EC2 instance.  
2️⃣ Connect via SSH:
   ```bash
   ssh -i your-key.pem ubuntu@your-aws-instance-ip
   ```
3️⃣ Install Wazuh:
   ```bash
   curl -sO https://packages.wazuh.com/4.x/wazuh-install.sh
   sudo bash wazuh-install.sh --wazuh-server
   ```

---

## **📂 Step 2: Configure AWS Log Collection**
To monitor AWS security logs, Wazuh can collect:
✔ **AWS CloudTrail Logs** (User activity and API calls).  
✔ **AWS GuardDuty Alerts** (Threat detection logs).  
✔ **VPC Flow Logs** (Network traffic logs).  
✔ **AWS WAF Logs** (Blocked attacks).  

### **1️⃣ Enable CloudTrail Logs**
1. In the **AWS Console**, go to **CloudTrail → Create a new trail**.
2. Enable logging to an **S3 bucket**.
3. Copy the **S3 bucket name**.

### **2️⃣ Configure Wazuh to Collect CloudTrail Logs**
Edit Wazuh's configuration:
```bash
sudo nano /var/ossec/etc/ossec.conf
```
Add:
```xml
<aws-s3>
  <bucket>your-cloudtrail-bucket</bucket>
  <aws_region>us-east-1</aws_region>
  <access_key>YOUR_AWS_ACCESS_KEY</access_key>
  <secret_key>YOUR_AWS_SECRET_KEY</secret_key>
</aws-s3>
```
Restart Wazuh:
```bash
sudo systemctl restart wazuh-manager
```
🔹 Now, Wazuh **monitors AWS CloudTrail logs for security events**.

---

## **📊 Step 3: Visualize AWS Security Events in Kibana**
1. Open Kibana:  
   ```
   http://YOUR-WAZUH-INSTANCE:5601
   ```
2. Go to **"Discover"** and filter logs with:
   ```kibana
   event.module: aws
   ```

### **Create Dashboards for AWS Security Monitoring**
1. Navigate to **Dashboards → Create New Dashboard**.
2. Add:
   - **Unauthorized API Calls (CloudTrail)**
   - **Suspicious Traffic (VPC Flow Logs)**
   - **GuardDuty Threat Alerts**
3. Save the dashboard for **continuous monitoring**.

---

## **🚨 Step 4: Automate AWS Threat Response**
To **automatically block malicious IPs**, configure AWS Security Groups.

### **1️⃣ Detect Unauthorized Logins**
Edit:
```xml
<rule id="100002" level="10">
  <field name="aws.cloudtrail.eventName">ConsoleLogin</field>
  <description>AWS Console login detected</description>
</rule>
```

### **2️⃣ Auto-Block Malicious IPs**
Use the AWS CLI to block an IP:
```bash
aws ec2 revoke-security-group-ingress --group-id sg-12345678 --protocol tcp --port 22 --cidr 192.168.1.100/32
```
🔹 **Now, suspicious IPs will be automatically blocked**.

---

## Ref

- ChatGPT