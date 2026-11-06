# Exception

In Kotlin, exceptions are thrown using the `throw` keyword. Here's how you can throw an exception:

### **Throwing an Exception**
```kotlin
fun validateAge(age: Int) {
    if (age < 18) {
        throw IllegalArgumentException("Age must be 18 or older")
    }
    println("Valid age")
}

fun main() {
    validateAge(16) // This will throw an exception
}
```

### **Common Exception Classes in Kotlin**
- `IllegalArgumentException` - When an argument passed to a function is invalid.
- `IllegalStateException` - When a method has been invoked at an illegal state.
- `NullPointerException` - When an attempt is made to access an object reference that has the `null` value.
- `IndexOutOfBoundsException` - When accessing an index that is out of bounds in an array or list.
- `ArithmeticException` - When an illegal arithmetic operation occurs (e.g., division by zero).

### **Using `throw` with `Nothing`**
In Kotlin, `throw` is an expression of type `Nothing`, meaning it never returns:
```kotlin
fun fail(message: String): Nothing {
    throw IllegalStateException(message)
}

fun main() {
    val result = fail("This is an error") // Function never returns
}
```

### **Custom Exceptions**
You can create your own exception by extending the `Exception` class:
```kotlin
class CustomException(message: String) : Exception(message)

fun riskyFunction() {
    throw CustomException("Something went wrong!")
}

fun main() {
    riskyFunction()
}
```

## Handle Exception

### **Handling Exceptions in Kotlin**
In Kotlin, exceptions are handled using the `try`, `catch`, and `finally` blocks.

### **Basic Try-Catch**
```kotlin
fun main() {
    try {
        val result = 10 / 0  // This will throw ArithmeticException
        println(result)
    } catch (e: ArithmeticException) {
        println("Exception caught: ${e.message}")
    }
}
```
**Output:**
```
Exception caught: / by zero
```

### **Multiple Catch Blocks**
You can catch different types of exceptions separately.
```kotlin
fun main() {
    try {
        val list = listOf(1, 2, 3)
        println(list[5])  // This will throw IndexOutOfBoundsException
    } catch (e: ArithmeticException) {
        println("Arithmetic Exception: ${e.message}")
    } catch (e: IndexOutOfBoundsException) {
        println("Index Out of Bounds: ${e.message}")
    }
}
```
**Output:**
```
Index Out of Bounds: Index 5 out of bounds for length 3
```

### **Try as an Expression**
In Kotlin, `try` can be used as an expression, meaning it can return a value.
```kotlin
fun divide(a: Int, b: Int): Int {
    return try {
        a / b
    } catch (e: ArithmeticException) {
        println("Cannot divide by zero, returning -1")
        -1
    }
}

fun main() {
    val result = divide(10, 0)
    println("Result: $result")
}
```
**Output:**
```
Cannot divide by zero, returning -1
Result: -1
```

### **Finally Block**
The `finally` block runs regardless of whether an exception occurs or not.
```kotlin
fun main() {
    try {
        println("Trying to execute...")
        throw RuntimeException("Something went wrong")
    } catch (e: Exception) {
        println("Exception caught: ${e.message}")
    } finally {
        println("Finally block executed")
    }
}
```
**Output:**
```
Trying to execute...
Exception caught: Something went wrong
Finally block executed
```

### **Throwing and Handling Custom Exceptions**
```kotlin
class InvalidAgeException(message: String) : Exception(message)

fun validateAge(age: Int) {
    if (age < 18) {
        throw InvalidAgeException("Age must be at least 18")
    }
    println("Valid age: $age")
}

fun main() {
    try {
        validateAge(16)
    } catch (e: InvalidAgeException) {
        println("Custom Exception: ${e.message}")
    }
}
```
**Output:**
```
Custom Exception: Age must be at least 18
```

## **Exception Handling in Kotlin Coroutines**
In Kotlin coroutines, exception handling is a bit different because coroutines run asynchronously. Here are several ways to handle exceptions in coroutines:

---

