# Docker Lab5 - Springboot App Deployment with Docker

## Takeaway

* Introduce what `Springboot` framework is
* How to run a `Springboot` project
* How to dockerize a `Springboot` project

## What is Springboot

### What is Spring Boot? The Simple Answer

**Spring Boot is a framework that makes it incredibly easy to create stand-alone, production-grade applications based on the Spring framework.**

Think of it as an **opinionated** and **convention-over-configuration** extension of the Spring ecosystem. Its primary goal is to remove the boilerplate configuration and setup that was traditionally required to get a Spring application running, allowing you to focus on writing your business logic.

---

### The Analogy: Building a Car

*   **The Spring Framework** is like a massive warehouse full of every possible car part you could ever need (engines, wheels, seats, stereos, etc.) and the tools to assemble them. It's incredibly powerful, but to build a car, you need to know exactly which parts to choose and how to connect them all together. This requires a lot of expertise and time.

*   **Spring Boot** is like being given a pre-assembled car chassis with a great engine, wheels, and electrical system already perfectly installed and wired together. You just need to say, "I want a sports car" or "I want an SUV," and it will configure the appropriate parts. You can still swap out the stereo or the seats (customize it), but you start with a fully functional vehicle immediately.

---

### Key Problems Spring Boot Solves

Before Spring Boot, setting up a new Spring project involved:
1.  Writing extensive XML configuration files.
2.  Manually adding numerous library dependencies and ensuring their versions were compatible.
3.  Setting up a web server (like Tomcat) separately and deploying your application to it.

Spring Boot eliminates all this by providing:

1.  **Auto-Configuration:** Spring Boot automatically configures your application based on the dependencies you have added. For example, if you add the `spring-boot-starter-web` dependency, it automatically assumes you are building a web application and sets up an embedded Tomcat server and default Spring MVC configurations.

2.  **Standalone Applications:** Spring Boot applications can be packaged as a single, executable JAR file. This JAR contains an **embedded web server** (like Tomcat, Jetty, or Undertow), so you don't need to deploy your application to an external server. You can run it anywhere Java is installed with a simple command: `java -jar yourapp.jar`.

3.  **Starter Dependencies:** These are convenient dependency descriptors that bundle together all the necessary libraries for a specific purpose. Instead of manually defining dozens of dependencies for a web project, you just include **one** starter.
    *   **`spring-boot-starter-web`**: For building web applications and RESTful APIs.
    *   **`spring-boot-starter-data-jpa`**: For using Spring Data JPA with Hibernate.
    *   **`spring-boot-starter-test`**: For testing.
    *   **`spring-boot-starter-security`**: For adding Spring Security.

4.  **Production-Ready Features:** Spring Boot includes helpful tools to monitor and manage your application in production, known as **Actuator**. It provides endpoints (like `/health`, `/metrics`, `/info`) to check the application's status, metrics, and more.

---

### A Simple Example: Traditional Spring vs. Spring Boot

**Traditional Spring MVC Web App Setup:**
1.  `web.xml` for servlet configuration.
2.  A Spring application context XML file.
3.  A Spring Dispatcher servlet XML file.
4.  Configuration for a view resolver, component scan, etc.
5.  Set up an external Tomcat server.
6.  Build a WAR file and deploy it to Tomcat.

**Spring Boot Web App Setup:**
1.  **Create a main class:**
    ```java
    @SpringBootApplication
    public class MyApplication {
        public static void main(String[] args) {
            SpringApplication.run(MyApplication.class, args);
        }
    }
    ```
2.  **Create a controller:**
    ```java
    @RestController
    public class HelloController {
        @GetMapping("/")
        public String hello() {
            return "Hello, World!";
        }
    }
    ```
3.  **Add the `spring-boot-starter-web` dependency in `pom.xml` (Maven).**
4.  **Run the main method.** Your app is now live at `http://localhost:8080`.

That's it! No XML, no server setup.

---

### Core Features of Spring Boot

| Feature | Description |
| :--- | :--- |
| **`@SpringBootApplication`** | A convenience annotation that combines `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan`. It's typically placed on your main class. |
| **Embedded Servers** | Allows you to run your application from the command line without setting up a web server. |
| **Spring Boot Starters** | Simplifies your Maven/Gradle configuration by bundling common dependencies. |
| **Spring Boot Actuator** | Provides production-ready features to monitor and manage your application. |
| **Spring Boot CLI** | A command-line tool for quickly developing with Spring. |
| **Application Properties/YAML** | Easy externalized configuration using a simple `application.properties` or `application.yml` file. |

### When Should You Use Spring Boot?

*   **Microservices Architecture:** Its lightweight nature and standalone JAR deployment make it perfect for building microservices.
*   **RESTful APIs:** It's the de facto standard for building REST APIs in the Java world.
*   **Rapid Prototyping:** You can get a project up and running in minutes.
*   **Production Applications:** Its built-in production monitoring tools (Actuator) make it suitable for large-scale applications.

### Summary

In essence, **Spring Boot is not a replacement for the Spring Framework**; it's a tool that makes using the Spring Framework much, much easier. It takes an opinionated view of the Spring platform, drastically reduces the initial setup and development time, and allows developers to create production-ready applications with minimal effort.

