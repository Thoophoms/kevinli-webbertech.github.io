Persisting authentication state is essential for providing a seamless user experience. When a user logs in, their authentication state (e.g., token, user role) should be saved so that they remain logged in even after refreshing the page or closing the browser. This can be achieved using **`localStorage`** or **cookies**.

In this guide, we'll implement authentication state persistence using **`localStorage`** and **cookies** in a React app.

---

### **1. Using `localStorage`**
`localStorage` is a simple way to persist data in the browser. It stores data as key-value pairs and remains available even after the browser is closed.

#### **Step 1: Update `AuthContext` to Use `localStorage`**
Modify the `AuthContext` to save and retrieve the authentication state from `localStorage`.

#### **AuthContext.js**
```jsx
import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Check localStorage for saved user data on initial load
  useEffect(() => {
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
      setUser(JSON.parse(savedUser));
    }
  }, []);

  const login = (email, password) => {
    // Mock login logic
    let userData;
    if (email === 'admin@example.com' && password === 'admin123') {
      userData = { email, role: 'admin' };
    } else if (email === 'user@example.com' && password === 'user123') {
      userData = { email, role: 'user' };
    } else {
      throw new Error('Invalid credentials');
    }

    // Save user data to state and localStorage
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
  };

  const logout = () => {
    // Clear user data from state and localStorage
    setUser(null);
    localStorage.removeItem('user');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

#### **Explanation**
- **`useEffect`**: On initial load, check `localStorage` for saved user data and set it in the state.
- **`login`**: Save the user data to `localStorage` after a successful login.
- **`logout`**: Remove the user data from `localStorage` when the user logs out.

---

### **2. Using Cookies**
Cookies are another way to persist data. They are automatically sent with every HTTP request, making them ideal for storing authentication tokens.

#### **Step 1: Install a Cookie Library**
To simplify working with cookies, install the `js-cookie` library:
```bash
npm install js-cookie
```

#### **Step 2: Update `AuthContext` to Use Cookies**
Modify the `AuthContext` to save and retrieve the authentication state using cookies.

#### **AuthContext.js**
```jsx
import React, { createContext, useState, useEffect } from 'react';
import Cookies from 'js-cookie';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Check cookies for saved user data on initial load
  useEffect(() => {
    const savedUser = Cookies.get('user');
    if (savedUser) {
      setUser(JSON.parse(savedUser));
    }
  }, []);

  const login = (email, password) => {
    // Mock login logic
    let userData;
    if (email === 'admin@example.com' && password === 'admin123') {
      userData = { email, role: 'admin' };
    } else if (email === 'user@example.com' && password === 'user123') {
      userData = { email, role: 'user' };
    } else {
      throw new Error('Invalid credentials');
    }

    // Save user data to state and cookies
    setUser(userData);
    Cookies.set('user', JSON.stringify(userData), { expires: 7 }); // Expires in 7 days
  };

  const logout = () => {
    // Clear user data from state and cookies
    setUser(null);
    Cookies.remove('user');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

#### **Explanation**
- **`Cookies.get`**: Retrieve the user data from cookies on initial load.
- **`Cookies.set`**: Save the user data to cookies after a successful login. The `expires` option sets the cookie's expiration time.
- **`Cookies.remove`**: Remove the user data from cookies when the user logs out.

---

### **3. Test the Application**
1. Start the app:
   ```bash
   npm start
   ```
2. Log in as an admin (`admin@example.com`, `admin123`) or a user (`user@example.com`, `user123`).
3. Refresh the page or close and reopen the browser.
4. Verify that the user remains logged in.

---

### **4. Choosing Between `localStorage` and Cookies**
- **`localStorage`**:
  - Easier to use for storing simple data.
  - Data is not automatically sent with HTTP requests.
  - Vulnerable to XSS attacks if not handled properly.
- **Cookies**:
  - Automatically sent with every HTTP request.
  - Can be secured with `HttpOnly` and `Secure` flags to prevent XSS and ensure they are only sent over HTTPS.
  - More complex to implement but better for authentication tokens.

---

### **5. Secure Your Implementation**
- **For `localStorage`**:
  - Sanitize and validate all data to prevent XSS attacks.
  - Use HTTPS to encrypt data in transit.
- **For Cookies**:
  - Use the `HttpOnly` flag to prevent JavaScript access.
  - Use the `Secure` flag to ensure cookies are only sent over HTTPS.
  - Set the `SameSite` attribute to prevent CSRF attacks.

#### **Example: Secure Cookies**
```jsx
Cookies.set('user', JSON.stringify(userData), {
  expires: 7,
  secure: true,
  httpOnly: true,
  sameSite: 'strict',
});
```

---

### **6. Next Steps**
- Integrate with a real backend for authentication (e.g., JWT, OAuth).
- Use **React Query** or **SWR** to fetch user roles and permissions from an API.
- Implement **refresh tokens** for long-lived sessions.

Happy coding! 🚀