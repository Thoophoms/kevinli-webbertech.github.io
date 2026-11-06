# JVM (Java Virtual Machine) Architecture

## What is JVM?

The JVM (Java Virtual Machine) is an abstract machine that provides a runtime environment to execute Java bytecode.

## Key Points

- The JVM is a specification with multiple implementations (JRE).
- It loads, verifies, and executes Java bytecode.
- The JVM consists of various components like class loaders, memory areas, and execution engines.
- Understanding JVM internals helps in debugging and optimizing Java applications.

## Java Code Execution Process

**Class Loader**: Loads Java bytecode into runtime memory areas.
**Runtime Data Areas**: Memory areas where the bytecode is loaded.
**Execution Engine**: Executes the Java bytecode.

### Class Load Stages

**Loading**: Obtains the class and loads it into memory.

***Example of JVM ClassLoader:***

When you run a Java program, the JVM loads the required classes using its class loaders. Here's an example that shows the class loader hierarchy:

```java
public class ClassLoaderExample {
    public static void main(String[] args) {
        Class<?> cls = ClassLoaderExample.class;
        System.out.println("ClassLoader of this class: " + cls.getClassLoader());

        Class<?> stringClass = String.class;
        System.out.println("ClassLoader of String class: " + stringClass.getClassLoader());
    }
}
```

**Output:**

```
ClassLoader of this class: sun.misc.Launcher$AppClassLoader@4e0e2f2a
ClassLoader of String class: null
```

***Note:*** This output indicates that the `ClassLoaderExample` class is loaded by the application class loader, while the `String` class, which is part of the Java core libraries, is loaded by the bootstrap class loader.

**Verifying**: Ensures the class file is correct and safe.

**Preparing**: Allocates memory for class variables and sets default values.

**Resolving**: Converts symbolic references to direct references.

**Initializing**: Initializes static variables and runs static blocks.

### Runtime Data Areas

Memory areas used by JVM during execution:

**Method Area**: Stores class-level data like fields and methods.

### Class (Method) Area Example

The Class (Method) Area stores per-class structures like the runtime constant pool, field, and method data. This is more about the JVM internals, so here's a simple example to understand that static methods and fields are stored in the Method Area.

```java
public class MethodAreaExample {
    public static void main(String[] args) {
        System.out.println("Static method called");
        System.out.println("Static field: " + MyClass.staticField);
    }
}
```

**Heap**: Stores all objects and instance variables.

***Heap Example:***

```java
public class HeapExample {
    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
        System.out.println("Objects created on the heap: " + obj1 + ", " + obj2);
    }
}

class MyClass {
    int instanceVariable;
}
```

**Stack**: Stores method call frames, local variables, and partial results.

***Stack Example 1:***

The Stack stores frames, holding local variables and partial results. Each thread has its own JVM stack:

```java
public class StackExample {
    public static void main(String[] args) {
        method1();
    }

    public static void method1() {
        int x = 10;
        method2(x);
    }

    public static void method2(int y) {
        int z = y * 2;
        System.out.println("Result: " + z);
    }
}
```

***Stack Frame Configuration Example 2:***

```java
public class StackExample {
    public static void main(String[] args) {
        double score = calculateScore();
        System.out.println(normalizeScore(score));
    }

    public static double calculateScore() {
        // some calculation
        return 100.0;
    }

    public static double normalizeScore(double score) {
        double minScore = 0.0;
        double maxScore = 200.0;
        return (score - minScore) / (maxScore - minScore);
    }
}
```

**PC (Program Counter) Register**: Holds the address of the current instruction.

**Native Method Stack**: Supports native methods written in other languages.

***Native Method Stack Example:***

The Native Method Stack contains all the native methods used in the application:

```java
public class NativeMethodExample {
    static {
        System.loadLibrary("nativeLib");
    }

    private native void nativeMethod();

    public static void main(String[] args) {
        new NativeMethodExample().nativeMethod();
    }
}
```

