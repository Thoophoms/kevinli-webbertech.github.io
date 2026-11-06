# Exception Handling in Spring WebFlux - Topic 7 WebFlux

## Controller

```java

@RestController
@RequestMapping("/")
public class MyRestController {

    private final UserService service;

    public MyRestController(UserService service) {
        this.service = service;
    }

    @GetMapping("/users/{id}")
    Mono<UserDto> findUser(@PathVariable("id") Long id) {
        return service.findUserById(id)
                      .map(user -> new UserDto(user.name()));
    }
}
```

## Service

```java
import java.util.HashMap;
import java.util.Map;

@Service
public class UserService {

    private final Map<Long, User> users = new HashMap<>();

    public UserService() {
        users.put(1L, new User("Wim"));
        users.put(2L, new User("Simon"));
        users.put(3L, new User("Siva"));
        users.put(4L, new User("Josh"));
    }

    public Mono<User> findUserById(Long userId) {
        User user = users.get(userId);
        if (user == null) {
            throw new UserNotFoundException(userId);
        }
        return Mono.just(user);
    }
}
```

## Exception

```java
import io.github.wimdeblauwe.errorhandlingspringbootstarter.ResponseErrorProperty;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class UserNotFoundException extends RuntimeException {
private final Long userId;

    public UserNotFoundException(Long userId) {
        super("No user found for id " + userId);
        this.userId = userId;
    }

    @ResponseErrorProperty
    public Long getUserId() {
        return userId;
    }
}
```

### Exception Handling Example

When requesting a non-existing user, the error response looks like this:

***Request:***

```bash
GET localhost:8080/users/10
```

***Response:***

```json
{
  "code": "USER_NOT_FOUND",
  "message": "No user found for id 10",
  "userId": 10
}
```

## Test File

We can also validate this with the following `@WebFluxTest` test:

```java
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.reactive.WebFluxTest;
import org.springframework.context.annotation.Import;
import org.springframework.test.web.reactive.server.WebTestClient;

@WebFluxTest(MyRestController.class)
@Import(UserService.class)
class MyRestControllerTest {

    @Autowired
    WebTestClient webTestClient;

    @Test
    void testUserNotFound() {
        webTestClient.get()
                     .uri("/users/10")
                     .exchange()
                     .expectStatus().isNotFound()
                     .expectBody()
                     .consumeWith(System.out::println)
                     .jsonPath("$.code").isEqualTo("USER_NOT_FOUND")
                     .jsonPath("$.message").isEqualTo("No user found for id 10")
                     .jsonPath("$.userId").isEqualTo(10L);
    }
}
```

## WebFlux Exception Handling

### Example 1: WebFlux

There are many ways to handle exceptions coming from the web layer in WebFlux. The WebFlux exception handler that relies on the same way on the Map can look like this:

