Implementing **role-based access control (RBAC)** in a React application involves restricting access to certain parts of the app based on the user's role (e.g., admin, user). This is commonly used in applications where different users have different levels of access.

In this guide, we'll walk through how to implement RBAC in a React app using **React Router** and **React Query** (or any state management library). We'll create a simple example where:
- **Admins** can access all pages.
- **Users** can only access specific pages.

---

### **1. Setting Up the Project**
Start by creating a new React app (if you don’t have one already):
```bash
npx create-react-app rbac-demo
cd rbac-demo
```

Install the required dependencies:
```bash
npm install @tanstack/react-query react-router-dom
```

---

### **2. Create a Mock Authentication System**
For simplicity, we'll use a mock authentication system. In a real app, you'd replace this with a backend service (e.g., JWT, OAuth).

#### **AuthContext.js**
Create a context to manage authentication and user roles.

```jsx
import React, { createContext, useState } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = (email, password) => {
    // Mock login logic
    if (email === 'admin@example.com' && password === 'admin123') {
      setUser({ email, role: 'admin' });
    } else if (email === 'user@example.com' && password === 'user123') {
      setUser({ email, role: 'user' });
    } else {
      throw new Error('Invalid credentials');
    }
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
```

---

### **3. Create Protected Routes**
Create a `ProtectedRoute` component to restrict access based on the user's role.

#### **ProtectedRoute.js**
```jsx
import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from './AuthContext';

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

### **4. Set Up Routes with Role-Based Access**
Define your routes and apply role-based access control.

#### **App.js**
```jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AuthProvider, useAuth } from './AuthContext';
import ProtectedRoute from './ProtectedRoute';
import Home from './components/Home';
import Login from './components/Login';
import AdminPage from './components/AdminPage';
import UserPage from './components/UserPage';
import Profile from './components/Profile';

function App() {
  const { user, logout } = useAuth();

  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          {user && (
            <>
              <li>
                <Link to="/profile">Profile</Link>
              </li>
              {user.role === 'admin' && (
                <li>
                  <Link to="/admin">Admin</Link>
                </li>
              )}
              {user.role === 'user' && (
                <li>
                  <Link to="/user">User</Link>
                </li>
              )}
              <li>
                <button onClick={logout}>Logout</button>
              </li>
            </>
          )}
          {!user && (
            <li>
              <Link to="/login">Login</Link>
            </li>
          )}
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route element={<ProtectedRoute roles={['admin', 'user']} />}>
          <Route path="/profile" element={<Profile />} />
        </Route>
        <Route element={<ProtectedRoute roles={['admin']} />}>
          <Route path="/admin" element={<AdminPage />} />
        </Route>
        <Route element={<ProtectedRoute roles={['user']} />}>
          <Route path="/user" element={<UserPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default function AppWrapper() {
  return (
    <AuthProvider>
      <App />
    </AuthProvider>
  );
}
```

---

### **5. Create Components**
Create the components for each route.

#### **Home.js**
```jsx
import React from 'react';

function Home() {
  return <h1>Home Page</h1>;
}

export default Home;
```

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

  const handleSubmit = (e) => {
    e.preventDefault();
    try {
      login(email, password);
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

#### **AdminPage.js**
```jsx
import React from 'react';

function AdminPage() {
  return <h1>Admin Page</h1>;
}

export default AdminPage;
```

#### **UserPage.js**
```jsx
import React from 'react';

function UserPage() {
  return <h1>User Page</h1>;
}

export default UserPage;
```

#### **Profile.js**
```jsx
import React from 'react';
import { useAuth } from '../AuthContext';

function Profile() {
  const { user } = useAuth();

  return (
    <div>
      <h1>Profile</h1>
      <p>Email: {user?.email}</p>
      <p>Role: {user?.role}</p>
    </div>
  );
}

export default Profile;
```

---

### **6. Test the Application**
1. Start the app:
   ```bash
   npm start
   ```
2. Log in as an admin (`admin@example.com`, `admin123`) or a user (`user@example.com`, `user123`).
3. Verify that:
   - Admins can access `/admin` and `/profile`.
   - Users can access `/user` and `/profile`.
   - Unauthorized users are redirected to the login page.

---

### **7. Next Steps**
- Integrate with a real backend for authentication and role management.
- Use **React Query** to fetch user roles and permissions from an API.
- Add more granular permissions (e.g., specific actions for specific roles).

Happy coding! 🚀