Implementing **refresh tokens** is a common practice for maintaining long-lived user sessions while keeping your application secure. Refresh tokens allow users to stay authenticated without requiring them to log in repeatedly. Here's how it works:

1. **Access Token**: A short-lived token used to access protected resources.
2. **Refresh Token**: A long-lived token used to obtain a new access token when the current one expires.

When the access token expires, the client sends the refresh token to the server to get a new access token. This ensures that the user remains authenticated without compromising security.

---

### **1. Setting Up the Backend**
For this example, we'll assume you have a backend API that supports:
- **Login**: Returns an access token and a refresh token.
- **Refresh Token Endpoint**: Accepts a refresh token and returns a new access token.

#### **Example Backend Endpoints**
- **POST /login**: Authenticates the user and returns:
  ```json
  {
    "accessToken": "short-lived-token",
    "refreshToken": "long-lived-token"
  }
  ```
- **POST /refresh-token**: Accepts a refresh token and returns a new access token:
  ```json
  {
    "accessToken": "new-short-lived-token"
  }
  ```

---

### **2. Update the `AuthContext`**
We'll modify the `AuthContext` to handle access tokens, refresh tokens, and token refreshing.

#### **AuthContext.js**
```jsx
import React, { createContext, useState, useEffect } from 'react';
import Cookies from 'js-cookie';
import axios from 'axios';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState(null);
  const [refreshToken, setRefreshToken] = useState(null);

  // Check cookies for saved tokens on initial load
  useEffect(() => {
    const savedAccessToken = Cookies.get('accessToken');
    const savedRefreshToken = Cookies.get('refreshToken');
    const savedUser = Cookies.get('user');

    if (savedAccessToken && savedRefreshToken && savedUser) {
      setAccessToken(savedAccessToken);
      setRefreshToken(savedRefreshToken);
      setUser(JSON.parse(savedUser));
    }
  }, []);

  // Function to refresh the access token
  const refreshAccessToken = async () => {
    try {
      const response = await axios.post('/refresh-token', {
        refreshToken,
      });

      const newAccessToken = response.data.accessToken;
      setAccessToken(newAccessToken);
      Cookies.set('accessToken', newAccessToken, { expires: 1 }); // Expires in 1 day
    } catch (error) {
      console.error('Failed to refresh token:', error);
      logout();
    }
  };

  // Axios interceptor to handle token refreshing
  useEffect(() => {
    const requestInterceptor = axios.interceptors.request.use(
      (config) => {
        if (accessToken) {
          config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
      },
      (error) => Promise.reject(error)
    );

    const responseInterceptor = axios.interceptors.response.use(
      (response) => response,
      async (error) => {
        const originalRequest = error.config;

        // If the error is due to an expired token, try refreshing it
        if (error.response.status === 401 && !originalRequest._retry) {
          originalRequest._retry = true;
          await refreshAccessToken();
          return axios(originalRequest);
        }

        return Promise.reject(error);
      }
    );

    return () => {
      axios.interceptors.request.eject(requestInterceptor);
      axios.interceptors.response.eject(responseInterceptor);
    };
  }, [accessToken, refreshToken]);

  const login = async (email, password) => {
    try {
      const response = await axios.post('/login', { email, password });

      const { accessToken, refreshToken, user } = response.data;

      // Save tokens and user data to state and cookies
      setAccessToken(accessToken);
      setRefreshToken(refreshToken);
      setUser(user);

      Cookies.set('accessToken', accessToken, { expires: 1 }); // Expires in 1 day
      Cookies.set('refreshToken', refreshToken, { expires: 7 }); // Expires in 7 days
      Cookies.set('user', JSON.stringify(user), { expires: 7 });
    } catch (error) {
      throw new Error('Login failed');
    }
  };

  const logout = () => {
    // Clear state and cookies
    setAccessToken(null);
    setRefreshToken(null);
    setUser(null);

    Cookies.remove('accessToken');
    Cookies.remove('refreshToken');
    Cookies.remove('user');
  };

  return (
    <AuthContext.Provider value={{ user, accessToken, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

---

### **3. Using the `AuthContext`**
Now, you can use the `AuthContext` in your components to handle authentication.

#### **Login.js**
```jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await login(email, password);
      navigate('/');
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
```

#### **ProtectedRoute.js**
```jsx
import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../AuthContext';

const ProtectedRoute = ({ roles }) => {
  const { user } = useAuth();

  // If user is not logged in, redirect to login
  if (!user) {
    return <Navigate to="/login" />;
  }

  // If user does not have the required role, redirect to home
  if (!roles.includes(user.role)) {
    return <Navigate to="/" />;
  }

  // Allow access
  return <Outlet />;
};

export default ProtectedRoute;
```

---

### **4. Testing the Implementation**
1. Start the app:
   ```bash
   npm start
   ```
2. Log in as an admin (`admin@example.com`, `admin123`) or a user (`user@example.com`, `user123`).
3. Verify that:
   - The access token is refreshed automatically when it expires.
   - The user remains logged in even after refreshing the page.

---

### **5. Security Best Practices**
- **Use HTTPS**: Ensure all communication between the client and server is encrypted.
- **Secure Cookies**: Use the `HttpOnly`, `Secure`, and `SameSite` flags for cookies.
- **Short-Lived Access Tokens**: Set a short expiration time for access tokens (e.g., 15 minutes).
- **Long-Lived Refresh Tokens**: Store refresh tokens securely and set a longer expiration time (e.g., 7 days).
- **Token Rotation**: Invalidate the old refresh token when issuing a new one.

---

### **6. Next Steps**
- Implement **token blacklisting** to revoke compromised tokens.
- Add **role-based access control** to restrict access to specific routes or features.
- Use **React Query** or **SWR** for data fetching with automatic token refreshing.

Happy coding! 🚀