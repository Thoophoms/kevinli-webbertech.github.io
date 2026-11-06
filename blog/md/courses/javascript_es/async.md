# Javascript Async

**Definition**

In JavaScript, async refers to asynchronous programming, which allows code execution without blocking the program. It enables handling operations like fetching data, reading files, or waiting for timers without freezing the main thread.

**Key Concepts of JS Async**

1. Asynchronous Execution

- Code continues running while waiting for a task (e.g., API call) to complete.

2. async and await

- async makes a function return a Promise.
- await pauses execution until the Promise resolves.

3. Promises

- Objects representing an eventual completion or failure of an asynchronous operation.

4. Callbacks

- Functions passed as arguments to execute later (older way of handling async tasks).

5. Event Loop

- Mechanism that ensures non-blocking execution in JavaScript.

**JavaScript Callbacks**

A callback is a function passed as an argument to another function
This technique allows a function to call another function
A callback function can run after another function has finished

**Function Sequence**

JavaScript functions are executed in the sequence they are called. Not in the sequence they are defined.

This example will end up displaying "Goodbye":

Example
```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>Function Sequence</h2>
<p>JavaScript functions are executed in the sequence they are called.</p>

<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myFirst() {
  myDisplayer("Hello");
}

function mySecond() {
  myDisplayer("Goodbye");
}

myFirst();
mySecond();
</script>

</body>
</html>
```
# JavaScript Functions
Function Sequence
JavaScript functions are executed in the sequence they are called.

Goodbye

_____________________________________________________________

This example will end up displaying "Hello":
```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>Function Sequence</h2>
<p>JavaScript functions are executed in the sequence they are called.</p>

<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myFirst() {
  myDisplayer("Hello");
}

function mySecond() {
  myDisplayer("Goodbye");
}

mySecond();
myFirst();
</script>

</body>
</html>
```
Output:
# JavaScript Functions
**Function Sequence**

JavaScript functions are executed in the sequence they are called.

Hello
_____________________________________________________________
**Sequence Control**

Sometimes you would like to have better control over when to execute a function.

Suppose you want to do a calculation, and then display the result.

You could call a calculator function (myCalculator), save the result, and then call another function (myDisplayer) to display the result:
```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>Function Sequence</h2>
<p>JavaScript functions are executed in the sequence they are called.</p>

<p>The result of the calculation is:</p>
<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myCalculator(num1, num2) {
  let sum = num1 + num2;
  return sum;
}

let result = myCalculator(5, 5);
myDisplayer(result);
</script>

</body>
</html>
```

Output:
# JavaScript Functions
**Function Sequence**

JavaScript functions are executed in the sequence they are called.

The result of the calculation is:

10
_____________________________________________________________

Or, you could call a calculator function (myCalculator), and let the calculator function call the display function (myDisplayer):

```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>Function Sequence</h2>
<p>JavaScript functions are executed in the sequence they are called.</p>

<p>The result of the calculation is:</p>
<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myCalculator(num1, num2) {
  let sum = num1 + num2;
  myDisplayer(sum);
}

myCalculator(5, 5);
</script>

</body>
</html>
```
# JavaScript Functions
**Function Sequence**

JavaScript functions are executed in the sequence they are called.

The result of the calculation is:

10
_____________________________________________________________

The problem with the first example above, is that you have to call two functions to display the result.

The problem with the second example, is that you cannot prevent the calculator function from displaying the result.

Now it is time to bring in a callback.

**JavaScript Callbacks**

A callback is a function passed as an argument to another function.

Using a callback, you could call the calculator function (myCalculator) with a callback (myCallback), and let the calculator function run the callback after the calculation is finished:

```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>Callback Functions</h2>

<p>The result of the calculation is:</p>
<p id="demo"></p>

<script>
function myDisplayer(something) {
  document.getElementById("demo").innerHTML = something;
}

function myCalculator(num1, num2, myCallback) {
  let sum = num1 + num2;
  myCallback(sum);
}

myCalculator(5, 5, myDisplayer);
</script>

</body>
</html>
```
Output:
# JavaScript Functions
**Callback Functions**

