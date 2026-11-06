`awk` is a powerful text-processing tool in Linux—great for filtering, transforming, and reporting on structured text (like logs, CSVs, etc.). Here are practical examples from simple → more useful.

---

## 1. Print specific columns

```bash
echo "Alice 30\nBob 25" | awk '{print $1}'
```

**Output:**

```
Alice
Bob
```

Print multiple columns:

```bash
awk '{print $1, $2}' file.txt
```

---

## 2. Use a custom delimiter (`-F`)

For CSV:

```bash
echo "Alice,30,NY" | awk -F',' '{print $1, $3}'
```

**Output:**

```
Alice NY
```

---

## 3. Filter rows (conditions)

Print only lines where age > 25:

```bash
echo -e "Alice 30\nBob 25" | awk '$2 > 25'
```

**Output:**

```
Alice 30
```

---

## 4. Add calculations

```bash
echo -e "A 10\nB 20" | awk '{print $1, $2*2}'
```

**Output:**

```
A 20
B 40
```

---

## 5. Built-in variables

* `$0` → whole line
* `$1, $2...` → fields
* `NF` → number of fields
* `NR` → line number

Example:

```bash
awk '{print NR, $0}' file.txt
```

---

## 6. Print last column

```bash
awk '{print $NF}' file.txt
```

---

## 7. Sum a column

```bash
echo -e "10\n20\n30" | awk '{sum += $1} END {print sum}'
```

**Output:**

```
60
```

---

## 8. BEGIN and END blocks

```bash
awk 'BEGIN {print "Start"} {print $1} END {print "Done"}' file.txt
```

---

## 9. Pattern matching

Print lines containing "error":

```bash
awk '/error/' logfile.txt
```

---

## 10. Combine condition + print

```bash
awk '$3 == "ERROR" {print $1, $2}' logfile.txt
```

---

## 11. Format output (like printf)

```bash
awk '{printf "Name: %s Age: %d\n", $1, $2}' file.txt
```

---

## 12. Replace text in a column

```bash
echo "apple orange" | awk '{$2="banana"; print}'
```

---

## 13. Count lines

```bash
awk 'END {print NR}' file.txt
```

---

## 14. Remove duplicate lines

```bash
awk '!seen[$0]++' file.txt
```

---

## 15. Process a real log (common use case)

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -nr
```

👉 Counts requests per IP.

---

If you want, I can show:

* **awk for Kubernetes logs / DevOps use cases**
* **awk vs sed vs grep (when to use what)**
* or help write a real script for your Jenkins/K8s setup 👍
