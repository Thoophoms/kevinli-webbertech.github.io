# Java Optional

Purpose: Avoids `NullPointerException` by offering a container that may or may not hold a non-null value. Simplifies null checking and handling absent values in a more elegant and less error-prone manner.

## `IfPresent`

This example demonstrates the usage of the `Optional` class in Java, specifically focusing on the `ifPresent` method. The `ifPresent` method allows executing a block of code only if the `Optional` contains a non-null value.

```java
package com.webbertech.java;
import java.util.Optional;

public class OptionalIfPresentExample {

    public OptionalIfPresentExample() {
        // TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {

        Optional<String> gender = Optional.of("MALE");
        Optional<String> emptyGender = Optional.empty();

        if (gender.isPresent()) {
            System.out.println("Value available.");
        } else {
            System.out.println("Value not available.");
        }

        gender.ifPresent(g -> System.out.println("In gender Option, value available."));

        // condition failed, no output print
        emptyGender.ifPresent(g -> System.out.println("In emptyGender Option, value available."));

    }

}
```

## `IfPresentOrElse`

```java
import java.util.Optional;

public class IfPresentOrElseExample {
    public static void main(String[] args) {
        Optional<String> optional = Optional.ofNullable(getValue());
        optional.ifPresentOrElse(
            value -> System.out.println("Value is: " + value),
            () -> System.out.println("Value is not present")
        );
    }

    private static String getValue() {
        return null; // or return some value
    }
}
```

## `orElse` and `orElseGet`

This example demonstrates the usage of the `orElse` and `orElseGet` methods of the `Optional` class in Java. These methods provide a way to specify a default value to return if the `Optional` is empty.

```java
package com.webbertech.java;

import java.util.Optional;

public class OptionalOrElseExample {

    public OptionalOrElseExample() {
        // TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {

        Optional<String> gender = Optional.of("MALE");
        Optional<String> emptyGender = Optional.empty();

        System.out.println(gender.orElse("<N/A>")); // MALE
        System.out.println(emptyGender.orElse("<N/A>")); // <N/A>

        System.out.println(gender.orElseGet(() -> "<N/A>")); // MALE
        System.out.println(emptyGender.orElseGet(() -> "<N/A>")); // <N/A>

    }

}
```

## Optional Filter

This example demonstrates the use of the `Optional` class in Java, particularly the `filter` method, which allows conditional processing of the contained value.

```java
package com.webbertech.java;

import java.util.Optional;

public class OptionalFilterExample {

    public OptionalFilterExample() {
        // TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {

        Optional<String> gender = Optional.of("MALE");
        Optional<String> emptyGender = Optional.empty();

        // Filter on Optional
        System.out.println(gender.filter(g -> g.equals("male"))); // Optional.empty
        System.out.println(gender.filter(g -> g.equalsIgnoreCase("MALE"))); // Optional[MALE]
        System.out.println(emptyGender.filter(g -> g.equalsIgnoreCase("MALE"))); // Optional.empty

    }
}
```

## Optional FlatMap

This example demonstrates the usage of `Optional` in Java, particularly focusing on the `map` and `flatMap` methods. These methods allow transforming the value contained within an `Optional` in different ways, depending on whether the transformation produces another `Optional`.

```java
package com.webbertech.java;

import java.util.Optional;

public class OptionalFlatMapExample {

    public OptionalFlatMapExample() {
        // TODO Auto-generated constructor stub
    }

    public static void main(String[] args) {

        Optional<String> nonEmptyGender = Optional.of("male");
        Optional<String> emptyGender = Optional.empty();

        System.out.println("Non-Empty Optional:: " + nonEmptyGender.map(String::toUpperCase));
        System.out.println("Empty Optional    :: " + emptyGender.map(String::toUpperCase));

        Optional<Optional<String>> nonEmptyOptionalGender = Optional.of(Optional.of("male"));
        System.out.println("Optional value   :: " + nonEmptyOptionalGender);
        System.out.println("Optional.map     :: " + nonEmptyOptionalGender.map(gender -> gender.map(String::toUpperCase)));
        System.out.println("Optional.flatMap :: " + nonEmptyOptionalGender.flatMap(gender -> gender.map(String::toUpperCase)));

    }

}
```
