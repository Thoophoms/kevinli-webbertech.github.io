# **📊 Creating Custom Dashboards in Kibana**
Kibana allows you to build **custom dashboards** for **visualizing logs, monitoring security, and tracking system health**. Here’s how to create **interactive visual dashboards** for your log data.

---

## **🛠 Step 1: Log in to Kibana**
1. Open **Kibana** in your browser:
   ```
   http://localhost:5601
   ```
2. Navigate to **"Discover"** to check if logs are being indexed.

---

## **📂 Step 2: Create an Index Pattern**
1. Go to **"Stack Management" > "Index Patterns"**.
2. Click **"Create Index Pattern"**.
3. Enter your index name:
   ```
   syslog-*
   ```
4. Set **`@timestamp`** as the default time field.
5. Click **"Create Index Pattern"**.

🔹 This enables Kibana to read logs from **Elasticsearch**.

---

## **📊 Step 3: Create a Visualization**
### **1️⃣ Go to the Visualization Tab**
1. Click **"Visualize Library" > "Create Visualization"**.
2. Choose a visualization type (e.g., **Bar Chart, Pie Chart, Line Chart**).
   
### **2️⃣ Example: Failed SSH Logins Chart**
To create a **bar chart for failed SSH logins**:
1. Select **Bar Chart**.
2. Set **X-Axis**:
   - Field: `@timestamp`
   - Interval: `Hourly/Daily`
3. Set **Y-Axis**:
   - Metric: **Count**
4. Add a **Filter**:
   ```
   message: "Failed password"
   ```
5. Click **Save**.

🔹 This creates a **graph of failed SSH logins over time**.

---

## **📊 Step 4: Create a Custom Dashboard**
1. Go to **Dashboard > Create New Dashboard**.
2. Click **"Add Visualization"**.
3. Select:
   - **Failed SSH Logins (Bar Chart)**
   - **Top Failed Users (Pie Chart)**
   - **System Load (Metric Visualization)**.
4. Click **"Save"** and name your dashboard.

🔹 Now, you have **a live security monitoring dashboard**.

---

## **🚨 Step 5: Set Up Alerts for Suspicious Activity**
1. Go to **"Stack Management" > "Rules and Alerts"**.
2. Click **"Create Rule"**.
3. Choose **"Elasticsearch Query"**.
4. Use this query for brute force detection:
   ```kibana
   message: "Failed password" AND event.action: "authentication failure"
   ```
5. Set **Trigger: More than 5 failed logins in 5 minutes**.
6. Send alert **via email or Slack**.

🔹 Kibana will **notify you in real-time** when a brute-force attack happens.

---

## Ref

- ChatGPT