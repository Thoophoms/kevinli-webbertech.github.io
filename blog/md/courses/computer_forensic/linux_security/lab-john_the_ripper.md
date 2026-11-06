# Cracking Password Hashes with John the Ripper

**John the Ripper (JTR)** is a popular and versatile password-cracking tool. It supports various hashing algorithms like **MD5**, **SHA-1**, **SHA-256**, **LM**, and others. Here's an example of how to use **John the Ripper** to crack password hashes.

## **Step 1: Install John the Ripper (if needed)**

- John the Ripper comes pre-installed in **Kali Linux**, but if you need to install it manually, use the following command:
  ```bash
  sudo apt-get install john
  ```

## **Step 2: Prepare Password Hashes**

Let’s say you have a file containing **MD5 password hashes**. The file (e.g., `passwords.txt`) contains hashes like this:
```
5f4dcc3b5aa765d61d8327deb882cf99
```

This is the MD5 hash for the password `"password"`.

## **Step 3: Crack the Hash with John the Ripper**

Run **John the Ripper** to crack the hash:

```bash
john --format=raw-md5 passwords.txt
```

**Explanation:**

- `--format=raw-md5`: This specifies that the hashes in the file are in **raw MD5 format**. John the Ripper will attempt to crack the MD5 hashes.
- `passwords.txt`: The file containing the MD5 hashes.

**John the Ripper** will attempt different passwords from its internal dictionary and using brute force until it finds the correct one.

## **Step 4: Check the Cracked Password**

Once John the Ripper finishes, you can view the cracked password by running:

```bash
john --format=raw-md5 --show passwords.txt
```

The output will show the cracked password(s) and the associated hash(es):

```
passwords.txt
5f4dcc3b5aa765d61d8327deb882cf99:password
```
