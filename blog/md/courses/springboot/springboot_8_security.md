# Java Enterprise Development with Springboot - Topic 8 - Spring Security

## Spring Security Architecture

Spring Security is a framework that provides,

* authentication

* authorization

* protection against common attacks

https://docs.spring.io/spring-security/reference/features/exploits/index.html

such as CSRF (Cross Site Request Forgery (CSRF) attacks)

More can be found here,

https://docs.spring.io/spring-security/reference/features/exploits/csrf.html

On top of the current Springboot developments, it supports two mainstream applications,

* imperative

https://docs.spring.io/spring-security/reference/servlet/index.html

* reactive

https://docs.spring.io/spring-security/reference/reactive/index.html


Spring Security’s high-level architecture within Servlet based applications is based on Servlet Filters, so it is helpful to look at the role of Filters generally first. The following image shows the typical layering of the handlers for a single HTTP request.

**DelegatingFilterProxy**

Spring provides a Filter implementation named DelegatingFilterProxy that allows bridging between the Servlet container’s lifecycle and Spring’s ApplicationContext. The Servlet container allows registering Filter instances by using its own standards, but it is not aware of Spring-defined Beans. You can register DelegatingFilterProxy through the standard Servlet container mechanisms but delegate all the work to a Spring Bean that implements Filter.

