# tr command (From ChatGPT)

---

### 1. Convert lowercase → uppercase

```bash
echo "hello world" | tr 'a-z' 'A-Z'
```

**Output:**

```
HELLO WORLD
```

---

### 2. Convert uppercase → lowercase

```bash
echo "HELLO" | tr 'A-Z' 'a-z'
```

---

### 3. Replace characters

Replace spaces with underscores:

```bash
echo "hello world test" | tr ' ' '_'
```

**Output:**

```
hello_world_test
```

---

### 4. Delete characters

Remove all digits:

```bash
echo "abc123xyz" | tr -d '0-9'
```

**Output:**

```
abcxyz
```

---

### 5. Remove newline characters

```bash
echo -e "line1\nline2" | tr -d '\n'
```

**Output:**

```
line1line2
```

---

### 6. Squeeze repeated characters (`-s`)

Collapse multiple spaces into one:

```bash
echo "hello    world" | tr -s ' '
```

**Output:**

```
hello world
```

---

### 7. Replace multiple characters at once

```bash
echo "abcxyz" | tr 'abc' '123'
```

**Output:**

```
123xyz
```

---

### 8. Keep only certain characters (inverse delete)

Keep only letters:

```bash
echo "abc123!@#" | tr -cd 'a-zA-Z'
```

**Output:**

```
abc
```

---

### 9. ROT13 encoding (simple cipher)

```bash
echo "hello" | tr 'a-zA-Z' 'n-za-mN-ZA-M'
```

**Output:**

```
uryyb
```

---

If you meant something else by “tr” (like Terraform, table row in HTML, etc.), tell me and I’ll switch gears.
