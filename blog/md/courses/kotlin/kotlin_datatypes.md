# Kotlin Programming - Data Types

## Syntax

we created a Kotlin file called Main.kt,

```kotlin
fun main() {
  println("Hello World")
}
```

* fun as keyword; Java does not have that.
* file extention: .kt.

> This is for parser to transpile back into Java with a relative similar syntax.

## Kotlin Comments

* Single-line comments, `//`

* Multi-line Comments, `/* this is your comment block */`

## Kotlin Variables

**Syntax:**

```Java
var variableName = value
val variableName = value
```

or,

```Java
var name: String = "John" // String
val birthyear: Int = 1975 // Int

println(name)
println(birthyear)
```

**Example**

```Java
Example
var name = "John"
val birthyear = 1975

println(name)          // Print the value of name
println(birthyear)     // Print the value of birthyear
```

Kotlin is smart enough to understand that "John" is a String (text), and that 1975 is an Int (number) variable. And another language groovy is also similar in this sort.

* var value can be changed later.
* val value can not be changed later, more like const.
* if you give a type for var, you can change it, otherwise you can't if you declare a null value var since the parser does not know the real type and have no way to infer what it is without a value intially before it was stored in the main memory.

For example,

This works fine:

```java
var name: String
name = "John"
println(name)
```

This will generate an error:

```java
var name
name = "John"
println(name)
```

## Data Type

| one way | second way |
| --------| -----------|
|val myNum = 5             // Int|val myNum: Int = 5                // Int|
|val myDoubleNum = 5.99    // Double|val myDoubleNum: Double = 5.99    // Double|
|val myLetter = 'D'        // Char|val myLetter: Char = 'D'          // Char|
|val myBoolean = true      // Boolean|val myBoolean: Boolean = true     // Boolean|
|val myText = "Hello"      // String|val myText: String = "Hello"      // String|

**Details on Kotlin Number Types**

|Number Type|Range|
|-----------|------|
|  Byte     | -128 to 127 |
|  Short    | -32768 to 32767 |
|  Int      | -2147483648 to 2147483647 |
|  Long     | -9223372036854775808 to 9223372036854775807 |

## Operators

Kotlin divides the operators into the following groups:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators

* **Arithmetic Operators**

Arithmetic operators are used to perform common mathematical operations.

|Operator	Name	|Description	Example|
|---------------|--------------------|
|+	|Addition	Adds together two values	x + y	|
|-	|Subtraction	Subtracts one value from another	x - y	|
|*	|Multiplication	Multiplies two values	x * y	|
|/	|Division	Divides one value from another	x / y	|
|%	|Modulus	Returns the division remainder	x % y	|
|++	|Increment	Increases the value by 1	++x	|
|--	|Decrement	Decreases the value by 1	--x	|

Kotlin Assignment Operators
Assignment operators are used to assign values to variables.

In the example below, we use the assignment operator (=) to assign the value 10 to a variable called x:

|Operator	|Example|
|---------|--------|
|=        |	x = 5	x = 5	|
|+=       |	x += 3	x = x + 3	|
|-=       |	x -= 3	x = x - 3	|
|*=       |	x *= 3	x = x * 3	|
|/=       |	x /= 3	x = x / 3	|
|%=       |	x %= 3	x = x % 3 |

Kotlin Comparison Operators
Comparison operators are used to compare two values, and returns a Boolean value: either true or false.

|Operator	Name	| Example	|
|---------------|----------|
|==	|Equal to	x == y	|
|!=	|Not equal	x != y	|
|>	|Greater than	x > y	|
|<	|Less than	x < y	|
|>=	|Greater than or equal to	x >= y	|
|<=	|Less than or equal to	x <= y	|

* **Kotlin Logical Operators**

Logical operators are used to determine the logic between variables or values:

|Operator	Name|	Description	Example	|
|-------------|---------------------|
|&&| Logical and	Returns true if both statements are true	x < 5 &&  x < 10	|
||| Logical or	Returns true if one of the statements is true	x < 5 || x < 4	|
|!|	Logical not	Reverse the result, returns false if the result is true|

