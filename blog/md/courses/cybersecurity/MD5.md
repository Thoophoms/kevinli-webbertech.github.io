# MD5 (Message Digest Algorithm 5)

The **MD5 (Message Digest Algorithm 5)** is a widely used cryptographic hash function that produces a 128-bit (16-byte) hash value, typically expressed as a 32-character hexadecimal number. It was designed by **Ronald Rivest** in 1991 as an improved version of **MD4**.

### **Key Features of MD5**
1. **Fixed Output Size**: Always produces a 128-bit hash.
2. **Deterministic**: The same input always yields the same hash.
3. **Fast Computation**: Efficient for checksums and non-cryptographic uses.
4. **Pre-image Resistance**: Hard to reverse-engineer the original input from the hash.
5. **Collision Vulnerabilities**: MD5 is **cryptographically broken** due to collision attacks (two different inputs producing the same hash).

---

## **MD5 Algorithm Steps**
1. **Padding the Input**  
   - The message is padded to ensure its length is congruent to **448 mod 512** (i.e., `length ≡ 448 mod 512`).
   - Padding consists of:
     - A single `1` bit followed by `0`s.
     - A 64-bit representation of the original message length (before padding).

2. **Breaking into 512-bit Blocks**  
   - The padded message is divided into **512-bit (64-byte) chunks**.

3. **Initializing MD Buffer (State Variables)**  
   - Four 32-bit registers (`A, B, C, D`) are initialized with fixed constants:
     ```
     A = 0x67452301
     B = 0xEFCDAB89
     C = 0x98BADCFE
     D = 0x10325476
     ```

4. **Processing Each Block (Main Loop)**  
   - Each 512-bit block is processed in **four rounds (64 steps)**.
   - Each round uses a different **nonlinear function** (`F, G, H, I`) and a **constant array** (`T[1..64]`).
   - The operations include:
     - **Bitwise operations** (AND, OR, XOR, NOT).
     - **Modular addition** (with `2³²` wrap-around).
     - **Left rotations** (`<<<`) for diffusion.

5. **Output the Hash**  
   - After all blocks are processed, the final hash is the concatenation of `A, B, C, D` in **little-endian** format.

---

## **Example MD5 Hash**
- **Input**: `"hello"`
- **MD5 Hash**: `5d41402abc4b2a76b9719d911017c592`

---

## **Security Issues with MD5**
- **Collision Attacks**: It is computationally feasible to find two different inputs with the same MD5 hash (e.g., using the **Birthday Attack**).
- **Pre-image Attacks**: While harder than collisions, MD5 is no longer considered secure for cryptographic purposes.
- **Deprecated Usage**: MD5 is **not recommended** for:
  - Digital signatures.
  - SSL certificates.
  - Password hashing (use **bcrypt, Argon2, or SHA-256** instead).

---

## **Applications of MD5 (Non-Cryptographic)**
✔ **Checksums** (file integrity verification).  
✔ **Database indexing** (quick lookups).  
✔ **Non-security-critical applications** (e.g., partitioning in distributed systems).  

---

## **Alternatives to MD5**
| Algorithm | Hash Length | Security Level |
|-----------|------------|----------------|
| **SHA-1** | 160-bit    | Broken (collisions) |
| **SHA-256** | 256-bit | Secure (recommended) |
| **SHA-3** | Variable | Future-proof |
| **BLAKE3** | Variable | Fast & Secure |

### **Conclusion**
While MD5 is **fast and simple**, it should **not** be used for security-sensitive applications due to its vulnerabilities. For cryptographic purposes, **SHA-256 or SHA-3** are better choices.