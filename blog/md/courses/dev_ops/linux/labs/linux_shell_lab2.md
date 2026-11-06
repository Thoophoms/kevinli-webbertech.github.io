# # Linux Shell Programming - Lab 2 - `grep`, `awk`, `sed`, `ps`, `cut`, and `join`

If you ever wonder what would be the most useful tools or commands in linux to perform a day-to-day devOps job. 
Here they are. Today we will talk about and practice some commands with solid examples.

Combining commands like `grep`, `awk`, `sed`, `ps`, `cut`, and `join` is where the true power of the Linux command line shines. These "one-liners" allow you to perform complex data extraction and transformation with incredible efficiency.

Here are some practical, useful examples that demonstrate their combination.

### 1. Process Analysis with `ps`, `grep`, `awk`, and `cut`

**Goal:** Find the PID and command of all processes owned by the user `www-data` and calculate their total memory usage (RSS).

```bash
ps -u www-data -o pid,rss,comm | awk '{print $1, $2, $3} NR>1 {sum+=$2} END {print "Total RSS: " sum " kB"}'
```

*   `ps -u www-data -o pid,rss,comm`: `ps` lists processes for user `www-data`, outputting only the PID, Resident Set Size (memory), and command.
*   `awk '{print $1, $2, $3}`: `awk` prints the three columns neatly.
*   `NR>1 {sum+=$2}`: For all rows after the header (`NR>1`), add the value of the second column (RSS) to a variable `sum`.
*   `END {print "Total RSS: " sum " kB"}`: After processing all lines, print the total memory usage.

**Goal:** Find the process ID of a specific service (e.g., `nginx`) and kill it gracefully.

```bash
kill -TERM $(ps aux | grep '[n]ginx: master' | awk '{print $2}')
```

*   `ps aux`: Lists all processes.
*   `grep '[n]ginx: master'`: The clever `[n]` trick. It searches for `ginx: master` but the pattern `[n]ginx` prevents the `grep` command itself from appearing in the results. This is a classic trick to avoid `grep | grep -v grep`.
*   `awk '{print $2}'`: Extract just the second column, which is the PID.
*   `$(...)`: Command substitution. The output of the command inside (the PID) becomes the argument to `kill -TERM`.

---

### 2. Text Processing & Data Extraction with `awk`, `sed`, and `cut`

**Goal:** From a CSV file [`data.csv`](https://kevinli-webbertech.github.io/blog/md/courses/dev_ops/linux/labs/data.csv), extract the second and fifth fields, change the delimiter from a comma to a pipe `|`, and save it to a new file.

**data.csv:**
```
id,name,department,city,email,salary
101,Alice Johnson,Engineering,New York,alice.johnson@example.com,95000
102,Bob Smith,Marketing,Chicago,bob.smith@example.com,72000
103,Eve Davis,Engineering,San Francisco,eve.davis@example.com,105000
104,Mallory Brown,Sales,Austin,mallory.brown@example.com,68000
105,Charlie Wilson,Engineering,Seattle,charlie.wilson@example.com,98000
106,Dana Lee,Human Resources,Chicago,dana.lee@example.com,64000
107,Frank Miller,Marketing,New York,frank.miller@example.com,71000
108,Grace Kim,Finance,Boston,grace.kim@example.com,89000
109,Heidi Clark,Sales,Austin,heidi.clark@example.com,66000
110,Ivan Rodriguez,Engineering,Denver,ivan.rodriguez@example.com,102000
```

```bash
awk -F',' '{print $2 "|" $5}' data.csv > new_data.txt
# Or using cut (if fields are in order and no complex processing is needed)
cut -d',' -f2,5 data.csv | sed 's/,/|/g' > new_data.txt
```

*   `awk -F','`: Set the input field separator to a comma.
*   `cut -d',' -f2,5`: `cut` uses the comma delimiter to select fields 2 and 5.
*   `sed 's/,/|/g'`: `sed` substitutes every comma (` ,`) with a pipe (`|`). The `g` means "global," for all occurrences on the line.
*   The output (`name|email`) is exactly the second (`name`) and fifth (`email`) fields from `data.csv`.

**Goal:** Get the IP address from a system command like `ip a` (assuming `eth0`).

```bash
ip a show eth0 | grep 'inet ' | awk '{print $2}' | cut -d'/' -f1
# Alternative, using only awk
ip a show eth0 | awk '/inet / {split($2, a, "/"); print a[1]}'
```

*   `ip a show eth0`: Shows network info for interface `eth0`.
*   `grep 'inet '`: Finds the line containing an IPv4 address.
*   `awk '{print $2}'`: Prints the second field (e.g., `192.168.1.10/24`).
*   `cut -d'/' -f1`: Splits that field using the `/` delimiter and takes the first part (`192.168.1.10`).
*   The `awk`-only alternative uses the `split()` function to achieve the same result.

---

### 3. Joining Data from Different Sources with `join`

**Goal:** You have two files. `users.txt` contains user IDs and names, and `emails.txt` contains user IDs and emails. Join them to create a combined list.

**users.txt:**
```
101 alice
102 bob
103 eve
```

**emails.txt:**
```
101 alice@example.com
102 bob@company.org
104 mallory@test.net
```

```bash
join -a1 -a2 -o 0,1.2,2.2 <(sort users.txt) <(sort emails.txt)
```
**Output:**
```
101 alice alice@example.com
102 bob bob@company.org
103 eve
104  mallory@test.net
```

*   `join`: The core command. It joins two files on a common field (the first field by default).
*   **CRITICAL:** Input files **must be sorted** on the join field. We use `<(sort ...)` to sort them on the fly.
*   `-a1 -a2`: Print unpairable lines from both file 1 (`users.txt`) and file 2 (`emails.txt`). Eve has no email, Mallory has no user record.
*   `-o 0,1.2,2.2`: Format the output. `0` is the join field (user ID), `1.2` is the second field from the first file (name), `2.2` is the second field from the second file (email).

---

### 4. System Monitoring & Log Analysis

**Goal:** Parse `/etc/passwd` to get a list of all users and their default shell, but only for interactive shells (e.g., not `/bin/false` or `/usr/sbin/nologin`).

```bash
cut -d: -f1,7 /etc/passwd | grep -vE '(false|nologin)$' | sort
```

*   `cut -d: -f1,7`: `cut` uses the colon `:` as a delimiter to select fields 1 (username) and 7 (shell).
*   `grep -vE '(false|nologin)$'`: `-v` inverts the match (finds lines that do NOT match). `-E` enables extended regex. The pattern `(false|nologin)$` matches lines that *end with* (`$`) either "false" or "nologin".
*   `sort`: Sorts the final list alphabetically.

**Goal:** Find the top 5 most frequent error messages in the last 1000 lines of a log file.

```bash
tail -1000 /var/log/syslog | grep -i error | sort | uniq -c | sort -nr | head -5
```

*   `tail -1000`: Get the last 1000 lines of the file.
*   `grep -i error`: Filter for lines containing the word "error" (case-insensitive).
*   `sort`: Sort the lines. This is required for `uniq -c` to work correctly.
*   `uniq -c`: Count the occurrences of each unique line.
*   `sort -nr`: Sort the results numerically (`-n`) in reverse order (`-r`), so the highest count is first.
*   `head -5`: Show only the top 5 results.

These examples demonstrate the philosophy of "building pipelines." You start with a command that generates data, then you pipe (`|`) its output to a series of filters that progressively shape it into the exact information you need.