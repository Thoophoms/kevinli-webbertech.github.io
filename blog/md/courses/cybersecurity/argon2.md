# Argon2 Algorithm

Great choice—**Argon2** is currently considered the **most secure** password hashing algorithm available. It even won the [Password Hashing Competition](https://password-hashing.net) in 2015!

---

### 🔐 What is Argon2?

**Argon2** is a **modern password hashing algorithm** designed to:
- Be resistant to **brute-force** and **side-channel** attacks.
- Protect against **GPU and ASIC attacks** by using **memory-hard** functions.

It comes in three main variants:
1. **Argon2d** – Optimized against GPU cracking, more resistant to side-channel attacks.
2. **Argon2i** – More secure against side-channel attacks (e.g., timing attacks), good for password hashing.
3. **Argon2id** – A **hybrid** of Argon2d and Argon2i. It is the **recommended default** for password hashing.

---

### ⚙️ Key Features
- **Memory-hard**: Uses a lot of RAM to slow down parallel cracking attempts.
- **Configurable**:
  - **Memory cost** – How much RAM it uses.
  - **Time cost** – How many iterations it runs.
  - **Parallelism** – How many threads/cores are used.
- **Built-in salting** and versioning.

---

### 🛠️ Example in Python
Using the `argon2-cffi` library:

```bash
pip install argon2-cffi
```

```python
from argon2 import PasswordHasher

ph = PasswordHasher()

# Hash a password
hash = ph.hash("supersecret")

# Verify a password
try:
    ph.verify(hash, "supersecret")
    print("Password is correct!")
except:
    print("Invalid password.")
```

You can also tweak parameters:

```python
ph = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=4)
```

---

### ✅ Why Use Argon2?
- **State-of-the-art** protection.
- **Customizable security parameters**.
- **Argon2id** is **recommended by OWASP** and most security standards.