# IPv4

**IPv4 Subnetting** is the process of dividing a larger network into smaller, more manageable subnets. It allows an organization to use its IP address space more efficiently and improves network performance and security.

### Key Concepts of IPv4 Subnetting:

1. **IP Address**: 
   - An IPv4 address is a 32-bit address usually written in "dotted decimal" format, e.g., `192.168.1.1`.
   - It is divided into two parts:
     - **Network portion**: Identifies the network to which the device belongs.
     - **Host portion**: Identifies the device within that network.

2. **Subnet Mask**: 
   - The subnet mask is a 32-bit number that helps to distinguish the network portion of an IP address from the host portion.
   - It is written in dotted decimal notation, e.g., `255.255.255.0`, and is used to determine how many bits are allocated for the network and how many are left for hosts.

   **Example of subnet mask and IP address:**
   - IP address: `192.168.1.10`
   - Subnet mask: `255.255.255.0`

   This means the first 24 bits (the `255.255.255` part) are for the network, and the last 8 bits (`0`) are for the hosts.

3. **Subnetting**:
   - Subnetting involves borrowing bits from the host portion of the address to create additional subnets.
   - Each borrowed bit allows you to create more subnets but reduces the number of available hosts per subnet.

### **Steps for IPv4 Subnetting**:

1. **Determine the Network Requirements**:
   - Find out how many subnets and how many hosts per subnet are required. This will help determine how many bits to borrow from the host portion.

2. **Subnet Mask Calculation**:
   - Start with the default subnet mask for the class of the IP address (Class A, B, or C).
   - Borrow bits from the host portion of the address to create subnets.
   
   Example:
   - If you have a Class C IP address (default subnet mask `255.255.255.0`) and you need 4 subnets, you borrow 2 bits from the host portion (because 2^2 = 4 subnets).

3. **Subnetting Formula**:
   - The number of subnets created by borrowing `n` bits from the host portion of an IP address is `2^n`.
   - The number of hosts available per subnet is `2^h - 2`, where `h` is the number of host bits (the "-2" accounts for the network address and the broadcast address, which cannot be assigned to hosts).

4. **Subnetting Example**:
   Let's work through an example using an IP address and a subnet mask.

   - **Example IP address**: `192.168.1.0` (Class C)
   - **Default subnet mask**: `255.255.255.0`
   
   You need to create 4 subnets.

   - Borrow 2 bits from the host portion (since `2^2 = 4` subnets).
   - New subnet mask: `255.255.255.192` (since 2 bits are borrowed, the subnet mask will be `/26`).

   **Subnet Calculation**:
   - The subnet mask `/26` means 26 bits are allocated for the network and 6 bits for the hosts.
   - Number of subnets: `2^2 = 4`
   - Number of hosts per subnet: `2^6 - 2 = 62` hosts per subnet.

   The subnets will look like this:
   - Subnet 1: `192.168.1.0/26` (Range: `192.168.1.0 - 192.168.1.63`)
   - Subnet 2: `192.168.1.64/26` (Range: `192.168.1.64 - 192.168.1.127`)
   - Subnet 3: `192.168.1.128/26` (Range: `192.168.1.128 - 192.168.1.191`)
   - Subnet 4: `192.168.1.192/26` (Range: `192.168.1.192 - 192.168.1.255`)

### **IPv4 Subnetting Cheat Sheet**

| CIDR Notation | Subnet Mask     | Subnet Bits | Host Bits | Number of Subnets | Hosts per Subnet |
|---------------|-----------------|-------------|-----------|-------------------|------------------|
| /8            | 255.0.0.0       | 8           | 24        | 1                 | 16,777,214       |
| /16           | 255.255.0.0     | 16          | 16        | 256               | 65,534           |
| /24           | 255.255.255.0   | 24          | 8         | 65,536            | 254              |
| /25           | 255.255.255.128 | 25          | 7         | 128               | 126              |
| /26           | 255.255.255.192 | 26          | 6         | 256               | 62               |
| /27           | 255.255.255.224 | 27          | 5         | 512               | 30               |
| /28           | 255.255.255.240 | 28          | 4         | 1,024             | 14               |
| /29           | 255.255.255.248 | 29          | 3         | 2,048             | 6                |
| /30           | 255.255.255.252 | 30          | 2         | 4,096             | 2                |

