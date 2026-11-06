# Java Stream Tutorial

## Introduction

This tutorial provides an overview of Java Streams, introduced in JDK 8, along with various stream operations and examples.

Streams provide a modern and more concise way to work with collections in Java. They allow for declarative operations on data, making code more expressive and readable.

### Stream Creation

- **Creating Streams from Arrays:**
  - Streams can be created from arrays using `Stream.of()` or by converting arrays to lists and then obtaining a stream.

- **Stream Builder:**
  - Stream builder allows for the dynamic construction of streams by adding elements individually.

- **Converting Streams to Arrays:**
  - Streams can be converted to arrays using the `toArray` method.

### Stream Operations

- **forEach:**
  - `forEach` is used to iterate over elements of a stream and perform an action.

- **peek:**
  - `peek` is similar to `forEach`, but it allows chaining multiple operations together.

- **map:**
  - `map` transforms each element of a stream using a provided function.

- **flatMap:**
  - `flatMap` is used to flatten nested collections within a stream.

- **filter:**
  - `filter` selects elements from a stream based on a specified condition.

- **findFirst and orElse:**
  - `findFirst` returns the first element of a stream, while `orElse` provides a default value if the stream is empty.

- **orElseThrow:**
  - `orElseThrow` throws an exception if the stream is empty.

- **count:**
  - `count` terminal operation returns the number of elements in the stream.

### Method References and Lambdas

- **Method References:**
  - Method references (`System.out::println`) provide a shorthand notation for invoking methods.

- **Lambda Expressions:**
  - Lambda expressions (`e -> e.salaryIncrement(10.0)`) allow for concise function definitions inline.

### Stream Pipelines

- **Pipeline Structure:**
  - A stream pipeline consists of a stream source, followed by zero or more intermediate operations, and a terminal operation.

- **Intermediate and Terminal Operations:**
  - Intermediate operations (e.g., `map`, `filter`) produce a new stream, while terminal operations (e.g., `forEach`, `count`) produce a result or side-effect.

### Short-circuiting Operations

- **Short-circuiting Behavior:**
  - Short-circuiting operations like `findFirst` allow computations on infinite streams to complete in finite time by processing only the necessary elements.

