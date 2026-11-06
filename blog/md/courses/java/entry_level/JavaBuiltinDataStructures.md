# Builtin Data Structures

## Java LinkedHashMap Example

This example demonstrates the use of `LinkedHashMap` in Java. It highlights how `LinkedHashMap` maintains insertion order and handles `null` values as keys.


```java
package com.webbertech.java;

import java.util.*;

/*
 * 1/ LinkedHashMap keeps the order
 * 2/ Accepted the null, and one null as key
 * */

public class LinkedHashMapExample {

    public LinkedHashMapExample() {
        // TODO Auto-generated constructor stub
    }

    public static void main(String args[]) {

        LinkedHashMap<Integer, String> hm = new LinkedHashMap<Integer, String>();

        hm.put(100, "Amit");
        hm.put(100, "Amitxxxx");
        hm.put(101, "Vijay");
        hm.put(102, "Rahul");
        hm.put(null, "Rahul");
        hm.put(null, "Rahulxxx");

        for (Map.Entry m : hm.entrySet()) {
            System.out.println(m.getKey() + " " + m.getValue());
        }
        System.out.println(hm.size());
    }
}
```

## TreeMap

This example demonstrates the differences between `HashMap` and `TreeMap` in Java, focusing on their ordering properties. `HashMap` and `TreeMap` are both implementations of the `Map` interface in Java. However, they have different characteristics in terms of ordering and performance.

### HashMap

- `HashMap` is an unordered collection that stores key-value pairs.
- It uses hash table data structure to store elements.
- The elements are not sorted in any particular order.
- It offers constant-time performance for basic operations (add, remove, get), assuming the hash function disperses elements properly.

### TreeMap

- `TreeMap` is a Red-Black tree-based implementation of the `NavigableMap` interface.
- It stores key-value pairs in sorted order based on the natural ordering of its keys.
- The elements are sorted in ascending order of their keys.
- It provides guaranteed log(n) time cost for the containsKey, get, put, and remove operations.

### TreeMap Example

The `TreeMapExample` class demonstrates the usage of `HashMap` and `TreeMap`, showcasing their differences in ordering:

```java
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.TreeMap;

public class TreeMapExample1 {
    public static void main(String args[]) {
        // Creating HashMap
        HashMap<Integer, String> hm = new HashMap<Integer, String>();
        hm.put(1, "Data1");
        hm.put(23, "Data2");
        hm.put(70, "Data3");
        hm.put(4, "Data4");
        hm.put(2, "Data5");
        
        // Printing HashMap
        System.out.println("HashMap:");
        for (Entry<Integer, String> m : hm.entrySet()) {
            System.out.println(m.getKey() + " " + m.getValue());
        }
        
        // Creating TreeMap from HashMap
        TreeMap<Integer, String> tmap = new TreeMap<>(hm);
        
        // Printing TreeMap
        System.out.println("TreeMap:");
        for (Entry<Integer, String> m : tmap.entrySet()) {
            System.out.println(m.getKey() + " " + m.getValue());
        }
    }   
}
```

### TreeMap Example with Custom Objects

This example demonstrates the usage of `TreeMap` with custom objects (`Dog`) as keys.
`TreeMap` is a sorted map implementation in Java, where keys are ordered based on their natural ordering or a custom comparator. This example showcases how to use `TreeMap` with custom objects and provides insights into how the sorting mechanism works.

The `TreeMapExample2` class contains the main method to demonstrate the usage of `TreeMap` with custom objects:

```java
package com.webbertech.java;

import java.util.Map.Entry;
import java.util.TreeMap;

public class TreeMapExample2 {

    public static void main(String[] args) {
        Dog d1 = new Dog("red", 30);
        Dog d2 = new Dog("black", 20);
        Dog d3 = new Dog("white", 10);
        Dog d4 = new Dog("white", 10);
        
        TreeMap<Dog, Integer> treeMap = new TreeMap<>();
        treeMap.put(d1, 10);
        treeMap.put(d2, 15);
        treeMap.put(d3, 5);
        treeMap.put(d4, 20);
        
        for (Entry<Dog, Integer> entry : treeMap.entrySet()) {
            System.out.println(entry.getKey() + " - " + entry.getValue());
        }
    }
}

class Dog implements Comparable<Dog> {
    String color;
    int size;

    Dog(String c, int s) {
        color = c;
        size = s;
    }

    public String toString() {
        return color + " dog";
    }

    @Override
    public int compareTo(Dog o) {
        return o.size - this.size;
    }
}
```