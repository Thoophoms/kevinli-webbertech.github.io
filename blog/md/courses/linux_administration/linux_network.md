# Linux networking

## Takeway

* Basic understanding of Linux commands (Debian).
* Basic network commands and their usage.
* How to start/restart network services.
* Internal linux files that implement DNS and routing information.

## **Key Linux Networking Commands**

| **Command** | **Description** |
|------------|----------------|
| `ip a` | Show all network interfaces and IP addresses. |
| `ip r` | Display the routing table. |
| `ping <host>` | Test network connectivity. |
| `netstat -tulnp` | Show listening ports and running services. |
| `ss -tulnp` | Alternative to `netstat`, shows open ports and processes. |
| `traceroute <host>` | Show the path packets take to a destination. |
| `nslookup <domain>` | Query DNS for domain resolution. |
| `dig <domain>` | Detailed DNS lookup. |
| `hostname -I` | Get the IP address of the machine. |
| `ifconfig` (deprecated) | Show IP configuration (use `ip a` instead). |
| `ethtool <interface>` | Get network interface details. |

---

### **Adding Networking Functions to Your Script**

```python
def get_network_info():
    """Fetches network details using Linux commands."""
    commands = {
        "IP Addresses": ["ip", "a"],
        "Routing Table": ["ip", "r"],
        "Open Ports": ["ss", "-tulnp"],
        "DNS Resolution (Google)": ["nslookup", "google.com"],
        "Network Interfaces": ["ifconfig"]  # Use `ip a` if `ifconfig` is unavailable
    }

    for desc, cmd in commands.items():
        print(f"\n{desc}:\n{'-'*30}")
        subprocess.run(cmd)

# Call function to print network details
if __name__ == "__main__":
    get_network_info()
```

## Debian networking

### **Starting and Restarting Networking Services in Debian**

In Debian-based Linux distributions (including Ubuntu), networking services are managed using `systemd` or traditional service scripts. Here’s how you can **start, stop, and restart networking services**:

#### **1. Restart Network Service**

```bash
sudo systemctl restart networking
```
This restarts the **networking service**, which is useful when changes are made to `/etc/network/interfaces`.

#### **2. Restart NetworkManager (for GUI-based setups)**

```bash
sudo systemctl restart NetworkManager
```

If you are using **NetworkManager**, restart it instead.

#### **3. Bring Up/Down Specific Network Interfaces**

- **Disable an interface (e.g., `eth0`)**  

  ```bash
  sudo ifdown eth0
  ```

- **Enable an interface**

  ```bash
  sudo ifup eth0
  ```

#### **4. Restart Network Interface Dynamically**

```bash
sudo ip link set eth0 down && sudo ip link set eth0 up
```

This brings down and then reactivates the network interface.

---

## **Starting and Restarting Networking Services in Red Hat (RHEL & CentOS) and Fedora core**

In **Red Hat-based** distributions (RHEL, CentOS, Fedora), networking services can be managed using `systemctl` or `nmcli`.

---

### **1. Restart the Network Service**

```bash
sudo systemctl restart network
```
This restarts the `network` service, useful when managing static configurations in `/etc/sysconfig/network-scripts/`.

---

### **2. Restart NetworkManager**

```bash
sudo systemctl restart NetworkManager
```

If using **NetworkManager**, restart it instead.

---

### **3. Restart a Specific Network Interface**

```bash
sudo nmcli device reapply eth0
```
or  
```bash
sudo ifdown eth0 && sudo ifup eth0
```
---

### **4. Bring Up/Down an Interface Using `ip`**
- **Disable interface (`eth0`)**
  ```bash
  sudo ip link set eth0 down
  ```
- **Enable interface**
  ```bash
  sudo ip link set eth0 up
  ```

---

### **Code to Add**

```python
def restart_network_redhat():
    """Restarts network service on Red Hat-based systems."""
    subprocess.run(["sudo", "systemctl", "restart", "network"])
    subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"])

def restart_interface(interface):
    """Restarts a specific network interface."""
    subprocess.run(["sudo", "nmcli", "device", "reapply", interface])

# Example usage:
# restart_network_redhat()
# restart_interface("eth0")
```

---

### **Understanding `/etc/hosts` and `/etc/resolv.conf` in Linux**

#### **1. `/etc/hosts`**

The `/etc/hosts` file is used for **local hostname resolution**. It provides a static lookup table that maps IP addresses to hostnames, bypassing DNS queries.

##### **Example `/etc/hosts` file:**

```
127.0.0.1   localhost
192.168.1.100   myserver.local
8.8.8.8   google-dns
```

- The system first checks this file **before querying DNS**.
- Useful for setting up **local or custom domain names** without DNS.

##### **Usage in Linux:**

- Manually edit using:

  ```bash
  sudo nano /etc/hosts
  ```

- Flush DNS cache after modifying:

  ```bash
  sudo systemctl restart nscd
  ```

---

#### **2. `/etc/resolv.conf`**

The `/etc/resolv.conf` file defines the **DNS servers** used by the system to resolve domain names into IP addresses.

##### **Example `/etc/resolv.conf` file:**

```
nameserver 8.8.8.8
nameserver 1.1.1.1
```

- This tells the system to use **Google DNS (`8.8.8.8`) and Cloudflare DNS (`1.1.1.1`)**.

##### **Usage in Linux:**

- To manually edit:
  ```bash
  sudo nano /etc/resolv.conf
  ```

- Check current DNS settings:

  ```bash
  cat /etc/resolv.conf
  ```

- Set a custom DNS permanently:

  ```bash
  echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
  ```

---
