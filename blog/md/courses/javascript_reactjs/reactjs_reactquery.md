# **React Query** 

(also known as **TanStack Query**) is a powerful library for managing server state, caching, and data fetching in React applications. It simplifies data synchronization, background updates, and error handling, making it a go-to solution for modern React apps.

In this guide, we'll explore **React Query** in detail, including setup, basic usage, advanced features, and best practices.

---

### **1. Installation**
Install React Query using npm or yarn:
```bash
npm install @tanstack/react-query
# or
yarn add @tanstack/react-query
```

---

### **2. Setting Up React Query**
Wrap your app with the `QueryClientProvider` to enable React Query.

#### **index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import App from './App';

// Create a QueryClient instance
const queryClient = new QueryClient();

ReactDOM.render(
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
  document.getElementById('root')
);
```

---

### **3. Basic Usage**
React Query uses the `useQuery` hook to fetch and manage data.

#### **Fetching Data**
Here’s an example of fetching a list of posts from an API:

#### **App.js**
```jsx
import React from 'react';
import { useQuery } from '@tanstack/react-query';

// Fetch data from an API
const fetchPosts = async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

function Posts() {
  const { data, error, isLoading, isError } = useQuery(['posts'], fetchPosts);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

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
      <Posts />
    </div>
  );
}

export default App;
```

#### **Explanation**
- **`useQuery`**: Takes a unique key (`['posts']`) and a fetch function (`fetchPosts`).
- **States**:
  - `isLoading`: True while the data is being fetched.
  - `isError`: True if an error occurs.
  - `data`: The fetched data.
  - `error`: The error object if the fetch fails.

---

### **4. Advanced Features**

#### **a. Pagination**
React Query makes it easy to implement pagination.

#### **Example: Paginated Posts**
```jsx
import React, { useState } from 'react';
import { useQuery } from '@tanstack/react-query';

const fetchPosts = async ({ pageParam = 1 }) => {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts?_page=${pageParam}&_limit=10`
  );
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

function Posts() {
  const [page, setPage] = useState(1);
  const { data, isLoading, isError, error } = useQuery(
    ['posts', page],
    () => fetchPosts({ pageParam: page }),
    { keepPreviousData: true }
  );

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <ul>
        {data.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
      <button onClick={() => setPage((prev) => Math.max(prev - 1, 1))}>
        Previous
      </button>
      <button onClick={() => setPage((prev) => prev + 1)}>Next</button>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Posts />
    </div>
  );
}

export default App;
```

#### **Explanation**
- **`pageParam`**: Used to fetch data for a specific page.
- **`keepPreviousData`**: Keeps the previous data while fetching new data, providing a smoother UX.

---

#### **b. Infinite Queries**
For infinite loading (e.g., "Load More" buttons), use the `useInfiniteQuery` hook.

#### **Example: Infinite Posts**
```jsx
import React from 'react';
import { useInfiniteQuery } from '@tanstack/react-query';

const fetchPosts = async ({ pageParam = 1 }) => {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts?_page=${pageParam}&_limit=10`
  );
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

function Posts() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isLoading,
    isError,
    error,
  } = useInfiniteQuery(['posts'], fetchPosts, {
    getNextPageParam: (lastPage, allPages) => {
      return lastPage.length ? allPages.length + 1 : undefined;
    },
  });

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <ul>
        {data.pages.map((page, i) => (
          <React.Fragment key={i}>
            {page.map((post) => (
              <li key={post.id}>{post.title}</li>
            ))}
          </React.Fragment>
        ))}
      </ul>
      <button
        onClick={() => fetchNextPage()}
        disabled={!hasNextPage}
      >
        Load More
      </button>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Posts />
    </div>
  );
}

export default App;
```

#### **Explanation**
- **`useInfiniteQuery`**: Fetches data in pages.
- **`getNextPageParam`**: Determines the next page to fetch.
- **`fetchNextPage`**: Loads the next page of data.

---

#### **c. Mutations (Updating Data)**
Use the `useMutation` hook to create, update, or delete data.

#### **Example: Adding a Post**
```jsx
import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const fetchPosts = async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

const addPost = async (newPost) => {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newPost),
  });
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

function Posts() {
  const queryClient = useQueryClient();
  const { data, isLoading, isError, error } = useQuery(['posts'], fetchPosts);
  const mutation = useMutation(addPost, {
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries(['posts']);
    },
  });

  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    mutation.mutate({ title, body: 'New post', userId: 1 });
    setTitle('');
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a post"
        />
        <button type="submit">Add Post</button>
      </form>
      <ul>
        {data.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Posts />
    </div>
  );
}

