# Linux Shell Programming - Lab 1

Learning Linux shell programming (often called "bash scripting" because Bash is the most common shell) is one of the most valuable skills for a developer, system administrator, data scientist, or IT professional. It allows you to automate tasks, combine powerful command-line tools, and control your system efficiently.

Here is a structured learning path, from absolute beginner to advanced.

### The Philosophy
The Unix/Linux shell philosophy is:
*   **Write programs that do one thing and do it well.**
*   **Write programs to work together.**
*   **Write programs to handle text streams, because that is a universal interface.**

Your scripts should follow this: be a glue that connects simple, powerful commands to perform complex tasks.

---

### Phase 1: Foundation - The Basics of Bash

You cannot write scripts if you don't know how to use the shell interactively.

1.  **The Terminal:** Get comfortable with your terminal emulator (e.g., GNOME Terminal, Konsole, iTerm2 on Mac).
2.  **Basic Navigation:**
    *   `pwd` - Print Working Directory (where am I?)
    *   `ls` - List directory contents
    *   `cd` - Change Directory (e.g., `cd /home/user`, `cd ..`, `cd ~`)
    *   `mkdir` - Make Directory
    *   `rmdir` - Remove Directory
    *   `cp` - Copy files and directories
    *   `mv` - Move or rename files and directories
    *   `rm` - Remove files and directories (**Use with extreme caution, especially `rm -rf`**)
3.  **Working with Files:**
    *   `cat` - Concatenate and display file content
    *   `less` or `more` - View file content page by page
    *   `head` / `tail` - Display the first/last part of a file
    *   `nano` / `vim` / `emacs` - Learn a terminal text editor. Start with `nano` for simplicity, then **definitely learn the basics of `vim`** as it's ubiquitous.
4.  **Getting Help:**
    *   `man <command>` - The manual. Your best friend. (e.g., `man ls`)
    *   `<command> --help` - Often a shorter help summary.

---

### Phase 2: Core Scripting Concepts

A shell script is just a text file containing a sequence of these commands.

1.  **Create Your First Script:**
    ```bash
    #!/bin/bash
    # This is a comment. The first line is called the 'shebang' - it tells the system which interpreter to use.
    echo "Hello, World!"
    ```
    *   Save this as `hello.sh`.
    *   Make it executable: `chmod +x hello.sh`
    *   Run it: `./hello.sh`

2.  **Variables:**
    ```bash
    NAME="Alice"
    echo "Hello, $NAME"  # Double quotes allow variable expansion
    echo 'Hello, $NAME'  # Single quotes prevent expansion
    ```

3.  **User Input:**
    ```bash
    echo "What's your name?"
    read NAME
    echo "Hello, $NAME"
    ```

4.  **Control Structures:**
    *   **If/Then/Else:**
        ```bash
        if [ "$NAME" == "Alice" ]; then
          echo "Hello, Alice"
        elif [ "$NAME" == "Bob" ]; then
          echo "Hi, Bob"
        else
          echo "Who are you?"
        fi
        ```
    *   **Loops:**
        ```bash
        # For loop
        for i in {1..5}; do
          echo "Number: $i"
        done

        # While loop
        COUNT=0
        while [ $COUNT -lt 5 ]; do
          echo "Count: $COUNT"
          ((COUNT++))
        done
        ```

5.  **Command Arguments:**
    *   `$0` - Name of the script itself.
    *   `$1`, `$2`, ... `$9` - The first, second, ... ninth argument.
    *   `$@` - All arguments.
    *   `$#` - Number of arguments.
    ```bash
    # ./script.sh arg1 arg2
    echo "Running: $0"
    echo "First arg: $1"
    echo "All args: $@"
    echo "Number of args: $#"
    ```

---

### Phase 3: Intermediate Concepts - The Power of the Shell

1.  **Exit Status:** Every command returns an exit status (`$?`). `0` means success, anything else means an error.
    ```bash
    ls /some/directory
    if [ $? -eq 0 ]; then
      echo "Directory exists."
    else
      echo "Directory not found."
    fi
    ```

2.  **Logical Operators:** `&&` (AND) and `||` (OR)
    ```bash
    # Run command2 only if command1 succeeds
    mkdir /tmp/backup && cp important.file /tmp/backup/

    # Run command2 only if command1 fails
    cp important.file /tmp/backup/ || echo "Backup failed!"
    ```

3.  **Functions:**
    ```bash
    greet() {
      local NAME=$1 # Local variable
      echo "Hello, $NAME"
    }

    greet "Alice"
    greet "Bob"
    ```

4.  **Wildcards & Globbing:** `*` (matches any string), `?` (matches any single character).
    ```bash
    cp *.txt /backup/  # Copy all .txt files
    rm file?.log       # Remove file1.log, file2.log, etc.
    ```

---

### Phase 4: Advanced Topics - Gluing Commands Together

This is where the real power lies.

1.  **Pipes (`|`):** Take the output of one command and use it as the input for the next.
    ```bash
    # Find all .log files, search for the word "error", and count the lines
    find /var/log -name "*.log" -exec cat {} \; | grep -i "error" | wc -l
    ```

2.  **Command Substitution:** `$(command)` - Use the output of a command as a variable.
    ```bash
    TODAY=$(date +%Y-%m-%d)
    echo "Backup created on $TODAY"
    cp important.file "backup-$TODAY.file"
    ```

3.  **Input/Output Redirection:**
    *   `>` - Redirect standard output (overwrite)
    *   `>>` - Redirect standard output (append)
    *   `2>` - Redirect standard error
    *   `&>` - Redirect both standard output and standard error
    ```bash
    ls /tmp > list.txt     # Save output to list.txt
    ls /nonexistent 2> errors.log # Save errors to errors.log
    ls /tmp &> all_output.log # Save everything to all_output.log
    ```

---

### Phase 5: Practice, Practice, Practice

Theory is useless without practice. Here are some project ideas:

1.  **System Admin:**
    *   Write a backup script that tars and compresses a directory, names it with the current date, and copies it to another location.
    *   Write a script that checks disk usage and emails you if it's above 90%.
2.  **Developer:**
    *   Write a script that automates your git add, commit, and push process.
    *   Write a build script that compiles your code and runs tests.
3.  **Data Processing:**
    *   Write a script that downloads a CSV file from the internet, processes it with `awk`/`sed` (see below), and generates a summary report.

### Essential Tools to Learn Alongside Shell Scripting

*   `grep` - Search text using patterns. The workhorse of text filtering.
*   `awk` - A powerful programming language for text processing. Incredible for working with structured data (like CSV files). Start with simple one-liners (`awk '{print $1}'` to print the first column).
*   `sed` - A "stream editor" for filtering and transforming text (e.g., find and replace: `sed 's/find/replace/g'`).
*   `find` - Find files and execute commands on them. Much more powerful than the simple GUI search.

### Resources

*   **Google's Shell Style Guide:** Write clean, readable, and maintainable scripts.
    [https://google.github.io/styleguide/shellguide.html](https://google.github.io/styleguide/shellguide.html)
*   **`bash` man page:** It's massive and contains everything. Use it. (`man bash`)
*   **Advanced Bash-Scripting Guide:** A classic, deep dive into almost every aspect of bash.
    [https://tldp.org/LDP/abs/html/](https://tldp.org/LDP/abs/html/)

Start small, automate one tiny task, and gradually build up to more complex scripts. Good luck