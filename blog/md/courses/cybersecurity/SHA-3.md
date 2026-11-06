# SHA-3 Algorithm

---

### 🔐 What is SHA-3?

**SHA-3** is the third generation of the **Secure Hash Algorithm family**, officially standardized in **2015** by NIST.

- Based on the **Keccak** algorithm, which won the **NIST hash competition**.
- Unlike SHA-1 and SHA-2, it uses a **sponge construction** instead of the Merkle–Damgård structure.

---

### 📦 SHA-3 Variants

| Variant     | Output Size | Purpose                  |
|-------------|-------------|--------------------------|
| `SHA3-224`  | 224 bits    | Shorter hash             |
| `SHA3-256`  | 256 bits    | Drop-in SHA-256 alternative |
| `SHA3-384`  | 384 bits    | Longer hash              |
| `SHA3-512`  | 512 bits    | Maximum hash length      |
| `SHAKE128/256` | Variable output | Extendable-output functions (XOFs) |

---

### ✅ Why SHA-3?

- **Post-quantum resilient** design (more so than SHA-2)
- **Built-in resistance** to length extension attacks
- **Drop-in replacement** for SHA-2 (e.g. SHA3-256 ≈ SHA-256)
- **Flexible output sizes** (especially with SHAKE variants)

---

### 🛠️ SHA-3 in Python

Using `hashlib` (Python 3.6+):

```python
import hashlib

data = b"hello world"

# SHA3-256
hash_sha3_256 = hashlib.sha3_256(data).hexdigest()
print("SHA3-256:", hash_sha3_256)

# SHAKE256 (extendable output)
shake = hashlib.shake_256(data).hexdigest(64)  # 64 hex chars = 32 bytes
print("SHAKE256 (32 bytes):", shake)
```

---

### 🔄 SHA-2 vs SHA-3 vs BLAKE3

| Feature        | SHA-256      | SHA3-256     | BLAKE3         |
|----------------|--------------|--------------|----------------|
| Year released  | 2001         | 2015         | 2020           |
| Design         | Merkle–Damgård | Sponge      | Tree-hash      |
| Speed          | ⚡ Fast       | 🐢 Slower     | 🚀 Fastest      |
| Hardware opt.  | ✅ Yes        | ⚠️ Limited     | ✅ Yes          |
| Security       | ✅ Secure     | ✅✅ Very secure| ✅✅ Secure       |
| Use case       | Most common  | High-security| Fast hashing   |

---

### 🧠 Use Cases for SHA-3

- **High-security applications**
- **Digital signatures**
- **Secure MACs** (with HMAC or KMAC)
- **Smart contracts / blockchain**
- **Where SHA-2 is not ideal (e.g., side-channel attack resistance)**

---

Let me know if you want to use SHA-3 for HMACs, JWTs, or digital signatures — or compare performance in a benchmark!