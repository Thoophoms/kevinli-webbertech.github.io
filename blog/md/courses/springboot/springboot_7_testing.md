# Java Enterprise Development with Springboot - Topic 8 - Springboot Testing

## Testing web layer

### Step 1

* `git clone https://github.com/spring-guides/gs-testing-web.git`
* `cd into gs-testing-web/complete`

### Step 2

check we have the following code in place,

```java
src/main/java/com/example/testingweb/HomeController.java shows how to do so:

package com.example.testingweb;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HomeController {

	@RequestMapping("/")
	public @ResponseBody String greeting() {
		return "Hello, World";
	}

}
```

* Get test file

The `@SpringBootTest` annotation tells Spring Boot to look for a main configuration class (one with `@SpringBootApplication`, for instance) and use that to start a Spring application context. You can run this test in your IDE or on the command line (by running `./mvnw test` or `./gradlew test`), and it should pass. To convince yourself that the context is creating your controller, you could add an assertion, as the following example (from src/test/java/com/example/testingweb/SmokeTest.java) shows:

```java
package com.example.testingweb;
import static org.assertj.core.api.Assertions.assertThat;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SmokeTest {

	@Autowired
	private HomeController controller;

	@Test
	void contextLoads() throws Exception {
		assertThat(controller).isNotNull();
	}
}
```

* Then we need to do some api testing besides the sanity test,

The following listing (from src/test/java/com/example/testingweb/HttpRequestTest.java) shows how to do so:

```java
package com.example.testingweb;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.web.server.LocalServerPort;
import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class HttpRequestTest {

	@LocalServerPort
	private int port;

	@Autowired
	private TestRestTemplate restTemplate;

	@Test
	void greetingShouldReturnDefaultMessage() throws Exception {
		assertThat(this.restTemplate.getForObject("http://localhost:" + port + "/",
				String.class)).contains("Hello, World");
	}
}
```

Let us recall in the first class when we see a test file like the following,

```java
import static org.hamcrest.Matchers.equalTo;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

@SpringBootTest
@AutoConfigureMockMvc
public class HelloControllerTest {

	@Autowired
	private MockMvc mvc;

	@Test
	public void getHello() throws Exception {
		mvc.perform(MockMvcRequestBuilders.get("/").accept(MediaType.APPLICATION_JSON))
				.andExpect(status().isOk())
				.andExpect(content().string(equalTo("HelloWorld")));
	}
}
```

So the difference between the `TestRestTemplate` and `MockMvc` is that TestRestTemplate initializes with a custom ClientHttpRequestFactory. 
Implementations usually create ClientHttpRequest objects that open actual TCP/HTTP(s) connections. 
Whereas you can provide a mock implementation where you can do whatever you want MockMvc, 
you're typically setting up a whole web application context and mocking the HTTP requests and responses. 
So, although a fake DispatcherServlet is up and running, simulating how your MVC stack will function, 
there are no real network connections made.

## Mockito Testing

* Mocking test is a big part of software development aside from Integration test as it is at low cost.
* Mockito is a testing framework we use in Springboot project
* Mockito is normally used in testing business logic, data repository and service layers.

### Mockito.mock() and @Mock

`@Mock` annotation is a shorthand for the Mockito.mock() method.

If we are writing data repository or service level mocking testing, we could checkout the following example,

```java
@Test
public void repositoryMock() {
    UserRepository localMockRepository = Mockito.mock(UserRepository.class);
    Mockito.when(localMockRepository.count()).thenReturn(111L);
    long userCount = localMockRepository.count();
    Assert.assertEquals(111L, userCount);
    Mockito.verify(localMockRepository).count();
}
```

```java
@RunWith(MockitoJUnitRunner.class)
public class MockAnnotationUnitTest {

    @Mock
    UserRepository mockRepository;
    
    @Test
    public void givenCountMethodMocked_WhenCountInvoked_ThenMockValueReturned() {
        Mockito.when(mockRepository.count()).thenReturn(123L);

        long userCount = mockRepository.count();

        Assert.assertEquals(123L, userCount);
        Mockito.verify(mockRepository).count();
    }
}
```

