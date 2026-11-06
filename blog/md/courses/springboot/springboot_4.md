# Java Enterprise Development with Springboot - Topic 4 - Serving Web Content with Spring MVC

## Build the project

* git clone https://github.com/spring-guides/gs-serving-web-content.git

* cd into gs-serving-web-content/initial

## Create a Web Controller

```
package com.example.servingwebcontent;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class GreetingController {

	@GetMapping("/greeting")
	public String greeting(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model) {
		model.addAttribute("name", name);
		return "greeting";
	}

}
```

## Create a page

The following listing (from src/main/resources/templates/greeting.html) shows the greeting.html template:

```
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head> 
    <title>Getting Started: Serving Web Content</title> 
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
    <p th:text="|Hello, ${name}!|" />
</body>
</html>
```

Make sure you have Thymeleaf on your classpath (artifact co-ordinates: org.springframework.boot:spring-boot-starter-thymeleaf). It is already there in the "initial" and "complete" samples in Github.

## Spring Boot Devtools

* Enables hot swapping.

* Switches template engines to disable caching.

* Enables LiveReload to automatically refresh the browser.

* Other reasonable defaults based on development instead of production.

All you have to do is to put the following into your pom.xml if you use maven.
Note, we can just focus on maven for now. Gradle is similar.

```
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-devtools</artifactId>
        <optional>true</optional>
    </dependency>
```

## Run the Application

The following listing (from `src/main/java/com/example/servingwebcontent/ServingWebContentApplication.java`) shows the application class:

```
package com.example.servingwebcontent;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ServingWebContentApplication {

    public static void main(String[] args) {
        SpringApplication.run(ServingWebContentApplication.class, args);
    }

}
```

## Build an executable JAR

`./mvnw clean package`

`./gradlew build`

## Run an executable JAR

`java -jar build/libs/gs-serving-web-content-0.1.0.jar` or

`java -jar target/gs-serving-web-content-0.1.0.jar` or

`./gradlew bootRun` or

`./mvnw spring-boot:run`

## Test the Application

* try `http://localhost:8080/greeting` in your browser

* try `http://localhost:8080/greeting?name=User` in your broswer


## Add a homepage

you need to create the following file (which you can find in `src/main/resources/static/index.html`):

When you restart the application, you will see the HTML at http://localhost:8080/.

## REF

- https://spring.io/guides/gs/serving-web-content/