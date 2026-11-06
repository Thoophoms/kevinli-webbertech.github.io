# Kotlin Language - Function and Class

## function

Similar to Java, you would need a main() function in the file.

```java
fun hello() { 
  println("Hello World") 
}
```

```java
fun main() {
  myFunction() // Call myFunction
}
```

## Class

Kotlin OOP is the same as Java.

### Create a Class

To create a class, use the class keyword, and specify the name of the class:

```java
class Car {
  var brand = ""
  var model = ""
  var year = 0
} 
```

### Create an Object

```java
// Create a c1 object of the Car class
val c1 = Car()

// Access the properties and add some values to it
c1.brand = "Ford"
c1.model = "Mustang"
c1.year = 1969

println(c1.brand)   // Outputs Ford
println(c1.model)   // Outputs Mustang
println(c1.year)    // Outputs 1969
```

Another example,

```java
class Car(var brand: String, var model: String, var year: Int)

fun main() {
  val c1 = Car("Ford", "Mustang", 1969)
}
```

### class method/function

```java
class Car(var brand: String, var model: String, var year: Int) {
  // Class function
  fun drive() {
    println("Wrooom!")
  }
}

fun main() {
  val c1 = Car("Ford", "Mustang", 1969)
  
  // Call the function
  c1.drive()
}
```

### Class Function Parameters

Just like with regular functions, you can pass parameters to a class function:

```java
class Car(var brand: String, var model: String, var year: Int) {
  // Class function
  fun drive() {
    println("Wrooom!")
  }
  
  // Class function with parameters
  fun speed(maxSpeed: Int) {
    println("Max speed is: " + maxSpeed)
  }
}

fun main() {
  val c1 = Car("Ford", "Mustang", 1969)
  
  // Call the functions
  c1.drive()
  c1.speed(200)
}
```