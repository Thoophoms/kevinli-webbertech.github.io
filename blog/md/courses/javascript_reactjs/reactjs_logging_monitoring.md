## **logging and monitoring** 

**logging and monitoring** to your application is crucial for tracking token usage, detecting suspicious activity, and ensuring the security of your system. By logging key events and monitoring token usage, you can identify potential security threats (e.g., token theft, brute force attacks) and respond to them proactively.

In this guide, we'll implement logging and monitoring in a React app with a backend API. We'll focus on:
1. **Logging Key Events**: Log login attempts, token refreshes, and logout events.
2. **Monitoring Token Usage**: Track token usage patterns and detect anomalies.
3. **Alerting**: Send alerts for suspicious activity (e.g., multiple failed login attempts).

---

### **1. Backend Setup**
Your backend should log key events and monitor token usage. Here's an example implementation using **Node.js/Express** and **Winston** for logging.

#### **Install Dependencies**
```bash
npm install winston express-winston
```

#### **Backend Logging Setup**
```javascript
// server.js
const express = require('express');
const winston = require('winston');
const expressWinston = require('express-winston');

const app = express();

// Configure Winston logger
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'logs/activity.log' }),
  ],
});

// Log HTTP requests
app.use(
  expressWinston.logger({
    winstonInstance: logger,
    meta: true, // Log metadata (e.g., request body)
    msg: 'HTTP {{req.method}} {{req.url}}',
    level: 'info',
  })
);

// Example login endpoint
app.post('/login', (req, res) => {
  const { email, password } = req.body;

  // Mock authentication
  if (email === 'admin@example.com' && password === 'admin123') {
    logger.info('Successful login', { email });
    res.json({ accessToken: 'short-lived-token', refreshToken: 'long-lived-token' });
  } else {
    logger.warn('Failed login attempt', { email });
    res.status(401).json({ message: 'Invalid credentials' });
  }
});

// Example logout endpoint
app.post('/logout', (req, res) => {
  const { refreshToken } = req.body;
  logger.info('User logged out', { refreshToken });
  res.json({ message: 'Logged out successfully' });
});

// Example protected endpoint
app.get('/protected', (req, res) => {
  const token = req.headers.authorization?.split(' ')[1];
  logger.info('Access token used', { token });
  res.json({ message: 'Protected resource accessed' });
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

#### **Explanation**
- **Winston**: A logging library for Node.js.
- **express-winston**: Middleware to log HTTP requests.
- **Log Files**: Logs are saved to `logs/activity.log` and printed to the console.

---

### **2. Frontend Logging**
On the frontend, you can log key events (e.g., login attempts, token refreshes) using a logging service like **Sentry** or **LogRocket**. For simplicity, we'll use `console.log` in this example.

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

      console.log('Access token refreshed', { newAccessToken });
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

      console.log('User logged in', { email });
    } catch (error) {
      console.error('Login failed', { email, error });
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

      console.log('User logged out');
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

### **3. Monitoring and Alerting**
To monitor token usage and detect suspicious activity, you can use tools like:
- **Sentry**: For error tracking and performance monitoring.
- **LogRocket**: For session replay and frontend logging.
- **Prometheus + Grafana**: For backend monitoring and alerting.

#### **Example: Using Sentry for Frontend Monitoring**
1. Install Sentry:
   ```bash
   npm install @sentry/react @sentry/tracing
   ```
2. Initialize Sentry in your app:
   ```jsx
   import * as Sentry from '@sentry/react';
   import { BrowserTracing } from '@sentry/tracing';

   Sentry.init({
     dsn: 'YOUR_SENTRY_DSN', // Replace with your Sentry DSN
     integrations: [new BrowserTracing()],
     tracesSampleRate: 1.0,
   });
   ```
3. Log errors and events:
   ```jsx
   try {
     // Your code here
   } catch (error) {
     Sentry.captureException(error);
   }
   ```

---

### **4. Testing the Implementation**
1. Start the app:
   ```bash
   npm start
   ```
2. Perform actions like login, logout, and token refresh.
3. Check the logs (`logs/activity.log`) and monitoring tools for recorded events.

---

### **5. Security Best Practices**
- **Log Sensitive Data Carefully**: Avoid logging sensitive information like passwords or tokens.
- **Monitor Anomalies**: Set up alerts for unusual activity (e.g., multiple failed login attempts).
- **Use HTTPS**: Encrypt all communication between the client and server.
- **Regularly Review Logs**: Periodically review logs to identify potential security threats.

---

### **6. Next Steps**
- Implement **rate limiting** to prevent brute force attacks.
- Use **IP blocking** for repeated failed login attempts.
- Add **user activity tracking** to monitor actions within your app.

Happy coding! 🚀