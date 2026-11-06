# Functional

## Higher-Order Functions

A higher-order function is a function that takes another function as parameter and/or returns a function.

**Taking Functions as Parameters**

```java
fun calculate(x: Int, y: Int, operation: (Int, Int) -> Int): Int {  // 1
    return operation(x, y)                                          // 2
}
​
fun sum(x: Int, y: Int) = x + y                                     // 3
​
fun main() {
    val sumResult = calculate(4, 5, ::sum)                          // 4
    val mulResult = calculate(4, 5) { a, b -> a * b }               // 5
    println("sumResult $sumResult, mulResult $mulResult")
}

```

1. Declares a higher-order function. It takes two integer parameters, x and y. Additionally, it takes another function operation as a parameter. The operation parameters and return type are also defined in the declaration.

2. The higher order function returns the result of operation invocation with the supplied arguments.

3. Declares a function that matches the operationsignature.

4. Invokes the higher-order function passing in two integer values and the function argument ::sum. :: is the notation that references a function by name in Kotlin.

5. Invokes the higher-order function passing in a lambda as a function argument. Looks clearer, doesn't it?

**Returning Functions**

```java
fun operation(): (Int) -> Int {                                     // 1
    return ::square
}
​
fun square(x: Int) = x * x                                          // 2
​
fun main() {
    val func = operation()                                          // 3
    println(func(2))                                                // 4
}
```

* Declares a higher-order function that returns a function. (Int) -> Int represents the parameters and return type of the square function.

* Declares a function matching the signature.

* Invokes operation to get the result assigned to a variable. Here func becomes square which is returned by operation.

* Invokes func. The square function is actually executed.

## Lambda Functions

Lambda functions ("lambdas") are a simple way to create functions ad-hoc. Lambdas can be denoted very concisely in many cases thanks to type inference and the implicit it variable.

```java
// All examples create a function object that performs upper-casing.
// So it's a function from String to String

val upperCase1: (String) -> String = { str: String -> str.uppercase() } // 1

val upperCase2: (String) -> String = { str -> str.uppercase() }         // 2

val upperCase3 = { str: String -> str.uppercase() }                     // 3

// val upperCase4 = { str -> str.uppercase() }                          // 4

val upperCase5: (String) -> String = { it.uppercase() }                 // 5

val upperCase6: (String) -> String = String::uppercase                  // 6

println(upperCase1("hello"))
println(upperCase2("hello"))
println(upperCase3("hello"))
println(upperCase5("hello"))
println(upperCase6("hello"))
```

* A lambda in all its glory, with explicit types everywhere. The lambda is the part in curly braces, which is assigned to a variable of type (String) -> String (a function type).

* Type inference inside lambda: the type of the lambda parameter is inferred from the type of the variable it's assigned to.

* Type inference outside lambda: the type of the variable is inferred from the type of the lambda parameter and return value.

* You cannot do both together, the compiler has no chance to infer the type that way.

* For lambdas with a single parameter, you don't have to explicitly name it. Instead, you can use the implicit it variable. This is especially useful when the type of it can be inferred (which is often the case).

* If your lambda consists of a single function call, you may use function pointers (::) .


## Ref

- https://play.kotlinlang.org/byExample/04_functional/01_Higher-Order%20Functions
