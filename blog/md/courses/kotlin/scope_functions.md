# Kotlin Scope Function

## let

The Kotlin standard library function let can be used for scoping and null-checks. When called on an object, let executes the given block of code and returns the result of its last expression. The object is accessible inside the block by the reference it (by default) or a custom name.

```java
fun main() {
    val empty = "test".let {               // 1
        print(it)                          // 2
        it.isEmpty()                       // 3
    }
    println(" is empty: $empty")
}

fun printNonNull(str: String?) {
    println("Printing \"$str\":")

    str?.let {                         // 4
        print("\t")
        print(it)
        println()
    }
}

fun printIfBothNonNull(strOne: String?, strTwo: String?) {
    strOne?.let { firstString ->       // 5 
        strTwo?.let { secondString ->
            customPrint("$firstString : $secondString")
            println()
        }
    }
}

printNonNull(null)
printNonNull("my string") 
printIfBothNonNull("First","Second") 
```

* Calls the given block on the result on the string "test".
* Calls the function on "test" by the it reference.
* let returns the value of this expression.
* Uses safe call, so let and its code block will be executed only on non-null values.
* Uses the custom name instead of it, so that the nested let can access the context object of the outer let.

## run

Like let, run is another scoping function from the standard library. Basically, it does the same: executes a code block and returns its result. The difference is that inside run the object is accessed by this. This is useful when you want to call the object's methods rather than pass it as an argument.

```java
fun getNullableLength(ns: String?) {
    println("for \"$ns\":")
    ns?.run {                                                  // 1
        println("\tis empty? " + isEmpty())                    // 2
        println("\tlength = $length")                           
        length                                                 // 3
    }
}
getNullableLength(null)
getNullableLength("")
getNullableLength("some string with Kotlin")
```

* Calls the given block on a nullable variable.
* Inside run, the object's members are accessed without its name.
* run returns the length of the given String if it's not null.

## with

with is a non-extension function that can access members of its argument concisely: you can omit the instance name when referring to its members.

```java
with(configuration) {
    println("$host:$port")
}

// instead of:
println("${configuration.host}:${configuration.port}")  
```

* Creates a Person() instance with default property values.
* Applies the code block (next 3 lines) to the instance.
* Inside apply, it's equivalent to jake.name = "Jake".
* The return value is the instance itself, so you can chain other operations.

## apply

apply executes a block of code on an object and returns the object itself. Inside the block, the object is referenced by this. This function is handy for initializing objects.

```java
class Person {
    var name="";
    var age=0;
    var about="";
    override fun toString(): String {
        return "Person(name='$name', age=$age, about='$about')"
    }
}

fun main() {
    val empty = "test".let {               // 1
        print(it)                        // 2
        it.isEmpty()                       // 3
    }
    println(" is empty: $empty")

    val jake = Person()                                     // 1
    val stringDescription = jake.apply {                    // 2
        name = "Jake"                                       // 3
        age = 30
        about = "Android developer"
    }.toString()

    print(stringDescription.toString())
}
```

* Creates a Person() instance with default property values.
* Applies the code block (next 3 lines) to the instance.
* Inside apply, it's equivalent to jake.name = "Jake".
* The return value is the instance itself, so you can chain other operations.

## also

also works like apply: it executes a given block and returns the object called. Inside the block, the object is referenced by it, so it's easier to pass it as an argument. This function is handy for embedding additional actions, such as logging in call chains.

```java
val jake = Person("Jake", 30, "Android developer")   // 1
    .also {                                          // 2 
        writeCreationLog(it)                         // 3
}
```

## ref

- https://play.kotlinlang.org/byExample/06_scope_functions/01_let