**Note:** The above code requires a corresponding native library (`nativeLib`) and native method implementation, which would be written in C/C++.

**Execution Engine**

- Executes the bytecode.
**Interpreter**: Reads and executes bytecode instructions.

***Execution Engine Example:***

The Execution Engine includes an interpreter and JIT compiler. Here’s an example illustrating bytecode execution and JIT compilation:

```java
public class ExecutionEngineExample {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 0; i < 1000; i++) {
            sum += i;
        }
        System.out.println("Sum: " + sum);
    }
}
```

**Just-In-Time (JIT) Compiler**: Compiles bytecode into native code for performance.

***Example: JIT Compilation:***

```java
public class JITExample {
    public static void main(String[] args) {
        int sum = 10;
        for (int i = 0; i <= 10; i++) {
            sum += i;
        }
        System.out.println(sum);
    }
}
```

The JIT compiler optimizes this code by compiling the loop to native code, reducing memory access overhead.

### Garbage Collector

Automatically reclaims memory by removing unreferenced objects.

### Types of Garbage Collectors

**Serial GC**: Single-threaded, for small applications.

**Parallel GC**: Multi-threaded, default in JVM.

**G1 GC (Garbage First)**: For large heap sizes, prioritizes garbage collection in regions with the most garbage.

**Java Native Interface (JNI)**
    - Allows Java code to interact with code written in other languages like C and C++.

### Java Native Interface (JNI) Example

```java
public class JniExample {
    static {
        System.loadLibrary("nativeLib");
    }

    private native void nativeMethod();

    public static void main(String[] args) {
        new JniExample().nativeMethod();
    }
}
```

**Note:** This requires a native implementation of `nativeMethod` in a library named `nativeLib`.

### Common JVM Errors

**ClassNotFoundException**: Class loader can’t find the class.
**NoClassDefFoundError**: Class file found during compile time but not at runtime.
**OutOfMemoryError**: JVM runs out of memory.
**StackOverflowError**: JVM stack exceeds its limit.

### Conclusion

Understanding the JVM's structure helps in writing efficient Java code and troubleshooting runtime issues. While many Java developers may not delve deep into the JVM internals, having this knowledge can be incredibly beneficial for optimizing and debugging Java applications.

___

## Additional Topics

### Class Loaders in Depth

- **Custom Class Loaders**: You can create custom class loaders to load classes in a specific way, which is useful in application servers and frameworks like Spring and Hibernate.

```java
public class CustomClassLoader extends ClassLoader {
    @Override
    public Class<?> findClass(String name) throws ClassNotFoundException {
        byte[] b = loadClassData(name);
        return defineClass(name, b, 0, b.length);
    }

    private byte[] loadClassData(String name) {
        // Load the class data from the connection
        return new byte[0];
    }
}

public class CustomClassLoaderExample {
    public static void main(String[] args) throws Exception {
        CustomClassLoader loader = new CustomClassLoader();
        Class<?> clazz = loader.loadClass("MyClass");
        Object obj = clazz

.newInstance();
        System.out.println(obj.getClass().getName());
    }
}
```

- **Class Loader Hierarchy**: Understanding the delegation model (parent-first delegation) can help in diagnosing class loading issues.

```java
public class ClassLoaderHierarchy {
    public static void main(String[] args) {
        ClassLoader classLoader = ClassLoaderHierarchy.class.getClassLoader();
        while (classLoader != null) {
            System.out.println(classLoader);
            classLoader = classLoader.getParent();
        }
    }
}
```

### Memory Management Tools

- **VisualVM**: VisualVM can be launched from the JDK's bin directory and connects to running Java processes to monitor memory usage and performance.

```sh
# Start VisualVM
jvisualvm
```

- **JConsole**: JConsole can be started from the JDK's bin directory to monitor performance and resource consumption.

```sh
# Start JConsole
jconsole
```

- **JProfiler and YourKit**: These are commercial tools, but here is how you can integrate JProfiler with a Java application.

