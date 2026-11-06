# **AES (Advanced Encryption Standard) Algorithm**

The **Advanced Encryption Standard (AES)** is a symmetric-key block cipher used worldwide for secure data encryption. It was established by **NIST (National Institute of Standards and Technology)** in 2001 as a replacement for **DES (Data Encryption Standard)** due to its stronger security and efficiency.

## **Key Features of AES**
✔ **Symmetric Encryption**: Uses the same key for encryption and decryption.  
✔ **Block Cipher**: Encrypts data in fixed-size blocks (128 bits).  
✔ **Variable Key Lengths**: Supports **128-bit**, **192-bit**, and **256-bit** keys.  
✔ **Fast & Efficient**: Optimized for both hardware and software.  
✔ **Secure**: Resistant to known attacks when implemented correctly.  

---

## **AES Algorithm Overview**
AES operates on a **4×4 matrix** (16 bytes) called the **State** and processes data in multiple rounds.

### **1. Key Expansion**
- The original encryption key is expanded into a key schedule (an array of round keys).
- **Round keys** are derived using **Rijndael’s key schedule** (involves substitution, rotation, and XOR operations).

### **2. Initial Round (AddRoundKey)**
- The input block is XORed with the first round key.

### **3. Main Rounds (Repeated for Nr-1 times)**
AES performs **10, 12, or 14 rounds** (depending on key size):
- **128-bit key → 10 rounds**  
- **192-bit key → 12 rounds**  
- **256-bit key → 14 rounds**  

Each round consists of:
1. **SubBytes** – Non-linear substitution using the **S-box**.
2. **ShiftRows** – Cyclic shifting of rows in the State matrix.
3. **MixColumns** – Linear transformation (mixing column data).
4. **AddRoundKey** – XOR with the round key.

### **4. Final Round (No MixColumns)**
- The last round skips **MixColumns** for efficiency.

### **5. Output Ciphertext**
- The final State matrix is the encrypted output.

---

## **AES Encryption Steps in Detail**
### **1. SubBytes (Substitution)**
- Each byte in the State is replaced using a **substitution table (S-box)**.
- Provides **non-linearity** to resist cryptanalysis.

### **2. ShiftRows (Permutation)**
- Rows are shifted left:
  - **Row 0**: No shift.
  - **Row 1**: Shift by 1 byte.
  - **Row 2**: Shift by 2 bytes.
  - **Row 3**: Shift by 3 bytes.

### **3. MixColumns (Diffusion)**
- Each column is multiplied by a fixed matrix in **Galois Field (GF(2⁸))**.
- Ensures **diffusion** (small changes affect the entire block).

### **4. AddRoundKey (Key Mixing)**
- The State is XORed with the current round key.

---

## **AES Decryption**
- Uses **inverse operations** in reverse order:
  - **InvSubBytes** (inverse S-box)
  - **InvShiftRows** (right shifts)
  - **InvMixColumns** (reverse matrix multiplication)
  - **AddRoundKey** (same as encryption)

---

## **AES Modes of Operation**
Since AES encrypts **fixed-size blocks**, different **modes** are used to handle large data securely:

| Mode | Description | Use Case |
|------|------------|----------|
| **ECB (Electronic Codebook)** | Encrypts each block independently (weak, insecure for patterns). | Not recommended for secure data. |
| **CBC (Cipher Block Chaining)** | XORs each block with the previous ciphertext (requires IV). | File encryption, SSL/TLS. |
| **CTR (Counter)** | Encrypts a counter + nonce (parallelizable). | Streaming, disk encryption. |
| **GCM (Galois/Counter Mode)** | Combines CTR with authentication (AEAD). | TLS, VPNs. |
| **OFB (Output Feedback)** | Generates a keystream (error-resistant). | Satellite communications. |

---

## **Example AES Encryption (Python)**
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate a random 256-bit key
key = get_random_bytes(32)  # AES-256

# Create cipher object
cipher = AES.new(key, AES.MODE_GCM)

# Encrypt data
plaintext = b"Hello, AES!"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext.hex())
```

---

## **Security Considerations**
✔ **Key Size Matters**: AES-256 is stronger than AES-128 (but slower).  
✔ **Use Secure Modes**: **GCM** or **CBC with HMAC** for authentication.  
❌ **Avoid ECB**: It leaks patterns in plaintext.  
✔ **Random IVs**: Required for CBC, CTR, etc.  

---

## **Comparison with Other Algorithms**
| Algorithm | Type | Key Size | Speed | Security |
|-----------|------|---------|-------|----------|
| **AES** | Symmetric | 128/192/256-bit | Fast | Very Secure |
| **RSA** | Asymmetric | 2048-bit+ | Slow | Secure (if large keys) |
| **ChaCha20** | Symmetric | 256-bit | Very Fast | Secure (used in TLS) |
| **3DES** | Symmetric | 168-bit | Slow | Deprecated |

---

## **Conclusion**
AES is the **gold standard** for symmetric encryption due to its **speed, security, and standardization**. It is used in:
- **TLS/SSL** (HTTPS)
- **Disk Encryption** (BitLocker, FileVault)
- **VPNs** (IPSec, WireGuard)
- **Secure Messaging** (Signal, WhatsApp)

For most applications, **AES-256 in GCM mode** is the best choice. 🚀  
