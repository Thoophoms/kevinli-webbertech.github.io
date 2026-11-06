package com.webbertech.java;

import java.util.ArrayList;
import java.util.List;

public class GenericsBoundExample {

/*
 * Unbounded Wildcards: ?
 * 
 * The following does not work and 
 * neither does it work if you use List<?> as function argument.
 * 
 * 	List<?> stuff = new ArrayList<>();
			stuff.add("abc");
			stuff.add(new Object());
			stuff.add(3);
			int numElements = stuff.size();
			
			
    Upper bound
    List<? extends Number> 

    Lower bound
       List<? super Object> 
    The example below will work, because no class will be the super class of object, so
    it has to be object itself.
    
    
    Multiple bounds

One final note before looking at examples from the Java 8 API. A type parameter can have multiple bounds. The bounds are separated by an ampersand when they are defined.

T extends Runnable & AutoCloseable

You can have as many interface bounds as you like, but only one can be a class. If you have a class as a bound, it must be first in the list.

PECS
The term PECS stands for "Producer Extends, Consumer Super", which is an odd acronym coined by Joshua Block in his Effective Java book but provides a mnemonic on what to do. It means that if a parameterized type represents a producer, use extends. If it represents a consumer, use super. If the parameter is both, don’t use wildcards at all — the only type that satisfies both requirements is the explicit type itself.

The advice boils down to:

Use extends when you only get values out of a data structure

Use super when you only put values into a data structure

Use an explicit type when you plan to do both

 * */

	public static void main(String[] args) {
		List<? super Object> stuff = new ArrayList<>();
		stuff.add("abc");
		stuff.add(new Object());
		stuff.add(3);
		stuff.forEach(System.out::println);
		
		// Lower bound example
		List<? super Number> stuff1 = new ArrayList<>();
		stuff1.add(1);
		stuff1.add(1.2D);
		stuff1.forEach(System.out::println);
		
		List<? extends Number> stuff2 = new ArrayList<>();
		//stuff2.add(1); you can't do this as when it extracts, it does not know what type it is.
		//stuff2.add(1.2D);
		stuff2.forEach(System.out::println);
	}
}
