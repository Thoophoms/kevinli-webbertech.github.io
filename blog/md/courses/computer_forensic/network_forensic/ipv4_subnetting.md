# IPv4 Subnetting

**Subnetting** in IPv4 is the process of dividing a larger network into smaller, more manageable sub-networks or subnets. It helps improve network efficiency, security, and organization. Subnetting enables better utilization of IP addresses by dividing the available address space into multiple subnets.

## Key Concepts in Subnetting:

1. **IP Address Structure:**
   An IPv4 address consists of 32 bits, usually written in dotted decimal notation (e.g., `192.168.1.0`).
   - This address is divided into two parts: the **network** and the **host** portion.
   - A subnet mask is used to indicate which part of the IP address represents the network and which part represents the host.

2. **Subnet Mask:**
   The subnet mask is a 32-bit number that defines the boundary between the network and host portion of an IP address. The subnet mask has `1` bits for the network portion and `0` bits for the host portion. For example:
   - A subnet mask of `255.255.255.0` (`11111111.11111111.11111111.00000000`) tells us that the first 24 bits are the network portion and the remaining 8 bits are for the host portion.

3. **CIDR Notation:**
   CIDR (Classless Inter-Domain Routing) notation is used to represent the subnet mask in a compact form, for example, `192.168.1.0/24`. The `/24` indicates that the first 24 bits are for the network.

### Steps for Subnetting an IPv4 Network:

1. **Determine the Number of Subnets Needed:**
   - Calculate how many subnets you need. The formula for determining the number of subnets is:  
     \[
     \text{Number of subnets} = 2^n
     \]
     Where `n` is the number of bits borrowed from the host portion of the address to create subnets.

2. **Find the New Subnet Mask:**
   - If you're borrowing bits, you'll extend the network portion of the address by `n` bits. For example, if you're using a `/24` network (`255.255.255.0`) and borrow 2 bits, you’ll get a `/26` network (`255.255.255.192`).
   
3. **Calculate the Number of Hosts per Subnet:**
   - The formula for the number of hosts per subnet is:  
     \[
     \text{Number of hosts} = 2^h - 2
     \]
     Where `h` is the number of bits left for the host portion, and the `-2` accounts for the network address and broadcast address.

4. **Identify the Subnets:**
   - Once you have the new subnet mask, you can determine the subnets by incrementing the subnet portion of the address. For example, if you have a network `192.168.1.0/24` and want to create 4 subnets, the new subnet mask will be `/26`. This will give you the subnets:
     - `192.168.1.0/26`
     - `192.168.1.64/26`
     - `192.168.1.128/26`
     - `192.168.1.192/26`

### **Example of Subnetting:**

Let’s subnet the network `192.168.1.0/24` into 4 subnets.

1. **Calculate the Number of Bits to Borrow:**
   We need to create 4 subnets, so:
   \[
   2^n \geq 4 \quad \Rightarrow \quad n = 2
   \]
   So, we need to borrow 2 bits from the host portion.

2. **New Subnet Mask:**
   - Original mask: `/24` or `255.255.255.0`
   - Borrowing 2 bits gives us a new mask of `/26` (which is `255.255.255.192`).

3. **Number of Hosts per Subnet:**
   - Number of host bits = 6 (because `32 - 26 = 6`).
   - Number of hosts = \(2^6 - 2 = 62\) hosts per subnet.

4. **Identify the Subnets:**
   - Subnet 1: `192.168.1.0/26` (Range: `192.168.1.0` to `192.168.1.63`)
   - Subnet 2: `192.168.1.64/26` (Range: `192.168.1.64` to `192.168.1.127`)
   - Subnet 3: `192.168.1.128/26` (Range: `192.168.1.128` to `192.168.1.191`)
   - Subnet 4: `192.168.1.192/26` (Range: `192.168.1.192` to `192.168.1.255`)

### **Subnetting Table:**

| Subnet Address | Subnet Mask     | Usable IP Range        | Broadcast Address |
|----------------|-----------------|------------------------|-------------------|
| 192.168.1.0    | 255.255.255.192 | 192.168.1.1 - 192.168.1.62 | 192.168.1.63     |
| 192.168.1.64   | 255.255.255.192 | 192.168.1.65 - 192.168.1.126 | 192.168.1.127    |
| 192.168.1.128  | 255.255.255.192 | 192.168.1.129 - 192.168.1.190 | 192.168.1.191    |
| 192.168.1.192  | 255.255.255.192 | 192.168.1.193 - 192.168.1.254 | 192.168.1.255    |

### Summary of Key Points:
- **Subnet Mask** helps identify the network and host portions of an address.
- **CIDR Notation** (`/24`, `/26`) is a compact way of representing subnet masks.
- **Borrowing bits** from the host portion allows you to create more subnets, but reduces the number of hosts per subnet.
- The number of available subnets is \(2^n\) (where `n` is the number of borrowed bits), and the number of hosts per subnet is \(2^h - 2\) (where `h` is the remaining host bits).

## Subnetting Precedure

1. **Subnet Mask**: A subnet mask defines the boundary between the network portion and the host portion of an IP address. The mask uses `1`s for the network part and `0`s for the host part.

   For example, in IPv4:
   - `255.255.255.0` is a common subnet mask, written as `/24` in CIDR notation (Classless Inter-Domain Routing).

