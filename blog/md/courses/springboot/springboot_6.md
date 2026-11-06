# Java Enterprise Development with Springboot - Topic 6 - Lombok and JDBCTemplate

## Today's Takeway

* Lombok
* Jackson
* JDBCTemplate

## Part I Lombok

IntelliJ Lombok plugin for code generation.

```java
A plugin that adds first-class support for Project Lombok

@Getter and @Setter
@FieldNameConstants
@ToString
@EqualsAndHashCode
@AllArgsConstructor, @RequiredArgsConstructor and @NoArgsConstructor
@Log,@Log4j, @Log4j2, @Slf4j, @XSlf4j, @CommonsLog, @JBossLog, @Flogger, @CustomLog
@Data
@Builder
```

## How to get Lombok in IntelliJ

* Go to the site of following for more info,

https://plugins.jetbrains.com/plugin/6317-lombok

* Install the plugin by downloading the zip.

![lombok_installation.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/lombok_installation.png)

or

* Install online (Recommended)

![lombok_installation.jpg](https://kevinli-webbertech.github.io/blog/images/springboot/lombok_installation.jpg)

You need to Enable Annotation Processing on IntelliJ IDEA,

`> Settings > Build, Execution, Deployment > Compiler > Annotation Processors`

## Update our code

Now let us add these annotations and imports,

![lombok usage1](https://kevinli-webbertech.github.io/blog/images/springboot/lombok1.jpg)

Another one,

![lombok usage2](https://kevinli-webbertech.github.io/blog/images/springboot/lombok2.jpg)

Now, there are no getter and setters!!

![no setter and getter](https://kevinli-webbertech.github.io/blog/images/springboot/No_Getter_Setter.jpg)

**Does this violate our rules of Java programming?**

The answer is: No, because this is not the final Java file. It would have the preprocessor, similar to C's macro, so the final expanded Java file would have everything.
This is again another nice feature to allow you to ease your rapid development.

### Test our code

You should start Springboot project and re check that everything should work as usual. For the conciseness, I will not show the screenshots here.

### Ref

- https://projectlombok.org/features/Builder


## Part II Jackson fasterxml

These are the general purpose annotations for Jackson Data Processor, used on value and handler types. The only annotations not included are ones that require dependency to the Databind package. This package and annotions are helping you to control the keys to show in your final resultant json.

In your pom.xml,

```xml
<properties>
  ...
  <!-- Use the latest version whenever possible. -->
  <jackson.version>2.17.1</jackson.version>
  ...
</properties>

<dependencies>
  ...
  <dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>${jackson.version}</version>
  </dependency>
  ...
</dependencies>
```

Note that the variable definition in the maven config file in pom.xml. If you include a lot of libraires, and some of these variables can also be inherited by other sub projects.

With the Task/TaskList project we had in last class, we could modify the files, and include jackson annotations,

![jackson_annotation](https://kevinli-webbertech.github.io/blog/images/springboot/jackson_annotation.jpg)

The builder syntax was builtin, and you do not have to implement the `return this` to chain the method. The `@Builder` annotation will do the job for you when it code generating the setters.

![lombok_builder](https://kevinli-webbertech.github.io/blog/images/springboot/lombok_builder.jpg)

## Part III JDBCTemplate

Let us checkout spring io's example, and learn it a little bit,

* `git clone https://github.com/spring-guides/gs-relational-data-access.git`

* cd into `gs-relational-data-access/complete` and load into your IntelliJ

Let us take a look at the following code,

`src/main/java/com/example/relationaldataaccess/Customer.java` shows:

```java
package com.example.relationaldataaccess;

public class Customer {
  private long id;
  private String firstName, lastName;

  public Customer(long id, String firstName, String lastName) {
    this.id = id;
    this.firstName = firstName;
    this.lastName = lastName;
  }

  @Override
  public String toString() {
    return String.format(
        "Customer[id=%d, firstName='%s', lastName='%s']",
        id, firstName, lastName);
  }

  // getters & setters omitted for brevity
}
```

In our lab, I would request you to replace with Lombok so that you can practice it,

Next, let us take a look at this,

`src/main/java/com/example/relationaldataaccess/RelationalDataAccessApplication.java` shows a class that can store and retrieve data over JDBC:

```java
package com.example.relationaldataaccess;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@SpringBootApplication
public class RelationalDataAccessApplication implements CommandLineRunner {

  private static final Logger log = LoggerFactory.getLogger(RelationalDataAccessApplication.class);

  public static void main(String args[]) {
    SpringApplication.run(RelationalDataAccessApplication.class, args);
  }

  @Autowired
  JdbcTemplate jdbcTemplate;

  @Override
  public void run(String... strings) throws Exception {

    log.info("Creating tables");

    jdbcTemplate.execute("DROP TABLE customers IF EXISTS");
    jdbcTemplate.execute("CREATE TABLE customers(" +
        "id SERIAL, first_name VARCHAR(255), last_name VARCHAR(255))");

    // Split up the array of whole names into an array of first/last names
    List<Object[]> splitUpNames = Arrays.asList("John Woo", "Jeff Dean", "Josh Bloch", "Josh Long").stream()
        .map(name -> name.split(" "))
        .collect(Collectors.toList());

    // Use a Java 8 stream to print out each tuple of the list
    splitUpNames.forEach(name -> log.info(String.format("Inserting customer record for %s %s", name[0], name[1])));

    // Uses JdbcTemplate's batchUpdate operation to bulk load data
    jdbcTemplate.batchUpdate("INSERT INTO customers(first_name, last_name) VALUES (?,?)", splitUpNames);

    log.info("Querying for customer records where first_name = 'Josh':");
    jdbcTemplate.query(
        "SELECT id, first_name, last_name FROM customers WHERE first_name = ?",
        (rs, rowNum) -> new Customer(rs.getLong("id"), rs.getString("first_name"), rs.getString("last_name")), "Josh")
    .forEach(customer -> log.info(customer.toString()));
  }
}```

Some tips,

For single insert statements, the insert method of JdbcTemplate is good. However, for multiple inserts, it is better to use batchUpdate.

Use `?` for arguments to avoid SQL injection attacks by instructing JDBC to bind variables.

### Build an executable JAR

If you use Maven, you can run the application by using `./mvnw spring-boot:run`. 
Alternatively, you can build the JAR file with `./mvnw clean package` and,
then run the JAR file, as follows:

`java -jar target/gs-relational-data-access-0.1.0.jar`

Finally, test your code.


### REF

https://spring.io/guides/gs/relational-data-access