here are more examples, you can write something like the following,

```java
package com.journaldev.mockito.mock;
import java.util.List;
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class MockitoMockMethodExample {
	@SuppressWarnings("unchecked")
	@Test
	public void test() {
		// using Mockito.mock() method
		List<String> mockList = mock(List.class);
		when(mockList.size()).thenReturn(5);
		assertTrue(mockList.size()==5);
	}
}
```

and with annotation, you can do this,

```java
package com.journaldev.mockito.mock;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

public class MockitoMockAnnotationExample {

	@Mock
	List<String> mockList;
	
	@BeforeEach
	public void setup() {
		//if we don't call below, we will get NullPointerException
		MockitoAnnotations.initMocks(this);
	}
	
	@SuppressWarnings("unchecked")
	@Test
	public void test() {
		when(mockList.get(0)).thenReturn("JournalDev");
		assertEquals("JournalDev", mockList.get(0));
	}

}
```

### Mockito @InjectMocks Annotation

```java
package com.journaldev.mockito.mock;
import java.util.List;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

public class MockitoInjectMockAnnotationExample {

	@Mock
	List<String> mockList;
	
	//@InjectMock creates an instance of the class and 
	//injects the mocks that are marked with the annotations @Mock into it.
	@InjectMocks
	Fruits mockFruits;
	
	@BeforeEach
	public void setup() {
		//if we don't call below, we will get NullPointerException
		MockitoAnnotations.initMocks(this);
	}
	
	@SuppressWarnings("unchecked")
	@Test
	public void test() {
		when(mockList.get(0)).thenReturn("Apple");
		when(mockList.size()).thenReturn(1);
		assertEquals("Apple", mockList.get(0));
		assertEquals(1, mockList.size());
		
		//mockFruits names is using mockList, below asserts confirm it
		assertEquals("Apple", mockFruits.getNames().get(0));
		assertEquals(1, mockFruits.getNames().size());	
		
		mockList.add(1, "Mango");
		//below will print null because mockList.get(1) is not stubbed
		System.out.println(mockList.get(1));
	}
}

class Fruits{
private List<String> names;
	public List<String> getNames() {
		return names;
	}

	public void setNames(List<String> names) {
		this.names = names;
	}
}
```

## Testing Type

### A. Functionality test (Unit test)

* Integration Test

Firing http calls to real database server or http server.

Pros: You will see the real battle.
Cons: You have to maintain those database and servers either hardware or software, with licenses maybe and it is costly.

* Mocking Test

1/ We only test the logic, functions….
2/ When we test a function, we prep some data to pass into the function, and we know what the resultant data would come out, so we do assertion on the real result vs expected result.

So mocking is faking. But we hydrate on the method as a blackbox thus, we compare in and out.

Pros: It is cheap in a way of maintenance, but the development of tests are nontrivial. In a lot of time, the time spent in writing tests might take longer than you write the production code.

Cons: time consuming in the initial development stage, but maintenance cost might lower.

This will increase the test coverages and make sure the quality assurance criteria is met.

Sonarcube, Test server (commercial). It will send the test report to these servers, and the server will tell you if you can release or not.

### B. Performance Test/Stress Testing (Time, hardware, Resource...etc)

Loop testing, stress testing for,

* CPU/Memory consumption,
* for load balancing,
* for network,
* for user behavior,
* for speed

### C. Security Test (Penetration Test)

* Static code analysis.
* Penetration (https://www.nist.gov/,)

- https://www.imperva.com/learn/application-security/cve-cvss-vulnerability/
- https://nvd.nist.gov/vuln-metrics/cvss
- CVE Numbering Authority (CNA)
- National Vulnerability Database (NVD)
- Vulnerability Database (VULDB)
- Security Content Automation Protocol (SCAP).

### D. AB Testing(Comparison)

Pixel to pixel


### REF

- https://spring.io/guides/gs/testing-web/
- https://www.digitalocean.com/community/tutorials/mockito-mock-examples