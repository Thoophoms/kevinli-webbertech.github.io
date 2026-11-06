# **Password Cracking Using Kali Linux**

Password cracking is the process of trying to recover or "crack" passwords from stored data (such as password hashes) by using a variety of methods, such as **brute-force attacks**, **dictionary attacks**, and **rainbow table attacks**.

## **Cracking Hashes with Brute Force**

While **dictionary attacks** are the most efficient, there may be cases where the password is not in the wordlist. In such cases, you can use a **brute-force attack**, where Hashcat will try every possible combination of characters until it finds the correct one.

For example, to perform a brute-force attack with **Hashcat**, use the following command:

```bash
hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a?a?a?a
```

Explanation:

- `-m 0`: Specifies the hash mode (MD5 in this case).
- `-a 3`: Selects the **brute-force attack** mode.
- `?a?a?a?a?a?a?a?a`: Specifies a mask where `?a` means any **alphanumeric character** (lowercase, uppercase, digits, and special characters), and `?a?a?a?a?a?a?a?a` defines an 8-character password.

The brute-force attack will try all combinations of 8 characters, but this can take a long time depending on the length and complexity of the password.

---

## **Cracking Windows Password Hashes**

If you have access to a Windows system's **SAM** (Security Account Manager) file, which contains the password hashes, you can use **John the Ripper** or **Hashcat** to crack them.

### **Step 1: Extract the Hashes**

You can extract the password hashes from a Windows system using tools like **Mimikatz** or **Samdump2**.

For example, with **Samdump2**, you can extract the hashes from the SAM file like this:

```bash
samdump2 SYSTEM SAM > hashes.txt
```

### **Step 2: Crack the Hashes**

Once you have the password hashes, use **John the Ripper** or **Hashcat** to crack them.

With **John the Ripper**:
```bash
john hashes.txt
```

With **Hashcat**:
```bash
hashcat -m 1000 -a 0 hashes.txt /path/to/wordlist.txt
```

Explanation:
- `-m 1000`: Specifies the hash mode for Windows NTLM hashes.
- `-a 0`: Straight mode (using a wordlist attack).

---

## **Conclusion**

Password cracking is an essential part of **penetration testing** and **security auditing**, and Kali Linux provides powerful tools like **John the Ripper** and **Hashcat** to perform these tasks. Whether you're cracking **MD5 hashes**, **WPA2 passwords**, or **Windows NTLM hashes**, Kali Linux offers a versatile platform for testing password strength and improving security.