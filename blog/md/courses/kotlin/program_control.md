## Kotlin Programming - Program Control

**Kotlin has the following conditionals:**

* Use if to specify a block of code to be executed, if a specified condition is true
* Use else to specify a block of code to be executed, if the same condition is false
* Use else if to specify a new condition to test, if the first condition is false
* Use when to specify many alternative blocks of code to be executed

**Syntax**

```java
if (condition) {
  // block of code to be executed if the condition is true
} else {
  // block of code to be executed if the condition is false
}
```

```java
if (condition1) {
  // block of code to be executed if condition1 is true
} else if (condition2) {
  // block of code to be executed if the condition1 is false and condition2 is true
} else {
  // block of code to be executed if the condition1 is false and condition2 is false
}
```

* **Kotlin If..Else Expressions**

```java
val time = 20
val greeting = if (time < 18) {
  "Good day."
} else {
  "Good evening."
}
println(greeting)
```

more concisely,

```java
fun main() {
  val time = 20
  val greeting = if (time < 18) "Good day." else "Good evening."
  println(greeting)
}
```

## Kotlin when

Similar to switch() {} in other language,

```java
val day = 4

val result = when (day) {
  1 -> "Monday"
  2 -> "Tuesday"
  3 -> "Wednesday"
  4 -> "Thursday"
  5 -> "Friday"
  6 -> "Saturday"
  7 -> "Sunday"
  else -> "Invalid day."
}
println(result)

// Outputs "Thursday" (day 4)
```

## Loop

### while loop

**Syntax**

```java
while (condition) {
  // code block to be executed
}
```

```java
do {
  // code block to be executed
}
while (condition);
```

### for loop

```java
val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
for (x in cars) {
  println(x)
}
```

**Traditional For Loop**

Unlike Java and other programming languages, there is no traditional for loop in Kotlin.

## Kotlin Break

The break statement is used to jump out of a loop.

```java
var i = 0
while (i < 10) {
  println(i)
  i++
  if (i == 4) {
    break
  }
}
```

## Kotlin Continue
The continue statement breaks one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop.

var i = 0
while (i < 10) {
  if (i == 4) {
    i++
    continue
  }
  println(i)
  i++
}

## Kotlin Arrays

To create an array, use the arrayOf() function, and place the values in a comma-separated list inside it:

`val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")`

* **Access the Elements of an Array**

```java
val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
println(cars[0])
// Outputs Volvo 
```

* **Change an Array Element**

`cars[0] = "Opel"`

* **Array Length / Size**

To find out how many elements an array have, use the size property:

**Example**

```java
val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
println(cars.size)
// Outputs 4 
```

* **Check if an Element Exists**

You can use the in operator to check if an element exists in an array:

**Example**

```java
val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
if ("Volvo" in cars) {
  println("It exists!")
} else {
  println("It does not exist.")
}
```

## Kotlin Ranges

With the for loop, you can also create ranges of values with "..":

**Example 1**

Print the whole alphabet:

```java
for (chars in 'a'..'x') {
  println(chars)
}

for (nums in 5..15) {
  println(nums)
} 
```

**Example 2**

```java
val nums = arrayOf(2, 4, 6, 8)
if (2 in nums) {
  println("It exists!")
} else {
  println("It does not exist.")
}
```

**Example 3**

```java
val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
if ("Volvo" in cars) {
  println("It exists!")
} else {
  println("It does not exist.")
}
```