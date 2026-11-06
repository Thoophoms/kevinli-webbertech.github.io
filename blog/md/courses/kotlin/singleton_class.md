### **`object` Class in Kotlin**

In Kotlin, the `object` keyword is used to create **singleton objects, companion objects, and anonymous objects**. It is useful when you want a **single instance of a class** without needing to instantiate it manually.

---

## **1. Singleton Object**

Kotlin provides a built-in way to create a **singleton** using `object`.

**Example:**

```kotlin
object Database {
    val name = "MyDatabase"
    fun connect() {
        println("Connected to $name")
    }
}

fun main() {
    Database.connect() // Connected to MyDatabase
}
```
- No need to create an instance (`Database()`)
- The object is **thread-safe and lazily initialized**.

---

## **2. Companion Object (Static-like Behavior)**
Kotlin does not have `static` methods like Java. Instead, you can use a **companion object** inside a class.

**Example:**
```kotlin
class Logger {
    companion object {
        fun log(message: String) {
            println("Log: $message")
        }
    }
}

fun main() {
    Logger.log("Hello, World!") // Log: Hello, World!
}
```
- Methods inside a `companion object` can be called **without creating an instance** of the class.
- Equivalent to `static` methods in Java.

---

## **3. Anonymous Object (Object Expression)**
You can create an **anonymous object** for **one-time use**.

**Example:**
```kotlin
interface ClickListener {
    fun onClick()
}

fun main() {
    val buttonClickListener = object : ClickListener {
        override fun onClick() {
            println("Button Clicked!")
        }
    }

    buttonClickListener.onClick() // Button Clicked!
}
```
- Useful for implementing interfaces or extending classes **without creating a named class**.

---

### **4. Object Declaration vs. Object Expression**
| Feature | `object` Declaration | `object` Expression |
|---------|---------------------|---------------------|
| Name required? | Yes (e.g., `object Singleton`) | No (anonymous) |
| Singleton? | Yes | No |
| Use case | Global single instance | One-time object |

---

### **Summary**
- ✅ `object` **Declaration** → Singleton (e.g., `object Database`)
- ✅ `companion object` → Static-like members inside a class
- ✅ `object` **Expression** → Anonymous objects for one-time use

Would you like a real-world example? 🚀