# BLAKE3 Algorithm

---

### ⚡ What is **BLAKE3**?

**BLAKE3** is a cryptographic hash function released in **2020**, designed to be:

- **Faster** than MD5, SHA-1, SHA-2, and even BLAKE2.
- **Secure**, with a security strength similar to SHA-3.
- **Parallelizable**, scalable across multiple CPU cores.
- **Deterministic** and cryptographically strong.

> 🚫 Not suitable for password hashing on its own — it's *too fast*, which is bad for password security.

---

### 🔍 What's it good for?

✅ General-purpose hashing:  
- File checksums  
- Data integrity  
- Fingerprinting  
- Hash trees (Merkle trees)  
- Cryptographic applications (when used properly)

🚫 Not for:
- Password hashing (use `argon2`, `bcrypt`, or `scrypt` instead)

---

### ⚙️ Key Features

- **Extremely fast** (faster than SHA-256, BLAKE2, etc.)
- **128-bit or 256-bit output**
- **Built-in support** for:
  - Keyed hashing (MACs)
  - Extendable-output functions (XOF)
- **Thread-friendly**, thanks to its tree structure

---

### 🛠️ Python Example

You can install it via pip:

```bash
pip install blake3
```

Then use it like this:

```python
from blake3 import blake3

# Simple hash
h = blake3()
h.update(b"hello world")
digest = h.hexdigest()
print(f"Hash: {digest}")

# Keyed hash (e.g., for MAC)
keyed = blake3(key=b"this is a secret key")
keyed.update(b"message")
print(f"Keyed hash: {keyed.hexdigest()}")
```

---

### 🚀 Speed Benchmarks

| Algorithm | Speed (MB/s, approx) |
|-----------|----------------------|
| MD5       | ~500 MB/s            |
| SHA-256   | ~300 MB/s            |
| BLAKE2b   | ~700 MB/s            |
| **BLAKE3**| **~1500+ MB/s**       |

(*Real speeds vary by hardware*)

---

### Why use Blake3

- 🔥 **BLAKE3** is amazing for fast, secure general-purpose hashing.
- ❌ Not a good choice for password hashing (too fast).
- ✅ Great for checksums, file integrity, MACs, etc.