## Code
```java
import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;

public class StreamTutorial {

    static class Employee implements Serializable, Cloneable, Comparable<Employee> {
        int id;
        String name;
        double salary;

        Employee(int id, String name, double salary) {
            this.id = id;
            this.name = name;
            this.salary = salary;
        }

        double salaryIncrement(double increase) {
            this.salary += increase;
            return this.salary;
        }

        @Override
        public String toString() {
            return "Employee{" +
                    "id=" + id +
                    ", name='" + name + '\'' +
                    ", salary=" + salary +
                    '}';
        }

        @Override
        protected Object clone() throws CloneNotSupportedException {
            return super.clone();
        }

        @Override
        public int compareTo(Employee other) {
            return Double.compare(this.salary, other.salary);
        }
    }

    static double scale(double e) {
        return Math.exp(e) + 2;
    }

    public static void main(String[] args) {
        System.out.println("Hello world!");

        Employee[] arrayOfEmps = {
                new Employee(1, "Jeff Bezos", 100000.0),
                new Employee(2, "Bill Gates", 200000.0),
                new Employee(3, "Mark Zuckerberg", 300000.0)
        };

        // create stream from array
        Stream<Employee> s = Stream.of(arrayOfEmps);
        Stream<Employee> s1 = Stream.of(arrayOfEmps[0], arrayOfEmps[1], arrayOfEmps[2]);

        // create stream from array
        List<Employee> empList = Arrays.asList(arrayOfEmps);
        Stream<Employee> s3 = empList.stream();

        // stream builder
        Stream.Builder<Employee> empStreamBuilder = Stream.builder();
        empStreamBuilder.accept(arrayOfEmps[0]);
        empStreamBuilder.accept(arrayOfEmps[1]);
        empStreamBuilder.accept(arrayOfEmps[2]);
        Stream<Employee> s4 = empStreamBuilder.build();

        // toArray
        Employee[] employees = empList.stream().toArray(Employee[]::new);

        // Java Stream Operations

        /*
        * forEach();
        * */
        System.out.println("Test in forEach....");
        empList.stream().forEach(e -> System.out.println(e.salary));
        // or
        empList.stream().forEach(System.out::println);

        /*
        * peek
        *  forEach() is one pass but peek() can chain together multiple operations.
        * */
        System.out.println("Testing in peek....");
        empList.stream()
                .peek(e -> e.salaryIncrement(10.0))
                .peek(System.out::println).forEach(e -> System.out.println(e.salary));
                //.collect(Collectors.toList());

        /*
        map() and collect

        map() produces a new stream after applying a function to each element of the original stream.
        The new stream could be of different type.
        */
        Double[] empIds = { 1d, 2d, 3d };

        List<Double> ids = Stream.of(empIds)
                .map(e -> StreamTutorial.scale(e))
                .collect(Collectors.toList());
        System.out.println(ids);

        List<Double> ids1 = Stream.of(empIds)
                .map(StreamTutorial::scale)
                .collect(Collectors.toList());
        System.out.println(ids1);

        /*
        * flatMap
        * flatMap() helps us to flatten the data structure to simplify further operations
        * */
        List<List<String>> namesNested = Arrays.asList(
                Arrays.asList("Jeff", "Bezos"),
                Arrays.asList("Bill", "Gates"),
                Arrays.asList("Mark", "Zuckerberg"));

        System.out.println("Testing in flatMap....");
        System.out.println("before flatten:\n" + namesNested);
        List<String> namesFlatStream = namesNested.stream()
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
        System.out.println("after flatten:\n" + namesFlatStream);

        /* or */
        List<String> namesFlatStream1 = namesNested.stream()
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
        System.out.println("after flatten:\n" + namesFlatStream1);

        /*
        * filter
        * */
        System.out.println("Testing in filter....");
        List<Double> filtered = Stream.of(empIds)
                .map(e -> StreamTutorial.scale(e))
                .filter(e -> e > 9)
                .collect(Collectors.toList());
        System.out.println(filtered);

        /*
         * findFirst and .orElse
         * */
        System.out.println("Testing in findFirst and orElse....");
        Double findFirst = Stream.of(empIds)
                .map(e -> StreamTutorial.scale(e))
                .filter(e -> e > 9).findFirst().orElse(null);
        System.out.println(findFirst);

        /*
        .orElseThrow()
        * */
        Double findFirstException = Stream.of(empIds)
                .map(e -> StreamTutorial.scale(e))
                .filter(e -> e > 9).findFirst().orElseThrow();
        System.out.println(findFirstException);

        /*Method types and Pipelines
        *
        * A stream pipeline consists of a stream source,
        * followed by zero or more intermediate operations, and a terminal operation.
        *
        * The chained methods are called pipeline.
        *
        * Some operation is intermediate and some are terminal.
        * For example, filter() is the intermediate operation and count is the terminal operation:
        * */
        System.out.println("Testing in pipeline....");
        Long empCount = empList.stream()
                .filter(e -> e.salary > 200000) // Intermediate operation: filter
                .count(); // Terminal operation: count
        System.out.println(empCount);

        /*
        * short-circuiting operations
        * Short-circuiting operations allow computations on infinite streams to complete in finite time
        * */
        System.out.println("Testing short-circuiting operations....");
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Example of short-circuiting operation: findFirst
        Integer first = numbers.stream()
                .filter(n -> n > 5)
                .findFirst()
                .orElse(null);
        System.out.println("First number greater than 5: " + first);

        // Example of short-circuiting operation: limit
        List<Integer> limitedNumbers = numbers.stream()
                .limit(5)
                .collect(Collectors.toList());
        System.out.println("First 5 numbers: " + limitedNumbers);

        /*
        * Infinite stream with short-circuiting
        * */
        Stream<Integer> infiniteStream = Stream.iterate(1, n -> n + 1);
        List<Integer> firstTen = infiniteStream
                .limit(10)
                .collect(Collectors.toList());
        System.out.println("First 10 numbers of infinite stream: " + firstTen);

        /*
        * Demonstrating Serializable
        * */
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("employees.ser"))) {
            out.writeObject(arrayOfEmps);
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("employees.ser"))) {
            Employee[] deserializedEmps = (Employee[]) in.readObject();
            System.out.println("Deserialized employees: " + Arrays.toString(deserializedEmps));
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        /*
        * Demonstrating Cloneable
        * */
        try {
            Employee original = new Employee(4, "Sundar Pichai", 400000.0);
            Employee cloned = (Employee) original.clone();
            System.out.println("Original: " + original);
            System.out.println("Cloned: " + cloned);
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }

        /*
        * Demonstrating Comparable
        * */
        List<Employee> sortedEmps = empList.stream()
                .sorted()
                .collect(Collectors.toList());
        System.out.println("Sorted employees by salary: " + sortedEmps);

        /*
        * Demonstrating Predicate<T>
        * */
        System.out.println("Demonstrating Predicate...");
        Predicate<Employee> salaryPredicate = e -> e.salary > 150000;
        List<Employee> filteredEmployees = empList.stream()
                .filter(salaryPredicate)
                .collect(Collectors.toList());
        System.out.println("Employees with salary > 150000: " + filteredEmployees);

        /*
        * Demonstrating Function<T, R>
        * */
        System.out.println("Demonstrating Function...");
        Function<Employee, String> employeeNameFunction = Employee::getName;
        List<String> employeeNames = empList.stream()
                .map(employeeNameFunction)
                .collect(Collectors.toList());
        System.out.println("Employee names: " + employeeNames);

        /*
        * Demonstrating Consumer<T>
        * */
        System.out.println("Demonstrating Consumer...");
        Consumer<Employee> salaryIncrementConsumer = e -> e.salaryIncrement(5000);
        empList.forEach(salaryIncrementConsumer);
        System.out.println("Employees after salary increment: " + empList);

        /*
        * Demonstrating Supplier<T>
        * */
        System.out.println("Demonstrating Supplier...");
        Supplier<Employee> employeeSupplier = () -> new Employee(5, "Larry Page", 500000.0);
        Employee newEmployee = employeeSupplier.get();
        System.out.println("New Employee: " + newEmployee);

        /*
        * Demonstrating BiConsumer<T, U>
        * */
        System.out.println("Demonstrating BiConsumer...");
        BiConsumer<Employee, Double> salaryBiConsumer = (e, increment) -> e.salaryIncrement(increment);
        empList.forEach(e -> salaryBiConsumer.accept(e, 10000.0));
        System.out.println("Employees after BiConsumer salary increment: " + empList);

        /*
        * Demonstrating UnaryOperator<T>
        * */
        System.out.println("Demonstrating UnaryOperator...");
        UnaryOperator<Double> salaryUnaryOperator = salary -> salary * 1.1;
        List<Double> updatedSalaries = empList.stream()
                .map(Employee::getSalary)
                .map(salaryUnaryOperator)
                .collect(Collectors.toList());
        System.out.println("Updated Salaries: " + updatedSalaries);

        /*
        * Demonstrating BinaryOperator<T>
        * */
        System.out.println("Demonstrating BinaryOperator...");
        BinaryOperator<Double> salaryBinaryOperator = Double::sum;
        Double totalSalary = empList.stream()
                .map(Employee::getSalary)
                .reduce(0.0, salaryBinaryOperator);
        System.out.println("Total Salary: " + totalSalary);

        /*
        * Demonstrating Collector<T, A, R>
        * */
        System.out.println("Demonstrating Collector...");
        Collector<Employee, ?, Map<Integer, String>> employeeCollector = Collectors.toMap(Employee::getId, Employee::getName);
        Map<Integer, String> employeeMap = empList.stream()
                .collect(employeeCollector);
        System.out.println("Employee Map: " + employeeMap);

        /*
        * Demonstrating ToIntFunction<T>
        * */
        System.out.println("Demonstrating ToIntFunction...");
        ToIntFunction<Employee> toIntFunction = e -> (int) e.getSalary();
        List<Integer> intSalaries = empList.stream()
                .mapToInt(toIntFunction)
                .boxed()
                .collect(Collectors.toList());
        System.out.println("Int Salaries: " + intSalaries);

        /*
        * Demonstrating ToLongFunction<T>
        * */
        System.out.println("Demonstrating ToLongFunction...");
        ToLongFunction<Employee> toLongFunction = e -> (long) e.getSalary();
        List<Long> longSalaries = empList.stream()
                .mapToLong(toLongFunction)
                .boxed()
                .collect(Collectors.toList());
        System.out.println("Long Salaries: " + longSalaries);

        /*
        * Demonstrating ToDoubleFunction<T>
        * */
        System.out.println("Demonstrating ToDoubleFunction...");
        ToDoubleFunction<Employee> toDoubleFunction = Employee::getSalary;
        List<Double> doubleSalaries = empList.stream()
                .mapToDouble(toDoubleFunction)
                .boxed()
                .collect(Collectors.toList());
        System.out.println("Double Salaries: " + doubleSalaries);
    }
}
```



#### References
https://stackify.com/streams-guide-java-8/
https://openjdk.org/projects/amber/
https://wiki.openjdk.org/display/loom/Main
https://openjdk.org/projects/panama/
