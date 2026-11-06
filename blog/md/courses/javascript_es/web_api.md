# Web APIs 

A Web API is a developer's dream.

- It can extend the functionality of the browser
- It can greatly simplify complex functions
- It can provide easy syntax to complex code

**Browser APIs**

All browsers have a set of built-in Web APIs to support complex operations, and to help accessing data.

For example, the Geolocation API can return the coordinates of where the browser is located.

```
<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Geolocation</h1>

<p>Click the button to get your coordinates.</p>

<button onclick="getLocation()">Try It</button>

<p id="demo"></p>

<script>
const x = document.getElementById("demo");

function getLocation() {
  try {
    navigator.geolocation.getCurrentPosition(showPosition);
  } catch(err) {
    x.innerHTML = err;
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
</script>

</body>
</html>
```


<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Geolocation</h1>

<p>Click the button to get your coordinates.</p>

<button onclick="getLocation()">Try It</button>

<p id="demo"></p>

<script>
const x = document.getElementById("demo");

function getLocation() {
  try {
    navigator.geolocation.getCurrentPosition(showPosition);
  } catch(err) {
    x.innerHTML = err;
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
</script>

</body>
</html>

Latitude: 40.9164805

Longitude: -74.1204244

**Third Party APIs**

Third party APIs are not built into your browser.

To use these APIs, you will have to download the code from the Web.

Examples:

- YouTube API - Allows you to display videos on a web site.
- Twitter API - Allows you to display Tweets on a web site.
- Facebook API - Allows you to display Facebook info on a web site.

**JavaScript Validation API**

Constraint Validation DOM Methods:

checkValidity()	: Returns true if an input element contains valid data.

setCustomValidity()	: Sets the validationMessage property of an input element.

If an input field contains invalid data, display a message:

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Validation</h2>

<p>Enter a number and click OK:</p>

<input id="id1" type="number" min="100" max="300" required>
<button onclick="myFunction()">OK</button>

<p>If the number is less than 100 or greater than 300, an error message will be displayed.</p>

<p id="demo"></p>

<script>
function myFunction() {
  const inpObj = document.getElementById("id1");
  if (!inpObj.checkValidity()) {
    document.getElementById("demo").innerHTML = inpObj.validationMessage;
  } else {
    document.getElementById("demo").innerHTML = "Input OK";
  } 
} 
</script>

</body>
</html>

```

<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Validation</h2>

<p>Enter a number and click OK:</p>

<input id="id1" type="number" min="100" max="300" required>
<button onclick="myFunction()">OK</button>

<p>If the number is less than 100 or greater than 300, an error message will be displayed.</p>

<p id="demo"></p>

<script>
function myFunction() {
  const inpObj = document.getElementById("id1");
  if (!inpObj.checkValidity()) {
    document.getElementById("demo").innerHTML = inpObj.validationMessage;
  } else {
    document.getElementById("demo").innerHTML = "Input OK";
  } 
} 
</script>

</body>
</html>

**Constraint Validation DOM Properties**

validity:	Contains boolean properties related to the validity of an input element.

validationMessage:	Contains the message a browser will display when the validity is false.

willValidate:	Indicates if an input element will be validated.

Validity Properties
The validity property of an input element contains a number of properties related to the validity of data:

- customError:	Set to true, if a custom validity message is set.
- patternMismatch:	Set to true, if an element's value does not match its pattern attribute.
- rangeOverflow:	Set to true, if an element's value is greater than its max attribute.
- rangeUnderflow: 	Set to true, if an element's value is less than its min attribute.
- stepMismatch:	Set to true, if an element's value is invalid per its step attribute.
- tooLong:	Set to true, if an element's value exceeds its maxLength attribute.
- typeMismatch:	Set to true, if an element's value is invalid per its type attribute.
- valueMissing:	Set to true, if an element (with a required attribute) has no value.
- valid:	Set to true, if an element's value is valid.

Examples

If the number in an input field is greater than 100 (the input's max attribute), display a message:

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Validation</h2>

<p>Enter a number and click OK:</p>

<input id="id1" type="number" max="100">
<button onclick="myFunction()">OK</button>

<p>If the number is greater than 100 (the input's max attribute), an error message will be displayed.</p>

<p id="demo"></p>

<script>
function myFunction() {
  let text;
  if (document.getElementById("id1").validity.rangeOverflow) {
    text = "Value too large";
  } else {
    text = "Input OK";
  } 
  document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Validation</h2>

<p>Enter a number and click OK:</p>

<input id="id1" type="number" max="100">
<button onclick="myFunction()">OK</button>

<p>If the number is greater than 100 (the input's max attribute), an error message will be displayed.</p>

<p id="demo"></p>

<script>
function myFunction() {
  let text;
  if (document.getElementById("id1").validity.rangeOverflow) {
    text = "Value too large";
  } else {
    text = "Input OK";
  } 
  document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>

If the number in an input field is less than 100 (the input's min attribute), display a message:

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Validation</h2>

<p>Enter a number and click OK:</p>

<input id="id1" type="number" min="100">
<button onclick="myFunction()">OK</button>

<p>If the number is less than 100 (the input's min attribute), an error message will be displayed.</p>

<p id="demo"></p>

<script>
function myFunction() {
  let text;
  if (document.getElementById("id1").validity.rangeUnderflow) {
    text = "Value too small";
  } else {
    text = "Input OK";
  } 
  document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>
```

<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Validation</h2>

<p>Enter a number and click OK:</p>

<input id="id1" type="number" min="100">
<button onclick="myFunction()">OK</button>

<p>If the number is less than 100 (the input's min attribute), an error message will be displayed.</p>

<p id="demo"></p>

<script>
function myFunction() {
  let text;
  if (document.getElementById("id1").validity.rangeUnderflow) {
    text = "Value too small";
  } else {
    text = "Input OK";
  } 
  document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>

**Web History API**

The Web History API provides easy methods to access the windows.history object.

The window.history object contains the URLs (Web Sites) visited by the user.

**The History back() Method**

The back() method loads the previous URL in the windows.history list.

It is the same as clicking the "back arrow" in your browser.

```
<button onclick="myFunction()">Go Back</button>

<script>
function myFunction() {
  window.history.back();
}
</script>

```

<button onclick="myFunction()">Go Back</button>

<script>
function myFunction() {
  window.history.back();
}
</script>

**The History go() Method**

The go() method loads a specific URL from the history list:

Example

```
<button onclick="myFunction()">Go Back 2 Pages</button>

<script>
function myFunction() {
  window.history.go(-2);
}
</script>
```

<button onclick="myFunction()">Go Back 2 Pages</button>

<script>
function myFunction() {
  window.history.go(-2);
}
</script>

**History Object Properties**

- length:	Returns the number of URLs in the history list

**History Object Methods**

- back():	Loads the previous URL in the history list
- forward():	Loads the next URL in the history list
- go():	Loads a specific URL from the history list

**Web Storage API**

The Web Storage API is a simple syntax for storing and retrieving data in the browser. It is very easy to use:
```
<p id="demo"></p>

<script>
localStorage.setItem("name","John Doe");
document.getElementById("demo").innerHTML = localStorage.getItem("name");
</script>

```

**The localStorage Object**

The localStorage object provides access to a local storage for a particular Web Site. It allows you to store, read, add, modify, and delete data items for that domain.

The data is stored with no expiration date, and will not be deleted when the browser is closed.

The data will be available for days, weeks, and years.

**The setItem() Method**

The localStorage.setItem() method stores a data item in a storage.

It takes a name and a value as parameters:

Example

`localStorage.setItem("name", "John Doe");`

**The getItem() Method**

The localStorage.getItem() method retrieves a data item from the storage.

It takes a name as parameter:

Example

`localStorage.getItem("name");`

**The sessionStorage Object**

The sessionStorage object is identical to the localStorage object.

The difference is that the sessionStorage object stores data for one session.

The data is deleted when the browser is closed.

Example

`sessionStorage.getItem("name");`

**The setItem() Method**

The sessionStorage.setItem() method stores a data item in a storage.

It takes a name and a value as parameters:

Example

`sessionStorage.setItem("name", "John Doe");`

**The getItem() Method**

The sessionStorage.getItem() method retrieves a data item from the storage.

It takes a name as parameter:

Example

`sessionStorage.getItem("name");`

**Storage Object Properties and Methods**

- key(n):	Returns the name of the nth key in the storage
- length:	Returns the number of data items stored in the Storage object
- getItem(keyname):	Returns the value of the specified key name
- setItem(keyname, value):	Adds a key to the storage, or updates a key value (if it already exists)
- removeItem(keyname):	Removes that key from the storage
- clear():	Empty all key out of the storage

**Related Pages for Web Storage API**

- window.localStorage: 	Allows to save key/value pairs in a web browser. Stores the data with no expiration date
- window.sessionStorage:	Allows to save key/value pairs in a web browser. Stores the data for one session
_________________________

**Web Workers API**

A web worker is a JavaScript running in the background, without affecting the performance of the page.

**What is a Web Worker?**

When executing scripts in an HTML page, the page becomes unresponsive until the script is finished.

A web worker is a JavaScript that runs in the background, independently of other scripts, without affecting the performance of the page. You can continue to do whatever you want: clicking, selecting things, etc., while the web worker runs in the background.

Web Workers Example:

The example below creates a simple web worker that count numbers in the background:
```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Web Workers API</h2>
<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button> 
<button onclick="stopWorker()">Stop Worker</button>

<script>
let w;

function startWorker() {
  if(typeof(w) == "undefined") {
    w = new Worker("demo_workers.js");
  }
  w.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data;
  };
}

function stopWorker() { 
  w.terminate();
  w = undefined;
}
</script>

</body>
</html>

```

<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Web Workers API</h2>
<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button> 
<button onclick="stopWorker()">Stop Worker</button>

<script>
let w;

function startWorker() {
  if(typeof(w) == "undefined") {
    w = new Worker("demo_workers.js");
  }
  w.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data;
  };
}

function stopWorker() { 
  w.terminate();
  w = undefined;
}
</script>

</body>
</html>


**Check Web Worker Support**

Before creating a web worker, check whether the user's browser supports it:
```
if (typeof(Worker) !== "undefined") {
// Yes! Web worker support!
// Some code.....
} else {
// Sorry! No Web Worker support..
}

```

**Create a Web Worker File**

Now, let's create our web worker in an external JavaScript.

Here, we create a script that counts. The script is stored in the "demo_workers.js" file:
```
let i = 0;

function timedCount() {
i ++;
postMessage(i);
setTimeout("timedCount()",500);
}
timedCount();
```

The important part of the code above is the postMessage() method - which is used to post a message back to the HTML page.

Note: Normally web workers are not used for such simple scripts, but for more CPU intensive tasks.

**Create a Web Worker Object**

Now that we have the web worker file, we need to call it from an HTML page.

The following lines checks if the worker already exists, if not - it creates a new web worker object and runs the code in "demo_workers.js":
```
if (typeof(w) == "undefined") {
w = new Worker("demo_workers.js");
}

```
Then we can send and receive messages from the web worker.

Add an "onmessage" event listener to the web worker.

```
w.onmessage = function(event){
document.getElementById("result").innerHTML = event.data;
};
```
When the web worker posts a message, the code within the event listener is executed. The data from the web worker is stored in event.data.


**Terminate a Web Worker**

When a web worker object is created, it will continue to listen for messages (even after the external script is finished) until it is terminated.

To terminate a web worker, and free browser/computer resources, use the terminate() method:

`w.terminate();`

**Reuse the Web Worker**

If you set the worker variable to undefined, after it has been terminated, you can reuse the code:

`w = undefined;`

**Full Web Worker Example Code**

We have already seen the Worker code in the .js file. Below is the code for the HTML page:
```
<!DOCTYPE html>
<html>
<body>

<p>Count numbers: <output id="result"></output></p>
<button onclick="startWorker()">Start Worker</button>
<button onclick="stopWorker()">Stop Worker</button>

<script>
let w;

function startWorker() {
  if (typeof(w) == "undefined") {
    w = new Worker("demo_workers.js");
  }
  w.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data;
  };
}

function stopWorker() {
  w.terminate();
  w = undefined;
}
</script>

</body>
</html>

```

**Web Workers and the DOM**

Since web workers are in external files, they do not have access to the following JavaScript objects:

- The window object
- The document object
- The parent object

**JavaScript Fetch API**

The Fetch API interface allows web browser to make HTTP requests to web servers.

No need for XMLHttpRequest anymore.

A Fetch API Example 

The example below fetches a file and displays the content:
```
<!DOCTYPE html>
<html>
<body>
<p id="demo">Fetch a file to change this text.</p>
<script>

let file = "fetch_info.txt"

fetch (file)
.then(x => x.text())
.then(y => document.getElementById("demo").innerHTML = y);

</script>
</body>
</html>

```

Since Fetch is based on async and await, the example above might be easier to understand like this:
```
async function getText(file) {
let x = await fetch(file);
let y = await x.text();
myDisplay(y);
}

```

Or even better: Use understandable names instead of x and y:
```
async function getText(file) {
let myObject = await fetch(file);
let myText = await myObject.text();
myDisplay(myText);
}

```
**Web Geolocation API**

**Locate the User's Position**

The HTML Geolocation API is used to get the geographical position of a user.

Since this can compromise privacy, the position is not available unless the user approves it.

Note:
The Geolocation API will only work on secure contexts such as HTTPS.

If your site is hosted on a non-secure origin (such as HTTP) the requests to get the users location will no longer function.

**Using the Geolocation API**

The getCurrentPosition() method is used to return the user's position.

The example below returns the latitude and longitude of the user's position:
```
<script>
const x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
</script>

```

Example explained:

- Check if Geolocation is supported
- If supported, run the getCurrentPosition() method. If not, display a message to the user
- If the getCurrentPosition() method is successful, it returns a coordinates object to the function specified in the parameter (showPosition)
- The showPosition() function outputs the Latitude and Longitude

The example above is a very basic Geolocation script, with no error handling.

**Handling Errors and Rejections**

The second parameter of the getCurrentPosition() method is used to handle errors. It specifies a function to run if it fails to get the user's location:
```
function showError(error) {
switch(error.code) {
case error.PERMISSION_DENIED:
x.innerHTML = "User denied the request for Geolocation."
break;
case error.POSITION_UNAVAILABLE:
x.innerHTML = "Location information is unavailable."
break;
case error.TIMEOUT:
x.innerHTML = "The request to get user location timed out."
break;
case error.UNKNOWN_ERROR:
x.innerHTML = "An unknown error occurred."
break;
}
}

```
**Displaying the Result in a Map**

To display the result in a map, you need access to a map service, like Google Maps.

In the example below, the returned latitude and longitude is used to show the location in a Google Map (using a static image):

```
function showPosition(position) {
let latlon = position.coords.latitude + "," + position.coords.longitude;

let img_url = "https://maps.googleapis.com/maps/api/staticmap?center=
"+latlon+"&zoom=14&size=400x300&sensor=false&key=YOUR_KEY";

document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
}

```
**Location-specific Information**

This page has demonstrated how to show a user's position on a map.

Geolocation is also very useful for location-specific information, like:

- Up-to-date local information
- Showing Points-of-interest near the user
- Turn-by-turn navigation (GPS)

**The getCurrentPosition() Method - Return Data**

The getCurrentPosition() method returns an object on success. The latitude, longitude and accuracy properties are always returned. The other properties are returned if available:

- coords.latitude	The latitude as a decimal number (always returned)
- coords.longitude	The longitude as a decimal number (always returned)
- coords.accuracy	The accuracy of position (always returned)
- coords.altitude	The altitude in meters above the mean sea level (returned if available)
- coords.altitudeAccuracy	The altitude accuracy of position (returned if available)
- coords.heading	The heading as degrees clockwise from North (returned if available)
- coords.speed	The speed in meters per second (returned if available)
- timestamp	The date/time of the response (returned if available)

**Geolocation Object - Other interesting Methods**

The Geolocation object also has other interesting methods:

- watchPosition() - Returns the current position of the user and continues to return updated position as the user moves (like the GPS in a car).
- clearWatch() - Stops the watchPosition() method.

The example below shows the watchPosition() method. You need an accurate GPS device to test this (like smartphone):
```
<script>
const x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}
</script>

```