### **Subnetting in Practice**

1. **Determining Subnets and Hosts**:
   - The number of **subnets** is calculated by determining how many bits you borrow from the host portion.
   - The number of **hosts** in each subnet is calculated by the number of remaining bits for the host part, i.e., `2^h - 2`.

2. **Example**: You are given the IP address `10.0.0.0/8` (Class A network) and need to create 1000 subnets. How would you do it?

   **Solution**:
   - For 1000 subnets, you need to borrow 10 bits (since `2^10 = 1024` subnets, which is enough to cover 1000).
   - The new subnet mask will be `/18` (8 bits from Class A default mask plus 10 bits borrowed).
   - New subnet mask: `255.255.192.0` (first 18 bits as 1s in binary).
   - Number of hosts per subnet: `2^14 - 2 = 16,382` hosts per subnet.

### **Key Points to Remember**:
- **Network Address**: The first address in each subnet. It cannot be assigned to a host.
- **Broadcast Address**: The last address in each subnet. It cannot be assigned to a host.
- **Usable IP Range**: The addresses between the network address and the broadcast address.

### Conclusion

Subnetting is an essential skill for network administrators as it helps efficiently utilize IP address space. IPv4 subnetting involves breaking up large networks into smaller subnets, improving security and traffic management. By mastering the concepts of subnet masks, CIDR notation, and the process of borrowing bits, you can easily create subnets to meet the needs of your network.


## IPv6

### **IPv6 Overview**

IPv6 (Internet Protocol version 6) is the most recent version of the Internet Protocol designed to replace IPv4. It was developed to address the limitations of IPv4, particularly the exhaustion of IP addresses due to the growing number of devices connected to the internet.

### **Key Differences Between IPv4 and IPv6**:

1. **Address Size**:
   - **IPv4**: Uses a 32-bit address space, which provides about 4.3 billion unique addresses (`2^32`).
   - **IPv6**: Uses a 128-bit address space, which provides approximately **340 undecillion** (3.4 × 10^38) unique addresses (`2^128`), offering a vastly larger address pool.

