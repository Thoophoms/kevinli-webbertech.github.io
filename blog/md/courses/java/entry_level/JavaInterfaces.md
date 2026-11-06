# Important Java built-in interfaces

**Serializable**

The class implementing java.io.Serializable interface enables its objects to be serialized. This interface doesn’t have any method. Such an interface is called Marker Interface.

If the classes need to handle the serialization and deserialization in a different way, the class implementing java.io.Serializable must implement special method.

`private void writeObject(java.io.ObjectOutputStream out) throws IOException`

`private void readObject(java.io.ObjectInputStream in) throws IOException, ClassNotFoundException;`

`private void readObjectNoData() throws ObjectStreamException;`

**Cloneable**

The class that implements java.lang.Cloneable assures that it conforms to the contract of Object.clone() method to copy the instances of the class.

**Iterable**

Implementing this interface allows an object to be the target of the foreach statement.

**Comparable**

By implementing this interface, the class has the opportunity to compare the object with another specified object conforming to the order.

**Runnable**

This interface is mainly used to facilitate users to provide Thread Task definition. The difficulty of using this SAM interface for Thread Task Definition is that it doesn’t return any value.

**Callable**

This interface is also used to provide Thread Task definition in a parameterized way which has the capability to return the computed value as well.

**Readable**

If a class implements java.lang.Readable assures that it provides source of characters to read from. The user can read the source of characters using its read() method.

**Appendable**

This java.lang.Appendable interface specifies the contract to append character values to the implementing class object. As an example, the widely used java.lang.StringBuffer and java.lang.StringBuilder implement this interface to mutate the sequence of characters.

**Closeable**

java.io.Closeable interface provides the contract for the user to close a source or a destination of data. It declares its contract through close() method which is invoked to release the currently acquired resources.

**AutoCloseable**

java.io.AutoCloseable has been introduces lately in Java 1.7 which ensures the source or destination of data implementing java.io.AutoCloseable interface can be used in accordance with try with resources block. The benefit of using try with resources block is that it automatically closes the data source and it releases the current resources.

**Observable**

This class ensures an object to be monitored in the Model-View Controller programming paradigm.

**Repeatable**

This is basically an annotation which has been introduced in Java 8. This annotation ensures to use it multiple times as mentioned below.

```java
public final class Sample {

	@Repeatable(value = Fruits.class)
	public @interface Place {
		String value();
	}

	@Retention(RetentionPolicy.RUNTIME)
	public @interface TechnicalUniversities {
		Place[] value() default {};
	}

	@Place("Apple")
	@Place("Orange")
	@Place("Pear")
	@Place("Kiwi")
	public interface Fruits {
	};
}
```

Prior to Java 8, we could achieve the same by annotating TechnicalUniversity interface with an array of Places which looks a bit cluttered.

Synchronizable : Not available but wish it were

In a DZone Java entry by Lucas Eder, it has been mentioned that it could have been in the JDK if Java has been developed today.

Just to give you a glimpse of it, in Java we hardly use the Synchronized modifier

```java
public synchronized void func1() {}
public void func2() {
    synchronized (this) {
      //logic
    }
}
```

This modifier is unnecessary at the method level as we need to synchronize a block of code. Hence, we mostly write the following way.

```java
public final class Sample {

	private final Object LOCK = new Object();

	private void func() {
		synchronized (this.LOCK) {
			// actual logic
		}
	}
}
```

So, if we try to rewrite the same using the following version of code, it would work.

```java
public final class Sample {

	private void func() {
		synchronized ("LOCK") {
			// actual logic
		}
	}
}
```
