package com.webbertech.java;

import java.util.Arrays;
import java.util.List;

public class MethodReference {
	public static void main(String args[]) {
		  // This is the usage of a convenient util
	      List<String> names = Arrays.asList("Mahesh","Suresh","Ramesh","Naresh","Kalpesh");
	      
	      // The following line is the usage of the method reference
	      names.forEach(System.out::println);
	}
}