```sh
# Start JProfiler with a Java application
java -agentpath:/path/to/jprofiler/bin/linux-x64/libjprofilerti.so=port=8849,nowait MyApplication
```

### Advanced Garbage Collection (GC) Tuning

- **GC Logs**: Enable GC logging with `-Xlog:gc*` to analyze GC behavior and performance.

```sh
java -Xlog:gc* -jar MyApplication.jar
```

- **GC Tuning Flags**: Example of tuning GC with flags.

```sh
java -XX:NewRatio=2 -XX:SurvivorRatio=8 -XX:MaxGCPauseMillis=200 -jar MyApplication.jar
```

### JVM Monitoring and Profiling

**Java Flight Recorder (JFR)**

```sh
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar MyApplication.jar
```

**Mission Control**

```sh
# Start Mission Control
jmc
```

### Just-In-Time (JIT) Compiler

- **HotSpot Compiler**: Example to demonstrate JIT compilation.

```java
public class JITExample {
    public static void main(String[] args) {
        for (int i = 0; i < 1000000; i++) {
            calculate(i);
        }
    }

    public static int calculate(int value) {
        return value * value;
    }
}
```

- **Tiered Compilation**: Enable tiered compilation.

```sh
java -server -XX:+TieredCompilation -jar MyApplication.jar
```

### Java Memory Model (JMM)

- **Happens-Before Relationship**: Example to demonstrate happens-before.

```java
public class HappensBeforeExample {
    private int value = 0;
    private boolean flag = false;

    public void writer() {
        value = 42;
        flag = true;
    }

    public void reader() {
        if (flag) {
            System.out.println(value); // This will print 42
        }
    }
}
```

- **Volatile Variables**: Example of using volatile variables.

```java
public class VolatileExample {
    private volatile boolean flag = false;

    public void writer() {
        flag = true;
    }

    public void reader() {
        if (flag) {
            System.out.println("Flag is true");
        }
    }
}
```

- **Atomic Classes**: Example of using atomic classes.

```java
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicExample {
    private AtomicInteger counter = new AtomicInteger(0);

    public void increment() {
        counter.incrementAndGet();
    }

    public int getValue() {
        return counter.get();
    }
}
```

### Advanced Native Interface (JNI)

- **Performance Considerations**: Example to demonstrate JNI usage.

```java
public class JNIDemo {
    static {
        System.loadLibrary("nativeLib");
    }

    public native void nativeMethod();

    public static void main(String[] args) {
        new JNIDemo().nativeMethod();
    }
}
```

### JVM Languages

- **Polyglot JVM**: Example of interoperability with Kotlin.

```java
public class KotlinExample {
    public static void main(String[] args) {
        KotlinInteropKt.printMessage("Hello from Java!");
    }
}
```

Kotlin file (KotlinInterop.kt):

```kotlin
fun printMessage(message: String) {
    println(message)
}
```

### Debugging Tools and Techniques

- **jdb**: Example of using `jdb`.

```sh
# Start jdb with a Java application
jdb -attach 8000
```

- **Remote Debugging**: Enable remote debugging.

```sh
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005 -jar MyApplication.jar
```

- **Heap Dumps**: Create heap dumps using `jmap`.

```sh
# Create a heap dump
jmap -dump:live,format=b,file=heapdump.hprof <pid>
```

### Common Performance Pitfalls

- **Excessive Object Creation**: Example to demonstrate excessive object creation.

```java
public class ObjectCreationExample {
    public static void main(String[] args) {
        for (int i = 0; i < 1000000; i++) {
            String s = new String("example");
        }
    }
}
```

- **Large Heap Sizes**: Can result in longer GC pauses.

```sh
# Example to set heap size
java -Xms2g -Xmx4g -jar MyApplication.jar
```

- **Inefficient Synchronization**: Example to demonstrate synchronization issues.

```java
public class SyncExample {
    private int counter = 0;

    public synchronized void increment() {
        counter++;
    }

    public int getCounter() {
        return counter;
    }
}
```

