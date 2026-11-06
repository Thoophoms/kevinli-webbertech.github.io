# SHA-2 Algorithm

### 🔐 What is SHA-2?

**SHA-2** is the second generation of the **Secure Hash Algorithm** family, released in **2001** by **NIST**. It’s widely used in **cryptographic applications** such as SSL/TLS certificates, digital signatures, and blockchain.

SHA-2 is known for its strong security and is **still widely used** today, especially in systems where **SHA-1** is now considered **vulnerable**.

---

### 📦 SHA-2 Variants

| Variant     | Output Size  | Common Use Case                           |
|-------------|--------------|-------------------------------------------|
| **SHA-224** | 224 bits     | File integrity, checksums (rare)          |
| **SHA-256** | 256 bits     | Blockchains (Bitcoin), certificates, file hashes |
| **SHA-384** | 384 bits     | High-security applications, digital signatures |
| **SHA-512** | 512 bits     | Secure file hashing, long-term security   |

---

### ✅ Why Use SHA-2?

- **Security**: Strong against collision and preimage attacks.
- **Widely used**: It’s the foundation for many protocols (TLS, IPsec, Bitcoin, etc.).
- **Efficient**: Designed to be fast while providing robust security.
- **Versatility**: Can be used for file hashes, digital signatures, integrity checks, etc.

---

### 🛠️ SHA-2 in Python (Using hashlib)

Here’s a simple example of using **SHA-256** (you can swap for other variants like `SHA-512`):

```python
import hashlib

# Data to hash
data = b"hello world"

# SHA-256 hash
hash_sha256 = hashlib.sha256(data).hexdigest()
print("SHA-256 Hash:", hash_sha256)

# SHA-512 hash
hash_sha512 = hashlib.sha512(data).hexdigest()
print("SHA-512 Hash:", hash_sha512)
```

### 📁 Example: File Integrity Check with SHA-256

```python
import hashlib

def hash_file_sha256(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

print("File SHA-256:", hash_file_sha256("example.txt"))
```

---

### 🔄 SHA-1 vs SHA-2 vs SHA-3

| Feature       | SHA-1     | SHA-2      | SHA-3     |
|---------------|-----------|------------|-----------|
| Output Size   | 160-bit   | 224, 256, 384, 512 bits | 224, 256, 384, 512 bits |
| Security      | Broken    | Secure     | Very secure |
| Speed         | Fast      | Moderate   | Slower     |
| Attack Resistance | Weak    | Strong     | Strong     |
| Status        | Deprecated | Widely used| Modern     |

---

### ⚠️ When to Avoid SHA-2?

- **Password Hashing**: While SHA-2 is secure, it’s not ideal for **password storage** because it’s too fast, making brute-forcing easier. Use **bcrypt**, **argon2**, or **scrypt** instead.
- **High-security cryptography**: For the most modern security, consider **SHA-3** or **BLAKE3**, which are designed with stronger security foundations and faster performance for certain tasks.

---

### 🔄 SHA-2 and HMAC

To use **SHA-2** with HMAC (for authentication):

```python
import hmac
import hashlib

# Message and key
message = b"important message"
key = b"supersecretkey"

# HMAC with SHA-256
hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()
print("HMAC-SHA256:", hmac_sha256)
```

---

### 🔄 SHA-2 in Digital Signatures

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
message = b"message to sign"

# Sign with SHA-256
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verify
public_key = private_key.public_key()
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Signature verified (SHA-256)")
except:
    print("❌ Signature invalid")
```

---

### 🔥 Summary

- **SHA-2** is the most commonly used family of hash functions, with **SHA-256** being the most popular variant.
- It’s widely trusted for **blockchains**, **digital signatures**, **certificates**, and more.
- While secure, it **shouldn't** be used for **password hashing** (prefer **bcrypt**, **argon2**, or **scrypt**).
  
Let me know if you want to see SHA-2 in more contexts, like **JWT signing**, **file encryption**, or **blockchain**!