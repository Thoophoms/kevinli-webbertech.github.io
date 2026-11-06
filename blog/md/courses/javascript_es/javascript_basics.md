# Javascript Basics

## Code comments

**Single line comment**

```
<html>
<head>
  <title> Single line comments </title>
</head>
<body>
  <script>
    // Defining the string1
    var string1 = "JavaScript";
    // Defining the string2
    var string2 = "TypeScript";
    // Printing the strings
    document.write(string1, " ", string2);
  </script>
</body>
</html>
```

**Multiple line comment**

```ecma script level 4
<html>
<head>
  <title> Multi line comments </title>
</head>
<body>
  <script>
    var a = 100;
    var b = 200;

    /* a = a + b;
    b = a - b;
    a = a - b; */

    document.write("a = " + a + "<br>" + "b = " + b);
  </script>
</body>
</html>
```

## JavaScript Variables

4 Ways you can do it,

* Without using any keywords.

* Using the 'var' keyword.

* Using the 'let' keyword.

* Using the 'const' keyword.

The let and const keywords were introduced to JavaScript in 2015 (ES6). Prior to ES6, only var keyword was used to declare the variable in JavaScript. In this section, we will discuss 'var' keyword. We will cover the 'let' and 'const' keywords in subsequent chapters.

**Examples 1**

```ecma script level 4
<script>
   Money = 10;
   Name = "tutorialspoint";
</script>

```

**Examples 2**

```ecma script level 4
<script>
   var money;
   var name;
</script>
```

**Examples 3**

```ecma script level 4
 var money, name;
```

## Variable initalization and assignment operator

```ecma script level 4
 <script>
   var num = 765; // Number
   var str = "Welcome"; // String
   var bool = false; // Boolean
 </script>
```

## Variable names

* **Valid characters** − In JavaScript, a variable name can contain digits, alphabetical characters, and special characters like underscore (_) and dollar sign ($). JavaScript variable names should not start with a numeral (0-9). They must begin with a letter or an underscore character. For example, 123test is an invalid variable name but _123test is a valid one..

* **Case sensitivity** − Variable names are case sensitive. It means Name and name are different identifiers.

* **Unicode support** − The identifiers can also contain the Unicode. So, developers may define variables in any language.

* **Reserve keywords** − You should not use any of the JavaScript reserved keywords as a variable name. For example, break or boolean variable names are not valid. Here, we have given a full list of the JavaScript revered keywords.

**Example**

```ecma script level 4
<html>
<head>
    <title> Variables in JavaScript </title>
</head>
<body>
   <script>
        var _abc = "Hi!";
        var $abc = "Hello!";
        //  var 9abc = "Bye!";  // This is invalid
        document.write("_abc " + _abc + "<br>");
        document.write("$abc = " + $abc + "<br>");
    </script>
</body>
</html>
```

## Data Types

```ecma script level 4
<script>
   var num = 765; // Number
   var str = "Welcome"; // String
   var bool = false; // Boolean
</script>
```

## Undefined Variable Value in JavaScript

```ecma script level 4
<html>
<body>
   <script>
      var num;
      document.write("The value of num is: " + num + "<br/>");
   </script>
</body>
</html>
```

This produces the following result −

`The value of num is: undefined`

## JavaScript Variable Scope

**Global Variables** − A global variable has global scope which means it can be defined anywhere in your JavaScript code.

**Local Variables** − A local variable will be visible only within a function where it is defined. Function parameters are always local to that function.

```ecma script level 4
<html>
<head>
   <title> JavaScript Variable Scope Example</title>
</head>
<body onload = checkscope();>   
   <script>
	  var myVar = "global";      // Declare a global variable
	  function checkscope( ) {
		 var myVar = "local";    // Declare a local variable
		 document.write(myVar);
	  }
   </script>     
</body>
</html>
```

**another example**

```ecma script level 4
<html>
<head>
   <title> Variables without var keyword </title>
</head>
<body>
   <script>
      name = "student"; // String type variable
      score = 10.25; // Number type variable
      document.write("name = " + name + ", score = " + score + "<br>");
   </script>
</body>
</html>
```

## `let` variable

JavaScript Block Scope vs. Function Scope
The scope of the variable declared with the let keyword is a block-scope. It means if you define the variable with the let keyword in the specific block, you can access the variable inside that particular block only, and if you try to access the variable outside the block, it raises an error like 'variable is not defined'.

```ecma script level 4
{
    let x = "John";
}
```

//here x can't be accessed
The var keyword has a function scope, meaning if you define the variable using the var keyword in any function block, you can access it throughout the function.

```ecma script level 4
function foo(){
    if (true){
        let x = 5
        var y = 10
    }
// here x can't be accessed while y is accessible
}
```

Sometimes, we require to define the variable with the same name in different blocks of one function. Conflicts may occur with the variable value if they use the var keyword.


**Example 1**