### **1. Try-Catch Inside Coroutine**
You can catch exceptions within a coroutine using `try-catch` like normal:
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    try {
        launch {
            println("Before exception")
            throw ArithmeticException("Something went wrong!")
        }
    } catch (e: Exception) {
        println("Caught an exception: ${e.message}")
    }
}
```
**Issue:** This won't catch the exception because `launch` creates a separate coroutine, and the exception is thrown in another execution context.

---

### **2. Handling Exceptions in `launch` (CoroutineExceptionHandler)**
When using `launch`, you need to use `CoroutineExceptionHandler` to catch uncaught exceptions:
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val handler = CoroutineExceptionHandler { _, exception ->
        println("Caught exception: ${exception.message}")
    }

    val job = launch(handler) {
        println("Before exception")
        throw RuntimeException("Something went wrong!")
    }
    
    job.join()
}
```
**Output:**
```
Before exception
Caught exception: Something went wrong!
```
👉 **`CoroutineExceptionHandler` works only with `launch` and not `async` because `async` expects the caller to handle exceptions.**

---

### **3. Handling Exceptions in `async`**
If you use `async`, the exception needs to be handled explicitly by calling `await()` inside a `try-catch` block:
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val deferred = async {
        println("Before exception in async")
        throw IllegalStateException("Something went wrong in async!")
    }

    try {
        deferred.await() // Exception is thrown here
    } catch (e: Exception) {
        println("Caught exception: ${e.message}")
    }
}
```
**Output:**
```
Before exception in async
Caught exception: Something went wrong in async!
```
👉 Unlike `launch`, exceptions inside `async` must be handled explicitly when calling `await()`.

---

### **4. SupervisorJob – Preventing Failure Propagation**
By default, if a child coroutine fails, the parent also gets canceled. To prevent this, use `SupervisorJob`:
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val supervisor = SupervisorJob()

    val scope = CoroutineScope(coroutineContext + supervisor)

    val job1 = scope.launch {
        delay(500)
        throw RuntimeException("Job 1 failed")
    }

    val job2 = scope.launch {
        delay(1000)
        println("Job 2 completed successfully")
    }

    delay(1500)
}
```
**Output:**
```
Job 2 completed successfully
Exception in thread "main" java.lang.RuntimeException: Job 1 failed
```
👉 `job2` is not canceled because `SupervisorJob` allows independent failure handling.

---

### **5. `supervisorScope` – Handling Exceptions at Scope Level**
Unlike `CoroutineScope`, `supervisorScope` allows child coroutines to fail independently:
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    supervisorScope {
        launch {
            delay(500)
            throw IllegalArgumentException("Launch failed")
        }

        launch {
            delay(1000)
            println("Other coroutine still running")
        }
    }
}
```
**Output:**
```
Other coroutine still running
Exception in thread "main" java.lang.IllegalArgumentException: Launch failed
```
👉 The second `launch` is **not canceled**, unlike normal `coroutineScope`.

---

### **Key Takeaways**
1. **Use `try-catch` inside coroutines** for simple exception handling.
2. **Use `CoroutineExceptionHandler` for `launch`** to catch uncaught exceptions.
3. **Use `try-catch` with `async.await()`** because exceptions must be handled explicitly.
4. **Use `SupervisorJob`** to prevent failure propagation to sibling coroutines.
5. **Use `supervisorScope`** to allow individual coroutines to fail without affecting others.


## **Exception Handling with Structured Concurrency in Kotlin Coroutines**
Structured concurrency ensures that all coroutines launched inside a given scope are completed before the scope itself is completed. Here’s how exception handling works in structured concurrency:

---

### **1. Handling Exceptions in `coroutineScope`**
If one coroutine fails inside `coroutineScope`, all sibling coroutines **are canceled** automatically.

### **Example: Exception Cancels All Coroutines**
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    try {
        coroutineScope {
            launch {
                delay(1000)
                println("Coroutine 1 finished")
            }

            launch {
                delay(500)
                throw RuntimeException("Coroutine 2 failed!") // This will cancel Coroutine 1
            }
        }
    } catch (e: Exception) {
        println("Caught exception: ${e.message}")
    }

    println("Main function continues...")
}
```
**Output:**
```
Caught exception: Coroutine 2 failed!
Main function continues...
```
👉 **Since `coroutineScope` cancels all coroutines on failure, `Coroutine 1` never completes.**

