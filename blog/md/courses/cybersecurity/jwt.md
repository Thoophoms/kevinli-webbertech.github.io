# JWT

JWT stands for JSON Web Token. It's an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed.

A typical JWT is composed of three parts:

1. **Header**: Usually consists of the type of the token (JWT) and the signing algorithm (e.g., HMAC SHA256 or RSA).
   
   Example:
   ```json
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```

2. **Payload**: Contains the claims or statements about an entity (typically, the user) and additional data. Claims can be:
   - **Registered Claims**: Predefined claims like `iss` (issuer), `exp` (expiration), `sub` (subject), etc.
   - **Public Claims**: Claims that are not registered and can be defined by those using JWT.
   - **Private Claims**: Custom claims shared between the parties that agree on using them.
   
   Example:
   ```json
   {
     "sub": "1234567890",
     "name": "John Doe",
     "iat": 1516239022
   }
   ```

3. **Signature**: The signature is created by taking the encoded header, encoded payload, a secret key, and the signing algorithm. This part ensures the token's integrity and authenticity.

   Example (if using the HMAC SHA256 algorithm):
   ```text
   HMACSHA256(
     base64UrlEncode(header) + "." +
     base64UrlEncode(payload),
     secret)
   ```

### JWT Structure
A JWT is represented as a string with three parts, separated by periods (`.`):
```
header.payload.signature
```

### Use Cases
- **Authentication**: After a user logs in, a JWT can be used to authenticate subsequent requests. It is sent in the Authorization header (usually in the format `Bearer <token>`).
- **Authorization**: Allows verifying whether a user has the necessary permissions to access a resource.
- **Information Exchange**: A JWT can securely transmit information between parties since it is digitally signed, ensuring that the data has not been tampered with.
