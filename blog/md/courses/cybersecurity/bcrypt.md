# bcrypt Algorithm

The `bcrypt` algorithm is a popular and secure **password hashing function** designed for storing passwords safely. Here's a breakdown of what it is and how it works:

---

### 🔐 What is `bcrypt`?
- `bcrypt` is a **key derivation function** used for hashing passwords.
- It was designed by **Niels Provos and David Mazières** in 1999, based on the **Blowfish** cipher.
- It's specifically designed to be **computationally expensive** to resist brute-force attacks.

---

### ⚙️ How Does `bcrypt` Work?
1. **Salting**: 
   - A **unique salt** (random string) is added to the password before hashing to prevent **rainbow table** attacks.
2. **Key stretching**:
   - `bcrypt` repeats the hashing process multiple times (configurable with a **cost factor**, also called "work factor").
   - This makes brute-forcing slower and more resource-intensive.
3. **Output**: 
   - The final hash includes the algorithm identifier, cost factor, salt, and hash — all in one string.
   - Example: `$2b$12$KIXoE3zM.P1G1FbnZ5ZzOOGtrm06tu3FkPobWc1KdzzFZaqLfr0Zu`

---

### 🛠️ Example in Python
Using the `bcrypt` library:
```python
import bcrypt

# Hashing a password
password = b"supersecret"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Verifying a password
if bcrypt.checkpw(password, hashed):
    print("Password matches!")
else:
    print("Invalid password.")
```

---

### 🔒 Why Use `bcrypt`?
- **Slow by design** (helps against brute-force).
- **Built-in salt generation**.
- **Widely adopted** and well-tested.