The result of the calculation is:

10

In the example above, myDisplayer is a called a callback function.

It is passed to myCalculator() as an argument.

Note
When you pass a function as an argument, remember not to use parenthesis.

Right: myCalculator(5, 5, myDisplayer);

Wrong: ~~myCalculator(5, 5, myDisplayer());~~
_____________________________________________________________
```
<!DOCTYPE html>
<html>
<body style="text-align: right">

<h1>JavaScript Functions</h1>
<h2>Callback Functions</h2>
<p id="demo"></p>

<script>
// Create an Array
const myNumbers = [4, 1, -20, -7, 5, 9, -6];

// Call removeNeg with a Callback
const posNumbers = removeNeg(myNumbers, (x) => x >= 0);

// Display Result
document.getElementById("demo").innerHTML = posNumbers;

// Remove negative numbers
function removeNeg(numbers, callback) {
  const myArray = [];
  for (const x of numbers) {
    if (callback(x)) {
      myArray.push(x);
    }
  }
  return myArray;
}
</script>

</body>
</html>
```

# JavaScript Functions
# Callback Functions
4,1,5,9

In the example above, (x) => x >= 0 is a callback function.

It is passed to removeNeg() as an argument.

**When to Use a Callback?**

The examples above are not very exciting.

They are simplified to teach you the callback syntax.

Where callbacks really shine are in asynchronous functions, where one function has to wait for another function (like waiting for a file to load).

**Asynchronous JavaScript**

The examples used in the previous chapter, was very simplified.

The purpose of the examples was to demonstrate the syntax of callback functions:

```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>Callback Functions</h2>

<p>The result of the calculation is:</p>
<p id="demo"></p>

<script>
function myDisplayer(something) {
  document.getElementById("demo").innerHTML = something;
}

function myCalculator(num1, num2, myCallback) {
  let sum = num1 + num2;
  myCallback(sum);
}

myCalculator(5, 5, myDisplayer);
</script>

</body>
</html>
```

# JavaScript Functions
**Callback Functions**

The result of the calculation is:

10

In the example above, myDisplayer is the name of a function.

It is passed to myCalculator() as an argument.

In the real world, callbacks are most often used with asynchronous functions.

A typical example is JavaScript setTimeout().
_____________________________________________________________
**Waiting for a Timeout**

When using the JavaScript function setTimeout(), you can specify a callback function to be executed on time-out:
```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>setTimeout() with a Callback</h2>

<p>Wait 3 seconds (3000 milliseconds) for this page to change.</p>

<h1 id="demo"></h1>

<script>
setTimeout(myFunction, 3000);

function myFunction() {
  document.getElementById("demo").innerHTML = "I love Javascript !!";
}
</script>

</body>
</html>
```
output:
# JavaScript Functions
**setTimeout() with a Callback**

Wait 3 seconds (3000 milliseconds) for this page to change.

# I love Javascript !!

In the example above, myFunction is used as a callback.

myFunction is passed to setTimeout() as an argument.

3000 is the number of milliseconds before time-out, so myFunction() will be called after 3 seconds.

Note:
When you pass a function as an argument, remember not to use parenthesis.

Right: setTimeout(myFunction, 3000);

Wrong: ~~setTimeout(myFunction(), 3000);~~

___________________
**Waiting for Intervals**

When using the JavaScript function setInterval(), you can specify a callback function to be executed for each interval:
```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>setInterval() with a Callback</h2>

<p>Using setInterval() to display the time every second (1000 milliseconds).</p>

<h1 id="demo"></h1>

<script>
setInterval(myFunction, 1000);

function myFunction() {
  let d = new Date();
  document.getElementById("demo").innerHTML=
  d.getHours() + ":" +
  d.getMinutes() + ":" +
  d.getSeconds();
}
</script>

</body>
```

In the example above, myFunction is used as a callback.

myFunction is passed to setInterval() as an argument.

