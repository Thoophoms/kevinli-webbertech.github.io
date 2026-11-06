Protected routes are a common pattern in React applications to restrict access to certain pages based on authentication status. For example, you might want to allow only logged-in users to access a dashboard page.

In this tutorial, I'll show you how to implement protected routes in a React application using React Router.

---

### **1. Setting Up Authentication**
For simplicity, we'll use a mock authentication system. In a real app, you'd replace this with an actual authentication mechanism (e.g., JWT, OAuth).

#### **Create an Auth Context**
Create a context to manage authentication state.

#### **AuthContext.js**
```jsx
import React, { createContext, useState } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const login = () => {
    setIsAuthenticated(true);
  };

  const logout = () => {
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

---

### **2. Wrap Your App with the Auth Provider**
Wrap your entire application with the `AuthProvider` to make the authentication state available everywhere.

#### **index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { AuthProvider } from './AuthContext';

ReactDOM.render(
  <AuthProvider>
    <App />
  </AuthProvider>,
  document.getElementById('root')
);
```

---

### **3. Create a Protected Route Component**
Create a `ProtectedRoute` component that checks if the user is authenticated. If not, it redirects to the login page.

#### **ProtectedRoute.js**
```jsx
import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from './AuthContext';

const ProtectedRoute = () => {
  const { isAuthenticated } = useAuth();

  return isAuthenticated ? <Outlet /> : <Navigate to="/login" />;
};

export default ProtectedRoute;
```

---

### **4. Set Up Routes**
Define your routes, including protected routes.

#### **App.js**
```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useAuth } from './AuthContext';
import Home from './components/Home';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import ProtectedRoute from './ProtectedRoute';

function App() {
  const { isAuthenticated, logout } = useAuth();

  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
          <li>
            {isAuthenticated ? (
              <button onClick={logout}>Logout</button>
            ) : (
              <Link to="/login">Login</Link>
            )}
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<Dashboard />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
```

---

### **5. Create the Login Component**
Create a `Login` component to handle user authentication.

#### **Login.js**
```jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../AuthContext';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Mock authentication
    if (username === 'admin' && password === 'password') {
      login();
      navigate('/dashboard');
    } else {
      alert('Invalid credentials');
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Username:</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
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

---

### **6. Create the Dashboard Component**
Create a `Dashboard` component that is only accessible to authenticated users.

#### **Dashboard.js**
```jsx
import React from 'react';

function Dashboard() {
  return <h1>Welcome to the Dashboard!</h1>;
}

export default Dashboard;
```

---

### **7. Handle Logout**
Add a logout button in the navigation to allow users to log out.

#### **App.js (Updated)**
```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useAuth } from './AuthContext';
import Home from './components/Home';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import ProtectedRoute from './ProtectedRoute';

function App() {
  const { isAuthenticated, logout } = useAuth();

  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
          <li>
            {isAuthenticated ? (
              <button onClick={logout}>Logout</button>
            ) : (
              <Link to="/login">Login</Link>
            )}
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<Dashboard />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
```

---

### **8. Test the Application**
1. Start the app:
   ```bash
   npm start
   ```
2. Try accessing `/dashboard` without logging in. You should be redirected to `/login`.
3. Log in with the username `admin` and password `password`.
4. After logging in, you should be able to access `/dashboard`.

---

9. Next Steps
Integrate with a real backend for authentication (e.g., Firebase, Auth0, or your own API).

Add role-based access control (e.g., admin vs. user).

Persist authentication state using localStorage or cookies.