```java
public class ReactiveExceptionHandler extends AbstractErrorWebExceptionHandler {
    private final Map<Class<? extends Exception>, HttpStatus> exceptionToStatusCode;
    private final HttpStatus defaultStatus;

    public ReactiveExceptionHandler(ErrorAttributes errorAttributes, WebProperties.Resources resources,
                                    ApplicationContext applicationContext, 
                                    Map<Class<? extends Exception>, HttpStatus> exceptionToStatusCode,
                                    HttpStatus defaultStatus) {
        super(errorAttributes, resources, applicationContext);
        this.exceptionToStatusCode = exceptionToStatusCode;
        this.defaultStatus = defaultStatus;
    }

    @Override
    protected RouterFunction<ServerResponse> getRoutingFunction(ErrorAttributes errorAttributes) {
        return RouterFunctions.route(RequestPredicates.all(), this::renderErrorResponse);
    }

    private Mono<ServerResponse> renderErrorResponse(ServerRequest request) {
        Throwable error = getError(request);
        log.error("An error has occurred", error);
        HttpStatus httpStatus;
        if (error instanceof Exception exception) {
            httpStatus = exceptionToStatusCode.getOrDefault(exception.getClass(), defaultStatus);
        } else {
            httpStatus = HttpStatus.INTERNAL_SERVER_ERROR;
        }
        return ServerResponse
                .status(httpStatus)
                .contentType(MediaType.APPLICATION_JSON)
                .body(BodyInserters.fromValue(ErrorResponse
                        .builder()
                        .code(httpStatus.value())
                        .message(error.getMessage())
                        .build())
                );
    }
}
```
Ref: [Error Handling with Spring WebFlux](https://www.wimdeblauwe.com/blog/2022/04/11/error-handling-with-spring-webflux/)


### Example 2

Throw exception in your codes:

```java
@GetMapping(value = "/{id}")
public Mono<Post> get(@PathVariable(value = "id") Long id) {
    return this.posts.findById(id).switchIfEmpty(Mono.error(new PostNotFoundException(id)));
}
```

Create a standalone `@ControllerAdvice` annotated class or `@ExceptionHandler` annotated method in your controller class to handle the exceptions:

```java
@RestControllerAdvice
@Slf4j
class RestExceptionHandler {

    @ExceptionHandler(PostNotFoundException.class)
    ResponseEntity<?> postNotFound(PostNotFoundException ex) {
        log.debug("handling exception::" + ex);
        return ResponseEntity.notFound().build();
    }
}
```
`@RestControllerAdvice` only works for `@RestController`. If you are using `RouterFunction`, create a `WebExceptionHandler` bean to handle it manually:

```java
@Bean
public WebExceptionHandler exceptionHandler() {
    return (ServerWebExchange exchange, Throwable ex) -> {
        if (ex instanceof PostNotFoundException) {
            exchange.getResponse().setStatusCode(HttpStatus.NOT_FOUND);
            return exchange.getResponse().setComplete();
        }
        return Mono.error(ex);
    };
}
```
For more details, please see:
- [Boot Exception Handler](https://github.com/hantsy/spring-reactive-sample/blob/master/boot-exception-handler/src/main/java/com/example/demo/DemoApplication.java)

References:

- [Web Exception](https://hantsy.github.io/spring-reactive-sample/web/exception.html)
- [Exception Handler](https://github.com/hantsy/spring-reactive-sample/tree/master/exception-handler)
- [Boot Exception Handler](https://github.com/hantsy/spring-reactive-sample/tree/master/boot-exception-handler)


### Example 3

```java
@Override
public Mono<SignupResponse> signup(SignupRequest request) {
    String email = request.getEmail().trim().toLowerCase();
    String password = request.getPassword();
    String salt = BCrypt.gensalt();
    String hash = BCrypt.hashpw(password, salt);
    String secret = totpManager.generateSecret();
    User user = new User(null, email, hash, salt, secret);

    return repository.findByEmail(email)
        .defaultIfEmpty(user)
        .flatMap(result -> {
            if (result.getUserId() == null) {
                return repository.save(result).flatMap(result2 -> {
                    String userId = result2.getUserId();
                    String token = tokenManager.issueToken(userId);
                    SignupResponse signupResponse = new SignupResponse(userId, token, secret);
                    return Mono.just(signupResponse);
                });
            } else {
                return Mono.error(new AlreadyExistsException());
            }
        });
}
```

```java
// Signup handler refactored
Mono<ServerResponse> signup(ServerRequest request) {
    Mono<SignupRequest> body = request.bodyToMono(SignupRequest.class);
    Mono<SignupResponse> result = body.flatMap(service::signup);
    
    return result.flatMap(data -> ServerResponse.ok()
                                                .contentType(MediaType.APPLICATION_JSON)
                                                .bodyValue(data))
                 .onErrorResume(error -> ServerResponse.badRequest().build());
}
```

Take a look on the `login` handle initial implementation:

```java
Mono<ServerResponse> login(ServerRequest request) {
    Mono<LoginRequest> body = request.bodyToMono(LoginRequest.class);
    Mono<LoginResponse> result = body.flatMap(service::login);
    
    return ServerResponse.ok()
                         .contentType(MediaType.APPLICATION_JSON)
                         .body(result, LoginResponse.class);
}
```

```java
Mono<ServerResponse> login(ServerRequest request) {
    Mono<LoginRequest> body = request.bodyToMono(LoginRequest.class);
    Mono<LoginResponse> result = body.flatMap(service::login);

    return result.flatMap(data -> ServerResponse.ok()
                                                .contentType(MediaType.APPLICATION_JSON)
                                                .bodyValue(data))
                 .switchIfEmpty(ServerResponse.notFound().build())
                 .onErrorResume(error -> {
                     if (error instanceof LoginDeniedException) {
                         return ServerResponse.badRequest().build();
                     }
                     return ServerResponse.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
                 });
}
```

```java
@GetMapping("/{id}")
public Mono<Post> get(@PathVariable("id") String id) {
    return this.posts.findById(id)
                     .switchIfEmpty(Mono.error(new PostNotFoundException(id)));
}

@PutMapping("/{id}")
public Mono<Post> update(@PathVariable("id") String id, @RequestBody Post post) {
    return this.posts.findById(id)
                     .switchIfEmpty(Mono.error(new PostNotFoundException(id)))
                     .map(p -> {
                         p.setTitle(post.getTitle());
                         p.setContent(post.getContent());
                         return p;
                     })
                     .flatMap(p -> this.posts.save(p));
}

@DeleteMapping("/{id}")
public Mono<Void> delete(@PathVariable("id") String id) {
    return this.posts.deleteById(id)
                     .switchIfEmpty(Mono.error(new PostNotFoundException(id)));
}
```

### 2. Throw exception in your codes

```java
@GetMapping(value = "/{id}")
public Mono<Post> get(@PathVariable(value = "id") long id) {
    return this.posts.findById(id)
                     .switchIfEmpty(Mono.error(new PostNotFoundException(id)));
}
```

### 3. Create a standalone `@ControllerAdvice` annotated class or `@ExceptionHandler` annotated method in your controller class to handle the exceptions.

```java
@RestControllerAdvice
@Slf4j
class RestExceptionHandler {

    @ExceptionHandler(PostNotFoundException.class)
    ResponseEntity<?> postNotFound(PostNotFoundException ex) {
        log.debug("handling exception::" + ex);
        return ResponseEntity.notFound().build();
    }
}
```

`@RestControllerAdvice` only works for `@RestController`. 

If you are using `RouterFunction`, create a `WebExceptionHandler` bean to handle it manually.

```java
@Bean
public WebExceptionHandler exceptionHandler() {
    return (ServerWebExchange exchange, Throwable ex) -> {
        if (ex instanceof PostNotFoundException) {
            exchange.getResponse().setStatusCode(HttpStatus.NOT_FOUND);
            return exchange.getResponse().setComplete();
        }
        return Mono.error(ex);
    };
}
```

References:
- [Error Handling in Spring WebFlux](https://dzone.com/articles/error-handling-in-spring-webflux)
- [Stack Overflow - How to Handle Errors in Spring Reactor Mono or Flux](https://stackoverflow.com/questions/51024279/how-to-handle-errors-in-spring-reactor-mono-or-flux)
- [Error Handling with Spring WebFlux](https://www.wimdeblauwe.com/blog/2022/04/11/error-handling-with-spring-webflux/)
- [Baeldung - Spring Boot Custom WebFlux Exceptions](https://www.baeldung.com/spring-boot-custom-webflux-exceptions)
- [Error Handling with Spring WebFlux](https://www.wimdeblauwe.com/blog/2022/04/11/error-handling-with-spring-webflux/)
