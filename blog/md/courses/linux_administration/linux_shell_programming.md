# Shell Scripting Cheatsheet

---
title: Shell Scripting Cheatsheeet

date: 06/13/2024
---

## variable

```bash
name="John"
echo $name  # see below
echo "$name"
echo "${name}!"
```

Generally quote your variables unless they contain wildcards to expand or command fragments.

```bash
wildcard="*.txt"
options="iv"
cp -$options $wildcard /tmp
```

## String Quotes

```bash
String quotes
name="John"
echo "Hi $name"  #=> Hi John
echo 'Hi $name'  #=> Hi $name
```

## Shell execution

```bash
echo "I'm in $(pwd)"
echo "I'm in `pwd`"  # obsolescent
```

## Strict mode

```bash
set -euo pipefail
IFS=$'\n\t'
```

## Options

`set -o noclobber`  # Avoid overlay files (echo "hi" > foo)

`set -o errexit`    # Used to exit upon error, avoiding cascading errors

`set -o pipefail`   # Unveils hidden failures

`set -o nounset`    # Exposes unset variables

*Glob options*

`shopt -s nullglob`    # Non-matching globs are removed  ('*.foo' => '')

`shopt -s failglob`    # Non-matching globs throw errors

`shopt -s nocaseglob`  # Case insensitive globs

`shopt -s dotglob`     # Wildcards match dotfiles ("*.sh" => ".foo.sh")

`shopt -s globstar`    # Allow ** for recursive matches ('lib/**/*.rb' => 'lib/a/b/c.rb')

Set GLOBIGNORE as a colon-separated list of patterns to be removed from glob matches.

# Conditional Execution

```bash
git commit && git push
git commit || echo "Commit failed"
```

## Brace Expansion
{% raw %}
```
echo {A,B}.js
{A,B}` Same as A B
{A,B}.js Same as A.js B.js
{1..5} Same as 1 2 3 4 5
{{1..3},{7..9}}
```
{% endraw %}

 Same as 1 2 3 7 8 9

*example*

{% raw %}
```bash
xiaofengli@xiaofenglx:~$ echo {1..5}
1 2 3 4 5
xiaofengli@xiaofenglx:~$ echo {{1..5},{6..9}}
1 2 3 4 5 6 7 8 9
```
{% endraw %}

## Loop

**for in loop**

```bash
for i in /etc/rc.*; do
  echo "$i"
done
```

**for in with range**

```bash
for i in {1..5}; do
    echo "Welcome $i"
done
```

**for in with step**

```bash
for i in {5..50..5}; do
    echo "Welcome $i"
done
```

**while loop**

```bash
x=1;
while [ $x -le 5 ]; do
  echo "Hello World"
  ((x=x+1))
done
```

**C-like for loop**

```bash
for ((i = 0 ; i < 100 ; i++)); do
  echo "$i"
done
```

**Read lines from file**

```bash
while read -r line; do
  echo "$line"
done <file.txt
```

## Function

```bash
get_name() {
  echo "John"
}

echo "You are $(get_name)"
```

another example,

```bash
myfunc() {
    echo "hello $1"
}
# Same as above (alternate syntax)
function myfunc {
    echo "hello $1"
}
myfunc "John"
```

**Returning values**

```bash
myfunc() {
    local myresult='some value'
    echo "$myresult"
}
result=$(myfunc)
```

**Raising errors**

```bash
myfunc() {
  return 1
}
if myfunc; then
  echo "success"
else
  echo "failure"
fi
```

**Arguments**

- `$#` Number of arguments
- `$*` All positional arguments (as a single word)
- `$@` All positional arguments (as separate strings)
- `$1` First argument
- `$`_ Last argument of the previous command


## Conditions

**if** and **exit**

* exit code: 0 is success, other integer are errors. This is similar to c language.

* POSIX vs Bash extension:

`[` is POSIX
`[[` is a Bash extension inspired from KornShell

```bash
if [ -z "$1" ]; then
  echo "No parameter";
  exit 22;
fi
```

**if/else**

```bash
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
else
  echo "This never happens"
fi
```

**`$?`**

check exit code,

`echo $?`

