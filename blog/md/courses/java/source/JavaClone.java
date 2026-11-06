package com.webbertech.java;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

// Shallow copy example
class EmployeeA implements Cloneable {

	private int id;
	private String name;
	private Map<String, String> props;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Map<String, String> getProps() {
		return props;
	}

	public void setProps(Map<String, String> p) {
		this.props = p;
	}

	@Override
	public Object clone() throws CloneNotSupportedException {
		return super.clone();
	}
}

class EmployeeB implements Cloneable {

	private int id;
	private String name;
	private Map<String, String> props;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Map<String, String> getProps() {
		return props;
	}

	public void setProps(Map<String, String> p) {
		this.props = p;
	}

	
	// Deep clone
	public Object clone() throws CloneNotSupportedException {

		Object obj = super.clone(); // utilize clone Object method

		EmployeeB emp = (EmployeeB) obj;

		// Deep cloning for immutable fields
		emp.setProps(null);
		Map<String, String> hm = new HashMap<>();
		String key;
		Iterator<String> it = this.props.keySet().iterator();
		
		// Deep Copy of field by field
		while (it.hasNext()) {
			key = it.next();
			hm.put(key, this.props.get(key));
		}
		emp.setProps(hm);

		return emp;
	}
	
	
	// You can use constructor to clone as well
	public EmployeeB() throws CloneNotSupportedException {

		Object obj = super.clone(); // utilize clone Object method

		EmployeeB emp = (EmployeeB) obj;

		// deep cloning for immutable fields
		emp.setProps(null);
		Map<String, String> hm = new HashMap<>();
		String key;
		Iterator<String> it = this.props.keySet().iterator();
		// Deep Copy of field by field
		while (it.hasNext()) {
			key = it.next();
			hm.put(key, this.props.get(key));
		}
		emp.setProps(hm);
	}
}

public class JavaClone {

	public static void main(String[] args) throws CloneNotSupportedException {
		EmployeeA emp = new EmployeeA();

		emp.setId(1);
		emp.setName("Pankaj");
		Map<String, String> props = new HashMap<>();
		props.put("salary", "10000");
		props.put("city", "Bangalore");
		emp.setProps(props);

		EmployeeA clonedEmp = (EmployeeA) emp.clone();

		// Check whether the emp and clonedEmp attributes are same or different
		System.out.println("emp and clonedEmp == test: " + (emp == clonedEmp));

		System.out.println("emp and clonedEmp HashMap == test: " + (emp.getProps() == clonedEmp.getProps()));

		// Let's see the effect of using default cloning

		// change emp props
		emp.getProps().put("title", "CEO");
		emp.getProps().put("city", "New York");
		System.out.println("clonedEmp props:" + clonedEmp.getProps());

		// change emp name
		emp.setName("new");
		System.out.println("clonedEmp name:" + clonedEmp.getName());

		props.put("city", "shanghai");
		System.out.println("clonedEmp props:" + clonedEmp.getProps());
	}
}