In the example below, we have defined the variable x using the let keyword and variable y using the var keyword. Also, we have assigned 10 and 20 values to both variables, respectively.

We defined the test() function, redeclared the x and y variables inside it, and initialized them with 50 and 100 values, respectively. We print variable values inside the function, and it prints the 50 and 100 as it gives first preference to the local variables over global variables.

```ecma script level 4
<html>
<head>
   <title> Variable declaration with let keyword </title>
</head>
<body>
   <script>
      let x = 10;
	  var y = 20;
	  function test() {
	     let x = 50;
	     var y = 100;
	     document.write("x = " + x + ", y = " + y + "<br/>");
	  }
	  test();
   </script>
</body>
</html>
```

**Example 2**

Try the following example, and predict what the values would be,

```ecma script level 4
<html>
<head>
   <title> Variable declaration with let keyword </title>
</head>
<body>
   <script>
      function test() {
	     let bool = true;
		 if (bool) {
		    let x = 30;

		    var y = 40;
		    document.write("x = " + x + ", y = " + y + "<br/>");
		 }
		 // x can't be accessible here
		 document.write("y = " + y + "<br/>");
		}
      test();
   </script>
</body>
</html>
```

output,

```ecma script level 4
x = 30, y = 40
y = 40
```

## Redeclaring Variables in JavaScript

You can't redeclare the variables declared with the let keyword in the same block. However, you can declare the variables with the same name into the different blocks with the same function.

**Example**

In the example below, you can observe that variables declared with the let keyword can’t be redeclared in the same block, but variables declared with the var keyword can be redeclared in the same block.

The code prints the value of the newly declared variable in the output.

```ecma script level 4
<html>
<head>
   <title> Variable redeclaring </title>
</head>
<body>
   <script>
      function test() {
	     if (1) {
	        let m = 70;
			// let m = 80; // redeclaration with let keyword is not	possible
			var n = 80;
			var n = 90; // redeclaration with var keyword is possible
			document.write("m = " + m + ", n = " + n);
		 }
	  }
      test();
   </script>
</body>
</html>
```

## Variable Hoisting

The hoisting behaviors of JavaScript move the declaration of the variables at the top of the code. The let keyword doesn't support hoisting, but the var keyword supports the hosting.

**Example**

In the example below, you can see that we can initialize and print the value of the variable n before its declaration as it is declared using the var keyword.

```ecma script level 4
<html>
<head>
   <title> Variable hoisting </title>
</head>
<body>
   <script>
      function test() {
         // Hoisiting is not supported by let keyword
         // m = 100;
         // document.write("m = " + m + "<br/>");
         // let m;
         n = 50;
         document.write("n = " + n + "<br/>");
         var n;
      }
      test();
   </script>
</body>
</html>
```

## JavaScript Constants

JavaScript constants are the variables whose values remain unchanged throughout the execution of the program. You can declare constants using the const keyword.

The const keyword is introduced in the ES6 version of JavaScript with the let keyword. The const keyword is used to define the variables having constant reference. A variable defined with const can't be redeclared, reassigned. The const declaration have block as well as function scope.

**Declaring JavaScript Constants**

You always need to assign a value at the time of declaration if the variable is declared using the const keyword.

`const x = 10; // Correct Way`

In any case, you can't declare the variables with the const keyword without initialization.

```ecma script level 4
const y; // Incorrect way
y = 20; 
```

**Can't be Reassigned**

```ecma script level 4
const y = 20; 
y = 40; // This is not possible
```

**Block Scope**

A JavaScript variable declared with const keyword has block-scope. This means same variable is treated as different outside the blcok.

In the below example, the x declared within block is different from x declared outside the blcok. So we can redeclare the same variable outsite the block

```ecma script level 4
{
    const x = "john";
}
const x = "Doe"
```

But we can't redeclare the const varaible within the same block.

```ecma script level 4
{
const x = "john";
const x = "Doe" // incorrect
}
```

**No Const Hoisting**

Varaibles defined with const keyword are not hoisted at the top of the code.

In the example below, the const variable x is accessed before it defined. It will cause an error. We can catch the error using try-catch statement.
The following will result in error.

```ecma script level 4
<html>
<body>
   <script>
      document.write(x);
	  const x = 10;	  
   </script>
</body>
</html>
```

## Takeaway

* Difference between var, let and const

We have given the comparison table between the variables declared with the var, let, and const keywords.

|Comparison basis|	var|	let|	const|
|----------------|-----|-------|---------|
|Scope|	Function|	Block|	Block|
|Hoisted|	Yes|	No|	No|
|Reassign|	Yes|	Yes|	No|
|Redeclare	|Yes	|No	|No|
|Bind This|	Yes|	No|	No|

* Redeclaring variables is not a good practice. So, you should avoid it, but if necessary, you may use the var keyword.

## Arrays

**Constant Array**

