# Javascript Classes 

# Definition

A class in JavaScript is a blueprint for creating objects. It encapsulates data (properties) and behavior (methods) within a single entity, following the principles of object-oriented programming (OOP). Classes allow for code reusability, better organization, and easier maintenance by defining a structured way to create multiple objects with similar properties and behaviors.

**Key Components of a JavaScript Class**

1. Class Declaration

- A class is defined using the class keyword followed by the class name.

2. Constructor Method (constructor)

- A special method called automatically when an object is created using the new keyword.
- It initializes the object’s properties.

3. Properties

- Variables that store data related to the object.
- Defined inside the constructor method using this.propertyName.

4. Methods

- Functions inside a class that define behaviors of an object.
- Called on an instance of the class.

5. Instantiation

- Creating objects (instances) from a class using the new keyword.

6. Encapsulation

- Restricting direct access to certain properties and methods, often using private fields.

7. Inheritance

- A mechanism where a class (child) can inherit properties and methods from another class (parent).

# JavaScript Class Syntax

Use the keyword class to create a class.

Always add a method named constructor():

`class ClassName {
constructor() { ... }
}`

**Example**

`class Car {
constructor(name, year) {
this.name = name;
this.year = year;
}
}`

The example above creates a class named "Car".

The class has two initial properties: "name" and "year".

Note: A JavaScript class is not an object. It is a template for JavaScript objects.

**Using a Class** 

When you have a class, you can use the class to create objects:

Example

```<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Classes</h1>
<p>Creating two car objects from a car class:</p>

<p id="demo"></p>

<script>
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

const myCar1 = new Car("Ford", 2014);
const myCar2 = new Car("Audi", 2019);

document.getElementById("demo").innerHTML =
myCar1.name + " " + myCar2.name;
</script>

</body>
</html>
```
The output:

# JavaScript Classes

Creating two car objects from a car class:

Ford Audi

The example above uses the Car class to create two Car objects.
__________________________________________________________

**The Constructor Method**

The constructor method is a special method:

- It has to have the exact name "constructor"
- It is executed automatically when a new object is created
- It is used to initialize object properties

If you do not define a constructor method, JavaScript will add an empty constructor method.

**Class Methods** 

Class methods are created with the same syntax as object methods.

Use the keyword class to create a class.

Always add a constructor() method.

Then add any number of methods.

**syntax**

```
class ClassName {
constructor() { ... }
method_1() { ... }
method_2() { ... }
method_3() { ... }
}
```
Example:

Create a Class method named "age", that returns the Car age:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Methods</h1>
<p>How to define and use a Class method.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;

  }
  age() {
    const date = new Date();
    return date.getFullYear() - this.year;
  }
}

const myCar = new Car("Ford", 2014);
document.getElementById("demo").innerHTML =
"My car is " + myCar.age() + " years old.";
</script>

</body>
</html>
```
The output:


# JavaScript Class Methods
How to define and use a Class method.

My car is 11 years old.
__________________________________________________________

You can send parameters to Class methods:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Method</h1>
<p>Pass a parameter into the "age()" method.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age(x) {
    return x - this.year;
  }
}

const date = new Date();
let year = date.getFullYear();

const myCar = new Car("Ford", 2014);
document.getElementById("demo").innerHTML=
"My car is " + myCar.age(year) + " years old.";
</script>

</body>
</html>
```

The output:

# JavaScript Class Method
Pass a parameter into the "age()" method.

My car is 11 years old.
__________________________________________________________

**"use strict"**

The syntax in classes must be written in "strict mode".

You will get an error if you do not follow the "strict mode" rules.

Example

In "strict mode" you will get an error if you use a variable without declaring it:

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Classes uses "strict mode"</h1>

<p>In a JavaScript Class you cannot use variable without declaring it.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;

  }
  age() {
   // date = new Date();  // This will not work
   const date = new Date(); // This will work
   return date.getFullYear() - this.year;
  }
}

const myCar = new Car("Ford", 2014);
document.getElementById("demo").innerHTML =
"My car is " + myCar.age() + " years old.";
</script>

</body>
</html>
```
Output:

# JavaScript Classes uses "strict mode"
In a JavaScript Class you cannot use variable without declaring it.

My car is 11 years old.

in the above example,

date = new Date(); --> This will not work

const date = new Date(); --> This will work
__________________________________________________________


**Class Inheritance**

To create a class inheritance, use the extends keyword.

A class created with a class inheritance inherits all the methods from another class:

Example

Create a class named "Model" which will inherit the methods from the "Car" class:

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Inheritance</h1>

<p>Use the "extends" keyword to inherit all methods from another class.</p>
<p>Use the "super" method to call the parent's constructor function.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(brand) {
    this.carname = brand;
  }
  present() {
    return 'I have a ' + this.carname;
  }
}

class Model extends Car {
  constructor(brand, mod) {
    super(brand);
    this.model = mod;
  }
  show() {
    return this.present() + ', it is a ' + this.model;
  }
}

const myCar = new Model("Ford", "Mustang");
document.getElementById("demo").innerHTML = myCar.show();
</script>

</body>
</html>
```

