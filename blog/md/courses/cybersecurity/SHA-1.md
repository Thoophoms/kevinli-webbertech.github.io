# **SHA-1** Algorithm

---

### 🧾 What is SHA-1?

**SHA-1** stands for **Secure Hash Algorithm 1**, designed by the **NSA** and published by **NIST** in **1995**. It produces a **160-bit (20-byte)** hash value and was widely used for:

- Digital signatures (e.g. SSL/TLS certificates)
- File integrity checks
- Version control systems (like Git)

---

### 🚨 Is SHA-1 Secure?

**Short answer: No.**

SHA-1 is **broken** — it’s vulnerable to **collision attacks**, where two different inputs produce the same hash.

#### Timeline of SHA-1’s Demise:
- **2005**: First theoretical collision attacks published.
- **2017**: Google and CWI Amsterdam performed a real-world collision: **SHAttered** attack.
- **2020+**: Most major platforms (Microsoft, Google, Apple, GitHub) deprecated or outright blocked SHA-1.

> ⚠️ Today, **you should never use SHA-1 for security purposes.**

---

### 🔥 SHA-1 vs Others

| Algorithm | Hash Size | Security | Status     |
|-----------|-----------|----------|------------|
| SHA-1     | 160-bit   | 🔴 Weak  | Deprecated |
| SHA-256   | 256-bit   | ✅ Strong | Recommended |
| BLAKE3    | 256-bit+  | ✅✅✅    | Modern     |
| SHA-3     | 256-bit+  | ✅✅     | Very secure |
| MD5       | 128-bit   | 🔥 Broken | Totally insecure |

---

### 🛠️ SHA-1 in Python

Still useful for **non-security uses** like hash tables or legacy compatibility.

```python
import hashlib

data = b"hello world"
hash_sha1 = hashlib.sha1(data).hexdigest()
print(f"SHA-1 Hash: {hash_sha1}")
```

---

### ✅ When (If Ever) Should You Use SHA-1?

- ✔️ **Versioning** (like Git, though it's moving toward SHA-256)
- ❌ **Passwords, tokens, certificates, digital signatures** – use **SHA-256** or **SHA-3** instead.

---

Let me know if you want help migrating away from SHA-1, or if you're comparing it to something like SHA-2, SHA-3, or BLAKE2/BLAKE3!