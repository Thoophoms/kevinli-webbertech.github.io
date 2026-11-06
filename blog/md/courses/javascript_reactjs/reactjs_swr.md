# SWR

Both **React Query** and **SWR** are powerful libraries for data fetching in React applications. They simplify data management, caching, and synchronization, and they integrate seamlessly with **Suspense** for a smoother user experience.

In this guide, we'll explore how to use **React Query** and **SWR** with **Suspense** for advanced data fetching.

---

### **1. Using React Query with Suspense**

React Query is a popular library for managing server state, caching, and background updates. It works well with Suspense for declarative data fetching.

#### **Step 1: Install React Query**
```bash
npm install @tanstack/react-query
```

#### **Step 2: Set Up React Query Provider**
Wrap your app with the `QueryClientProvider` to enable React Query.

#### **index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import App from './App';

const queryClient = new QueryClient();

ReactDOM.render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
  document.getElementById('root')
);
```

#### **Step 3: Fetch Data with Suspense**
Use the `useQuery` hook with the `suspense: true` option to enable Suspense.

#### **App.js**
```jsx
import React, { Suspense } from 'react';
import { useQuery } from '@tanstack/react-query';

function fetchData() {
  return fetch('https://jsonplaceholder.typicode.com/posts').then((res) =>
    res.json()
  );
}

function Posts() {
  const { data } = useQuery(['posts'], fetchData, { suspense: true });

  return (
    <ul>
      {data.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <Posts />
      </Suspense>
    </div>
  );
}

export default App;
```

#### **Explanation**
- **`useQuery`**: Fetches data and manages caching.
- **`suspense: true`**: Enables Suspense mode for the query.
- **`Suspense`**: Displays a fallback UI while the data is being fetched.

---

### **2. Using SWR with Suspense**

SWR (Stale-While-Revalidate) is a lightweight library for data fetching. It also supports Suspense for declarative data fetching.

#### **Step 1: Install SWR**
```bash
npm install swr
```

#### **Step 2: Fetch Data with Suspense**
Use the `useSWR` hook with the `suspense: true` option.

#### **App.js**
```jsx
import React, { Suspense } from 'react';
import useSWR from 'swr';

const fetcher = (url) => fetch(url).then((res) => res.json());

function Posts() {
  const { data } = useSWR('https://jsonplaceholder.typicode.com/posts', fetcher, {
    suspense: true,
  });

  return (
    <ul>
      {data.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <Posts />
      </Suspense>
    </div>
  );
}

export default App;
```

#### **Explanation**
- **`useSWR`**: Fetches data and handles caching and revalidation.
- **`suspense: true`**: Enables Suspense mode for the SWR hook.
- **`Suspense`**: Displays a fallback UI while the data is being fetched.

---

### **3. Combining React Query/SWR with Error Boundaries**
To handle errors gracefully, wrap your Suspense components with an **Error Boundary**.

#### **Step 1: Create an Error Boundary**
```jsx
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong. Please try again later.</h1>;
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
```

#### **Step 2: Wrap Suspense with Error Boundary**
```jsx
import React, { Suspense } from 'react';
import { useQuery } from '@tanstack/react-query';
import ErrorBoundary from './ErrorBoundary';

function fetchData() {
  return fetch('https://jsonplaceholder.typicode.com/posts').then((res) =>
    res.json()
  );
}

function Posts() {
  const { data } = useQuery(['posts'], fetchData, { suspense: true });

  return (
    <ul>
      {data.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <ErrorBoundary>
        <Suspense fallback={<div>Loading...</div>}>
          <Posts />
        </Suspense>
      </ErrorBoundary>
    </div>
  );
}

export default App;
```

---

### **4. Advanced Features**

#### **React Query**
- **Background Refetching**: Automatically refetches data in the background when the app regains focus or the network reconnects.
- **Pagination**: Use `useQuery` with pagination keys to fetch paginated data.
- **Optimistic Updates**: Update the UI optimistically before the server responds.

#### **SWR**
- **Revalidation on Focus**: Automatically refetches data when the window regains focus.
- **Dependent Fetching**: Fetch data conditionally based on other data.
- **Middleware**: Extend SWR with custom logic using middleware.

---

### **5. Choosing Between React Query and SWR**
- **React Query**: More feature-rich, suitable for complex apps with advanced caching and synchronization needs.
- **SWR**: Lightweight and simple, ideal for smaller apps or projects with minimal data fetching requirements.

---

### **6. Next Steps**
- Explore **React Query Devtools** for debugging and monitoring queries.
- Use **SWR’s middleware** for custom caching and fetching logic.
- Combine **React Query/SWR** with **React Server Components** for server-side data fetching.

Happy coding! 🚀


