# Springboot Cheatsheet Ref

## Terminology

### DI (Dependency Injection)

The technology that Spring is most identified with is the Dependency Injection (DI) flavor of Inversion of Control. The Inversion of Control (IoC) is a general concept, and it can be expressed in many different ways. Dependency Injection is merely one concrete example of Inversion of Control.

For example,

```java
package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class DatabaseAccountService implements AccountService {

	private final RiskAssessor riskAssessor;

	@Autowired
	public DatabaseAccountService(RiskAssessor riskAssessor) {
		this.riskAssessor = riskAssessor;
	}

	// ...

}
```

If a bean has one constructor, you can omit the @Autowired, as shown in the following example:

```java
@Service
public class DatabaseAccountService implements AccountService {

	private final RiskAssessor riskAssessor;

	public DatabaseAccountService(RiskAssessor riskAssessor) {
		this.riskAssessor = riskAssessor;
	}

	// ...
}
```

### IoC container

IoC container, or spring container is a concept of a software system during runtime, when the spring or springboot application was deployed and running. It is only making sense when the Spring/Springboot app is running.

The Spring container is at the core of the Spring Framework. The container will create the objects, wire them together, configure them, and manage their complete life cycle from creation till destruction. The Spring container uses DI to manage the components that make up an application. These objects are called Spring Beans,

The configuration metadata can be represented either by XML, Java annotations, or Java code. The following are the legacy and modern ways to configure Spring or Springboot project.

* XMl configuration: old way of doing configuration file from XML files, and Spring main methods load those xml either by explicitly define where they are or by reading from default locations.

* Annotation: default in Springboot and popular

* Application.properties or YML file: These are modern configuration files.

Spring provides the following two distinct types of containers.

* Spring BeanFactory Container

This is the simplest container providing the basic support for `DI` and is defined by the `org.springframework.beans.factory.BeanFactory` interface. The BeanFactory and related interfaces, such as `BeanFactoryAware`, `InitializingBean`, `DisposableBean`, are still present in Spring for the purpose of backward compatibility with a large number of third-party frameworks that integrate with Spring.

* Spring ApplicationContext Container

This container adds more enterprise-specific functionality such as the ability to resolve textual messages from a properties file and the ability to publish application events to interested event listeners. This container is defined by the org.springframework.context.ApplicationContext interface.

The `ApplicationContext container` includes all functionality of the BeanFactorycontainer, so it is generally **recommended** over BeanFactory. BeanFactory can still be used for lightweight applications like mobile devices or applet-based applications where data volume and speed is significant.

### Spring/Springboot Bean

The objects that form the backbone of your application and that are managed by the Spring IoC container are called beans. A bean is an object that is instantiated, assembled, and otherwise managed by a Spring IoC container. These beans are created with the configuration metadata that you supply to the container.

Three things we need to understand,

* How to create a bean
* Bean's lifecycle details
* Bean's dependencies

For example, application components (@Component, @Service, @Repository, @Controller etc.) are automatically registered as Spring Beans.

### Bean scope

When defining a <bean> you have the option of declaring a scope for that bean. For example, to force Spring to produce a new bean instance each time one is needed, you should declare the bean's scope attribute to be prototype. Similarly, if you want Spring to return the same bean instance each time one is needed, you should declare the bean's scope attribute to be singleton.

* `1 singleton`

This scopes the bean definition to a single instance per Spring IoC container (default).

* `2 prototype`

This scopes a single bean definition to have any number of object instances.

* `3 request`

This scopes a bean definition to an HTTP request. Only valid in the context of a web-aware Spring ApplicationContext.

* `4 session`

This scopes a bean definition to an HTTP session. Only valid in the context of a web-aware Spring ApplicationContext.

* `5 global-session`

This scopes a bean definition to a global HTTP session. Only valid in the context of a web-aware Spring ApplicationContext.

### Bean properties

All the above configuration metadata translates into a set of the following properties that make up each bean definition.

**Sr.No.** 	   **Properties & Description**

**1 class**

This attribute is mandatory and specifies the bean class to be used to create the bean.

**2 name**

This attribute specifies the bean identifier uniquely. In XMLbased configuration metadata, you use the id and/or name attributes to specify the bean identifier(s).

**scope**

This attribute specifies the scope of the objects created from a particular bean definition and it will be discussed in bean scopes chapter.

**constructor-arg**

This is used to inject the dependencies and will be discussed in subsequent chapters.

**properties**

This is used to inject the dependencies and will be discussed in subsequent chapters.

**autowiring mode**

This is used to inject the dependencies and will be discussed in subsequent chapters.

**lazy-initialization mode**

A lazy-initialized bean tells the IoC container to create a bean instance when it is first requested, rather than at the startup.

**8 initialization method**

A callback to be called just after all necessary properties on the bean have been set by the container. It will be discussed in bean life cycle chapter.

**9 destruction method**

A callback to be used when the container containing the bean is destroyed. It will be discussed in bean life cycle chapter.

Ref:

https://www.tutorialspoint.com/spring

### Bean life cycle

**Initialization callbacks**

The `org.springframework.beans.factory.InitializingBean` interface specifies a single method −

```java
public class ExampleBean implements InitializingBean {
   public void afterPropertiesSet() {
      // do some initialization work
   }
}
```

**Destruction callbacks**

public class ExampleBean implements DisposableBean {
   public void destroy() {
      // do some destruction work
   }
}

## Annotations

- @Autowired
- @SpringBootApplication
- @Component
- @Service
- @Repository
- @Configuration
- @RequestMapping vs @GetMapping
- @Bean
- @Qualifier
- @RequestBody
- @RequestParam
- @PathVariable
- @RequestBody

## Json libraries with Springboot

## Testing
- @SpringBootTest

## Java Reactive and WebFlux

## Spring lifecycle

## Filter and interception

## Monitoring

## Security
- JWT
- OAuth
- OIDC



