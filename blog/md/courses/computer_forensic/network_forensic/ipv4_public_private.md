# IPv4 Part I

### **Public IP Address**

A **public IP address** is an IP address that is accessible over the internet and can be reached by any device or server on the global network. These IPs are assigned by the Internet Service Provider (ISP) to your home, office, or data center, making your network reachable from anywhere in the world.

- **Public IPs** are unique and globally routable.
- Devices or servers with a public IP address can directly communicate with other devices or servers over the internet.
- For most people, their **router** or **modem** is assigned a public IP address by the ISP, and this is what the world sees as the address for your internet connection.

#### Example:
- **IPv4 Example**: `203.0.113.5`
- **IPv6 Example**: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

### **Private IP Address**
A **private IP address** is used within a local network and is not routable over the internet. These addresses are used for devices like computers, printers, and smartphones in your internal network. They allow devices to communicate with each other in the local network but not directly with the outside world.

- **Private IPs** are used to conserve public IP addresses.
- Devices in a local network (such as your home Wi-Fi) will have private IP addresses assigned to them.
- **Private IPs** are not directly reachable from the internet. To access the internet, a router uses **Network Address Translation (NAT)** to map private IPs to the public IP.

#### Common Private IP Address Ranges (for IPv4):
- **Class A**: `10.0.0.0` to `10.255.255.255`
- **Class B**: `172.16.0.0` to `172.31.255.255`
- **Class C**: `192.168.0.0` to `192.168.255.255`

### Key Differences:
| **Feature**          | **Public IP**                               | **Private IP**                             |
|----------------------|---------------------------------------------|--------------------------------------------|
| **Access**           | Can be accessed from anywhere on the internet | Can only be accessed within the local network |
| **Assignment**       | Assigned by ISP                             | Assigned by the network administrator or DHCP server |
| **Routing**          | Routable on the internet                    | Not routable on the internet               |
| **Security**         | More exposed to security risks              | More secure because they are not accessible from outside |
| **Example Range**    | `203.0.113.0/24`, `2001:0db8:...`           | `192.168.x.x`, `10.x.x.x`, `172.16.x.x`    |