### Secure Coding Practices

- **Class Loader Security**: Example to prevent unauthorized classes from being loaded.

```java
public class SecureClassLoaderExample {
    public static void main(String[] args) {
        System.setSecurityManager(new SecurityManager());
    }
}
```

- **Code Injection Prevention**: Example to validate inputs.

```java
public class InputValidationExample {
    public static void main(String[] args) {
        String userInput = "user input";
        if (userInput.matches("[a-zA-Z0-9]+")) {
            System.out.println("Valid input");
        } else {
            System.out.println("Invalid input");
        }
    }
}
```

### JVM Ecosystem and Community

- **OpenJDK**: The reference implementation of the Java Platform, Standard Edition.
- **AdoptOpenJDK**: Provides prebuilt OpenJDK binaries for various platforms.
- **JCP (Java Community Process)**: Allows the community to participate in the evolution of Java standards.


## Revisit JVM Heap

The **JVM heap** (Java Virtual Machine heap) is a portion of memory used by Java applications to store objects during runtime. Here's a concise breakdown:

---

### 🔹 What is the JVM Heap?

* It is **part of the memory allocated to the JVM** process for dynamic memory allocation.
* All **Java class instances** (objects) and **arrays** are stored in the heap.
* Managed by the **Garbage Collector (GC)**, which reclaims memory used by objects no longer reachable.

---

### 🔹 Heap Structure (in most JVM implementations like HotSpot)

1. **Young Generation (Young Gen):**

   * **Eden Space**: Where new objects are initially allocated.
   * **Survivor Spaces (S0 & S1)**: Hold objects that survive garbage collection in Eden.
   * **Minor GC** is triggered when Young Gen is full.

2. **Old Generation (Tenured Gen):**

   * Stores long-lived objects that survived multiple GCs.
   * **Major GC (or Full GC)** is more expensive and cleans up the Old Gen.

3. **(Optional) Metaspace / PermGen:**

   * Metaspace (Java 8+): Stores class metadata (not part of heap).
   * PermGen (Java ≤7): Older version of metaspace.

### **How Java Garbage Collection (GC) Works: Heap Management**  

Java's **Garbage Collection (GC)** automatically manages memory by reclaiming unused objects in the **heap**. Here’s a breakdown of how it works:

---

## **1. Java Heap Memory Structure**

The heap is divided into **generations**, each optimized for different object lifespans:  

| **Generation**       | **Purpose**                                                                 | **GC Type**               |
|----------------------|----------------------------------------------------------------------------|--------------------------|
| **Young Generation** | Stores short-lived objects (newly created).                                | **Minor GC** (Fast)      |
| - Eden Space         | New objects are allocated here.                                            |                           |
| - Survivor Spaces (S0, S1) | Surviving objects from Eden are moved here (cyclic copying).           |                           |
| **Old Generation**   | Long-lived objects (after surviving multiple Minor GCs).                   | **Major GC** (Slower)    |
| **Metaspace** (Java 8+) | Stores class metadata (replaces PermGen). Not part of heap.            | **Class unloading**      |

---

## **2. How Garbage Collection Works**

### **Step 1: Object Allocation**
- New objects are allocated in **Eden Space**.
- When **Eden fills up**, a **Minor GC** is triggered.

### **Step 2: Minor GC (Young Generation Collection)**
1. **Live objects** in Eden are copied to **Survivor Space (S0 or S1)**.  
2. **Dead objects** are discarded (memory reclaimed).  
3. Objects that survive **multiple Minor GCs** (default: 15) are promoted to the **Old Generation**.  

### **Step 3: Major GC (Old Generation Collection)**
- When the **Old Generation fills up**, a **Major GC** (or **Full GC**) runs.  
- Algorithms like **Mark-Sweep-Compact** or **Concurrent Mark-Sweep (CMS)** are used.  
- **Slower** because it scans the entire heap.  

---

## **3. GC Algorithms (Java HotSpot JVM)**
Different algorithms optimize for **throughput** or **low latency**:

| **GC Algorithm**      | **How It Works**                                                   | **Use Case**               |
|-----------------------|--------------------------------------------------------|---------------------------|
| **Serial GC**         | Single-threaded, stops the world (STW).               | Small apps (low resources) |
| **Parallel GC**       | Multi-threaded Minor/Major GC (default in JDK 8).     | High throughput           |
| **G1 GC** (Garbage-First) | Divides heap into regions, prioritizes garbage-heavy zones (JDK 9+ default). | Balanced latency/throughput |
| **ZGC / Shenandoah**  | Ultra-low pause times (concurrent GC). | Large heaps, real-time apps |

---

## **4. Key Concepts**
- **Stop-The-World (STW):** Pauses application threads during GC.  
- **GC Roots:** Objects always reachable (e.g., static fields, active threads).  
- **Memory Leaks:** Objects unintentionally held in memory (e.g., static `HashMap` caches).  

---

## **5. Monitoring & Tuning**
- **Flags:**  
  ```sh
  -Xms512m -Xmx2G           # Min/max heap size
  -XX:+UseG1GC              # Use G1 GC
  -XX:MaxGCPauseMillis=200  # Target max pause time
  ```
- **Tools:**  
  - `jstat -gc <pid>` (GC stats)  
  - VisualVM, GC logs (`-Xlog:gc*`)  

---

### **Summary**
- **Young Gen (Minor GC):** Fast, frequent collections.  
- **Old Gen (Major GC):** Slower, less frequent.  
- **Choose GC based on:** Latency vs. throughput needs.  

---

### 🔹 JVM Heap Size Options

You can control heap size with the following options when starting the JVM:

| Option       | Description           |
| ------------ | --------------------- |
| `-Xms<size>` | Initial heap size     |
| `-Xmx<size>` | Maximum heap size     |
| `-Xmn<size>` | Size of the Young Gen |

**Example:**

```bash
java -Xms512m -Xmx2g -jar yourapp.jar
```

* Starts with 512MB heap, maxes at 2GB.

---

### 🔹 Monitoring & Tuning Tools

* **VisualVM**
* **JConsole**
* **jstat**, **jmap**, **jstack**
* **Garbage Collection logs**
* **Heap dumps**

---

## GC Tuning

Great! Let’s dive deeper into **Java Garbage Collection (GC)**, covering advanced topics like **GC tuning, log analysis, and real-world optimization strategies**.  

---

## **1. Advanced GC Algorithms**  
### **G1 Garbage Collector (Garbage-First)**
- **Default in Java 9+**, designed for **large heaps** (multi-GB) with **predictable pause times**.  
- **How it works:**  
  - Divides the heap into **equal-sized regions** (1MB–32MB).  
  - Prioritizes regions with the most garbage ("garbage-first").  
  - Uses **concurrent marking** + **compaction** to avoid fragmentation.  
- **Key Flags:**  
  ```sh
  -XX:+UseG1GC                 # Enable G1
  -XX:MaxGCPauseMillis=200     # Target max pause (ms)
  -XX:G1HeapRegionSize=16m     # Region size
  ```

### **ZGC (Z Garbage Collector)**
- **Ultra-low latency** (sub-10ms pauses) for **large heaps** (TB-scale).  
- **Key Features:**  
  - **Concurrent** (no STW for most operations).  
  - Uses **colored pointers** and **load barriers**.  
- **Flags:**  
  ```sh
  -XX:+UseZGC                  # Java 11+ (Linux/macOS)
  -XX:+ZGenerational           # Java 21+ (generational ZGC)
  ```

### **Shenandoah GC**
- Similar to ZGC but **backported to Java 8+**.  
- **Key Features:**  
  - **Concurrent compaction** (no pauses for defragmentation).  
  - Optimized for **multi-core machines**.  
- **Flags:**  
  ```sh
  -XX:+UseShenandoahGC
  -XX:ShenandoahGCHeuristics=adaptive  # Dynamic tuning
  ```