2. **CIDR Notation**: This notation is used to specify the subnet mask. For example, `192.168.1.0/24` means the first 24 bits are the network address.

3. **IP Address**: An IP address is a unique identifier for a device on a network. It is divided into two parts: the **network portion** and the **host portion**.

4. **Subnet**: A subnet is essentially a smaller network within a larger network. The subnet mask tells you how many bits of the IP address are reserved for the network, and the remaining bits are used for host addresses.

### Steps for Subnetting

Let’s go over an example of how to subnet a network.

#### Example 1: Subnetting a Class C Network

Assume we have the following:
- **IP Address**: `192.168.1.0`
- **Subnet Mask**: `255.255.255.0` (which is `/24` in CIDR notation)

We want to divide this into **4 subnets**.

##### Step 1: Determine the Number of Subnets Needed

To determine the number of bits we need to borrow from the host part of the address, use the formula:
\[
2^n \geq \text{Number of subnets}
\]
Where **n** is the number of bits borrowed. For 4 subnets, the equation would be:
\[
2^n \geq 4
\]
Here, `n = 2` (because `2^2 = 4`).

##### Step 2: Calculate New Subnet Mask

We borrowed 2 bits from the host portion of the IP address. Since the original subnet mask is `/24` (which gives us 8 bits for the host), we now have `/26` as the new subnet mask.

- **Old subnet mask**: `/24` → `255.255.255.0`
- **New subnet mask**: `/26` → `255.255.255.192` (or `11111111.11111111.11111111.11000000` in binary)

##### Step 3: Calculate the Number of Hosts per Subnet

The number of hosts per subnet is determined by the number of remaining bits in the host portion of the address. In a `/26` subnet mask, we have 6 bits left for hosts (32 total bits minus 26 bits for the network).

- Number of host bits: 6
- Number of hosts: \( 2^6 - 2 = 62 \) (subtract 2 for the network address and broadcast address)

Each subnet will have **62 usable host addresses**.

##### Step 4: List the Subnets

Now, let’s calculate the subnets. With a subnet mask of `/26`, the subnet size is 64 addresses per subnet (because \(2^6 = 64\), where 6 bits are left for the host part).

- **Subnet 1**: `192.168.1.0/26` → Address range: `192.168.1.0` to `192.168.1.63`  
  Usable addresses: `192.168.1.1` to `192.168.1.62`
  
- **Subnet 2**: `192.168.1.64/26` → Address range: `192.168.1.64` to `192.168.1.127`  
  Usable addresses: `192.168.1.65` to `192.168.1.126`
  
- **Subnet 3**: `192.168.1.128/26` → Address range: `192.168.1.128` to `192.168.1.191`  
  Usable addresses: `192.168.1.129` to `192.168.1.190`
  
- **Subnet 4**: `192.168.1.192/26` → Address range: `192.168.1.192` to `192.168.1.255`  
  Usable addresses: `192.168.1.193` to `192.168.1.254`

### Example 2: Subnetting a Class B Network

Now, let's take a **Class B** IP address (for example, `172.16.0.0/16`) and subnet it into smaller networks.

#### Step 1: Determine the Number of Subnets Needed

Let’s say we want to divide the `172.16.0.0/16` network into **8 subnets**.

We use the same formula for calculating the required number of bits:
\[
2^n \geq 8
\]
Here, `n = 3` (because `2^3 = 8`).

#### Step 2: Calculate New Subnet Mask

We borrow 3 bits from the host part of the address. Starting with a `/16` subnet mask:
- **Old subnet mask**: `/16` → `255.255.0.0`
- **New subnet mask**: `/19` → `255.255.224.0` (or `11111111.11111111.11100000.00000000` in binary)

#### Step 3: Calculate the Number of Hosts per Subnet

In a `/19` subnet, we have 13 bits left for hosts (32 total bits minus 19 bits for the network).

- Number of host bits: 13
- Number of hosts: \( 2^{13} - 2 = 8190 \) (subtract 2 for the network and broadcast addresses)

Each subnet will have **8190 usable host addresses**.

#### Step 4: List the Subnets

Each subnet has 8192 addresses (since \( 2^{13} = 8192 \)).

- **Subnet 1**: `172.16.0.0/19` → Address range: `172.16.0.0` to `172.16.31.255`  
  Usable addresses: `172.16.0.1` to `172.16.31.254`
  
- **Subnet 2**: `172.16.32.0/19` → Address range: `172.16.32.0` to `172.16.63.255`  
  Usable addresses: `172.16.32.1` to `172.16.63.254`
  
- **Subnet 3**: `172.16.64.0/19` → Address range: `172.16.64.0` to `172.16.95.255`  
  Usable addresses: `172.16.64.1` to `172.16.95.254`
  
- **Subnet 4**: `172.16.96.0/19` → Address range: `172.16.96.0` to `172.16.127.255`  
  Usable addresses: `172.16.96.1` to `172.16.127.254`

And so on for 8 subnets.

---

### Summary of Subnetting Calculations

1. **Determine the required number of subnets** using \( 2^n \geq \text{Number of subnets} \).
2. **Borrow bits** from the host part of the address to create subnets.
3. **Calculate the new subnet mask** by adding the borrowed bits to the original mask.
4. **Calculate the number of hosts** per subnet using \( 2^n - 2 \).
5. **List the subnets** and their usable addresses.