![alt text](https://kevinli-webbertech.github.io/blog/images/springboot/DelegatingFilterProxy.png)

**FilterChainProxy**

Spring Security’s Servlet support is contained within FilterChainProxy. FilterChainProxy is a special Filter provided by Spring Security that allows delegating to many Filter instances through SecurityFilterChain. Since FilterChainProxy is a Bean, it is typically wrapped in a DelegatingFilterProxy.

![alt text](https://kevinli-webbertech.github.io/blog/images/springboot/FilterChainProxy.png)

**SecurityFilterChain**

![alt text](https://kevinli-webbertech.github.io/blog/images/springboot/SecurityFilterChain.png)

SecurityFilterChain is used by FilterChainProxy to determine which Spring Security Filter instances should be invoked for the current request.

The Security Filters in SecurityFilterChain are typically Beans, but they are registered with FilterChainProxy instead of DelegatingFilterProxy. FilterChainProxy provides a number of advantages to registering directly with the Servlet container or DelegatingFilterProxy. First, it provides a starting point for all of Spring Security’s Servlet support. For that reason, if you try to troubleshoot Spring Security’s Servlet support, adding a debug point in FilterChainProxy is a great place to start.

Second, since FilterChainProxy is central to Spring Security usage, it can perform tasks that are not viewed as optional. For example, it clears out the SecurityContext to avoid memory leaks. It also applies Spring Security’s HttpFirewall to protect applications against certain types of attacks.

In addition, it provides more flexibility in determining when a SecurityFilterChain should be invoked. In a Servlet container, Filter instances are invoked based upon the URL alone. However, FilterChainProxy can determine invocation based upon anything in the HttpServletRequest by using the RequestMatcher interface.

![alt text](https://kevinli-webbertech.github.io/blog/images/springboot/MultipleSecurityChain.png)

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(Customizer.withDefaults())
            .authorizeHttpRequests(authorize -> authorize
                .anyRequest().authenticated()
            )
            .httpBasic(Customizer.withDefaults())
            .formLogin(Customizer.withDefaults());
        return http.build();
    }

}
```

![alt text](https://kevinli-webbertech.github.io/blog/images/springboot/filterOrder.png)

### Adding a Custom Filter to the Filter Chain

```java
public class TenantFilter implements Filter {

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) servletRequest;
        HttpServletResponse response = (HttpServletResponse) servletResponse;

        String tenantId = request.getHeader("X-Tenant-Id"); 
        boolean hasAccess = isUserAllowed(tenantId); 
        if (hasAccess) {
            filterChain.doFilter(request, response); 
            return;
        }
        throw new AccessDeniedException("Access denied"); 
    }
}
```

The sample code above does the following:

* Get the tenant id from the request header.
* Check if the current user has access to the tenant id.
* If the user has access, then invoke the rest of the filters in the chain.
* If the user does not have access, then throw an AccessDeniedException.

Instead of implementing Filter, you can extend from OncePerRequestFilter which is a base class for filters that are only invoked once per request and provides a doFilterInternal method with the HttpServletRequest and HttpServletResponse parameters.

The following code uses HttpSecurity#addFilterBefore to add the TenantFilter before the AuthorizationFilter.

```java
@Bean
SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        // ...
        .addFilterBefore(new TenantFilter(), AuthorizationFilter.class); 
    return http.build();
}
```

By adding the filter before the AuthorizationFilter we are making sure that the TenantFilter is invoked after the authentication filters. You can also use HttpSecurity#addFilterAfter to add the filter after a particular filter or HttpSecurity#addFilterAt to add the filter at a particular filter position in the filter chain.

And that’s it, now the TenantFilter will be invoked in the filter chain and will check if the current user has access to the tenant id.

Be careful when you declare your filter as a Spring bean, either by annotating it with @Component or by declaring it as a bean in your configuration, because Spring Boot will automatically register it with the embedded container. That may cause the filter to be invoked twice, once by the container and once by Spring Security and in a different order.

If you still want to declare your filter as a Spring bean to take advantage of dependency injection for example, and avoid the duplicate invocation, you can tell Spring Boot to not register it with the container by declaring a FilterRegistrationBean bean and setting its enabled property to false:

```java
@Bean
public FilterRegistrationBean<TenantFilter> tenantFilterRegistration(TenantFilter filter) {
    FilterRegistrationBean<TenantFilter> registration = new FilterRegistrationBean<>(filter);
    registration.setEnabled(false);
    return registration;
}
```

### Handling Security Exceptions

The ExceptionTranslationFilter allows translation of AccessDeniedException and AuthenticationException into HTTP responses.

ExceptionTranslationFilter is inserted into the FilterChainProxy as one of the Security Filters.

The following image shows the relationship of ExceptionTranslationFilter to other components:

![alt text](https://kevinli-webbertech.github.io/blog/images/springboot/securityExceptionHandler.png)

The pseudocode for ExceptionTranslationFilter looks something like this:

ExceptionTranslationFilter pseudocode,

```java
try {
	filterChain.doFilter(request, response); 
} catch (AccessDeniedException | AuthenticationException ex) {
	if (!authenticated || ex instanceof AuthenticationException) {
		startAuthentication(); 
	} else {
		accessDenied(); 
	}
}
```

### Springboot Logging to help debugging security issues

Let’s consider an example where a user tries to make a POST request to a resource that has CSRF protection enabled without the CSRF token. With no logs, the user will see a 403 error with no explanation of why the request was rejected. However, if you enable logging for Spring Security, you will see a log message like this:

```shell
2023-06-14T09:44:25.797-03:00 DEBUG 76975 --- [nio-8080-exec-1] o.s.security.web.FilterChainProxy        : Securing POST /hello
2023-06-14T09:44:25.797-03:00 TRACE 76975 --- [nio-8080-exec-1] o.s.security.web.FilterChainProxy        : Invoking DisableEncodeUrlFilter (1/15)
2023-06-14T09:44:25.798-03:00 TRACE 76975 --- [nio-8080-exec-1] o.s.security.web.FilterChainProxy        : Invoking WebAsyncManagerIntegrationFilter (2/15)
2023-06-14T09:44:25.800-03:00 TRACE 76975 --- [nio-8080-exec-1] o.s.security.web.FilterChainProxy        : Invoking SecurityContextHolderFilter (3/15)
2023-06-14T09:44:25.801-03:00 TRACE 76975 --- [nio-8080-exec-1] o.s.security.web.FilterChainProxy        : Invoking HeaderWriterFilter (4/15)
2023-06-14T09:44:25.802-03:00 TRACE 76975 --- [nio-8080-exec-1] o.s.security.web.FilterChainProxy        : Invoking CsrfFilter (5/15)
2023-06-14T09:44:25.814-03:00 DEBUG 76975 --- [nio-8080-exec-1] o.s.security.web.csrf.CsrfFilter         : Invalid CSRF token found for http://localhost:8080/hello
2023-06-14T09:44:25.814-03:00 DEBUG 76975 --- [nio-8080-exec-1] o.s.s.w.access.AccessDeniedHandlerImpl   : Responding with 403 status code
2023-06-14T09:44:25.814-03:00 TRACE 76975 --- [nio-8080-exec-1] o.s.s.w.header.writers.HstsHeaderWriter  : Not injecting HSTS header since it did not match request to [Is Secure]
```

To configure your application to log all the security events, you can add the following to your application:

```java
application.properties in Spring Boot
logging.level.org.springframework.security=TRACE
logback.xml
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <!-- ... -->
    </appender>
    <!-- ... -->
    <logger name="org.springframework.security" level="trace" additivity="false">
        <appender-ref ref="Console" />
    </logger>
</configuration>
```

## Lab: Securing a Web Application




## Securing a SPA(single app application)

### Ref

- [Spring bean life cycle](https://www.tutorialspoint.com/spring/spring_bean_life_cycle.htm#:~:text=The%20life%20cycle%20of%20a,some%20cleanup%20may%20be%20required.)
- [spring security architecture](https://spring.io/guides/topicals/spring-security-architecture)
- [Securing a Web Application](https://spring.io/guides/gs/securing-web/)
- [spring security and angular-js](https://spring.io/guides/tutorials/spring-security-and-angular-js)