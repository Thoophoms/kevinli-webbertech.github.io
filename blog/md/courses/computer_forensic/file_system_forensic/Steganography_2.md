# **🔐 Encrypting Steganographic Messages**
Steganography **hides** information, but encryption ensures that even if discovered, the hidden data remains unreadable. The best approach is **steganography + encryption**.

---

## **🛠 1. Encrypt a Message Before Hiding**
We will use **AES encryption** before embedding data into an image or audio file.

### **🔹 Encrypt the Message (Using OpenSSL)**
```bash
echo "This is a secret message" | openssl enc -aes-256-cbc -salt -out secret.enc -pass pass:StrongPassword123
```
🔹 **Breakdown**:
- `openssl enc -aes-256-cbc` → Uses **AES-256 encryption**.
- `-salt` → Adds randomness for stronger encryption.
- `-out secret.enc` → Saves the encrypted file.
- `-pass pass:StrongPassword123` → Sets a **password**.

### **🔹 Hide the Encrypted Message in an Image (Steghide)**
```bash
steghide embed -cf cover.jpg -ef secret.enc -p HiddenPass456
```
🔹 Now, **even if someone extracts the hidden file**, it remains encrypted.

### **🔍 Extract & Decrypt the Message**
1️⃣ **Extract the Encrypted File**:
```bash
steghide extract -sf cover.jpg -p HiddenPass456
```
2️⃣ **Decrypt the Extracted File**:
```bash
openssl enc -aes-256-cbc -d -in secret.enc -out decrypted.txt -pass pass:StrongPassword123
cat decrypted.txt
```

---

## **🔊 2. Encrypt & Hide Messages in Audio**
We can also encrypt messages and embed them in **audio files**.

### **🔹 Encrypt the Message**
```bash
gpg --symmetric --cipher-algo AES256 secret.txt
```
🔹 This creates **`secret.txt.gpg`** (AES-256 encrypted).

### **🔹 Hide Encrypted Data in an Audio File**
```python
from steganography.steganography import Steganography
Steganography.encode("input.wav", "output.wav", "secret.txt.gpg")
```

### **🔍 Extract & Decrypt**
1️⃣ **Extract the Hidden File**:
```python
Steganography.decode("output.wav")
```
2️⃣ **Decrypt the File**:
```bash
gpg --decrypt secret.txt.gpg
```

---

## **🔑 Advanced Encryption with PGP**
For extra security, encrypt messages with **PGP keys** instead of passwords.

### **🔹 Encrypt the Message with PGP**
```bash
gpg --encrypt --recipient "YourEmail@example.com" secret.txt
```

### **🔹 Hide the PGP Encrypted File in an Image**
```bash
steghide embed -cf rdesktop1.png -ef secret.txt.gpg -p HiddenPass
```

### **🔍 Extract & Decrypt**
```bash
steghide extract -sf rdesktop1.png -p HiddenPass
gpg --decrypt secret.txt.gpg
```

---

## Ref

- ChatGPT