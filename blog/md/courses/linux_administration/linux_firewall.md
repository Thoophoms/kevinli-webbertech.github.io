# Linux Firewall

## Goal

* low-level: iptables
* high-level: ufw

## iptables

`iptables` is a user-space utility program that allows a system administrator to configure the IP packet filter rules of the Linux kernel firewall. It is used for setting up, maintaining, and inspecting the tables of IP packet filter rules in the Linux kernel. Below are some common usages and commands for `iptables`.

### Basic Commands

1. **List Rules**
   ```sh
   sudo iptables -L
   ```

2. **Flush All Rules**
   ```sh
   sudo iptables -F
   ```

3. **Delete Specific Rule**
   ```sh
   sudo iptables -D INPUT -s 192.168.1.1 -j DROP
   ```

4. **Insert Rule at Specific Line Number**
   ```sh
   sudo iptables -I INPUT 1 -s 192.168.1.1 -j DROP
   ```

5. **Append Rule**
   ```sh
   sudo iptables -A INPUT -s 192.168.1.1 -j DROP
   ```

6. **Save Rules**
   ```sh
   sudo sh -c "iptables-save > /etc/iptables/rules.v4"
   ```

7. **Restore Rules**
   ```sh
   sudo iptables-restore < /etc/iptables/rules.v4
   ```

### Common Rule Examples

1. **Allow All Incoming SSH**
   ```sh
   sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
   ```

2. **Allow All Incoming HTTP and HTTPS**
   ```sh
   sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
   sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
   ```

3. **Block All Incoming Traffic From Specific IP**
   ```sh
   sudo iptables -A INPUT -s 192.168.1.100 -j DROP
   ```

4. **Allow All Traffic on Loopback Interface**
   ```sh
   sudo iptables -A INPUT -i lo -j ACCEPT
   ```

5. **Allow Established and Related Incoming Traffic**
   ```sh
   sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
   ```

6. **Block All Incoming Traffic by Default**
   ```sh
   sudo iptables -P INPUT DROP
   sudo iptables -P FORWARD DROP
   sudo iptables -P OUTPUT ACCEPT
   ```

### Basic Chain Operations

- **INPUT Chain**: Rules for incoming traffic.
- **OUTPUT Chain**: Rules for outgoing traffic.
- **FORWARD Chain**: Rules for traffic being routed through the server.

### Example Configuration Script

Create a script, e.g., `/etc/iptables/firewall.sh`, and add the following content:

```sh
#!/bin/bash

# Flush all current rules from iptables
iptables -F

# Set default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow all loopback (lo0) traffic and drop all traffic to 127/8 that doesn't use lo0
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT ! -i lo -s 127.0.0.0/8 -j DROP

# Allow incoming SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow incoming HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow established and related incoming traffic
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Save the iptables rules
iptables-save > /etc/iptables/rules.v4
```

Make the script executable and run it:

```sh
sudo chmod +x /etc/iptables/firewall.sh
sudo /etc/iptables/firewall.sh
```

By following these steps and examples, you should be able to configure and manage `iptables` effectively on your Linux system.


## ufw

`ufw` (Uncomplicated Firewall) is a user-friendly front-end for managing iptables firewall rules. It is particularly useful for users who need basic firewall functionality without having to deal with the complexities of iptables. Below are the steps and examples to help you get started with `ufw`.

### Installation

To install `ufw` on a Debian-based system (like Ubuntu), use the following command:

```sh
sudo apt-get install ufw
```

### Basic Commands

1. **Enable UFW**
   ```sh
   sudo ufw enable
   ```

2. **Disable UFW**
   ```sh
   sudo ufw disable
   ```

3. **Check Status**
   ```sh
   sudo ufw status
   ```

4. **Reset UFW (clear all rules)**
   ```sh
   sudo ufw reset
   ```

5. **Allow Incoming Connection on a Port**
   ```sh
   sudo ufw allow 22  # For SSH
   ```

6. **Deny Incoming Connection on a Port**
   ```sh
   sudo ufw deny 23  # Deny Telnet
   ```

7. **Delete a Rule**
   ```sh
   sudo ufw delete allow 22
   ```

8. **Enable UFW Logging**
   ```sh
   sudo ufw logging on
   ```

### Common Rule Examples

1. **Allow SSH**
   ```sh
   sudo ufw allow ssh
   ```

2. **Allow HTTP and HTTPS**
   ```sh
   sudo ufw allow http
   sudo ufw allow https
   ```

3. **Allow Specific IP**
   ```sh
   sudo ufw allow from 192.168.1.100
   ```

4. **Allow Specific IP to Access Specific Port**
   ```sh
   sudo ufw allow from 192.168.1.100 to any port 22
   ```

5. **Allow Subnet**
   ```sh
   sudo ufw allow from 192.168.1.0/24
   ```

6. **Deny All Incoming Traffic Except SSH**
   ```sh
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   sudo ufw allow ssh
   ```

### Advanced Usage

1. **Allow Service by Name**
   ```sh
   sudo ufw allow 'Apache Full'  # Allow Apache HTTP and HTTPS
   ```

2. **Allow Specific Port Range**
   ```sh
   sudo ufw allow 1000:2000/tcp
   ```

3. **Allow Specific Protocol**
   ```sh
   sudo ufw allow 123/udp
   ```

4. **Reject (send TCP RST or ICMP port unreachable)**
   ```sh
   sudo ufw reject http
   ```

5. **Limit Connections to Prevent Brute Force Attacks**
   ```sh
   sudo ufw limit ssh
   ```

### Example Configuration

To create a basic firewall configuration that allows SSH, HTTP, and HTTPS traffic while denying all other incoming traffic:

```sh
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

This configuration will block all incoming traffic except for SSH, HTTP, and HTTPS, while allowing all outgoing traffic.

By using `ufw`, you can simplify the process of managing your firewall rules and enhance the security of your system.