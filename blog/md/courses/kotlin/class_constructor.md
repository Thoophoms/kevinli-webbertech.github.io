In Kotlin, constructors are used to initialize objects. There are **primary constructors** and **secondary constructors**, and you can also use **initializer blocks (`init`)**.

---

### **1. Primary Constructor**
The primary constructor is declared in the class header.

```kotlin
class Person(val name: String, var age: Int)
```
- `val name: String` → Read-only property (Immutable)
- `var age: Int` → Mutable property

**Usage:**
```kotlin
val person = Person("Alice", 25)
println(person.name) // Alice
println(person.age)  // 25
```

---

### **2. Primary Constructor with `init` Block**
If you need additional logic during initialization, use an `init` block.

```kotlin
class Person(val name: String, var age: Int) {
    init {
        println("Person named $name is created with age $age")
    }
}
```

---

### **3. Secondary Constructor**
Secondary constructors allow additional initialization logic or alternative ways to instantiate objects.

```kotlin
class Person {
    var name: String
    var age: Int

    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }
}
```
**Usage:**
```kotlin
val person = Person("Bob", 30)
```

> **Note:** If a class has a **primary constructor**, every secondary constructor **must** call it using `this()`.

Example:

```kotlin
class Person(val name: String, var age: Int) {
    constructor(name: String) : this(name, 0) // Calls primary constructor
}
```

---

### **4. Default Values in Constructor**
Kotlin allows default parameter values, reducing the need for multiple constructors.

```kotlin
class Person(val name: String = "Unknown", var age: Int = 18)
```

**Usage:**
```kotlin
val person1 = Person()  // Uses default values
val person2 = Person("Emma")  // age defaults to 18
val person3 = Person("John", 25)  // Both values provided
```

---

### **5. Data Class Constructor (Shortcut for POJOs)**
If a class is meant to hold data, use a **data class**.

```kotlin
data class Person(val name: String, var age: Int)
```

This automatically provides:
- `toString()`
- `equals()`
- `copy()`
- `hashCode()`