1000 is the number of milliseconds between intervals, so myFunction() will be called every second.

**Callback Alternatives**

With asynchronous programming, JavaScript programs can start long-running tasks, and continue running other tasks in parallel.

But, asynchronus programmes are difficult to write and difficult to debug.

Because of this, most modern asynchronous JavaScript methods don't use callbacks. Instead, in JavaScript, asynchronous programming is solved using Promises instead.

**JavaScript Promise Object**

A Promise contains both the producing code and calls to the consuming code:

Promise Syntax

```
let myPromise = new Promise(function(myResolve, myReject) {
// "Producing Code" (May take some time)
myResolve(); // when successful
myReject();  // when error
});
// "Consuming Code" (Must wait for a fulfilled Promise)
myPromise.then(
function(value) { /* code if successful */ },
function(error) { /* code if some error */ }
);
```
When the producing code obtains the result, it should call one of the two callbacks:

When	Call
Success	myResolve(result value)
Error	myReject(error object)

| when    | call |
|---------|------|
| Success |  myResolve(result value)    |
| Error     |  myReject(error object)    |


**Promise Object Properties**

A JavaScript Promise object can be:

- Pending
- Fulfilled
- Rejected

The Promise object supports two properties: state and result.

While a Promise object is "pending" (working), the result is undefined.

When a Promise object is "fulfilled", the result is a value.

When a Promise object is "rejected", the result is an error object.

| myPromise.state  |  myPromise.result |
|---|---|
| "pending"  | undefined
|
|  "fulfilled"	 |  a result value |
|  "rejected"	 |  an error object |

You cannot access the Promise properties state and result.

You must use a Promise method to handle promises.

**Promise How To**

Here is how to use a Promise:

```
myPromise.then(
function(value) { /* code if successful */ },
function(error) { /* code if some error */ }
);
```
Example:
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Promise Object</h1>
<h2>The then() Method</h2>

<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

let myPromise = new Promise(function(myResolve, myReject) {
  let x = 0;

// some code (try to change x to 5)

  if (x == 0) {
    myResolve("OK");
  } else {
    myReject("Error");
  }
});

myPromise.then(
  function(value) {myDisplayer(value);},
  function(error) {myDisplayer(error);}
);
</script>

</body>
</html>
```
Output:

# JavaScript Promise Object
**The then() Method**

OK
___________

**JavaScript Promise Examples**

To demonstrate the use of promises, we will use the callback examples from the previous chapter:

- Waiting for a Timeout
- Waiting for a File

**Waiting for a Timeout**

Example Using Callback
```
<!DOCTYPE html>
<html>
<body>

<h1>JavaScript Functions</h1>
<h2>setTimeout() with a Callback</h2>

<p>Wait 3 seconds (3000 milliseconds) for this page to change.</p>

<h1 id="demo"></h1>

<script>
setTimeout(function() { myFunction("I love You !!!"); }, 3000);

function myFunction(value) {
  document.getElementById("demo").innerHTML = value;
}
</script>

</body>
</html>
```
Output:

# JavaScript Functions
**setTimeout() with a Callback**

Wait 3 seconds (3000 milliseconds) for this page to change.

I love You !!!

_____________
Example Using Promise
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Promise Object</h1>
<h2>The then() Method</h2>

<p>Wait 3 seconds (3000 milliseconds) for this page to change.</p>

<h1 id="demo"></h1>

<script>
const myPromise = new Promise(function(myResolve, myReject) {
  setTimeout(function(){ myResolve("I love You !!"); }, 3000);
});

myPromise.then(function(value) {
  document.getElementById("demo").innerHTML = value;
});
</script>

</body>
</html>
```
Output:

# JavaScript Promise Object
**The then() Method**

Wait 3 seconds (3000 milliseconds) for this page to change.

I love You !!

_____________

**Waiting for a file**

