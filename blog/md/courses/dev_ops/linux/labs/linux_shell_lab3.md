# Linux Shell Programming - Lab 3 - pipe, redirect and file descriptors

This is a fundamental and powerful concept in Linux/Unix. Understanding file descriptors, pipes, and redirection is key to mastering the command line.

### 1. The Core Concept: File Descriptors (FDs)

Think of a **File Descriptor** as a number that the operating system uses to keep track of open "files". In Linux, *everything is a file*: not just text files, but also hardware devices, pipes, and network sockets.

By default, every command run from the terminal has three standard data streams connected to it:

| FD Number | Name          | Description                                                                 | Default Target |
| :-------- | :------------ | :-------------------------------------------------------------------------- | :------------- |
| **0**     | Standard Input (stdin)  | The stream from which a program reads its input.                              | Your keyboard  |
| **1**     | Standard Output (stdout) | The stream to which a program writes its normal output.                       | Your terminal  |
| **2**     | Standard Error (stderr) | The stream to which a program writes error messages.                          | Your terminal  |

The key idea is that we can **redirect** these streams away from their default targets.

---

### 2. Redirection: Controlling Where Data Goes

Redirection is all about changing the source of input or the destination of output.

| Operator      | Name                          | Effect                                                                 |
| :------------ | :---------------------------- | :---------------------------------------------------------------------- |
| `>`           | Output redirect (overwrite)   | Sends **stdout** to a file, **overwriting** it.                        |
| `>>`          | Output redirect (append)      | Sends **stdout** to a file, **appending** to the end.                  |
| `<`           | Input redirect                | Reads **stdin** from a file instead of the keyboard.                   |
| `2>`          | Error redirect (overwrite)    | Sends **stderr** to a file, **overwriting** it.                        |
| `2>>`         | Error redirect (append)       | Sends **stderr** to a file, **appending** to the end.                  |
| `2>&1`        | Merge stderr into stdout      | Redirects **stderr** to wherever **stdout** is currently going.        |
| `&>`          | Combined redirect (overwrite) | Sends **both stdout and stderr** to a file, **overwriting** it.        |
| `>&`          | Combined redirect (alias)     | Same as `&>`; sends **both stdout and stderr** to a file.              |
| `&>>`         | Combined redirect (append)    | Sends **both stdout and stderr** to a file, **appending** to the end.  |

#### Output Redirection (`>` and `>>`)

*   `command > file`
    *   **Action:** Redirects **stdout** of `command` to `file`.
    *   **Effect:** **Overwrites** the file if it exists, or creates it if it doesn't.
    *   **Example:** `ls > list.txt` (Saves the directory listing to `list.txt`, wiping out its previous contents.)

*   `command >> file`
    *   **Action:** Redirects **stdout** of `command` to `file`.
    *   **Effect:** **Appends** to the end of the file.
    *   **Example:** `date >> log.txt` (Adds the current date to the end of `log.txt`.)

#### Input Redirection (`<`)

*   `command < file`
    *   **Action:** Redirects **stdin** to read from `file` instead of the keyboard.
    *   **Example:** `sort < unsorted_list.txt` (The `sort` command gets its input from the file.)

#### Error Redirection (`2>` and `2>>`)

Since FD 2 is stderr, we use its number to redirect it specifically.

*   `command 2> error_log.txt`
    *   **Action:** Redirects **stderr** to `error_log.txt`.
    *   **Example:** `rm nonexistent_file.txt 2> errors.log` (The error message goes to the file, not your screen.)

#### Advanced Redirection: Combining & File Descriptor Gymnastics

*   **Redirect both stdout and stderr to the same place:**
    *   `command &> file` (Bash preferred shorthand)
    *   `command > file 2>&1` (The classic, universally understood method)
        *   **Explanation:** First, `> file` redirects FD1 (stdout) to the `file`.
        *   Then, `2>&1` means "redirect FD2 (stderr) to wherever FD1 is currently going." Since FD1 is going to the file, FD2 will follow.

*   **Redirect stdout and stderr to different places:**
    *   `command > output.log 2> error.log`
    *   **Perfect for scripts:** Normal output is saved, errors are logged separately.

*   **Redirect stderr to stdout, and then pipe stdout:**
    *   `command 2>&1 | less`
    *   **Explanation:** First, `2>&1` sends stderr to the same place as stdout (the terminal, for now). Then, the pipe `|` sends that combined output to `less`.

#### Example: A Script That Writes to Both stdout and stderr

Save the following as `output_test.sh`. It writes normal messages to **stdout**, an error message to **stderr**, and then runs a command (`ls` on a nonexistent path) that itself produces a real **stderr** error.

```bash
#!/bin/bash

echo "This message goes to STDOUT"

echo "This message goes to STDERR" >&2

echo "Another STDOUT message"

ls /path/that/does/not/exist

echo "Script finished"
```

Save it as `output_test.sh`, then run:

```
chmod +x output_test.sh
./output_test.sh
```

Now redirect stdout and stderr into separate files:

```
./output_test.sh > stdout.log 2> stderr.log
```

Then:

```
cat stdout.log
cat stderr.log
```

You can also redirect both into one file:

```
./output_test.sh > combined.log 2>&1
```

---

### 3. Pipes (`|`): Connecting Streams Between Commands

A **pipe** is one of the most brilliant ideas in Unix. It takes the **stdout** of one command and connects it to the **stdin** of the next command.

*   **Syntax:** `command1 | command2 | command3`
*   **What happens:** `command1` runs, and its output is not printed to the screen. Instead, it is instantly fed as the input to `command2`. `command2` processes it and sends its own output to `command3`.

**Examples:**
*   `ls -la | grep "myfile"`
    *   `ls` lists all files. Its output is piped to `grep`, which filters it, showing only lines containing "myfile".
*   `ps aux | grep '[n]ginx' | awk '{print $2}'`
    *   `ps` lists all processes. `grep` filters for nginx processes. `awk` extracts just the second column (the PID).

**Crucial Point:** Pipes **only** handle **stdout**. **stderr** is not piped by default and will still print to your terminal, which is why you often see `2>&1` used before a pipe to also catch errors.

```bash
# This will still show errors on your screen
find / -name "*.conf" 2> /dev/null | head -5

# This sends errors to the black hole (/dev/null), so only valid output is piped
find / -name "*.conf" 2> /dev/null | head -5
```

---

### Summary & Mental Model

| Symbol         | Meaning                                                                                          |
| :------------- | :----------------------------------------------------------------------------------------------- |
| `command > file`  | **Replace** `file` with the **stdout** of `command`.                                               |
| `command >> file` | **Append** the **stdout** of `command` to `file`.                                                  |
| `command < file`  | Use `file` as the **stdin** for `command`.                                                         |
| `command 2> file` | **Replace** `file` with the **stderr** of `command`.                                               |
| `command1 | command2`  | The **stdout** of `command1` becomes the **stdin** of `command2`.                                |
| `&>` or `2>&1`   | "And also." Redirect both **stdout** and **stderr** to the same place. Must be used *after* `> file`. |

Think of it like plumbing:
*   **File Descriptors** are different water pipes (0: input pipe, 1: output pipe, 2: overflow/error pipe).
*   **Redirection** (`>`, `<`) is you pointing the end of a pipe into a bucket (a file) or hooking it up to a water source.
*   **Pipes** (`|`) are you connecting the output pipe of one pump (command) directly to the input pipe of the next pump.