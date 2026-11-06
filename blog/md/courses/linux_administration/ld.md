# LD (gcc linker)

`ld` is the **GNU linker** in Linux, responsible for linking object files (`.o`) and libraries to produce an executable or another object file. It is usually called by the compiler (e.g., `gcc` or `clang`) rather than being used directly.

## **What `ld` Does**

1. **Combines multiple object files** (`.o`) into a single executable.
2. **Resolves symbol references** across files.
3. **Links against libraries** (static `.a` or shared `.so`).
4. **Assigns addresses** to symbols and sections.
5. **Produces an output binary** (executable or another object file).

## **Basic Usage**

```sh
ld -o output_file input_files.o
```

However, `ld` is a **low-level** tool. Typically, you'd use `gcc` or `clang`, which internally call `ld`:

```sh
gcc -o my_program file1.o file2.o -lmylib
```

This automatically invokes `ld` with the correct system libraries.

## **Common `ld` Options**

- `-o <file>`: Specifies output file name.
- `-r`: Generates a relocatable object file instead of an executable.
- `-L<dir>`: Adds a directory to the library search path.
- `-l<lib>`: Links with a library (e.g., `-lm` for `libm.so`).
- `-T <script>`: Uses a custom linker script.

## **Example: Manually Linking**

Compile object files:

```sh
gcc -c file1.c file2.c
```

Manually link:

```sh
ld -o my_program file1.o file2.o -lc
```

(`-lc` links with the C standard library.)

## LD usage in assembly

Please use the following steps on my computer to create a file called `hello.s`.

```assembly
xiaofengli@xiaofenglx:~/git/assembly$ cat hello.s 
global _start

section .text

_start:
  mov rax, 1        ; write(
  mov rdi, 1        ;   STDOUT_FILENO,
  mov rsi, msg      ;   "Hello, world!\n",
  mov rdx, msglen   ;   sizeof("Hello, world!\n")
  syscall           ; );

  mov rax, 60       ; exit(
  mov rdi, 0        ;   EXIT_SUCCESS
  syscall           ; );

section .rodata
  msg: db "Hello, world!", 10
  msglen: equ $ - msg
```

Please try the following in your computer and use the `ld` command to link the objects and libs files to finalize the binary for use.

```shell
xiaofengli@xiaofenglx:~/git/assembly$ nasm -f elf64 -o hello.o hello.s
xiaofengli@xiaofenglx:~/git/assembly$ ls
hello.o  hello.s
xiaofengli@xiaofenglx:~/git/assembly$ ld -o hello hello.o
xiaofengli@xiaofenglx:~/git/assembly$ ls
hello  hello.o	hello.s
xiaofengli@xiaofenglx:~/git/assembly$ ./hello 
Hello, world!
```

Another loop exmaple in assemply,

```nasm
section .text
   global _start        ;must be declared for using gcc

_start:                 ;tell linker entry point
   mov ecx,10
   mov eax, '1'

l1:
   mov [num], eax
   mov eax, 4
   mov ebx, 1
   push rcx

   mov ecx, num
   mov edx, 1
   int 0x80

   mov eax, [num]
   sub eax, '0'
   inc eax
   add eax, '0'
   pop rcx
   loop l1

   mov eax,1             ;system call number (sys_exit)
   int 0x80              ;call kernel
section .bss
num resb 1
```

Output should look like this,

```shell
xiaofengli@xiaofenglx:~/git/assembly$ nasm -f elf64 -o loop.o loop.s 
xiaofengli@xiaofenglx:~/git/assembly$ ld -o loop loop.o
xiaofengli@xiaofenglx:~/git/assembly$ ./loop
123456789
```

## Ref

- https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/x64-architecture

- https://www.tutorialspoint.com/assembly_programming/assembly_loops.htm