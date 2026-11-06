# Setting up a VPN on an AWS EC2 instance 

Below is a general guide to setting up a VPN server using OpenVPN
on an AWS EC2 instance. This guide assumes you have some familiarity
with AWS and Linux.

### Step 1: Launch an EC2 Instance
1. **Log in to AWS Management Console**: Go to the [AWS Management Console](https://aws.amazon.com/console/).
2. **Launch an EC2 Instance**:
   - Navigate to the EC2 dashboard.
   - Click on "Launch Instance".
   - Choose an Amazon Machine Image (AMI). For this guide, we'll use an Ubuntu Server AMI.
   - Select an instance type (e.g., t2.micro for free tier).
   - Configure instance details (default settings are usually fine).
   - Add storage (default is usually sufficient).
   - Add tags if necessary.
   - Configure security group:
     - Add a rule to allow SSH (port 22) from your IP.
     - Add a rule to allow all traffic from the VPN (e.g., port 1194 for OpenVPN).
   - Review and launch the instance.
   - Create a new key pair or use an existing one, and download the `.pem` file.

### Step 2: Connect to Your EC2 Instance
1. **SSH into the Instance**:
   - Open a terminal.
   - Navigate to the directory where your `.pem` file is located.
   - Run the following command to connect to your instance:
     ```bash
     ssh -i your-key.pem ubuntu@your-ec2-public-ip
     ```
   - Replace `your-key.pem` with your key file and `your-ec2-public-ip` with the public IP of your EC2 instance.

### Step 3: Install OpenVPN
1. **Update the Package List**:
   ```bash
   sudo apt-get update
   ```
2. **Install OpenVPN and Easy-RSA**:
   ```bash
   sudo apt-get install openvpn easy-rsa
   ```

### Step 4: Set Up the OpenVPN Server
1. **Set Up the Easy-RSA PKI**:
   ```bash
   make-cadir ~/openvpn-ca
   cd ~/openvpn-ca
   ```
2. **Configure the PKI Variables**:
   - Edit the `vars` file:
     ```bash
     nano vars
     ```
   - Set the following variables (replace with your own details):
     ```bash
     export KEY_COUNTRY="US"
     export KEY_PROVINCE="CA"
     export KEY_CITY="SanFrancisco"
     export KEY_ORG="YourOrg"
     export KEY_EMAIL="your@email.com"
     export KEY_OU="MyOrganizationalUnit"
     ```
   - Save and exit the editor.
3. **Build the Certificate Authority**:
   ```bash
   source vars
   ./clean-all
   ./build-ca
   ```
4. **Generate Server Certificate and Key**:
   ```bash
   ./build-key-server server
   ```
5. **Generate Diffie-Hellman Parameters**:
   ```bash
   ./build-dh
   ```
6. **Generate HMAC Signature**:
   ```bash
   openvpn --genkey --secret keys/ta.key
   ```

### Step 5: Configure the OpenVPN Server
1. **Copy the Certificates and Keys**:
   ```bash
   cd ~/openvpn-ca/keys
   sudo cp ca.crt server.crt server.key ta.key dh2048.pem /etc/openvpn
   ```
2. **Configure the Server**:
   - Copy the sample configuration file:
     ```bash
     gunzip -c /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz | sudo tee /etc/openvpn/server.conf
     ```
   - Edit the server configuration:
     ```bash
     sudo nano /etc/openvpn/server.conf
     ```
   - Ensure the following lines are correctly set:
     ```bash
     ca ca.crt
     cert server.crt
     key server.key
     dh dh2048.pem
     tls-auth ta.key 0
     ```
   - Optionally, you can enable compression and push DNS settings:
     ```bash
     comp-lzo
     push "redirect-gateway def1 bypass-dhcp"
     push "dhcp-option DNS 8.8.8.8"
     push "dhcp-option DNS 8.8.4.4"
     ```
   - Save and exit the editor.

### Step 6: Enable IP Forwarding
1. **Edit sysctl.conf**:
   ```bash
   sudo nano /etc/sysctl.conf
   ```
2. **Uncomment the following line**:
   ```bash
   net.ipv4.ip_forward=1
   ```
3. **Apply the Changes**:
   ```bash
   sudo sysctl -p
   ```

### Step 7: Configure NAT for VPN Traffic
1. **Add IP Tables Rules**:
   ```bash
   sudo iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
   ```
2. **Save IP Tables Rules**:
   ```bash
   sudo sh -c "iptables-save > /etc/iptables.rules"
   ```
3. **Make IP Tables Rules Persistent**:
   - Edit the `/etc/network/interfaces` file:
     ```bash
     sudo nano /etc/network/interfaces
     ```
   - Add the following line at the end of the file:
     ```bash
     pre-up iptables-restore < /etc/iptables.rules
     ```

### Step 8: Start and Enable OpenVPN
1. **Start the OpenVPN Service**:
   ```bash
   sudo systemctl start openvpn@server
   ```
2. **Enable OpenVPN to Start on Boot**:
   ```bash
   sudo systemctl enable openvpn@server
   ```

### Step 9: Generate Client Certificates and Configuration
1. **Generate Client Certificate and Key**:
   ```bash
   cd ~/openvpn-ca
   source vars
   ./build-key client1
   ```
2. **Create Client Configuration**:
   - Copy the sample client configuration:
     ```bash
     cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf ~/client1.ovpn
     ```
   - Edit the client configuration:
     ```bash
     nano ~/client1.ovpn
     ```
   - Update the following lines:
     ```bash
     remote your-ec2-public-ip 1194
     ca ca.crt
     cert client1.crt
     key client1.key
     tls-auth ta.key 1
     ```
   - Save and exit the editor.
3. **Transfer the Client Configuration**:
   - Use `scp` to transfer the `.ovpn` file to your local machine:
     ```bash
     scp -i your-key.pem ubuntu@your-ec2-public-ip:~/client1.ovpn .
     ```

### Step 10: Connect to the VPN
1. **Install OpenVPN Client**:
   - On your local machine, install an OpenVPN client (e.g., OpenVPN GUI for Windows, Tunnelblick for macOS, or `openvpn` package for Linux).
2. **Import the Client Configuration**:
   - Import the `client1.ovpn` file into your OpenVPN client.
3. **Connect to the VPN**:
   - Use the OpenVPN client to connect to your VPN server using the imported configuration.

### Step 11: Test the VPN Connection
1. **Verify IP Address**:
   - Once connected, check your IP address to ensure it reflects the VPN connection.
2. **Test Connectivity**:
   - Ensure you can access resources on the VPN network and that your internet traffic is routed through the VPN.

### Additional Considerations
- **Security**: Ensure your EC2 instance is secure by regularly updating the system, using strong passwords, and limiting SSH access.
- **Cost**: Be aware of the costs associated with running an EC2 instance and data transfer.