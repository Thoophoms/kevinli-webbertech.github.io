# Java Enterprise Development with Springboot - Topic 2- Data Access

## Outline of today's Lab

* Mysql Configuration
* GemFire cache
* MongoDB
* Neo4j

## Lab 1 Accessing data with MySQL

### Build the project

Download and unzip the source repository for this guide, or clone it using Git: 

* git clone https://github.com/spring-guides/gs-accessing-data-mysql.git

* cd into gs-accessing-data-mysql/initial

* Install mysql

- https://dev.mysql.com/downloads/installer/

* Login to your mysql from commandline
![mysql login](https://kevinli-webbertech.github.io/blog/images/springboot/mysql_login.png)

* Configure and start mysql

```
mysql> create database db_example; -- Creates the new database
mysql> create user 'springuser'@'%' identified by 'ThePassword'; -- Creates the user
mysql> grant all on db_example.* to 'springuser'@'%'; -- Gives all privileges to the new user on the newly created database
```

For the above commands, you should see them like the following,

![mysql login](https://kevinli-webbertech.github.io/blog/images/springboot/mysql.png)

* Security Changes

The following command revokes all the privileges from the user associated with the Spring application:

`mysql> revoke all on db_example.* from 'springuser'@'%';`

Now the Spring application cannot do anything in the database.

The application must have some privileges, so use the following command to grant the minimum privileges the application needs:

`GRANT ALL PRIVILEGES ON db_example.* TO 'springuser'@'%';`

* Create a resource file called `src/main/resources/application.properties`

```java
spring.jpa.generate-ddl=true
spring.jpa.hibernate.ddl-auto=create
spring.jpa.show-sql=true
spring.datasource.url=jdbc:mysql://localhost:3306/db_example
spring.datasource.username=springuser
spring.datasource.password=ThePassword
#spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
```

Here, spring.jpa.hibernate.ddl-auto can be none, update, create, or create-drop. See the Hibernate documentation for details.

* none: The default for MySQL. No change is made to the database structure.

* update: Hibernate changes the database according to the given entity structures.

* create: Creates the database every time but does not drop it on close.

* create-drop: Creates the database and drops it when SessionFactory closes.

You must begin with either create or update, because you do not yet have the database structure. After the first run, you can switch it to update or none, according to program requirements. Use update when you want to make some change to the database structure.

The default for H2 and other embedded databases is create-drop. For other databases, such as MySQL, the default is none.

* Create the @Entity Model

You need to create the entity model, as the following listing (in `src/main/java/com/example/accessingdatamysql/User.java`) shows:

```java
package com.example.accessingdatamysql;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity // This tells Hibernate to make a table out of this class
public class User {
  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Integer id;

  private String name;

  private String email;

  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }
}

```

`Hibernate` automatically translates the entity into a table.

* Create the Repository

You need to create the repository that holds user records, as the following listing (in src/main/java/com/example/accessingdatamysql/UserRepository.java) shows:

```java
package com.example.accessingdatamysql;

import org.springframework.data.repository.CrudRepository;

import com.example.accessingdatamysql.User;

// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

public interface UserRepository extends CrudRepository<User, Integer> {

}
```

Spring automatically implements this repository interface in a bean that has the same name (with a change in the case — it is called userRepository).

* Create a Controller

You need to create a controller to handle HTTP requests to your application, as the following listing (in src/main/java/com/example/accessingdatamysql/MainController.java) shows:

```java
package com.example.accessingdatamysql;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // This means that this class is a Controller
@RequestMapping(path="/demo") // This means URL's start with /demo (after Application path)
public class MainController {
  @Autowired // This means to get the bean called userRepository
         // Which is auto-generated by Spring, we will use it to handle the data
  private UserRepository userRepository;

  @PostMapping(path="/add") // Map ONLY POST Requests
  public @ResponseBody String addNewUser (@RequestParam String name
      , @RequestParam String email) {
    // @ResponseBody means the returned String is the response, not a view name
    // @RequestParam means it is a parameter from the GET or POST request

    User n = new User();
    n.setName(name);
    n.setEmail(email);
    userRepository.save(n);
    return "Saved";
  }

  @GetMapping(path="/all")
  public @ResponseBody Iterable<User> getAllUsers() {
    // This returns a JSON or XML with the users
    return userRepository.findAll();
  }
}
```

The preceding example explicitly specifies POST and GET for the two endpoints. By default, @RequestMapping maps all HTTP operations.

* Create an Application Class

Spring Initializr creates a simple class for the application. The following listing shows the class that Initializr created for this example (in src/main/java/com/example/accessingdatamysql/AccessingDataMysqlApplication.java):

```java
package com.example.accessingdatamysql;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AccessingDataMysqlApplication {

  public static void main(String[] args) {
    SpringApplication.run(AccessingDataMysqlApplication.class, args);
  }

}
```

For this example, you need not modify the AccessingDataMysqlApplication class.

@SpringBootApplication is a convenience annotation that adds all of the following:

- @Configuration: Tags the class as a source of bean definitions for the application context.

- @EnableAutoConfiguration: Tells Spring Boot to start adding beans based on classpath settings, other beans, and various property settings. For example, if spring-webmvc is on the classpath, this annotation flags the application as a web application and activates key behaviors, such as setting up a DispatcherServlet.

- @ComponentScan: Tells Spring to look for other components, configurations, and services in the com/example package, letting it find the controllers.

The main() method uses Spring Boot’s SpringApplication.run() method to launch an application. Did you notice that there was not a single line of XML? There is no web.xml file, either. This web application is 100% pure Java and you did not have to deal with configuring any plumbing or infrastructure.

### Build an executable JAR

`./gradlew build` or `./mvnw clean package`

### Run the executable JAR

* For gradle, it is in `build` dir,

`java -jar build/libs/gs-accessing-data-mysql-0.1.0.jar`

or you can run it with `./gradlew bootRun`

* For maven, it is in `target` dir,

`java -jar target/gs-accessing-data-mysql-0.1.0.jar`

or you can run it with `./mvnw spring-boot:run`


### Test the Application

* `POST localhost:8080/demo/add`

```shell
$ curl http://localhost:8080/demo/add -d name=First -d email=someemail@someemailprovider.com
```

* `GET localhost:8080/demo/all`

 Gets all data.

 `$ curl http://localhost:8080/demo/all`
 
 The reply should be as follows:

[{"id":1,"name":"First","email":"someemail@someemailprovider.com"}]


## Lab 2 Accessing Data with JPA

### Build the project

* git clone https://github.com/spring-guides/gs-accessing-data-jpa.git

* cd into gs-accessing-data-jpa/initial

* Define a Simple Entity

In this example, you store Customer objects, each annotated as a JPA entity. The following listing shows the Customer class (in src/main/java/com/example/accessingdatajpa/Customer.java):

```java
package com.example.accessingdatajpa;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Customer {

  @Id
  @GeneratedValue(strategy=GenerationType.AUTO)
  private Long id;
  private String firstName;
  private String lastName;

  protected Customer() {}

  public Customer(String firstName, String lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  @Override
  public String toString() {
    return String.format(
        "Customer[id=%d, firstName='%s', lastName='%s']",
        id, firstName, lastName);
  }

  public Long getId() {
    return id;
  }

  public String getFirstName() {
    return firstName;
  }

  public String getLastName() {
    return lastName;
  }
}
```

* Create Simple Queries

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

* Create an Application Class

Spring Initializr creates a simple class for the application. The following listing shows the class that Initializr created for this example (in src/main/java/com/example/accessingdatajpa/AccessingDataJpaApplication.java):

```java
package com.example.accessingdatajpa;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AccessingDataJpaApplication {


	private static final Logger log = LoggerFactory.getLogger(AccessingDataJpaApplication.class);


  public static void main(String[] args) {
    SpringApplication.run(AccessingDataJpaApplication.class, args);
  }

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

```
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

## Lab 3 Accessing Data with MongoDB

### Build the project

* git clone https://github.com/spring-guides/gs-accessing-data-mongodb.git
 
* cd into gs-accessing-data-mongodb/initial

* Install and Launch MongoDB

`$ brew install mongodb`

* Start MongoDB Server
`$ mongod`

You should see output similar to the following:

`all output going to: /usr/local/var/log/mongodb/mongo.log`

* Define a Simple Entity
The following listing shows the Customer class (in src/main/java/com/example/accessingdatamongodb/Customer.java):

```java
package com.example.accessingdatamongodb;

import org.springframework.data.annotation.Id;

public class Customer {

  @Id
  public String id;

  public String firstName;
  public String lastName;

  public Customer() {}

  public Customer(String firstName, String lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  @Override
  public String toString() {
    return String.format(
        "Customer[id=%s, firstName='%s', lastName='%s']",
        id, firstName, lastName);
  }

}
```

* Create Simple Queries

To see how this works, create a repository interface that queries Customer documents, as the following listing (in src/main/java/com/example/accessingdatamongodb/CustomerRepository.java) shows:

```java
package com.example.accessingdatamongodb;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface CustomerRepository extends MongoRepository<Customer, String> {

  public Customer findByFirstName(String firstName);
  public List<Customer> findByLastName(String lastName);

}
```

* Create an Application Class

Spring Initializr creates a simple class for the application. The following listing shows the class that Initializr created for this example (in src/main/java/com/example/accessingdatamongodb/AccessingDataMongodbApplication.java):

```java
package com.example.accessingdatamongodb;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AccessingDataMongodbApplication {

  public static void main(String[] args) {
    SpringApplication.run(AccessingDataMongodbApplication.class, args);
  }

}
```

Spring Boot automatically handles those repositories as long as they are included in the same package (or a sub-package) of your @SpringBootApplication class. For more control over the registration process, you can use the @EnableMongoRepositories annotation.

By default, @EnableMongoRepositories scans the current package for any interfaces that extend one of Spring Data’s repository interfaces. You can use its basePackageClasses=MyRepository.class to safely tell Spring Data MongoDB to scan a different root package by type if your project layout has multiple projects and it does not find your repositories.
Spring Data MongoDB uses the MongoTemplate to execute the queries behind your find* methods. You can use the template yourself for more complex queries, but this guide does not cover that. (see the Spring Data MongoDB Reference Guide)

Now you need to modify the simple class that the Initializr created for you. You need to set up some data and use it to generate output. The following listing shows the finished AccessingDataMongodbApplication class (in

```java
package com.example.accessingdatamongodb;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AccessingDataMongodbApplication implements CommandLineRunner {

  @Autowired
  private CustomerRepository repository;

  public static void main(String[] args) {
    SpringApplication.run(AccessingDataMongodbApplication.class, args);
  }

  @Override
  public void run(String... args) throws Exception {

    repository.deleteAll();

    // save a couple of customers
    repository.save(new Customer("Alice", "Smith"));
    repository.save(new Customer("Bob", "Smith"));

    // fetch all customers
    System.out.println("Customers found with findAll():");
    System.out.println("-------------------------------");
    for (Customer customer : repository.findAll()) {
      System.out.println(customer);
    }
    System.out.println();

    // fetch an individual customer
    System.out.println("Customer found with findByFirstName('Alice'):");
    System.out.println("--------------------------------");
    System.out.println(repository.findByFirstName("Alice"));

    System.out.println("Customers found with findByLastName('Smith'):");
    System.out.println("--------------------------------");
    for (Customer customer : repository.findByLastName("Smith")) {
      System.out.println(customer);
    }

  }

}
```

### Build an executable JAR

`/mvnw clean package` 

### Run the executable JAR

`./mvnw spring-boot:run`

As AccessingDataMongodbApplication implements CommandLineRunner, the run method is automatically invoked when Spring Boot starts. You should see something like the following (with other output, such as queries, as well):

```
== Customers found with findAll():
Customer[id=51df1b0a3004cb49c50210f8, firstName='Alice', lastName='Smith']
Customer[id=51df1b0a3004cb49c50210f9, firstName='Bob', lastName='Smith']

== Customer found with findByFirstName('Alice'):
Customer[id=51df1b0a3004cb49c50210f8, firstName='Alice', lastName='Smith']
== Customers found with findByLastName('Smith'):
Customer[id=51df1b0a3004cb49c50210f8, firstName='Alice', lastName='Smith']
Customer[id=51df1b0a3004cb49c50210f9, firstName='Bob', lastName='Smith']
```

## Lab 4 Accessing Data in Pivotal GemFire (issues)

### What You Will build

You will use Spring Data for Apache Geode to store and retrieve POJOs.

 - `git clone https://github.com/spring-guides/gs-accessing-data-gemfire.git`

 - `cd into gs-accessing-data-gemfire/initial`

### Define a Simple Entity

Apache Geode is an `In-Memory Data Grid (IMDG)` that maps data to regions. You can configure distributed regions that partition and replicate data across multiple nodes in a cluster. However, in this guide, we use a LOCAL region so that you need not set up anything extra, such as an entire cluster of servers.

`Apache Geode` is a `key/value store`, and a region implements the java.util.concurrent.ConcurrentMap interface. Though you can treat a region as a java.util.Map, it is quite a bit more sophisticated than just a simple Java Map, given that data is distributed, replicated, and generally managed inside the region.

In this example, you store Person objects in Apache Geode (a region) by using only a few annotations.

`src/main/java/hello/Person.java`

```
package hello;

import java.io.Serializable;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.PersistenceConstructor;
import org.springframework.data.gemfire.mapping.annotation.Region;

import lombok.Getter;

@Region(value = "People")
public class Person implements Serializable {

  @Id
  @Getter
  private final String name;

  @Getter
  private final int age;

  @PersistenceConstructor
  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  @Override
  public String toString() {
    return String.format("%s is %d years old", getName(), getAge());
  }
}
```

### Create Simple Queries

Spring Data for Apache Geode focuses on storing and accessing data in Apache Geode using Spring. It also inherits powerful functionality from the Spring Data Commons project, such as the ability to derive queries. Essentially, you need not learn the query language of Apache Geode (OQL). You can write a handful of methods, and the framework writes the queries for you.

To see how this works, create an interface that queries Person objects stored in Apache Geode:

`src/main/java/hello/PersonRepository.java`

```
package hello;

import org.springframework.data.gemfire.repository.query.annotation.Trace;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {

  @Trace
  Person findByName(String name);

  @Trace
  Iterable<Person> findByAgeGreaterThan(int age);

  @Trace
  Iterable<Person> findByAgeLessThan(int age);

  @Trace
  Iterable<Person> findByAgeGreaterThanAndAgeLessThan(int greaterThanAge, int lessThanAge);

}

```

PersonRepository extends the CrudRepository interface from Spring Data Commons and specifies types for the generic type parameters for both the value and the ID (key) with which the Repository works (Person and String, respectively). This interface comes with many operations, including basic CRUD (create, read, update, delete) and simple query data access operations (such a findById(..)).

You can define other queries as needed by declaring their method signature. In this case, we add findByName, which essentially searches for objects of type Person and finds one that matches on name.

You also have:

- findByAgeGreaterThan: To find people above a certain age

- findByAgeLessThan: To find people below a certain age

- findByAgeGreaterThanAndAgeLessThan: To find people in a certain age range

### Create an Application Class

The following example creates an application class with all the components:

`src/main/java/hello/Application.java`

```
package hello;

import static java.util.Arrays.asList;
import static java.util.stream.StreamSupport.stream;

import org.apache.geode.cache.client.ClientRegionShortcut;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.gemfire.config.annotation.ClientCacheApplication;
import org.springframework.data.gemfire.config.annotation.EnableEntityDefinedRegions;
import org.springframework.data.gemfire.repository.config.EnableGemfireRepositories;

@SpringBootApplication
@ClientCacheApplication(name = "AccessingDataGemFireApplication")
@EnableEntityDefinedRegions(
  basePackageClasses = Person.class,
  clientRegionShortcut = ClientRegionShortcut.LOCAL
)
@EnableGemfireRepositories
public class Application {

  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }

  @Bean
  ApplicationRunner run(PersonRepository personRepository) {

    return args -> {

      Person alice = new Person("Adult Alice", 40);
      Person bob = new Person("Baby Bob", 1);
      Person carol = new Person("Teen Carol", 13);

      System.out.println("Before accessing data in Apache Geode...");

      asList(alice, bob, carol).forEach(person -> System.out.println("\t" + person));

      System.out.println("Saving Alice, Bob and Carol to Pivotal GemFire...");

      personRepository.save(alice);
      personRepository.save(bob);
      personRepository.save(carol);

      System.out.println("Lookup each person by name...");

      asList(alice.getName(), bob.getName(), carol.getName())
        .forEach(name -> System.out.println("\t" + personRepository.findByName(name)));

      System.out.println("Query adults (over 18):");

      stream(personRepository.findByAgeGreaterThan(18).spliterator(), false)
        .forEach(person -> System.out.println("\t" + person));

      System.out.println("Query babies (less than 5):");

      stream(personRepository.findByAgeLessThan(5).spliterator(), false)
        .forEach(person -> System.out.println("\t" + person));

      System.out.println("Query teens (between 12 and 20):");

      stream(personRepository.findByAgeGreaterThanAndAgeLessThan(12, 20).spliterator(), false)
        .forEach(person -> System.out.println("\t" + person));
    };
  }
}
```

In the configuration, you need to add the `@EnableGemfireRepositories` annotation.

By default, `@EnableGemfireRepositories` scans the current package for any interfaces that extend one of Spring Data’s repository interfaces. You can use its basePackageClasses = MyRepository.class to safely tell Spring Data for Apache Geode to scan a different root package by type for application-specific Repository extensions.

A Apache Geode cache containing one or more regions is required to store all the data. For that, you use one of Spring Data for Apache Geode’s convenient configuration-based annotations: `@ClientCacheApplication`, `@PeerCacheApplication`, or `@CacheServerApplication`.

Apache Geode supports different cache topologies, such as client/server, peer-to-peer (p2p), and even WAN arrangements. In p2p, a peer cache instance is embedded in the application, and your application would have the ability to participate in a cluster as a peer cache member. However, your application is subject to all the constraints of being a peer member in the cluster, so this is not as commonly used as, say, the client/server topology.

In our case, we use `@ClientCacheApplication` to create a “client” cache instance, which has the ability to connect to and communicate with a cluster of servers. However, to keep things simple, the client stores data locally by using a LOCAL client region, without the need to setup or run any servers.

Now, remember how you tagged Person to be stored in a region called People by using the SDG mapping annotation, `@Region("People")?` You define that region here by using the ClientRegionFactoryBean<String, Person> bean definition. You need to inject an instance of the cache you just defined while also naming it People.

### Build an executable JAR

You can run the application from the command line with Gradle or Maven. You can also build a single executable JAR file that contains all the necessary dependencies, classes, and resources and run that. Building an executable jar makes it easy to ship, version, and deploy the service as an application throughout the development lifecycle, across different environments, and so forth.

### Run executable JAR

If you use Gradle, you can run the application by using `./gradlew bootRun`. Alternatively, you can build the JAR file by using `./gradlew build` and then run the JAR file, as follows:

`java -jar build/libs/gs-accessing-data-gemfire-0.1.0.jar`

If you use Maven, you can run the application by using ./mvnw spring-boot:run. Alternatively, you can build the JAR file with ./mvnw clean package and then run the JAR file, as follows:

`java -jar target/gs-accessing-data-gemfire-0.1.0.jar`

You should see something like this (with other content, such as queries):


## Lab 5 Accessing Data with Neo4j 

Note: Some issue with this (dependencies)

### BUild the project

*  `git clone https://github.com/spring-guides/gs-accessing-data-neo4j.git`
* `cd into gs-accessing-data-neo4j/initial`
* Install neo4j
  1.  ` brew install neo4j`
  2. For other options, visit https://neo4j.com/download/community-edition/.

Once installed, launch it with its default settings by running the following command:
* Start neo4j
`$ neo4j start`

You should see output similar to the following:

```
Starting Neo4j.
Started neo4j (pid 96416). By default, it is available at http://localhost:7474/
There may be a short delay until the server is ready.
See /usr/local/Cellar/neo4j/3.0.6/libexec/logs/neo4j.log for current status.
```

* Define a Simple Entity

Apache Geode is an In-Memory Data Grid (IMDG) that maps data to regions. You can configure distributed regions that partition and replicate data across multiple nodes in a cluster. However, in this guide, we use a LOCAL region so that you need not set up anything extra, such as an entire cluster of servers.

Apache Geode is a key/value store, and a region implements the java.util.concurrent.ConcurrentMap interface. Though you can treat a region as a java.util.Map, it is quite a bit more sophisticated than just a simple Java Map, given that data is distributed, replicated, and generally managed inside the region.

In this example, you store Person objects in Apache Geode (a region) by using only a few annotations.

src/main/java/hello/Person.java

```java
package hello;

import java.io.Serializable;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.PersistenceConstructor;
import org.springframework.data.gemfire.mapping.annotation.Region;

import lombok.Getter;

@Region(value = "People")
public class Person implements Serializable {

  @Id
  @Getter
  private final String name;

  @Getter
  private final int age;

  @PersistenceConstructor
  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  @Override
  public String toString() {
    return String.format("%s is %d years old", getName(), getAge());
  }
}
```

* Create Simple Queries

To see how this works, create an interface that queries Person objects stored in Apache Geode:

src/main/java/hello/PersonRepository.java

```java
package hello;

import org.springframework.data.gemfire.repository.query.annotation.Trace;
import org.springframework.data.repository.CrudRepository;

public interface PersonRepository extends CrudRepository<Person, String> {

  @Trace
  Person findByName(String name);

  @Trace
  Iterable<Person> findByAgeGreaterThan(int age);

  @Trace
  Iterable<Person> findByAgeLessThan(int age);

  @Trace
  Iterable<Person> findByAgeGreaterThanAndAgeLessThan(int greaterThanAge, int lessThanAge);

}
```

* Create an Application Class

The following example creates an application class with all the components:

src/main/java/hello/Application.java

```
package hello;

import static java.util.Arrays.asList;
import static java.util.stream.StreamSupport.stream;

import org.apache.geode.cache.client.ClientRegionShortcut;

import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.gemfire.config.annotation.ClientCacheApplication;
import org.springframework.data.gemfire.config.annotation.EnableEntityDefinedRegions;
import org.springframework.data.gemfire.repository.config.EnableGemfireRepositories;

@SpringBootApplication
@ClientCacheApplication(name = "AccessingDataGemFireApplication")
@EnableEntityDefinedRegions(
  basePackageClasses = Person.class,
  clientRegionShortcut = ClientRegionShortcut.LOCAL
)
@EnableGemfireRepositories
public class Application {

  public static void main(String[] args) {
    SpringApplication.run(Application.class, args);
  }

  @Bean
  ApplicationRunner run(PersonRepository personRepository) {

    return args -> {

      Person alice = new Person("Adult Alice", 40);
      Person bob = new Person("Baby Bob", 1);
      Person carol = new Person("Teen Carol", 13);

      System.out.println("Before accessing data in Apache Geode...");

      asList(alice, bob, carol).forEach(person -> System.out.println("\t" + person));

      System.out.println("Saving Alice, Bob and Carol to Pivotal GemFire...");

      personRepository.save(alice);
      personRepository.save(bob);
      personRepository.save(carol);

      System.out.println("Lookup each person by name...");

      asList(alice.getName(), bob.getName(), carol.getName())
        .forEach(name -> System.out.println("\t" + personRepository.findByName(name)));

      System.out.println("Query adults (over 18):");

      stream(personRepository.findByAgeGreaterThan(18).spliterator(), false)
        .forEach(person -> System.out.println("\t" + person));

      System.out.println("Query babies (less than 5):");

      stream(personRepository.findByAgeLessThan(5).spliterator(), false)
        .forEach(person -> System.out.println("\t" + person));

      System.out.println("Query teens (between 12 and 20):");

      stream(personRepository.findByAgeGreaterThanAndAgeLessThan(12, 20).spliterator(), false)
        .forEach(person -> System.out.println("\t" + person));
    };
  }
}
```

In the configuration, you need to add the @EnableGemfireRepositories annotation.

By default, @EnableGemfireRepositories scans the current package for any interfaces that extend one of Spring Data’s repository interfaces. You can use its basePackageClasses = MyRepository.class to safely tell Spring Data for Apache Geode to scan a different root package by type for application-specific Repository extensions.

A Apache Geode cache containing one or more regions is required to store all the data. For that, you use one of Spring Data for Apache Geode’s convenient configuration-based annotations: @ClientCacheApplication, @PeerCacheApplication, or @CacheServerApplication.

Apache Geode supports different cache topologies, such as client/server, peer-to-peer (p2p), and even WAN arrangements. In p2p, a peer cache instance is embedded in the application, and your application would have the ability to participate in a cluster as a peer cache member. However, your application is subject to all the constraints of being a peer member in the cluster, so this is not as commonly used as, say, the client/server topology.

In our case, we use @ClientCacheApplication to create a “client” cache instance, which has the ability to connect to and communicate with a cluster of servers. However, to keep things simple, the client stores data locally by using a LOCAL client region, without the need to setup or run any servers.

Now, remember how you tagged Person to be stored in a region called People by using the SDG mapping annotation, @Region("People")? You define that region here by using the ClientRegionFactoryBean<String, Person> bean definition. You need to inject an instance of the cache you just defined while also naming it People.

A Apache Geode cache instance (whether a peer or client) is just a container for regions, which store your data. You can think of the cache as a schema in an RDBMS and regions as the tables. However, a cache also performs other administrative functions to control and manage all your Regions.
The types are <String, Person>, matching the key type (String) with the value type (Person).
The public static void main method uses Spring Boot’s SpringApplication.run() to launch the application and invoke the ApplicationRunner (another bean definition) that performs the data access operations on Apache Geode using the application’s Spring Data repository.

The application autowires an instance of PersonRepository that you just defined. Spring Data for Apache Geode dynamically creates a concrete class that implements this interface and plugs in the needed query code to meet the interface’s obligations. This repository instance is used by the run() method to demonstrate the functionality.

* Store and fetch data

In this guide, you create three local Person objects: Alice, Baby Bob, and Teen Carol. Initially, they only exist in memory. After creating them, you have to save them to Apache Geode.

Now you can run several queries. The first looks up everyone by name. Then you can run a handful of queries to find adults, babies, and teens, all by using the age attribute. With logging turned on, you can see the queries Spring Data for Apache Geode writes on your behalf.

To see the Apache Geode OQL queries that are generated by SDG, change the @ClientCacheApplication annotation logLevel attribute to config. Because the query methods (such as findByName) are annotated with SDG’s @Trace annotation, this turns on Apache Geode’s OQL query tracing (query-level logging), which shows you the generated OQL, execution time, whether any Apache Geode indexes were used by the query to gather the results, and the number of rows returned by the query.

### Build an executable JAR

`./mvnw clean package `

### Run the executable JAR

`./mvnw spring-boot:run`

You should see something like this (with other content, such as queries):

```
Before linking up with {apache-geode-name}...
	Alice is 40 years old.
	Baby Bob is 1 years old.
	Teen Carol is 13 years old.
Lookup each person by name...
	Alice is 40 years old.
	Baby Bob is 1 years old.
	Teen Carol is 13 years old.
Adults (over 18):
	Alice is 40 years old.
Babies (less than 5):
	Baby Bob is 1 years old.
Teens (between 12 and 20):
	Teen Carol is 13 years old.
```

## REF

- https://spring.io/guides/gs/accessing-data-mysql/
- https://spring.io/guides/gs/accessing-data-jpa/
- https://spring.io/guides/gs/accessing-data-gemfire
- https://spring.io/guides/gs/accessing-data-mongodb
- https://spring.io/guides/gs/accessing-data-neo4j