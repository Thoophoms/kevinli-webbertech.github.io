**Token blacklisting** is a security mechanism used to revoke compromised or invalidated tokens. When a token is blacklisted, it can no longer be used to access protected resources. This is particularly important for refresh tokens, as they have a longer lifespan and could be exploited if compromised.

In this guide, we'll implement token blacklisting in a React app with a backend API. We'll assume you have a backend that supports:
- **Blacklisting Tokens**: Stores invalidated tokens in a database or cache.
- **Checking Blacklisted Tokens**: Verifies if a token is blacklisted before allowing access.

---

### **1. Backend Setup**
Your backend should have the following endpoints:
1. **POST /logout**: Blacklists the current refresh token.
2. **Middleware to Check Blacklisted Tokens**: Verifies if a token is blacklisted before processing requests.

#### **Example Backend Implementation (Pseudocode)**
```javascript
// Pseudocode for a Node.js/Express backend

const blacklistedTokens = new Set(); // Use a database or cache in production

// Middleware to check blacklisted tokens
function checkBlacklistedToken(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1]; // Extract token from header
  if (blacklistedTokens.has(token)) {
    return res.status(401).json({ message: 'Token is blacklisted' });
  }
  next();
}

// Endpoint to blacklist a token
app.post('/logout', (req, res) => {
  const token = req.body.refreshToken; // Assume the refresh token is sent in the request body
  blacklistedTokens.add(token); // Add the token to the blacklist
  res.json({ message: 'Logged out successfully' });
});
```

---

### **2. Update the `AuthContext`**
We'll modify the `AuthContext` to handle token blacklisting during logout.

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

  const logout = async () => {
    try {
      // Blacklist the refresh token
      await axios.post('/logout', { refreshToken });

      // Clear state and cookies
      setAccessToken(null);
      setRefreshToken(null);
      setUser(null);

      Cookies.remove('accessToken');
      Cookies.remove('refreshToken');
      Cookies.remove('user');
    } catch (error) {
      console.error('Logout failed:', error);
    }
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
Now, you can use the `AuthContext` in your components to handle authentication and logout.

#### **Logout Button**
Add a logout button to your app:

```jsx
import React from 'react';
import { useAuth } from '../AuthContext';

function LogoutButton() {
  const { logout } = useAuth();

  return <button onClick={logout}>Logout</button>;
}

export default LogoutButton;
```

#### **ProtectedRoute.js**
Ensure that protected routes check for blacklisted tokens.

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
3. Click the logout button to blacklist the refresh token.
4. Verify that:
   - The refresh token is blacklisted on the backend.
   - The user is logged out and cannot access protected routes.

---

### **5. Security Best Practices**
- **Use a Database or Cache**: Store blacklisted tokens in a database or cache (e.g., Redis) for scalability.
- **Expire Blacklisted Tokens**: Automatically remove blacklisted tokens after their expiration time.
- **Secure Communication**: Use HTTPS to encrypt all communication between the client and server.
- **Token Rotation**: Invalidate the old refresh token when issuing a new one.

---

### **6. Next Steps**
- Implement **role-based access control** to restrict access to specific routes or features.
- Use **React Query** or **SWR** for data fetching with automatic token refreshing.
- Add **logging and monitoring** to track token usage and detect suspicious activity.

Happy coding! 🚀