export default App;
```

#### **Explanation**
- **`useMutation`**: Handles data updates.
- **`onSuccess`**: Invalidates the `posts` query to refetch data after a mutation.

---

### **5. Devtools**
React Query provides **Devtools** for debugging and monitoring queries.

#### **Install Devtools**
```bash
npm install @tanstack/react-query-devtools
```

#### **Enable Devtools**
```jsx
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Posts />
      <ReactQueryDevtools initialIsOpen={false} />
    </div>
  );
}
```

---

### **6. Best Practices**
- **Use Unique Query Keys**: Ensure each query has a unique key for proper caching.
- **Leverage Caching**: React Query caches data automatically, so avoid unnecessary refetches.
- **Optimistic Updates**: Use `onMutate` in mutations for a smoother UX.

---

### **7. Next Steps**
- Explore **React Query’s official docs**: [https://tanstack.com/query](https://tanstack.com/query)
- Combine React Query with **React Router** for route-based data fetching.
- Use **Suspense** for declarative loading states.

## React Query Devtools

**React Query Devtools** is a powerful tool for debugging and monitoring your queries and mutations in real-time. It provides a visual interface to inspect the state of your queries, including their data, loading status, errors, and caching behavior.

In this guide, we'll explore how to set up and use **React Query Devtools** to debug and monitor your queries effectively.

---

### **1. Installation**
Install the React Query Devtools package:
```bash
npm install @tanstack/react-query-devtools
# or
yarn add @tanstack/react-query-devtools
```

---

### **2. Setting Up Devtools**
Wrap your app with the `ReactQueryDevtools` component to enable the Devtools.

#### **index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import App from './App';

// Create a QueryClient instance
const queryClient = new QueryClient();

ReactDOM.render(
  <QueryClientProvider client={queryClient}>
    <App />
    <ReactQueryDevtools initialIsOpen={false} />
  </QueryClientProvider>,
  document.getElementById('root')
);
```

#### **Explanation**
- **`ReactQueryDevtools`**: Adds a Devtools panel to your app.
- **`initialIsOpen`**: Controls whether the Devtools panel is open by default.

---

### **3. Using Devtools**
Once set up, you can access the Devtools by clicking the **React Query logo** in the bottom-left corner of your app.

#### **Features of Devtools**
1. **Query Explorer**:
   - View all active queries and their status (`loading`, `error`, `success`).
   - Inspect query data, error messages, and metadata.

2. **Mutation Explorer**:
   - Monitor active mutations and their status.

3. **Cache Viewer**:
   - Inspect the cached data for each query.

4. **Query Actions**:
   - Refetch queries manually.
   - Invalidate queries to trigger refetches.
   - Remove queries from the cache.

---

### **4. Example: Debugging Queries**
Let’s create an example app and use Devtools to debug its queries.

#### **App.js**
```jsx
import React from 'react';
import { useQuery } from '@tanstack/react-query';

// Fetch data from an API
const fetchPosts = async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

function Posts() {
  const { data, error, isLoading, isError } = useQuery(['posts'], fetchPosts);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

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
      <Posts />
    </div>
  );
}

export default App;
```

#### **Using Devtools**
1. Open the Devtools panel by clicking the React Query logo.
2. Inspect the `posts` query:
   - Check its status (`loading`, `success`, or `error`).
   - View the fetched data.
   - Refetch the query manually.

---

### **5. Debugging Mutations**
You can also use Devtools to monitor mutations.

#### **Example: Adding a Post**
```jsx
import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const fetchPosts = async () => {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

const addPost = async (newPost) => {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(newPost),
  });
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

function Posts() {
  const queryClient = useQueryClient();
  const { data, isLoading, isError, error } = useQuery(['posts'], fetchPosts);
  const mutation = useMutation(addPost, {
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries(['posts']);
    },
  });

  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    mutation.mutate({ title, body: 'New post', userId: 1 });
    setTitle('');
  };

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a post"
        />
        <button type="submit">Add Post</button>
      </form>
      <ul>
        {data.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Posts</h1>
      <Posts />
      <ReactQueryDevtools initialIsOpen={false} />
    </div>
  );
}

export default App;
```

#### **Using Devtools**
1. Open the Devtools panel.
2. Go to the **Mutations** tab to monitor the `addPost` mutation.
3. Inspect the mutation status (`idle`, `loading`, `success`, or `error`).

---

### **6. Advanced Features**
- **Query Invalidation**: Use the Devtools to manually invalidate queries and trigger refetches.
- **Cache Manipulation**: Remove or update cached data directly from the Devtools.
- **Network Simulation**: Simulate slow networks or errors to test your app’s resilience.

---

### **7. Best Practices**
- Use Devtools during development to debug and optimize your queries.
- Monitor query performance and caching behavior.
- Test error handling and retry mechanisms.

---

### **8. Next Steps**
- Explore **React Query’s official docs**: [https://tanstack.com/query](https://tanstack.com/query)
- Combine Devtools with **React Query’s suspense mode** for advanced debugging.
- Use Devtools to optimize query performance in production.

Happy debugging! 🚀