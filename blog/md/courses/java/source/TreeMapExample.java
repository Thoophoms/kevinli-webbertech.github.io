package com.webbertech.java;

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.TreeMap;

/*
 * TreeMap is Red-Black tree based NavigableMap implementation. It is sorted according to the natural ordering of its keys.
	TreeMap class implements Map interface similar to HashMap class. 
	The main difference between them is that HashMap is an unordered collection while TreeMap is sorted in the ascending order of its keys. 
	TreeMap is unsynchronized collection class which means it is not suitable for thread-safe operations until unless synchronized explicitly.
 * 
 * LinkedHashMap will preserve the order it was inserted while TreeMap will sort it.
 * */

public class TreeMapExample {
	public static void main(String args[]) {
		HashMap<Integer, String> hm = new HashMap<Integer, String>();
		hm.put(1, "Data1");
		hm.put(23, "Data2");
		hm.put(70, "Data3");
		hm.put(4, "Data4");
		hm.put(2, "Data5");
		
		System.out.println("The following is HashMap:");
		for (Entry<Integer, String> m : hm.entrySet()) {
			System.out.println(m.getKey() + " " + m.getValue());
		}
		
		TreeMap<Integer, String> tmap = new TreeMap<>(hm);
		System.out.println("The following is TreeMap:");
		for (Entry<Integer, String> m : tmap.entrySet()) {
			System.out.println(m.getKey() + " " + m.getValue());
		}
	}	
}