---

## **2. GC Tuning Strategies**  
### **Goal-Based Tuning**
| **Goal**               | **Recommended GC**      | **Key Flags**                          |
|------------------------|------------------------|---------------------------------------|
| **Throughput**         | Parallel GC            | `-XX:+UseParallelGC`                  |
| **Low Latency**        | G1 / ZGC / Shenandoah  | `-XX:+UseZGC -XX:MaxGCPauseMillis=10` |
| **Small Footprint**    | Serial GC              | `-XX:+UseSerialGC`                    |

### **Heap Sizing**
- **Rule of Thumb:**  
  - **Young Gen:** 1/3 of total heap.  
  - **Old Gen:** 2/3 of total heap.  
- **Flags:**  
  ```sh
  -Xms4G -Xmx4G               # Fixed heap (avoids resizing)
  -XX:NewRatio=2              # Old:Young = 2:1
  -XX:SurvivorRatio=8         # Eden:Survivor = 8:1:1
  ```

### **Avoiding Premature Promotion**
- Objects moving **too quickly** to Old Gen cause **frequent Major GCs**.  
- **Fix:** Increase survivor space or adjust `-XX:MaxTenuringThreshold`.  
  ```sh
  -XX:MaxTenuringThreshold=15  # Default (increase to 20)
  ```

---

## **3. Analyzing GC Logs**  
Enable detailed logs to diagnose issues:  
```sh
-XX:+PrintGCDetails -Xlog:gc*:file=gc.log -XX:+UseGCLogFileRotation
```

### **Common GC Problems & Fixes**
| **Symptom**                     | **Cause**                          | **Solution**                          |
|---------------------------------|------------------------------------|---------------------------------------|
| **Frequent Full GCs**           | Old Gen too small / memory leaks   | Increase `-Xmx`, fix leaks            |
| **Long Minor GC Pauses**        | Survivor space too small           | Adjust `-XX:SurvivorRatio`            |
| **High GC Overhead**            | Weak references / finalizers       | Replace `finalize()` with `Cleaner`   |
| **OutOfMemoryError**            | Heap exhaustion / metaspace leak   | Increase `-XX:MetaspaceSize`          |

---

## **4. Real-World Optimization Example**  
### **Scenario:**  
An app has **2-second Full GC pauses** every hour.  

### **Steps to Fix:**  
1. **Enable GC Logging:**  
   ```sh
   -Xlog:gc*,gc+heap=debug:file=gc.log
   ```
2. **Identify the Issue:**  
   - Logs show `Full GC (Allocation Failure)` before OOM.  
   - Old Gen is **99% full** before collection.  
3. **Apply Fixes:**  
   - **Increase heap size:** `-Xmx8G` (from 4G).  
   - **Switch to G1 GC:**  
     ```sh
     -XX:+UseG1GC -XX:MaxGCPauseMillis=200
     ```
   - **Tune Survivor Spaces:**  
     ```sh
     -XX:SurvivorRatio=6 -XX:MaxTenuringThreshold=10
     ```

---

## **5. Tools for GC Analysis**  
| **Tool**          | **Purpose**                              | **Command**                     |
|--------------------|------------------------------------------|---------------------------------|
| **jstat**         | Real-time GC stats                       | `jstat -gc <pid> 1s`            |
| **VisualVM**      | Heap dump analysis                       | `jvisualvm`                     |
| **Eclipse MAT**   | Memory leak detection                    | Analyze `.hprof` dumps          |
| **GCViewer**      | Visualize GC logs                        | Open `gc.log`                   |

---

### **Key Takeaways**  
✅ **Choose GC based on latency/throughput needs** (G1 for balance, ZGC for low latency).  
✅ **Monitor GC logs** to spot issues (long pauses, frequent collections).  
✅ **Tune survivor spaces & heap sizes** to avoid premature promotion.  
✅ **Use tools like `jstat` and VisualVM** for real-time debugging.  


