# Java Clonable Interface

This Java program demonstrates shallow and deep cloning techniques using the `clone()` method and constructors.

## Introduction

Cloning in Java refers to creating an exact copy of an object. This example showcases how to perform both shallow and deep cloning for objects of type `EmployeeA` and `EmployeeB`. Shallow cloning creates a new object with a copy of the fields, while deep cloning creates a new object with copies of all mutable fields.

## Code Overview

```java
package com.webbertech.java;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

// Shallow copy example
class EmployeeA implements Cloneable {
    // Class definition
}

class EmployeeB implements Cloneable {
    // Class definition
    
    // Deep clone
    public Object clone() throws CloneNotSupportedException {
        // Clone implementation
    }
    
    // Constructor clone
    public EmployeeB() throws CloneNotSupportedException {
        // Clone implementation
    }
}

public class JavaClone {
    public static void main(String[] args) throws CloneNotSupportedException {
        // Main method
    }
}
