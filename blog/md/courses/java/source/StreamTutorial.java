package com.webbertech.java;

/*
@author kevinli
@created 3/29/24

Stream was introduced in JDK8
*/

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class StreamTutorial {

    static class Employee {
        int id;
        String name;
        double salary;

        Employee(int id, String name, double salary) {
            this.id = id;
            this.name = name;
            this.salary = salary;
        }

        double salaryIncrement(double increase) {
            return salary + increase;
        }
    }

    static double scale(double e) {
        return Math.exp(e)+2;
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
        System.out.println("Testing in Pee....");
        empList.stream()
                .peek(e -> e.salaryIncrement(10.0))
                .peek(System.out::println).forEach(e->System.out.println(e.salary));
                //.collect(Collectors.toList());

        /*
        map() and collect

        map() produces a new stream after applying a function to each element of the original stream.
        The new stream could be of different type.
        */
        Double[] empIds = { 1d, 2d, 3d };

        List<Double> ids = Stream.of(empIds)
                .map(e-> StreamTutorial.scale(e))
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
        System.out.println("after flatten:\n" + namesFlatStream);


        /*
        * filter
        * */
        System.out.println("Testing in filter....");
        List<Double> filtered = Stream.of(empIds)
                .map(e-> StreamTutorial.scale(e))
                .filter(e -> e > 9)
                .collect(Collectors.toList());
        System.out.println(filtered);

        /*
         * findFirst and .orElse
         * */
        System.out.println("Testing in findFirst and orElse....");
        Double findFirst = Stream.of(empIds)
                .map(e-> StreamTutorial.scale(e))
                .filter(e -> e > 9).findFirst().orElse(null);
        System.out.println(findFirst);

        /*
        .orElseThrow()
        * */
        Double findFirstException = Stream.of(empIds)
                .map(e-> StreamTutorial.scale(e))
                .filter(e -> e > 9).findFirst().orElseThrow();
        System.out.println(findFirst);

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
                .filter(e -> e.salary> 200000)
                .count();
        System.out.println(empCount);

        /*
        * short-circuiting operations
        * Short-circuiting operations allow computations on infinite streams to complete in finite time
        * */

        //https://stackify.com/streams-guide-java-8/
        // https://openjdk.org/projects/amber/
        // https://wiki.openjdk.org/display/loom/Main
        // https://openjdk.org/projects/panama/
    }
}