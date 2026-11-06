# JWT application with RS256, HS256 and SHA-3-256

---

## JWTs with **RSA (`RS256`)** instead of HMAC (`HS256`)!

### 🧾 1. **HMAC with SHA-256**

HMAC (Hash-based Message Authentication Code) is used to ensure **data integrity** and **authenticity**.

```python
import hmac
import hashlib

message = b"this is a message"
key = b"supersecretkey"

hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"HMAC-SHA256: {hmac_sha256}")
```

---

### 📁 2. **File Integrity Check with SHA-256**

You can hash a file to verify its integrity:

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

### 🤜 SHA-256 vs SHA-3 vs BLAKE3 (Speed & Output)

```python
from hashlib import sha256, sha3_256
from blake3 import blake3
import time

data = b"hello world" * 1000

def benchmark(name, func):
    start = time.time()
    for _ in range(100000):
        func(data)
    end = time.time()
    print(f"{name}: {end - start:.2f} seconds")

benchmark("SHA-256", lambda d: sha256(d).digest())
benchmark("SHA3-256", lambda d: sha3_256(d).digest())
benchmark("BLAKE3", lambda d: blake3(d).digest())
```

> 💡 **Expected results** (will vary by system):
> - BLAKE3: 🏎️ Fastest
> - SHA-256: ⚡ Fast
> - SHA3-256: 🐢 Slower (but more secure in certain designs)

---

Perfect! Since you're interested in combining **SHA-256** with **digital signatures** and **JWTs**, here's how you can use SHA-256 in both scenarios, starting with Python examples.

---

### 🔏 1. **SHA-256 with Digital Signatures (using RSA)**

This is how you sign and verify a message using RSA + SHA-256:

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Generate private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Sign a message
message = b"secure message"
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Verify with public key
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
    print("✅ Signature is valid!")
except:
    print("❌ Invalid signature.")
```

---

### 🪪 2. **JWTs Signed with SHA-256 (HS256)**

JWTs (JSON Web Tokens) are often signed with HMAC + SHA-256 using the **HS256** algorithm.

Install the required package:
```bash
pip install pyjwt
```

Now create and decode a JWT:

```python
import jwt

payload = {"user_id": 42, "role": "admin"}
secret_key = "supersecret"

# Create a JWT
token = jwt.encode(payload, secret_key, algorithm="HS256")
print("JWT:", token)

# Decode & verify
decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
print("Decoded:", decoded)
```

---

### 🔒 When to Use What?

| Use Case                  | Hash Function Use                  |
|--------------------------|------------------------------------|
| **File integrity**       | SHA-256, SHA-3, BLAKE3              |
| **Password hashing**     | Argon2, bcrypt, scrypt             |
| **Data authenticity**    | HMAC-SHA256                        |
| **JWTs / Tokens**        | HMAC-SHA256 or RSA/ECDSA + SHA256 |
| **Digital signatures**   | SHA-256 (with RSA/ECDSA)           |

---


## JWT with **SHA-3**

1. ✅ **HMACs**
2. ✅ **JWTs (with SHA3 as a custom algorithm)**
3. ✅ **Digital Signatures**
4. ✅ **Benchmarking SHA-256 vs SHA3-256 vs BLAKE3**

---

### 🔑 1. HMAC with SHA3-256

```python
import hmac
import hashlib

message = b"authenticate this"
key = b"verysecretkey"

hmac_sha3 = hmac.new(key, message, hashlib.sha3_256).hexdigest()
print("HMAC-SHA3-256:", hmac_sha3)
```

> ✔️ Secure MAC (Message Authentication Code) using SHA-3.

---

### 🪪 2. JWT with SHA3 (custom usage – not standard!)

JWTs officially support `HS256`, `RS256`, `ES256`, etc.  
Using SHA-3 requires custom handling or non-standard libs.

Here’s how to *manually* sign a payload with HMAC + SHA3-256:

```python
import base64
import json
import hmac
import hashlib

def b64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=')

header = {"alg": "HS3-256", "typ": "JWT"}
payload = {"user_id": 123, "role": "admin"}
secret = b"customsecret"

header_b64 = b64url_encode(json.dumps(header).encode())
payload_b64 = b64url_encode(json.dumps(payload).encode())
signature = hmac.new(secret, header_b64 + b"." + payload_b64, hashlib.sha3_256).digest()
signature_b64 = b64url_encode(signature)

jwt_token = b".".join([header_b64, payload_b64, signature_b64])
print("Custom JWT (HS3-256):", jwt_token.decode())
```

> ⚠️ Custom! Not widely compatible with standard JWT libraries.

---

### ✍️ 3. Digital Signature with SHA3-256 (RSA)

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
message = b"digitally signed content"

# Sign with SHA3-256
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA3_256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA3_256()
)

# Verify
public_key = private_key.public_key()
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA3_256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA3_256()
    )
    print("✅ Signature verified (SHA3-256)")
except:
    print("❌ Signature invalid")
```

---

### 🧪 4. Benchmark: SHA-256 vs SHA3-256 vs BLAKE3

```python
from hashlib import sha256, sha3_256
from blake3 import blake3
import time

data = b"benchmark this payload" * 100

def benchmark(name, func):
    start = time.time()
    for _ in range(50000):
        func(data)
    end = time.time()
    print(f"{name}: {end - start:.2f} sec")

benchmark("SHA-256", lambda d: sha256(d).digest())
benchmark("SHA3-256", lambda d: sha3_256(d).digest())
benchmark("BLAKE3", lambda d: blake3(d).digest())
```

> 💡 Results will vary, but expect:  
> `BLAKE3` > `SHA-256` > `SHA3-256` in speed.
