# **Using `gcc` (GNU Compiler Collection) in Linux**

## Overview

* build binary using gcc
* link external library using gcc
* create a static library in linux
* create a dynamic library in linux

## GCC

`gcc` is the standard compiler for C and C++ programs on Linux. Here’s a quick guide on its usage:

### **1. Compiling a Simple C Program**

Save the following **C program** as `hello.c`:
```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

Compile it using:
```bash
gcc hello.c -o hello
```
Run the compiled program:
```bash
./hello
```

---

### **2. Compiling with Debugging Information (`-g` flag)**

To enable debugging support for `gdb`:
```bash
gcc -g hello.c -o hello
```
Now, you can debug it using:
```bash
gdb ./hello
```

---

### **3. Enabling Optimization (`-O` flags)**
Use optimization levels **O1, O2, O3** for performance:
```bash
gcc -O2 hello.c -o hello
```

---

### **4. Compiling Multiple Files**
If you have multiple source files:
```bash
gcc file1.c file2.c -o myprogram
```

---

### **5. Linking External Libraries**
Example: linking **math library (`-lm`)**:
```bash
gcc mathprog.c -o mathprog -lm
```

---

### **6. Compiling a C++ Program**
For **C++** programs, use `g++`:
```bash
g++ program.cpp -o program
```

---

## **Creating a Static Library Using `gcc` in Linux**

A **static library** in C is a collection of precompiled object files (`.o`) bundled into a single archive (`.a`) that can be linked into programs. Here’s how you can create one:

---

### **1. Create Source Code Files**

Let’s create two simple C files:  
#### **`math_operations.c`**
```c
#include "math_operations.h"

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}
```

#### **`math_operations.h`**
```c
#ifndef MATH_OPERATIONS_H
#define MATH_OPERATIONS_H

int add(int a, int b);
int subtract(int a, int b);

#endif
```

---

### **2. Compile Source Files into Object Files**
```bash
gcc -c math_operations.c -o math_operations.o
```
This generates an object file `math_operations.o`.

---

### **3. Create a Static Library (`.a` File)**
```bash
ar rcs libmath.a math_operations.o
```
- `ar` → Archive command  
- `rcs` → **r**eplace or add, **c**reate if not existing, and **s**ort index  
- `libmath.a` → Output static library  

---

### **4. Compile a Program Using the Static Library**

Create a **main program** using this library:

#### **`main.c`**

```c
#include <stdio.h>
#include "math_operations.h"

int main() {
    int result = add(5, 3);
    printf("Result: %d\n", result);
    return 0;
}
```

Compile with the static library:
```bash
gcc main.c -L. -lmath -o main
```
- `-L.` → Look for libraries in the current directory  
- `-lmath` → Link with `libmath.a`  

Run the program:
```bash
./main
```

---

## **Creating a Dynamic Library in Linux Using `gcc`**

A **dynamic library** (`.so` file) allows programs to load functions at runtime, reducing executable size and allowing updates without recompilation.

---

### **1. Create Source Code for the Library**

Let’s define a simple **math library**:

#### **`math_operations.c`**
```c
#include "math_operations.h"

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}
```

#### **`math_operations.h`**
```c
#ifndef MATH_OPERATIONS_H
#define MATH_OPERATIONS_H

int add(int a, int b);
int subtract(int a, int b);

#endif
```

---

### **2. Compile to Object File (`.o`)**

```bash
gcc -fPIC -c math_operations.c -o math_operations.o
```

- `-fPIC` → Generates **position-independent code** required for shared libraries.

---

### **3. Create the Shared Library (`.so`)**

```bash
gcc -shared -o libmath.so math_operations.o
```

- `-shared` → Creates a shared library.

---

### **4. Using the Dynamic Library in a Program**

Create a **main program** that uses `libmath.so`:

#### **`main.c`**

```c
#include <stdio.h>
#include "math_operations.h"

int main() {
    int result = add(10, 5);
    printf("Addition Result: %d\n", result);
    return 0;
}
```

Compile it by linking to the shared library:

```bash
gcc main.c -L. -lmath -o main
```
- `-L.` → Look in the current directory for `libmath.so`.
- `-lmath` → Links against `libmath.so`.

---

### **5. Run the Program**

Before running, set the library path:
```bash
export LD_LIBRARY_PATH=.
./main
```
or move the library to a standard location:
```bash
sudo mv libmath.so /usr/lib/
./main
```

---