---

### **2. Using `supervisorScope` to Prevent Cancellation**
If you don’t want sibling coroutines to be canceled when one fails, use `supervisorScope`.

### **Example: Failure Does Not Cancel Other Coroutines**
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    supervisorScope {
        launch {
            delay(1000)
            println("Coroutine 1 finished")
        }

        launch {
            delay(500)
            throw RuntimeException("Coroutine 2 failed!") // Only this coroutine fails
        }
    }

    println("Main function continues...")
}
```
**Output:**
```
Coroutine 1 finished
Exception in thread "main" java.lang.RuntimeException: Coroutine 2 failed!
Main function continues...
```
👉 **Unlike `coroutineScope`, `supervisorScope` allows `Coroutine 1` to finish even if `Coroutine 2` fails.**

---

### **3. Combining `CoroutineExceptionHandler` with `SupervisorJob`**
For advanced handling, you can combine `CoroutineExceptionHandler` and `SupervisorJob` inside a `CoroutineScope`.

### **Example: Isolating Failure from Affecting Other Jobs**
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val handler = CoroutineExceptionHandler { _, exception ->
        println("Caught exception: ${exception.message}")
    }

    val scope = CoroutineScope(SupervisorJob() + handler)

    scope.launch {
        delay(500)
        throw RuntimeException("Coroutine failed!")
    }

    scope.launch {
        delay(1000)
        println("Another coroutine finished successfully")
    }

    delay(1500)
}
```
**Output:**
```
Caught exception: Coroutine failed!
Another coroutine finished successfully
```
👉 **Using `SupervisorJob`, one coroutine can fail without affecting others. The exception is caught in `CoroutineExceptionHandler`.**

---

### **4. `try-catch` Inside `async` with Structured Concurrency**
Since `async` returns a `Deferred` result, exceptions must be handled explicitly when calling `await()`.

### **Example: Handling Exception in `async`**
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    val deferred = async {
        delay(500)
        throw IllegalArgumentException("Error in async")
    }

    try {
        deferred.await() // Exception is thrown here
    } catch (e: Exception) {
        println("Caught exception: ${e.message}")
    }

    println("Main function continues...")
}
```
**Output:**
```
Caught exception: Error in async
Main function continues...
```
👉 **Since we used `try-catch` around `await()`, the program doesn’t crash.**

---

## **5. `supervisorScope` + `async` for Independent Failures**
Using `supervisorScope`, we can allow `async` tasks to fail independently.

### **Example: One Async Task Fails, Others Continue**
```kotlin
import kotlinx.coroutines.*

fun main() = runBlocking {
    supervisorScope {
        val deferred1 = async {
            delay(1000)
            "Result from async 1"
        }

        val deferred2 = async {
            delay(500)
            throw RuntimeException("Async 2 failed!") // Only this one fails
        }

        try {
            println(deferred2.await()) // Exception thrown here
        } catch (e: Exception) {
            println("Caught exception: ${e.message}")
        }

        println(deferred1.await()) // This still runs
    }

    println("Main function continues...")
}
```
**Output:**
```
Caught exception: Async 2 failed!
Result from async 1
Main function continues...
```
👉 **The failure in `deferred2` does not affect `deferred1`, and the main function continues executing.**

---

## **Key Takeaways**
| **Concept** | **Behavior** |
|------------|------------|
| `coroutineScope` | Cancels all child coroutines if one fails |
| `supervisorScope` | Allows other child coroutines to continue if one fails |
| `CoroutineExceptionHandler` | Catches unhandled exceptions, works with `launch` but not `async` |
| `SupervisorJob` | Prevents failure from propagating to sibling coroutines |
| `async` | Exceptions must be caught explicitly with `await()` |

---

### **Conclusion**
Structured concurrency in Kotlin provides robust mechanisms for exception handling, ensuring that failures are managed properly without disrupting unrelated coroutines. 