Output:

# JavaScript Class Inheritance
Use the "extends" keyword to inherit all methods from another class.

Use the "super" method to call the parent's constructor function.

I have a Ford, it is a Mustang
__________________________________________________________

The super() method refers to the parent class.

By calling the super() method in the constructor method, we call the parent's constructor method and gets access to the parent's properties and methods.

Inheritance is useful for code reusability: reuse properties and methods of an existing class when you create a new class.

**Getters and Setters** 

Classes also allow you to use getters and setters.

It can be smart to use getters and setters for your properties, especially if you want to do something special with the value before returning them, or before you set them.

To add getters and setters in the class, use the get and set keywords.

Example

Create a getter and a setter for the "carname" property:

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Getter/Setter</h1>
<p>A demonstration of how to add getters and setters in a class, and how to use the getter to get the property value.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(brand) {
    this.carname = brand;
  }
  get cnam() {
    return this.carname;
  }
  set cnam(x) {
    this.carname = x;
  }
}

const myCar = new Car("Ford");

document.getElementById("demo").innerHTML = myCar.cnam;
</script>

</body>
</html>
```
Output:
# JavaScript Class Getter/Setter
A demonstration of how to add getters and setters in a class, and how to use the getter to get the property value.

Ford
__________________________________________________________

Note: even if the getter is a method, you do not use parentheses when you want to get the property value.

The name of the getter/setter method cannot be the same as the name of the property, in this case carname.


Many programmers use an underscore character _ before the property name to separate the getter/setter from the actual property:

Example

You can use the underscore character to separate the getter/setter from the actual property:

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Getter/Setter</h1>
<p>Using an underscore character is common practice when using getters/setters in JavaScript, but not mandatory, you can name them anything you like, but not the same as the property name.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(brand) {
    this._carname = brand;
  }
  get carname() {
    return this._carname;
  }
  set carname(x) {
    this._carname = x;
  }
}

const myCar = new Car("Ford");

document.getElementById("demo").innerHTML = myCar.carname;
</script>

</body>
</html>
```
Output:
# JavaScript Class Getter/Setter
Using an underscore character is common practice when using getters/setters in JavaScript, but not mandatory, you can name them anything you like, but not the same as the property name.

Ford
__________________________________________________________

To use a setter, use the same syntax as when you set a property value, without parentheses:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Setters</h1>
<p>When using a setter to set a property value, you do not use parantheses.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(brand) {
    this._carname = brand;
  }
  set carname(x) {
    this._carname = x;
  }
  get carname() {
    return this._carname;
  }
}

const myCar = new Car("Ford");
myCar.carname = "Volvo";
document.getElementById("demo").innerHTML = myCar.carname;
</script>
```
Output:
# JavaScript Class Setters
When using a setter to set a property value, you do not use parantheses.

Volvo
__________________________________________________________

**Hoisting**

Unlike functions, and other JavaScript declarations, class declarations are not hoisted.

That means that you must declare a class before you can use it:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Classes are not Hoisted</h1>
<p>You will get an error if you try to use a class before it is declared.</p>

<p id="demo"></p>

<script>
//You cannot use the class yet.
//myCar = new Car("Ford") will raise an error.

class Car {
  constructor(brand) {
    this.carname = brand;
  }
}

//Now you can use the class:
const myCar = new Car("Ford");
document.getElementById("demo").innerHTML = myCar.carname;

</script>

</body>
</html>
```

Output:
# JavaScript Classes are not Hoisted
You will get an error if you try to use a class before it is declared.

Ford

Note: For other declarations, like functions, you will NOT get an error when you try to use it before it is declared, because the default behavior of JavaScript declarations are hoisting (moving the declaration to the top).
__________________________________________________________

**JavaScript Static Methods**

Static class methods are defined on the class itself.

You cannot call a static method on an object, only on an object class.

Example:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Static Methods</h1>
<p>A static method is created with the "static" keyword, and you can only call the method on the class itself.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(name) {
    this.name = name;
  }
  static hello() {
    return "Hello!!";
  }
}

const myCar = new Car("Ford");

//You can call 'hello()' on the Car Class:
document.getElementById("demo").innerHTML = Car.hello();

// But NOT on  a Car Object:
// document.getElementById("demo").innerHTML = myCar.hello();
// this will raise an error.
</script>

</body>
</html>
```
Output:
# JavaScript Class Static Methods
A static method is created with the "static" keyword, and you can only call the method on the class itself.

Hello!!
__________________________________________________________

If you want to use the myCar object inside the static method, you can send it as a parameter:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Class Static Methods</h1>
<p>To use the "myCar" object inside the static method, you can send it as parameter.</p>

<p id="demo"></p>

<script>
class Car {
  constructor(name) {
    this.name = name;
  }
  static hello(x) {
    return "Hello " + x.name;
  }
}

const myCar = new Car("Ford");
document.getElementById("demo").innerHTML = Car.hello(myCar);
</script>

</body>
</html>
```

Output:
# JavaScript Class Static Methods
To use the "myCar" object inside the static method, you can send it as parameter.

Hello Ford
__________________________________________________________
