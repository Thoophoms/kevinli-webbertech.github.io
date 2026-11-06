# scrypt Algorithm

---

### 🔐 What is `scrypt`?

`scrypt` is a **password-based key derivation function (KDF)** created by **Colin Percival** in 2009. Like `bcrypt` and `argon2`, it's designed for **secure password hashing**, but it focuses specifically on being **memory-hard** to make it difficult and expensive to perform attacks using specialized hardware (e.g. GPUs, ASICs).

---

### ⚙️ Key Features

- **Memory-intensive**: Designed to use a lot of RAM, which makes it expensive for attackers to run parallel cracking attempts.
- **CPU-intensive**: Still takes time to compute even with high memory.
- **Good balance** of security and compatibility.
- Uses a salt and configurable parameters for security.

---

### 🔢 Parameters

`scrypt` has a few main parameters:
- `N`: CPU/memory cost factor (must be a power of 2, e.g., 2¹⁴).
- `r`: Block size (affects memory usage).
- `p`: Parallelization factor.

You can tweak these to make password hashing slower and more secure.

---

### 🛠️ Python Example

Using Python's built-in `hashlib` (Python 3.6+):

```python
import hashlib
import os

password = b"supersecret"
salt = os.urandom(16)

# Derive key using scrypt
key = hashlib.scrypt(password, salt=salt, n=2**14, r=8, p=1, dklen=64)

print(f"Derived key: {key.hex()}")
```

Note: `scrypt` generates a **key**, not a password hash string with metadata like `bcrypt` or `argon2`. If you're using it for password storage, you'll need to store the salt and parameters too.

---

### ✅ Why Use `scrypt`?

- Great **memory-hard** defense (especially vs GPUs).
- Still widely supported in many libraries.
- Good middle ground between `bcrypt` and `argon2`.

---

### 🔄 Quick Comparison

| Feature     | bcrypt    | scrypt    | argon2     |
|-------------|-----------|-----------|------------|
| Age         | 1999      | 2009      | 2015       |
| Memory-hard | ❌ (light) | ✅         | ✅✅✅        |
| Configurable| Limited   | Yes       | Very       |
| Default use | Legacy    | Decent    | Modern     |
| OWASP rec.  | ✅         | ✅         | ✅✅✅        |
