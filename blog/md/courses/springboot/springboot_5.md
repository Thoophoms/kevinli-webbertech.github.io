# Java Enterprise Development with Springboot - Topic 5 - More on Spring Data, JPA, JPQL

## Part I Warm up with a previous JPA data project

In the #2 class, we have a lab to show you how to run the example from springboot.io about the connection to MySQL database.
In today's first part, we would like to review that project, and pay attention to a few points that project was using,
and we will extend it a little bit to the following topics that we would like to cover in this section.

* JPA's CrudRepository and JPARepository
* JPQL

### Get Springboot configured with MySQL

* Prerequisite: mysql installation and configuration. Refer to our #2 class lab about MySQL access with Springboot.

* git clone https://github.com/spring-guides/gs-accessing-data-jpa.git

* cd into gs-accessing-data-jpa/complete(please skip the initial directory).

* Make sure the resource file called `src/main/resources/application.properties` contains the following,

```java
spring.jpa.generate-ddl=true
spring.jpa.hibernate.ddl-auto=create
spring.jpa.show-sql=true
spring.datasource.url=jdbc:mysql://localhost:3306/db_example
spring.datasource.username=springuser
spring.datasource.password=ThePassword
#spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

Spring Data JPA focuses on using JPA to store data in a relational database. Its most compelling feature is the ability to create repository implementations automatically, at runtime, from a repository interface.

To see how this works, create a repository interface that works with Customer entities as the following listing (in src/main/java/com/example/accessingdatajpa/CustomerRepository.java) shows:

```java
package com.example.accessingdatajpa;

import java.util.List;
import org.springframework.data.repository.CrudRepository;

public interface CustomerRepository extends CrudRepository<Customer, Long> {

  List<Customer> findByLastName(String lastName);

  Customer findById(long id);
}
```

Next add the following part into the above class,

```java
@Bean
  public CommandLineRunner demo(CustomerRepository repository) {
    return (args) -> {
      // save a few customers
      repository.save(new Customer("Jack", "Bauer"));
      repository.save(new Customer("Chloe", "O'Brian"));
      repository.save(new Customer("Kim", "Bauer"));
      repository.save(new Customer("David", "Palmer"));
      repository.save(new Customer("Michelle", "Dessler"));

      // fetch all customers
      log.info("Customers found with findAll():");
      log.info("-------------------------------");
      repository.findAll().forEach(customer -> {
        log.info(customer.toString());
      });
      log.info("");

      // fetch an individual customer by ID
      Customer customer = repository.findById(1L);
      log.info("Customer found with findById(1L):");
      log.info("--------------------------------");
      log.info(customer.toString());
      log.info("");

      // fetch customers by last name
      log.info("Customer found with findByLastName('Bauer'):");
      log.info("--------------------------------------------");
      repository.findByLastName("Bauer").forEach(bauer -> {
        log.info(bauer.toString());
      });
      log.info("");
    };
  }
```

### Build an executable JAR

`./mvnw clean package`

### Run the executable JAR

`./mvnw spring-boot:run`

When you run your application, you should see output similar to the following:

```bash
== Customers found with findAll():
Customer[id=1, firstName='Jack', lastName='Bauer']
Customer[id=2, firstName='Chloe', lastName='O'Brian']
Customer[id=3, firstName='Kim', lastName='Bauer']
Customer[id=4, firstName='David', lastName='Palmer']
Customer[id=5, firstName='Michelle', lastName='Dessler']

== Customer found with findById(1L):
Customer[id=1, firstName='Jack', lastName='Bauer']

== Customer found with findByLastName('Bauer'):
Customer[id=1, firstName='Jack', lastName='Bauer']
Customer[id=3, firstName='Kim', lastName='Bauer']
```

Now let us take a break here and pay attention to the `CustomerRepository` class which is the core of this entire session,
the magic is the above class file is an `interface` that **extends** another built-in interface called `CrudRepository`.

Without writting any real code implementation, this low-code idea allows us to write some function signature here using snake case.
`findByLastName` and `findById`. Note here, one database column is really called "id" and the other one is no doubt called "LastName".

When you did that, it will have the code generation or follow these schema meta information from the naming of the methods to retrieve the builtin database query for you without writing a lot of code. (This is the low-code and no-code concept.)

and if we recall how those were defined, they were defined like the following,

```java
@Entity
public class Customer {

	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Long id;
	private String firstName;
	private String lastName;
}
```

## JpaRepository Usage

In this project, I am going to show you a bit modification basedon the above project with which you could work on your midterm project.

In reality there are many ways to achieve the midterm project. There are many database connection libraries and technologies to achieve the goal so that you could write some queries. JPARepository is one of them the popular ones. Here in the following explanation, I will show you using `JPARepository` to write a native query so you could take advantage of writing native sql query and to use the default builtin queries as well.

### Step 1 set up the datasource

Please pay attention to the last one that I added and see if it works for you.

![Springboot_project_layout.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/Springboot_project_layout.jpg)

Also we could notice here, I try to create a few packages to make our code look cleaner.
This segragation is normally used for database projects where we keep SQL/DB access code into an OO class, thus upper level class just use it without knowing the details of the code. This is an important concept when we do mix programming. Believe or not, SQL in Java it is still a mix-programming paradigm and we want to keep it as clean as possible.

### Step 2 Method chaining pattern

I use a little software design pattern here, and the usage of the method chaining pattern is a modern feature, and it can be further reduced by using Lombok and other builder annoation which we could cover in the future.

![chain_pattern.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/chain_pattern.jpg)

### Step 3 Write some native query in the repository class

Note that we are using JPARepository interface which is a built-in feature of Spring Data project.

![JPA_query.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/JPA_query.jpg)

### Step 4 Service layer

We use service layer to segragate the business logic to make it clean.

![JPA_service.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/JPA_service.jpg)

### Step 5 Using some mapping

These usage and annotations are related to the joins (foreign keys) in the relational databases. In early days, there is an opensource project called Hibernate, and Spring Data incoporate its feature and tries to simply its usage and reduce its installation and configuration.

![JPA_Join1.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/JPA_Join1.jpg)

If I have two classes (vertically they present two database tables), then you could see the usage in each to join the objects on Java level when you make calls to them.

![JPA_join2.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/JPA_join2.jpg)

### Step 6 Initialize some data in our database

Now you can see how we actually create objects and call the related service-level class to save the data to the database without writing some messy SQL code.

![initialize_some_data.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/initialize_some_data.jpg)

### Step 7 Checking the data initalized

![check_data_initalization.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/check_data_initalization.jpg)

Up to here, you should be able to fullfil other endpoints development by exploring your options.