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
