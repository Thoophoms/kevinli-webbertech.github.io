# JavaScript Function

A JavaScript function is defined with the function keyword, followed by a name, followed by parentheses (). 

Function names can contain letters, digits, underscores, and dollar signs (same rules as variables).

The parentheses may include parameter names separated by commas:
(parameter1, parameter2, ...)

```javascript
function name(parameter1, parameter2, parameter3) {
  // code to be executed
}
```

## Function Invocation

The code inside the function will execute when "something" invokes (calls) the function:

* When an event occurs (when a user clicks a button)
* When it is invoked (called) from JavaScript code
* Automatically (self invoked)

## Function Return

When JavaScript reaches a return statement, the function will stop executing.

If the function was invoked from a statement, JavaScript will "return" to execute the code after the invoking statement.

Functions often compute a return value. The return value is "returned" back to the "caller":

```javascript
// Function is called, the return value will end up in x
let x = myFunction(4, 3);

function myFunction(a, b) {
// Function returns the product of a and b
  return a * b;
}
```

## The () Operator

```javascript
Convert Fahrenheit to Celsius:

function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
}

let value = toCelsius(77) 
```

Accessing a function without () returns the function and not the function result:

```javascript
function toCelsius(fahrenheit) {
  return (5/9) * (fahrenheit-32);
}

let value = toCelsius;
```

## Functions Used as Variable Values

Instead of using a variable to store the return value of a function:

```javascript
let x = toCelsius(77);
let text = "The temperature is " + x + " Celsius";
```

You can use the function directly, as a variable value:

`let text = "The temperature is " + toCelsius(77) + " Celsius";`

## Function scope

The function above does not belong to any object. But in JavaScript there is always a default global object.

In HTML the default global object is the HTML page itself, so the function above "belongs" to the HTML page.

In a browser the page object is the browser window. The function above automatically becomes a window function.

```javascript
function myFunction(a, b) {
  return a * b;
}
window.myFunction(10, 2);    // Will also return 20
```

## This keyword

In JavaScript, the this keyword refers to an object.

The this keyword refers to different objects depending on how it is used:

What is this?
In JavaScript, the this keyword refers to an object.

The this keyword refers to different objects depending on how it is used:

* In an object method, this refers to the object.
* Alone, this refers to the global object.
* In a function, this refers to the global object.
* In a function, in strict mode, this is undefined.
* In an event, this refers to the element that received the event.
* Methods like call(), apply(), and bind() can refer this to any object.

## JavaScript Function call()

In JavaScript all functions are object methods.

If a function is not a method of a JavaScript object, it is a function of the global object (see previous chapter).

The example below creates an object with 3 properties, firstName, lastName, fullName.

```javascript
const person = {
  firstName:"John",
  lastName: "Doe",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  }
}

// This will return "John Doe":
person.fullName();  
```

In the example above, this refers to the person object.

this.firstName means the firstName property of this.

Same as:

this.firstName means the firstName property of person.

**The call() method is a predefined JavaScript method**

It can be used to invoke (call) a method with an owner object as an argument (parameter).

```javascript
const person = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
const person1 = {
  firstName:"John",
  lastName: "Doe"
}
const person2 = {
  firstName:"Mary",
  lastName: "Doe"
}

// This will return "John Doe":
person.fullName.call(person1);
```

**The call() Method with Arguments**

The call() method can accept arguments:

```javascript
const person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}

const person1 = {
  firstName:"John",
  lastName: "Doe"
}

person.fullName.call(person1, "Oslo", "Norway");
```

## JavaScript Function apply()

```javascript
const person = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}

const person1 = {
  firstName: "Mary",
  lastName: "Doe"
}

// This will return "Mary Doe":
person.fullName.apply(person1);
```

apply() is similar to call(), the difference is ,

* The call() method takes arguments separately.

* The apply() method takes arguments as an array.

```javascript
const person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}

const person1 = {
  firstName:"John",
  lastName: "Doe"
}

person.fullName.apply(person1, ["Oslo", "Norway"]);
```

**Example usage of apply()**

Simulate a Max Method on Arrays

```javascript
Math.max(1,2,3);  // Will return 3
```

For an array, you can do this,

`Math.max.apply(null, [1,2,3]); // Will also return 3`

The first argument (null) does not matter. It is not used in this example.

These examples will give the same result:

`Math.max.apply(Math, [1,2,3]); // Will also return 3`

or 

`Math.max.apply(" ", [1,2,3]); // Will also return 3`

## JavaScript Function bind()

**Function Borrowing**

With the bind() method, an object can borrow a method from another object.

The example below creates 2 objects (person and member).

The member object borrows the fullname method from the person object:

```javascript
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Function bind()</h1>

<p>This example creates 2 objects (person and member).</p>
<p>The member object borrows the fullname method from person:</p> 

<p id="demo"></p>

<script>
const person = {
  firstName:"John",
  lastName: "Doe",
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}

const member = {
  firstName:"Hege",
  lastName: "Nilsen",
}

let fullName = person.fullName.bind(member);

document.getElementById("demo").innerHTML = fullName();
</script>

</body>
</html>
```

**Preserving this**

Sometimes the bind() method has to be used to prevent losing this.

In the following example, the person object has a display method. In the display method, this refers to the person object:

```javascript
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Function bind()</h1>

<p>In this example, the person object has a display method:</p>

<p id="demo"></p>

<script>
const person = {
  firstName:"John",
  lastName: "Doe",
  display: function() {
    let x = document.getElementById("demo");
    x.innerHTML = this.firstName + " " + this.lastName;
  }
}

person.display();
</script>

</body>
</html>
```

When a function is used as a callback, this is lost.

This example will try to display the person name after 3 seconds, but it will display undefined instead:

```javascript
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Function bind()</h1>

<p>This example will try to display a person name after 3 seconds.</p>

<p id="demo"></p>

<script>
const person = {
  firstName:"John",
  lastName: "Doe",
  display: function() {
    let x = document.getElementById("demo");
    x.innerHTML = this.firstName + " " + this.lastName;
  }
}

setTimeout(person.display, 3000);
</script>

</body>
</html>
```

The bind() method solves this problem.

In the following example, the bind() method is used to bind person.display to person.

This example will display the person name after 3 seconds:

```javascript

<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Function bind()</h1>

<p>This example will display a person name after 3 seconds:</p>

<p id="demo"></p>

<script>
const person = {
  firstName:"John",
  lastName: "Doe",
  display: function() {
    let x = document.getElementById("demo");
    x.innerHTML = this.firstName + " " + this.lastName;
  }
}

let display = person.display.bind(person);
setTimeout(display, 3000);
</script>

</body>
</html>
```

## JavaScript Closures

JavaScript variables can belong to the local or global scope.

Global variables can be made local (private) with closures.

**Global Variables**

A function can access all variables defined inside the function, like this:

```javascript
function myFunction() {
  let a = 4;
  return a * a;
}
```

But a function can also access variables defined outside the function, like this:

```javascript
let a = 4;
function myFunction() {
  return a * a;
}
```

## Ref

- https://www.w3schools.com/js/js_function_closures.asp