## Conditional Testing

Note: stay with double bracket

### String test

`[[ -z STRING ]]` Empty string

`[[ -n STRING ]]` Not empty string

`[[ STRING == STRING ]]` Equal

`[[ STRING != STRING ]]` Not Equal

### Integer test

`[[ NUM -eq NUM ]]` Equal

`[[ NUM -ne NUM ]]` Not equal

`[[ NUM -lt NUM ]]` Less than

`[[ NUM -le NUM ]]` Less than or equal

`[[ NUM -gt NUM ]]` Greater than

`[[ NUM -ge NUM ]]` Greater than or equal

`[[ STRING =~ STRING ]]` Regexp

`(( NUM < NUM ))` Numeric conditions

`[[ -o noclobber ]]` If OPTIONNAME is enabled

`[[ ! EXPR ]]` Not

`[[ X && Y ]]` And

`[[ X || Y ]]` Or

## File Testing

`[[ -f FILE ]]` File

`[[ -d FILE ]]` Directory

`[[ -h FILE ]]` Symlink

`[[ -e FILE ]]` Exists

`[[ -r FILE ]]` Readable

`[[ -w FILE ]]` Writable

`[[ -x FILE ]]` Executable

`[[ -s FILE ]]` Size is > 0 bytes

`[[ FILE1 -nt FILE2 ]]` 1 is more recent than 2

`[[ FILE1 -ot FILE2 ]]` 2 is more recent than 1

`[[ FILE1 -ef FILE2 ]]` Same files

**Examples**


```bash
if [[ -z "$string" ]]; then
  echo "String is empty"
elif [[ -n "$string" ]]; then
  echo "String is not empty"
fi

# Combinations
if [[ X && Y ]]; then
  ...
fi

# Equal
if [[ "$A" == "$B" ]]

# Regex
if [[ "A" =~ . ]]

if (( $a < $b )); then
   echo "$a is smaller than $b"
fi

if [[ -e "file.txt" ]]; then
  echo "file exists"
fi

```

## String slicing

## Arrays

### Defining arrays

```bash
Fruits=('Apple' 'Banana' 'Orange')
Fruits[0]="Apple"
Fruits[1]="Banana"
Fruits[2]="Orange"
```

### Array operations

```bash
Operations
Fruits=("${Fruits[@]}" "Watermelon")    # Push
Fruits+=('Watermelon')                  # Also Push
Fruits=( "${Fruits[@]/Ap*/}" )          # Remove by regex match
unset Fruits[2]                         # Remove one item
Fruits=("${Fruits[@]}")                 # Duplicate
Fruits=("${Fruits[@]}" "${Veggies[@]}") # Concatenate
lines=(`cat "logfile"`)                 # Read from file
```

### Array indexing

Working with arrays

```bash
echo "${Fruits[0]}"           # Element #0
echo "${Fruits[-1]}"          # Last element
echo "${Fruits[@]}"           # All elements, space-separated
echo "${#Fruits[@]}"          # Number of elements
echo "${#Fruits}"             # String length of the 1st element
echo "${#Fruits[3]}"          # String length of the Nth element
echo "${Fruits[@]:3:2}"       # Range (from position 3, length 2)
echo "${!Fruits[@]}"          # Keys of all elements, space-separated
```

Iteration

```bash
for i in "${arrayName[@]}"; do
  echo "$i"
done
```

## Dictionaries

It is an associative array. Just the key is a string.

### Definition

```bash
declare -A sounds
sounds[dog]="bark"
sounds[cow]="moo"
sounds[bird]="tweet"
sounds[wolf]="howl"
```

### Indexing

Working with dictionaries

```bash
echo "${sounds[dog]}" # Dog's sound
echo "${sounds[@]}"   # All values
echo "${!sounds[@]}"  # All keys
echo "${#sounds[@]}"  # Number of elements
unset sounds[dog]     # Delete dog
```

### Iteration

* Iterate over values

```bash
for val in "${sounds[@]}"; do
  echo "$val"
done
```

* Iterate over keys

```bash
for key in "${!sounds[@]}"; do
  echo "$key"
done
```

## Ref

-https://devhints.io/bash
