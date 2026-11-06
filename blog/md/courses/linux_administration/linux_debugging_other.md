### **Other GCC Debugging Tools in Linux**

Apart from `gdb`, there are several powerful tools for debugging C programs compiled with `gcc`:

---

## **1. `valgrind` (Memory Debugging)**
`valgrind` helps detect memory leaks, invalid memory access, and uninitialized variables.

### **Installation:**

```bash
sudo apt install valgrind  # Debian/Ubuntu
sudo yum install valgrind  # RHEL/CentOS
```

### **Usage:**

```bash
valgrind --leak-check=full ./program
```

This detects memory leaks and displays problematic memory access.

---

## **2. `strace` (System Call Tracing)**
`strace` monitors system calls made by a program.

### **Usage:**

```bash
strace ./program
```

or to save output:

```bash
strace -o output.txt ./program
```

This helps diagnose file access issues, missing libraries, and system call failures.

---

## **3. `ltrace` (Library Call Tracing)**
`ltrace` tracks dynamic library calls used by a program.

### **Usage:**

```bash
ltrace ./program
```

It helps debug dynamically linked functions and library calls.

---

## **4. `addr2line` (Find Code Location of an Address)**

If a segmentation fault gives an address (e.g., `0x400123`), you can map it to a line in your code.

### **Usage:**

```bash
addr2line -e program 0x400123
```

This points to the exact line in the source code.

---

## **5. `gprof` (Performance Profiling)**

`gprof` helps identify slow parts of a program by measuring execution time of functions.

### **Compile with profiling support:**

```bash
gcc -pg program.c -o program
```

### **Run the program and analyze:**

```bash
./program
gprof program gmon.out > analysis.txt
```

This generates a performance profile.

---

## **6. `sanitizers` (Runtime Error Detection)**

GCC has built-in sanitizers for runtime debugging.

### **Enable AddressSanitizer for memory errors:**

```bash
gcc -fsanitize=address -g program.c -o program
./program
```

### **Enable Undefined Behavior Sanitizer:**

```bash
gcc -fsanitize=undefined -g program.c -o program
./program
```

These sanitizers help catch **buffer overflows, memory leaks, and undefined behavior**.