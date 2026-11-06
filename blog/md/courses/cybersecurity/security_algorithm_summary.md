# Cyber Algorithm Summary

This document is not a complete cheatsheet but a summary of what we have learned by far.

## A general list of some popular cyber algorithms

| Algorithm | Category                                      | Usage                                                                                                              | Comment                                                                                                                                                                | Vulnerability/Security Level |
|-----------|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| MD5       | HASHING                                       | Fast looking/db indexing/non-security-critical app usage, checksum and always the same with the same content.      | Message Digest Algorithm 5. A hash function to create a 128-bit(16 bytes)/32-character hex decimal number. Designed by Ronald Rivest in 1991 succeding MD4.            | Collision vulnerabilities |
| SHA-1     | HASHING                                       | Digital signatures (e.g. SSL/TLS certificates), File integrity checks, Version control systems (like Git)          | 160-bit                                                                                                                                                                | Broken(collision) |
| SHA-256   | HASHING                                       | APIs and HMACs, file validation,  Digital certificates (SSL/TLS), Blockchain (Bitcoin uses it heavily),JWT signing | 256-bit                                                                                                                                                                | Secure (recommended) |
| SHA-2     | HASHING                                       | JWT signing, file encryption, or blockchain, not good for password hashing as it is too fast                       | Variable                                                                                                                                                               | Secure |
| SHA-3     | HASHING                                       | Digital signatures, Secure MACs (with HMAC or KMAC), High-security applications                                    | Variable                                                                                                                                                               | Future-proof |
| BLAKE3    | HASHING                                       | File checksums, Data integrity, Fingerprinting and Cryptographic applications,                                     | Variable                                                                                                                                                               | Fast & Secure |
| bcrypt    | HASHING                                       | Hashing passwords                                                                                                  | It was designed by **Niels Provos and David Mazières** in 1999, based on the **Blowfish** cipher.`bcrypt` is a **key derivation function** used for hashing passwords. | Fast & Secure |
| scrypt    | HASHING                                       | Hashing passwords                                                                                                  | [TODO] | Fast & Secure |
| argon2    | HASHING                                       | Hashing passwords                                                                                                  |[TODO]  | Fast & Secure |
| AES (Advanced Encryption Standard)                 | Symmetric Encryption(Private Key)             | Used in securing communications over HTTPS, disk encryption (BitLocker, FileVault), and VPNs.                      | It supports key sizes of 128, 192, and 256 bits.                                                                                                                       | Highly secure |
| DES (Data Encryption Standard)                     | Symmetric Encryption(Private Key)             | [TODO]                                                                                                             | small key size (56 bits)                                                                                                                                               | Vulnerability to brute-force attacks |
| 3DES (Triple DES)                                  | Symmetric Encryption(Private Key)             | [TODO]                                                                                                             | 3DES applies the DES algorithm three times with different keys to improve security                                                                                     | Outdated and slower compared to AES |
| RC4 (Rivest Cipher 4)                              | Symmetric Encryption(Private Key)             | RC4 is a stream cipher widely used in protocols like SSL/TLS in the past                                           |                                                                                                                                                                        | Not Secure |
| RSA (Rivest-Shamir-Adleman)                        | Asymmetric Encryption (Public Key Encryption) | Digital certificates (SSL/TLS), email encryption (PGP, S/MIME), and digital signatures                             | Used by ECDSA and ECDH                                                                                                                                                 | Secure |
| ECC (Elliptic Curve Cryptography)                  | Asymmetric Encryption (Public Key Encryption) | [TODO]                                                                                                             | ECC uses elliptic curves over finite fields for encryption. It offers stronger security with shorter key lengths compared to RSA.                                      | Secure |
| ECDSA (Elliptic Curve Digital Signature Algorithm) | Asymmetric Encryption (Public Key Encryption) | Digital signatures                                                                                                 |                                                                                                                                                                        | Secure |
| ECDH (Elliptic Curve Diffie-Hellman)               | Asymmetric Encryption (Public Key Encryption) | secure key exchange                                                                                                |                                                                                                                                                                        | Secure |


### Quick Comparison of `password` Hashing Algorithm 

| Feature     | bcrypt    | scrypt    | argon2     |
|-------------|-----------|-----------|------------|
| Age         | 1999      | 2009      | 2015       |
| Memory-hard | ❌ (light) | ✅         | ✅✅✅        |
| Configurable| Limited   | Yes       | Very       |
| Default use | Legacy    | Decent    | Modern     |
| OWASP rec.  | ✅         | ✅         | ✅✅✅        |

### 🚀 Speed Benchmarks

| Algorithm | Speed (MB/s, approx) |
|-----------|----------------------|
| MD5       | ~500 MB/s            |
| SHA-256   | ~300 MB/s            |
| BLAKE2b   | ~700 MB/s            |
| **BLAKE3**| **~1500+ MB/s**      |

### SHA-1 vs Others

| Algorithm | Hash Size | Security | Status     |
|-----------|-----------|----------|------------|
| SHA-1     | 160-bit   | 🔴 Weak  | Deprecated |
| SHA-256   | 256-bit   | ✅ Strong | Recommended |
| BLAKE3    | 256-bit+  | ✅✅✅    | Modern     |
| SHA-3     | 256-bit+  | ✅✅     | Very secure |
| MD5       | 128-bit   | 🔥 Broken | Totally insecure |

### SHA-1 vs SHA-256 vs SHA-3

| Feature      | SHA-1     | SHA-256   | SHA-3      |
|--------------|-----------|-----------|------------|
| Output size  | 160-bit   | 256-bit   | 256+ bit   |
| Secure?      | ❌ No     | ✅ Yes     | ✅✅ Yes     |
| Speed        | Fast      | Fast      | Slower     |
| Status       | Deprecated| Active    | Modern alt |
| Use case     | Legacy    | Standard  | Advanced   |

### SHA-2 vs SHA-3 vs BLAKE3

| Feature        | SHA-256      | SHA3-256     | BLAKE3         |
|----------------|--------------|--------------|----------------|
| Year released  | 2001         | 2015         | 2020           |
| Design         | Merkle–Damgård | Sponge      | Tree-hash      |
| Speed          | ⚡ Fast       | 🐢 Slower     | 🚀 Fastest      |
| Hardware opt.  | ✅ Yes        | ⚠️ Limited     | ✅ Yes          |
| Security       | ✅ Secure     | ✅✅ Very secure| ✅✅ Secure       |
| Use case       | Most common  | High-security| Fast hashing   |


### Algorithm and Applications

### 🔒 When to Use What?

| Use Case                  | Hash Function Use                  |
|--------------------------|------------------------------------|
| **File integrity**       | SHA-256, SHA-3, BLAKE3              |
| **Password hashing**     | Argon2, bcrypt, scrypt             |
| **Data authenticity**    | HMAC-SHA256                        |
| **JWTs / Tokens**        | HMAC-SHA256 or RSA/ECDSA + SHA256 |
| **Digital signatures**   | SHA-256 (with RSA/ECDSA)           |