## Kotlin Strings

A string contains a collection of characters surrounded by double quotes:

`var greeting: String = "Hello"`

* **Access a String**

To access the characters (elements) of a string, you must refer to the index number inside square brackets.

String indexes start with 0. In the example below, we access the first and third element in txt:

```java
var txt = "Hello World"
println(txt[0]) // first element (H)
println(txt[2]) // third element (l)
```

* **String Length**

```java
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
println("The length of the txt string is: " + txt.length)
```

* **String Functions**

```java
var txt = "Hello World"
println(txt.toUpperCase())   // Outputs "HELLO WORLD"
println(txt.toLowerCase())   // Outputs "hello world"
```

* **Comparing Strings**

The compareTo(string) function compares two strings and returns 0 if both are equal:

```java
var txt1 = "Hello World"
var txt2 = "Hello World"
println(txt1.compareTo(txt2))  // Outputs 0 (they are equal)
```

* **Finding a String in a String**

The indexOf() function returns the index (the position) of the first occurrence of a specified text in a string (including whitespace):

```java
var txt = "Please locate where 'locate' occurs!"
println(txt.indexOf("locate"))  // Outputs 7
```

* **Quotes Inside a String**

To use quotes inside a string, use single quotes ('):

```java
var txt1 = "It's alright"
var txt2 = "That's great"

* **String Concatenation**

```java
var firstName = "John"
var lastName = "Doe"
println(firstName + " " + lastName)
```

You can also use the plus() function to concatenate two strings:

```java
var firstName = "John "
var lastName = "Doe"
println(firstName.plus(lastName))
```

* **String Templates/Interpolation**

Instead of concatenation, you can also use "string templates", which is an easy way to add variables and expressions inside a string.

Just refer to the variable with the $ symbol:

```java
var firstName = "John"
var lastName = "Doe"
println("My name is $firstName $lastName")
```

## Kotlin Booleans

A boolean type can be declared with the Boolean keyword and can only take the values true or false:

```java
val isKotlinFun: Boolean = true
val isFishTasty: Boolean = false
println(isKotlinFun)   // Outputs true
println(isFishTasty)   // Outputs false 
```

or

```java
val isKotlinFun = true
val isFishTasty = false
println(isKotlinFun)   // Outputs true
println(isFishTasty)   // Outputs false 
```

## Boolean Expression

```java
val x = 10
val y = 9
println(x > y) // Returns true, because 10 is greater than 9
```

or,

`println(10 > 9) // Returns true, because 10 is greater than 9`

or,

`println(10 == 15); // Returns false, because 10 is not equal to 15`

## dynamic

dynamic is a special type in Kotlin/JS. It basically turns off Kotlin's type checker. That is needed in order to interoperate with untyped or loosely typed environments, such as the JavaScript ecosystem.

```java
val a: dynamic = "abc"                                               // 1
val b: String = a                                                    // 2

fun firstChar(s: String) = s[0]

println("${firstChar(a)} == ${firstChar(b)}")                        // 3

println("${a.charCodeAt(0, "dummy argument")} == ${b[0].toInt()}")   // 4

println(a.charAt(1).repeat(3))                                       // 5

fun plus(v: dynamic) = v + 2

println("2 + 2 = ${plus(2)}")                                        // 6
println("'2' + 2 = ${plus("2")}")
```

* Any value can be assigned to a dynamic variable type.
* A dynamic value can be assigned to anything.
* A dynamic variable can be passed as an argument to any function.
* Any property or function with any arguments can be called on a dynamic variable.
* A function call on a dynamic variable always returns a dynamic value, so it is possible to chain the calls.
* Operators, assignments, and indexed access ([..]) are translated "as is". Beware!

## Ref

- https://play.kotlinlang.org/byExample/09_Kotlin_JS/01_dynamic