2. **Notation**:
   - **IPv4**: Written in **dotted decimal** format (e.g., `192.168.1.1`).
   - **IPv6**: Written in **hexadecimal** format, separated by colons (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

3. **Header Complexity**:
   - **IPv4**: More complex header with multiple fields.
   - **IPv6**: Simplified header with fixed size, reducing the overhead on routers and improving packet processing.

4. **Addressing**:
   - **IPv4**: Uses **classes** (Class A, B, C) and **subnetting** for network management.
   - **IPv6**: Uses **CIDR notation** (Classless Inter-Domain Routing) for more flexible and efficient routing.

5. **NAT (Network Address Translation)**:
   - **IPv4**: Due to the limited address space, NAT is often used to allow multiple devices on a local network to share a single public IPv4 address.
   - **IPv6**: NAT is generally not needed because the vast address space allows each device to have its own globally unique IP address.

6. **Security**:
   - **IPv4**: Security was added later through extensions like IPsec.
   - **IPv6**: Security is built-in with mandatory support for IPsec (Internet Protocol Security), providing end-to-end encryption and authentication.

### **IPv6 Address Format**:

An IPv6 address is 128 bits long and is divided into 8 groups of 16 bits, each group is represented as four hexadecimal digits. For example:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

#### **IPv6 Address Structure**:
- **Global Prefix**: The first 3 bits are for the global routing prefix (for the global Internet network).
- **Subnet**: The next portion of the address is used for subnetting.
- **Interface Identifier**: The last 64 bits are typically used to identify the device itself within the subnet.

### **Types of IPv6 Addresses**:

1. **Unicast**:
   - Refers to a single sender and a single receiver. 
   - Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`

2. **Multicast**:
   - Refers to a single sender and multiple receivers.
   - Example: `FF00::/8` is the multicast address block for IPv6.

3. **Anycast**:
   - Refers to a single sender and multiple receivers, but the packet is delivered to the **nearest** receiver based on routing metrics.

4. **Broadcast**:
   - IPv6 does not use broadcast. Instead, it uses multicast and anycast for similar functionality.

### **IPv6 Address Notation and Simplification**:

IPv6 addresses can be shortened by applying the following rules:

1. **Leading Zeros**: You can omit leading zeros in each block.
   - Example: `2001:0db8:0000:0000:0000:0000:0000:0010` becomes `2001:db8:0:0:0:0:0:10`.

2. **Consecutive Zero Blocks**: You can replace one or more consecutive blocks of zeros with `::`. This can only be done once in an address.
   - Example: `2001:db8:0:0:0:0:0:10` becomes `2001:db8::10`.

### **IPv6 Subnetting**:

IPv6 uses **CIDR notation** (Classless Inter-Domain Routing) to define subnets. The subnet prefix is expressed as `/n`, where `n` is the number of bits in the network portion of the address.

For example:
- `2001:0db8:85a3::/64` represents an IPv6 address with the first 64 bits as the network part.

### **Example IPv6 Subnetting**:

1. **Global Prefix**:
   A typical IPv6 network might use `2001:0db8::/32` as its global routing prefix.

2. **Subnetting**:
   To create smaller subnets, you borrow bits from the 64-bit host portion. For example:
   - `2001:0db8:85a3::/64` (original subnet)
   - `2001:0db8:85a3:0001::/64` (subnet 1)
   - `2001:0db8:85a3:0002::/64` (subnet 2)
   
   Each `/64` subnet can have `2^64` possible addresses, which is an enormous number.

3. **Subnetting Example**:
   Suppose you have the IPv6 address `2001:db8::/32` and need to create 4 subnets. You can borrow 2 bits from the host portion:
   - `2001:db8:0000::/34`
   - `2001:db8:4000::/34`
   - `2001:db8:8000::/34`
   - `2001:db8:c000::/34`

   This gives you 4 subnets.

### **Benefits of IPv6**:

1. **Large Address Space**:
   IPv6 offers a virtually unlimited number of addresses, which resolves the issue of IPv4 address exhaustion.

2. **Simplified Header**:
   The IPv6 header is simpler and more efficient for routers to process, leading to better performance in some cases.

3. **Security**:
   IPv6 supports mandatory IPsec, which ensures encrypted and authenticated communication.

4. **Autoconfiguration**:
   IPv6 allows for **stateless autoconfiguration**, meaning devices can automatically configure their own IP address without the need for a DHCP server.

5. **Better Multicast and Anycast**:
   IPv6 improves support for multicast and anycast, which are useful for applications like streaming media and content delivery.

### **IPv6 Example**:

Here’s an example of an IPv6 address and how it is broken down:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

- **Global Prefix**: `2001:0db8::/32`
- **Subnet**: `2001:0db8:85a3::/64`
- **Interface Identifier**: `0000:0000:8a2e:0370:7334`

### **IPv6 and IPv4 Coexistence**:

Although IPv6 is slowly being adopted, IPv4 is still widely used, and both protocols often coexist in what is known as **dual stack** networks. There are various transition mechanisms to allow IPv6 and IPv4 to work together:

1. **Tunneling**: IPv6 packets are encapsulated inside IPv4 packets, allowing IPv6 to be sent over IPv4 networks.
2. **Translation**: IPv6 addresses are translated into IPv4 addresses when necessary.

### **Conclusion**:

IPv6 is the future of networking, designed to solve the limitations of IPv4, especially address exhaustion. It provides a larger address space, simpler header format, and improved security features. Although IPv4 is still prevalent, the transition to IPv6 is becoming increasingly important to support the growing number of devices connected to the internet.