### Ref

* https://spring.io/projects/spring-boot
* https://www.geeksforgeeks.org/advance-java/spring-boot/
* https://www.tutorialspoint.com/spring_boot/spring_boot_introduction.htm

## Springboot Application Deployment with Docker

### 1. Create a Simple Spring Boot Application

There are two ways you can create a `Springboot` projects,

* Solution1: Using the **Spring Initializr**

First, let's create a basic Spring Boot app. You can use **Spring Initializr** (https://start.spring.io/) with these settings:

    - **Project**: Maven
    - **Language**: Java
    - **Spring Boot**: 3.2.x
    - **Group**: com.example
    - **Artifact**: docker-demo
    - **Packaging**: Jar
    - **Java**: 17
    - **Dependencies**: Spring Web

**Project Structure:**
```
springboot-docker-demo/
├── src/
│   └── main/
│       └── java/
│           └── com/example/dockerdemo/
│               └── DockerDemoApplication.java
│               └── HelloController.java
├── pom.xml
└── Dockerfile
```

**HelloController.java:**
```java
package com.example.dockerdemo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/")
    public String hello() {
        return "Hello from Spring Boot in Docker!";
    }
    
    @GetMapping("/health")
    public String health() {
        return "Application is running healthy!";
    }
}
```

**Solution 2:**

Checkout a demo Springboot project from the following URL,

1/ git clone https://github.com/spring-guides/gs-spring-boot.git

2/ `cd` into the `complete` directory after you git clone it.

3/ Test to run the web application by doing the following,

`./mvnw spring-boot:run`

For example,

`cd gs-spring-boot/complete`

For more information, please go to this link for reference,

- https://spring.io/guides/gs/spring-boot

4/ Once you are done, please go to your browser and check the http://localhost:8080
or you can do,

```cmd
$ curl http://localhost:8080
Greetings from Spring Boot!

$ curl http://localhost:8080/actuator/health
{"status":"UP"}
```

> For more `Springboot` study and tutorials, please refer to the following sites,
> 
> a. https://spring.io/guides/
>
> b. https://www.tutorialspoint.com/spring_boot/index.htm

### 2. Create the Dockerfile

Create a `Dockerfile` in the root directory of your project:

```Dockerfile
# Stage 1: Build the application
FROM maven:3.8.7-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
# Download dependencies first (leverages Docker cache)
RUN mvn dependency:go-offline
COPY src ./src
# Package the application
RUN mvn clean package -DskipTests

# Stage 2: Create the runtime image
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Copy the built JAR from the builder stage
COPY --from=builder /app/target/*.jar app.jar

# Expose the port Spring Boot runs on
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 3. Create a .dockerignore file

Create a `.dockerignore` file to exclude unnecessary files:

```
Dockerfile
.dockerignore
target/
.git
.gitignore
.mvn/
*.log
*.tmp
```

### 4. Build and Run the Docker Image

**1. Build the Docker image:**
```bash
# Navigate to your project directory
cd springboot-docker-demo

# Build the image with a tag
docker build -t springboot-app:1.0 .
```

**2. Run the container:**
```bash
# Run the container, mapping port 8080
docker run -d -p 8080:8080 --name springboot-container springboot-app:1.0
```

**3. Test the application:**
```bash
# Check if container is running
docker ps

# Check logs
docker logs springboot-container

# Test the endpoints
curl http://localhost:8080
# Should return: "Hello from Spring Boot in Docker!"

curl http://localhost:8080/health
# Should return: "Application is running healthy!"
```

### 5. Docker Compose (Optional but Recommended)

For more complex setups, create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  springboot-app:
    build: .
    container_name: springboot-app
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_active=docker
    restart: unless-stopped
```

Then run with:
```bash
docker-compose up -d
```

### Key Points Explained:

1. **Multi-stage Build**: 
   - First stage uses Maven to build the application
   - Second stage uses a smaller JRE image to run the application
   - Results in a much smaller final image

2. **Dependency Caching**: 
   - Copying `pom.xml` first and running `mvn dependency:go-offline` leverages Docker's cache
   - Dependencies won't be re-downloaded unless `pom.xml` changes

3. **Small Base Image**: 
   - `eclipse-temurin:17-jre-alpine` is a very small Linux distribution
   - Contains only what's needed to run Java applications

4. **Port Mapping**: 
   - `-p 8080:8080` maps host port 8080 to container port 8080
   - Spring Boot defaults to port 8080

### Common Useful Commands:

```bash
# Stop the container
docker stop springboot-container

# Start the container
docker start springboot-container

# Remove the container
docker rm springboot-container

# Remove the image
docker rmi springboot-app:1.0

# See running containers
docker ps

# See all containers (including stopped)
docker ps -a

# View container logs
docker logs springboot-container

# View dynamic logs in real-time
docker logs -f springboot-container

# Note: you can use container id to replace the container name in the above example

# Execute command in running container
docker exec -it springboot-container sh
```

This setup gives you a production-ready Docker deployment for your Spring Boot application that is efficient, secure, and follows best practices!