```ecma script level 4
<html>
<head>
   <title> Consant Arrays </title>
</head>
<body>
   <script>
      // Defining the constant array
      const arr = ["door", "window", "roof", "wall"];
      // Updating arr[0]
      arr[0] = "gate";
      // Inserting an element to the array
      arr.push("fence");
	  //arr = ["table", "chair"] // reassiging array will cause error.
      // Printing the array
      document.write(arr);
   </script>
</body>
</html>
```

**Constant Objects**

```ecma script level 4
<html>
<head>
   <title> Constant Objects </title>
</head>
<body>
   <script>
      // Defining the constant object
      const obj = {
         animal: "Lion",
         color: "Yellow",
      };
      // Changing animal name
      obj.animal = "Tiger";
      // Inserting legs property
      obj.legs = 4;
      // Printing the object
      document.write(JSON.stringify(obj));
      // obj = { name: "cow" } // This is not possible
   </script>
</body>
</html>
```

## Data Types

1. String
2. Number
3. Bigint
4. Boolean
5. Undefined
6. Null
7. Symbol
8. Object

## Number Types

JavaScript Number Methods
These number methods can be used on all JavaScript numbers:

|Method|	Description|
|----------|--------|
|toString()|	Returns a number as a string|
|toExponential()|	Returns a number written in exponential notation|
|toFixed()|	Returns a number written with a number of decimals|
|toPrecision()|	Returns a number written with a specified length|
|valueOf()|	Returns a number as a number|

* JavaScript Numbers are Always 64-bit Floating Point

Unlike many other programming languages, JavaScript does not define different types of numbers, like integers, short, long, floating-point etc.

JavaScript numbers are always stored as double precision floating point numbers, following the international IEEE 754 standard.

This format stores numbers in 64 bits, where the number (the fraction) is stored in bits 0 to 51, the exponent in bits 52 to 62, and the sign in bit 63:

|Value (aka Fraction/Mantissa)|	Exponent	Sign|
52 bits (0 - 51) 	11 bits (52 - 62)	1 bit (63)

In JavaScript, all numbers are stored in a 64-bit floating-point format (IEEE 754 standard).

With this standard, large integer cannot be exactly represented and will be rounded.

Because of this, JavaScript can only safely represent integers:

Up to 9007199254740991 +(2^53-1)

and

Down to -9007199254740991 -(2^53-1).

Integer values outside this range lose precision.

* JavaScript BigInt

JavaScript BigInt variables are used to store big integer values that are too big to be represented by a normal JavaScript Number.

## Check types

```java
let x = BigInt(999999999999999);
let type = typeof x;
```

## String Types

## Arrays

## Operators

There are different types of JavaScript operators:

* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* String Operators
* Logical Operators
* Bitwise Operators
* Ternary Operators
* Type Operators

|Operator|	Description|
|--------|-------------|
|+|	Addition|
|-|	Subtraction|
|*|	Multiplication|
|**|	Exponentiation (ES2016)|
|/|	Division|
|%	Modulus (Division Remainder)|
|++|	Increment|
|--|	Decrement|

|Operator|	Example|	Same As|
|--------|---------|--------|
|=|	x = y|	x = y|
|+=|	x += y|	x = x + y|
|-=|	x -= y|	x = x - y|
|*=|	x *= y|	x = x * y|
|/=|	x /= y|	x = x / y|
|%=|	x %= y|	x = x % y|
|**=|	x **= y|	x = x ** y|

**JavaScript Comparison Operators**

|Operator|Description|
|--------|-------------|
|==	|equal to|
|===	|equal value and equal type|
|!=	|not equal|
|!==	|not equal value or not equal type|
|>|	greater than|
|<|	less than|
|>=|	greater than or equal to|
|<=|	less than or equal to|
|?|	ternary operator|

**JavaScript Logical Operators**

|Operator|	Description|
|&&|	logical and|
||||	logical or|
|!|	logical not|

**JavaScript Type Operators**

|Operator|	Description||
|typeof|	Returns the type of a variable|
|instanceof|	Returns true if an object is an instance of an object type|

**JavaScript Bitwise Operators**

Bit operators work on 32 bits numbers.

Any numeric operand in the operation is converted into a 32 bit number. The result is converted back to a JavaScript number.

|Operator|	Description|	Example|	Same as|	Result|	Decimal|
|--------|-------------|----------|--------|-------|---------|
|   &    |	AND        |	5 & 1	 | 0101 & 0001|	0001|	 1  |
|  OR    |	5|1	     |0101|0001 | 0101   |	 5|
|   ~	   |  NOT	     |~ 5	    | ~0101	  |1010	| 10 |
|   ^    |  XOR        |	5 ^ 1	 | 0101 ^ 0001	|0100|	 4|
|  <<    |	left shift |	5 << 1 |	0101 << 1|	1010|	 10|
|  >>    |	right shift|	5 >> 1 |	0101 >> 1|	0010|	  2|
|>>>|	unsigned right shift|	5 >>> 1|	0101 >>> 1|	0010|	  2|