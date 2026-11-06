# Typescript Training

## Origin

TypeScript (abbreviated as TS) is a free and open-source high-level programming language developed by Microsoft that adds static typing with optional type annotations to JavaScript. It is designed for the development of large applications and transpiles to JavaScript.

TypeScript may be used to develop JavaScript applications for both client-side and server-side execution (as with Node.js, Deno or Bun). Multiple options are available for transpilation. The default TypeScript Compiler can be used, or the Babel compiler can be invoked to convert TypeScript to JavaScript.

TypeScript supports definition files that can contain type information of existing JavaScript libraries, much like C++ header files can describe the structure of existing object files. This enables other programs to use the values defined in the files as if they were statically typed TypeScript entities. There are third-party header files for popular libraries such as jQuery, MongoDB, and D3.js. TypeScript headers for the Node.js library modules are also available, allowing development of Node.js programs within TypeScript.

## Release History (Skipped)

Please refer to wikipedia or its own website for more details.

## Features

TypeScript adds the following syntax extensions to JavaScript:

* Static Typing

Type annotation, inference and type checking.

* Interfaces

Interfaces define the structure of objects, ensuring that objects adhere to a specific contract.

* Generics, Tuples and other language supports

* Namespaces and modules

Modules help organize code into logical units, making it easier to manage and reuse code.

* Explicit Resource Management

* Transpilation

TypeScript code is transpiled into plain JavaScript, which can run on any browser or JavaScript engine.

## Linting tools

TSLint scans TypeScript code for conformance to a set of standards and guidelines. ESLint, a standard JavaScript linter, also provided some support for TypeScript via community plugins. However, ESLint's inability to leverage TypeScript's language services precluded certain forms of semantic linting and program-wide analysis. In early 2019, the TSLint team announced the linter's deprecation in favor of typescript-eslint, a joint effort of the TSLint, ESLint and TypeScript teams to consolidate linting under the ESLint umbrella for improved performance, community unity and developer accessibility.

## Quick Guide

* **Installation**

`npm install -g typescript`

* **Create a TypeScript file (e.g., app.ts):**

```javascript
 function greet(name: string): string {
       return `Hello, ${name}!`;
   }

   const message = greet("John"); 
   console.log(message); 
<<<<<<< HEAD
```

## Configure a TypeScript project with Reactj

To configure a TypeScript project with React, follow these steps:

### Step 1: Install Node.js

First, ensure that you have Node.js installed. You can download it from [here](https://nodejs.org/).

### Step 2: Create a New React Project

To create a new React project with TypeScript support, you can use `create-react-app` with the `--template typescript` flag. This command will create a React project with TypeScript preconfigured.

```bash
npx create-react-app my-app --template typescript
```

This will create a new folder named `my-app` with all the necessary configuration files for a TypeScript-React app.

### Step 3: Install Dependencies

If you are adding TypeScript to an existing React project, you can install the necessary dependencies:

```bash
npm install typescript @types/react @types/react-dom
```

### Step 4: TypeScript Configuration (Optional)

If the `tsconfig.json` file isn't automatically created (for example, if you're adding TypeScript to an existing project), create it manually at the root of your project. You can generate a `tsconfig.json` by running:

```bash
npx tsc --init
```

Here’s a basic `tsconfig.json` configuration for a React project:

```json
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "esnext"],
    "jsx": "react-jsx",
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "node",
    "module": "esnext"
  }
}
```

### Step 5: Rename Files

Rename your component files from `.js` to `.tsx`. React components that use JSX must be in `.tsx` files for TypeScript to parse them correctly.

For example:
- Rename `App.js` to `App.tsx`
- Rename any other component files that use JSX to `.tsx`

### Step 6: Writing TypeScript Code

Now you can start using TypeScript features in your React components. Here's an example of a simple React component with TypeScript:

```tsx
import React, { FC, useState } from 'react';

interface AppProps {
  message: string;
}

const App: FC<AppProps> = ({ message }) => {
  const [count, setCount] = useState<number>(0);

  return (
    <div>
      <h1>{message}</h1>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
    </div>
  );
};

export default App;
```

In this example:

- `FC<AppProps>` specifies that the component is a functional component with `AppProps` as its props type.
- `useState<number>(0)` explicitly declares that the state is of type `number`.

### Step 7: Run the App

You can now run your TypeScript + React app:

```bash
npm start
```

This will start the development server, and you can view your app in the browser.

---

That’s it! You’ve successfully configured TypeScript with React. Feel free to customize the project and start adding more complex components.


