# ReactJs Basics

ReactJS is a popular JavaScript library for building user interfaces, particularly for single-page applications. Below is a beginner-friendly tutorial to help you get started with ReactJS.

## Key Takeaways

* Installation and setup projects
* Component
* Adding styling or Import CSS
* Expression and embedded expression
* Using props
* State and hooks
* Handling events
* Build and deploy

---

### **1. Setting Up Your Environment**
Before you start coding, you need to set up your development environment.

#### **Install Node.js and npm**
- Download and install [Node.js](https://nodejs.org/).
- npm (Node Package Manager) is included with Node.js.

#### **Create a React App**
Use the `create-react-app` tool to set up a new React project:
```bash
npx create-react-app my-react-app
cd my-react-app
npm start
```
This will start a development server, and you can view your app at `http://localhost:3000`.

---

### **2. Understanding the Project Structure**
After creating your app, you’ll see the following structure:
```
my-react-app/
├── node_modules/
├── public/
│   ├── index.html
│   └── ...
├── src/
│   ├── App.js
│   ├── index.js
│   └── ...
├── package.json
└── ...
```
- **`public/index.html`**: The main HTML file.
- **`src/index.js`**: The entry point for your React app.
- **`src/App.js`**: The main component where you’ll write your code.

---

### **3. Writing Your First Component**
React is all about components. Let’s create a simple component.

#### **Edit `App.js`**
Replace the content of `src/App.js` with the following:
```jsx
import React from 'react';

function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
      <p>Welcome to your first React app.</p>
    </div>
  );
}

export default App;
```

#### **Run the App**
Save the file, and your browser should automatically update to show:
```
Hello, React!
Welcome to your first React app.
```

---

### **4. Understanding JSX**
JSX is a syntax extension for JavaScript that allows you to write HTML-like code in your React components.

Example:
```jsx
const element = <h1>Hello, World!</h1>;
```

#### **Embedding Expressions**
You can embed JavaScript expressions inside JSX using curly braces `{}`:
```jsx
const name = "John";
const element = <h1>Hello, {name}!</h1>;
```

---

### **5. Adding Styles**
You can add styles to your components using CSS.

#### **Create a CSS File**
Create a file named `App.css` in the `src` folder:
```css
h1 {
  color: blue;
}

p {
  font-size: 18px;
}
```

#### **Import the CSS File**
Import the CSS file in `App.js`:
```jsx
import React from 'react';
import './App.css';

function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
      <p>Welcome to your first React app.</p>
    </div>
  );
}

export default App;
```

---

### **6. Using Props**
Props (short for properties) allow you to pass data from a parent component to a child component.

#### **Create a New Component**
Create a new file `Greeting.js` in the `src` folder:
```jsx
import React from 'react';

function Greeting(props) {
  return <h2>Hello, {props.name}!</h2>;
}

export default Greeting;
```

#### **Use the Component in `App.js`**
Update `App.js` to use the `Greeting` component:
```jsx
import React from 'react';
import './App.css';
import Greeting from './Greeting';

function App() {
  return (
    <div>
      <h1>Hello, React!</h1>
      <p>Welcome to your first React app.</p>
      <Greeting name="Alice" />
      <Greeting name="Bob" />
    </div>
  );
}

export default App;
```

---

### **7. State and Hooks**
State allows you to manage data that changes over time. React provides the `useState` hook for this purpose.

#### **Add State to `App.js`**
Update `App.js` to include a button that increments a counter:
```jsx
import React, { useState } from 'react';
import './App.css';
import Greeting from './Greeting';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>Hello, React!</h1>
      <p>Welcome to your first React app.</p>
      <Greeting name="Alice" />
      <Greeting name="Bob" />
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default App;
```

---

### **8. Handling Events**
React uses camelCase for event handlers (e.g., `onClick`, `onChange`).

Example:
```jsx
<button onClick={() => alert('Button clicked!')}>Click Me</button>
```

---

### **9. Fetching Data**
You can use the `useEffect` hook to fetch data from an API.

#### **Example: Fetching Data**
Update `App.js` to fetch and display data:
```jsx
import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      <h1>Posts</h1>
      <ul>
        {data.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

---

### **10. Deploying Your App**
To deploy your app, build it for production:
```bash
npm run build
```
Then, upload the contents of the `build` folder to your hosting service (e.g., Netlify, Vercel, GitHub Pages).

---

### **Next Steps**
- Learn about **React Router** for navigation.
- Explore **state management** with Redux or Context API.
- Build more complex components and apps.

Happy coding! 🚀