Example using Callback
```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Callbacks</h2>

<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function getFile(myCallback) {
  let req = new XMLHttpRequest();
  req.onload = function() {
    if (req.status == 200) {
      myCallback(this.responseText);
    } else {
      myCallback("Error: " + req.status);
    }
  }
  req.open('GET', "mycar.html");
  req.send();
}

getFile(myDisplayer); 
</script>

</body>
</html>
```
Output:
# JavaScript Callbacks
Nice car
A car is a wheeled, self-powered motor vehicle used for transportation. Most definitions of the term specify that cars are designed to run primarily on roads, to have seating for one to eight people, to typically have four wheels.

(Wikipedia)

__________________

**Example using Promise**
```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Promise Object</h1>
<h2>The then() Method</h2>

<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

let myPromise = new Promise(function(myResolve, myReject) {
  let req = new XMLHttpRequest();
  req.open('GET', "mycar.html");
  req.onload = function() {
    if (req.status == 200) {
      myResolve(req.response);
    } else {
      myReject("File not Found");
    }
  };
  req.send();
});

myPromise.then(
  function(value) {myDisplayer(value);},
  function(error) {myDisplayer(error);}
);
</script>

</body>
</html>
```
# JavaScript Promise Object
**The then() Method**

Nice car

A car is a wheeled, self-powered motor vehicle used for transportation. Most definitions of the term specify that cars are designed to run primarily on roads, to have seating for one to eight people, to typically have four wheels.

(Wikipedia)
____________________

**Async Syntax**

The keyword async before a function makes the function return a promise:

Example

```
async function myFunction() {
return "Hello";
}
```
Is the same as:

```
function myFunction() {
return Promise.resolve("Hello");
}
```

Here is how to use the Promise:

```
myFunction().then(
function(value) { /* code if successful */ },
function(error) { /* code if some error */ }
);
```
Example

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript async / await</h1>
<p id="demo"></p>

<script>
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

async function myFunction() {return "Hello";}

myFunction().then(
  function(value) {myDisplayer(value);},
  function(error) {myDisplayer(error);}
);</script>

</body>
</html>
```
# JavaScript async / await
Hello

Or simpler, since you expect a normal value (a normal response, not an error):

```
async function myFunction() {
return "Hello";
}
myFunction().then(
function(value) {myDisplayer(value);}
);
```

**Await Syntax**

The await keyword can only be used inside an async function.

The await keyword makes the function pause the execution and wait for a resolved promise before it continues:

`let value = await promise;`

Example

Let's go slowly and learn how to use it.

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript async / await</h1>
<h2 id="demo"></h2>

<script>
async function myDisplay() {
  let myPromise = new Promise(function(resolve, reject) {
    resolve("I love Javascript !!");
  });
  document.getElementById("demo").innerHTML = await myPromise;
}

myDisplay();
</script>

</body>
</html>
```

Output:
# JavaScript async / await

I love Javascript !!
______________

The two arguments (resolve and reject) are pre-defined by JavaScript.

We will not create them, but call one of them when the executor function is ready.

Very often we will not need a reject function.

**Waiting for a Timeout**

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript async / await</h1>
<h2 id="demo"></h2>

<p>Wait 3 seconds (3000 milliseconds) for this page to change.</p>

<script>
async function myDisplay() {
  let myPromise = new Promise(function(resolve) {
    setTimeout(function() {resolve("I love Javascript !!");}, 3000);
  });
  document.getElementById("demo").innerHTML = await myPromise;
}

myDisplay();
</script>

</body>
</html>
```
Output:

JavaScript async / await
I love Javascript !!
Wait 3 seconds (3000 milliseconds) for this page to change.
______
Waiting for a File

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript async / await</h1>
<p id="demo"></p>

<script>
async function getFile() {
  let myPromise = new Promise(function(resolve) {
    let req = new XMLHttpRequest();
    req.open('GET', "mycar.html");
    req.onload = function() {
      if (req.status == 200) {
        resolve(req.response);
      } else {
        resolve("File not Found");
      }
    };
    req.send();
  });
  document.getElementById("demo").innerHTML = await myPromise;
}

getFile();
</script>

</body>
</html>
```
