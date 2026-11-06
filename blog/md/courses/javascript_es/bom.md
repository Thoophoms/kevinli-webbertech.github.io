# JavaScript Window - The Browser Object Model

**The Browser Object Model (BOM)**

There are no official standards for the Browser Object Model (BOM).

Since modern browsers have implemented (almost) the same methods and properties for JavaScript interactivity, it is often referred to, as methods and properties of the BOM.

**The Window Object**

The window object is supported by all browsers. It represents the browser's window.

All global JavaScript objects, functions, and variables automatically become members of the window object.

Global variables are properties of the window object.

Global functions are methods of the window object.

Even the document object (of the HTML DOM) is a property of the window object:

`window.document.getElementById("header");`

is the same as:

`document.getElementById("header");`
______________________

**Window Size**

Two properties can be used to determine the size of the browser window.

Both properties return the sizes in pixels:

window.innerHeight - the inner height of the browser window (in pixels)
window.innerWidth - the inner width of the browser window (in pixels)

The browser window (the browser viewport) is NOT including toolbars and scrollbars.

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Window</h2>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML =
"Browser inner window width: " + window.innerWidth + "px<br>" +
"Browser inner window height: " + window.innerHeight + "px";
</script>

</body>
</html>
```
**Other Window Methods**

Some other methods:

- window.open() - open a new window
- window.close() - close the current window
- window.moveTo() - move the current window
- window.resizeTo() - resize the current window
_____________________________________

**Window Screen**

The window.screen object contains information about the user's screen.

The window.screen object can be written without the window prefix.

Properties:

- screen.width
- screen.height
- screen.availWidth
- screen.availHeight
- screen.colorDepth
- screen.pixelDepth

**Window Screen Width**

The screen.width property returns the width of the visitor's screen in pixels.

Example:

Display the width of the screen in pixels:

```
document.getElementById("demo").innerHTML =
"Screen Width: " + screen.width;
```
Result will be:

`Screen Width: 1440`

**Window Screen Height**

The screen.height property returns the height of the visitor's screen in pixels.

Example:

Display the height of the screen in pixels:

```
document.getElementById("demo").innerHTML =
"Screen Height: " + screen.height;
```
Result will be:

`Screen Height: 900`

**Window Screen Available Width**

The screen.availWidth property returns the width of the visitor's screen, in pixels, minus interface features like the Windows Taskbar.

Example

Display the available width of the screen in pixels:

```
document.getElementById("demo").innerHTML =
"Available Screen Width: " + screen.availWidth;
```

Result will be:

`Available Screen Width: 1440`

**Window Screen Available Height**

The screen.availHeight property returns the height of the visitor's screen, in pixels, minus interface features like the Windows Taskbar.

Example

Display the available height of the screen in pixels:

```
document.getElementById("demo").innerHTML =
"Available Screen Height: " + screen.availHeight;
```
Result will be:

`Available Screen Height: 819`

**Window Screen Color Depth**
The screen.colorDepth property returns the number of bits used to display one color.

All modern computers use 24 bit or 32 bit hardware for color resolution:

- 24 bits =      16,777,216 different "True Colors"
- 32 bits = 4,294,967,296 different "Deep Colors"

Older computers used 16 bits: 65,536 different "High Colors" resolution.

Very old computers, and old cell phones used 8 bits: 256 different "VGA colors".

Example:

Display the color depth of the screen in bits:

```
document.getElementById("demo").innerHTML =
"Screen Color Depth: " + screen.colorDepth;
```

Result will be:

`Screen Color Depth: 24`

The #rrggbb (rgb) values used in HTML represents "True Colors" (16,777,216 different colors)

**Window Screen Pixel Depth**

The screen.pixelDepth property returns the pixel depth of the screen.

Example

Display the pixel depth of the screen in bits:

```
document.getElementById("demo").innerHTML =
"Screen Pixel Depth: " + screen.pixelDepth;
```

Result will be:

`Screen Pixel Depth: 24`

_________________________________
**JavaScript Window Location**

The window.location object can be used to get the current page address (URL) and to redirect the browser to a new page.

Window Location
The window.location object can be written without the window prefix.

Some examples:

- window.location.href returns the href (URL) of the current page
- window.location.hostname returns the domain name of the web host
- window.location.pathname returns the path and filename of the current page
- window.location.protocol returns the web protocol used (http: or https:)
- window.location.assign() loads a new document

**Window Location Href**

The window.location.href property returns the URL of the current page.

Example 

Display the href (URL) of the current page:

```
document.getElementById("demo").innerHTML =
"Page location is " + window.location.href;
```
Result is:

`Page location is https://www.w3schools.com/js/js_window_location.asp`

**Window Location Hostname**

The window.location.hostname property returns the name of the internet host (of the current page).

Example

Display the name of the host:

``` 
document.getElementById("demo").innerHTML =
"Page hostname is " + window.location.hostname;
```

Result is:

`Page hostname is www.w3schools.com`

**Window Location Pathname**

The window.location.pathname property returns the pathname of the current page.

Example

Display the path name of the current URL:

```
document.getElementById("demo").innerHTML =
"Page path is " + window.location.pathname;
```
Result is:

`Page path is /js/js_window_location.asp`

**Window Location Protocol**

The window.location.protocol property returns the web protocol of the page.

Example

Display the web protocol:

```
document.getElementById("demo").innerHTML =
"Page protocol is " + window.location.protocol;
```
Result is:

`Page protocol is https:`

**Window Location Port**

The window.location.port property returns the number of the internet host port (of the current page).

Example

Display the name of the host:

```
document.getElementById("demo").innerHTML =
"Port number is " + window.location.port;
```
Result is:

`Port number is`

Most browsers will not display default port numbers (80 for http and 443 for https)

**Window Location Assign**

The window.location.assign() method loads a new document.

Example
Load a new document:
```
<html>
<head>
<script>
function newDoc() {
  window.location.assign("https://www.w3schools.com")
}
</script>
</head>
<body>

<input type="button" value="Load new document" onclick="newDoc()">

</body>
</html>
```

<html>
<head>
<script>
function newDoc() {
  window.location.assign("https://www.w3schools.com")
}
</script>
</head>
<body>

<input type="button" value="Load new document" onclick="newDoc()">

</body>
</html>

________________________________
**JavaScript Window History**

The window.history object contains the browsers history.

**Window History**

The window.history object can be written without the window prefix.

To protect the privacy of the users, there are limitations to how JavaScript can access this object.

Some methods:

- history.back() - same as clicking back in the browser
- history.forward() - same as clicking forward in the browser

**Window History Back**

The history.back() method loads the previous URL in the history list.

This is the same as clicking the Back button in the browser.

Example
Create a back button on a page:

```
<html>
<head>
<script>
function goBack() {
  window.history.back()
}
</script>
</head>
<body>

<input type="button" value="Back" onclick="goBack()">

</body>
</html>
```
The output of the code above will be:
<html>
<head>
<script>
function goBack() {
  window.history.back()
}
</script>
</head>
<body>

<input type="button" value="Back" onclick="goBack()">

</body>
</html>

**Window History Forward**

The history.forward() method loads the next URL in the history list.

This is the same as clicking the Forward button in the browser.

Example

Create a forward button on a page:

```
<html>
<head>
<script>
function goForward() {
  window.history.forward()
}
</script>
</head>
<body>

<input type="button" value="Forward" onclick="goForward()">

</body>
</html>
```
The output of the code above will be:

Window History Forward
The history.forward() method loads the next URL in the history list.

This is the same as clicking the Forward button in the browser.

Example
Create a forward button on a page:

<html>
<head>
<script>
function goForward() {
  window.history.forward()
}
</script>
</head>
<body>

<input type="button" value="Forward" onclick="goForward()">

</body>
</html>

__________________________
**JavaScript Window Navigator**

The window.navigator object contains information about the visitor's browser.

**Window Navigator**

The window.navigator object can be written without the window prefix.

Some examples:

- navigator.cookieEnabled
- navigator.appCodeName
- navigator.platform

**Browser Cookies**

The cookieEnabled property returns true if cookies are enabled, otherwise false:
<p id="demo"></p>

```
<script>
document.getElementById("demo").innerHTML =
"cookiesEnabled is " + navigator.cookieEnabled;
</script>
```

**Browser Application Name**

The appName property returns the application name of the browser:

Example:

```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML =
"navigator.appName is " + navigator.appName;
</script>
```

Warning: 
This property is removed (deprecated) in the latest web standard.

Most browsers (IE11, Chrome, Firefox, Safari) returns Netscape as appName.

**Browser Application Code Name**

The appCodeName property returns the application code name of the browser:

Example

```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML =
"navigator.appCodeName is " + navigator.appCodeName;
</script>
```
Warning:
This property is removed (deprecated) in the latest web standard.

Most browsers (IE11, Chrome, Firefox, Safari, Opera) returns Mozilla as appCodeName.

**The Browser Engine**

The product property returns the product name of the browser engine:

```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML =
"navigator.product is " + navigator.product;
</script>
```
Warning:
This property is removed (deprecated) in the latest web standard.

Most browsers returns Gecko as product.

**The Browser Version**

The appVersion property returns version information about the browser:

Example:

```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.appVersion;
</script>
```
**The Browser Agent**

The userAgent property returns the user-agent header sent by the browser to the server:

Example
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.userAgent;
</script>
```
**The Browser Platform**

The platform property returns the browser platform (operating system):

Example
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.platform;
</script>
```
**The Browser Language**

The language property returns the browser's language:

Example
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.language;
</script>
```
**Is The Browser Online?**

The onLine property returns true if the browser is online:

Example
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.onLine;
</script>
```

**Is Java Enabled?**

The javaEnabled() method returns true if Java is enabled:

Example
```
<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = navigator.javaEnabled();
</script>
```
_______________________________

**JavaScript Popup Boxes**

JavaScript has three kind of popup boxes: Alert box, Confirm box, and Prompt box.

**Alert Box**

An alert box is often used if you want to make sure information comes through to the user.

When an alert box pops up, the user will have to click "OK" to proceed.

Syntax:

`window.alert("sometext");`

The window.alert() method can be written without the window prefix.

Example

`alert("I am an alert box!");`

**Confirm Box**

A confirm box is often used if you want the user to verify or accept something.

When a confirm box pops up, the user will have to click either "OK" or "Cancel" to proceed.

If the user clicks "OK", the box returns true. If the user clicks "Cancel", the box returns false.

Syntax:

`window.confirm("sometext");`

The window.confirm() method can be written without the window prefix.

Example

```
if (confirm("Press a button!")) {
txt = "You pressed OK!";
} else {
txt = "You pressed Cancel!";
}
```
**Prompt Box**

A prompt box is often used if you want the user to input a value before entering a page.

When a prompt box pops up, the user will have to click either "OK" or "Cancel" to proceed after entering an input value.

If the user clicks "OK" the box returns the input value. If the user clicks "Cancel" the box returns null.

Syntax:

`window.prompt("sometext","defaultText");`

The window.prompt() method can be written without the window prefix.

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Prompt</h2>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  let text;
  let person = prompt("Please enter your name:", "Harry Potter");
  if (person == null || person == "") {
    text = "User cancelled the prompt.";
  } else {
    text = "Hello " + person + "! How are you today?";
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

<h2>JavaScript Prompt</h2>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  let text;
  let person = prompt("Please enter your name:", "Harry Potter");
  if (person == null || person == "") {
    text = "User cancelled the prompt.";
  } else {
    text = "Hello " + person + "! How are you today?";
  }
  document.getElementById("demo").innerHTML = text;
}
</script>

</body>
</html>

**Line Breaks**

To display line breaks inside a popup box, use a back-slash followed by the character n.

Example:
```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript</h2>
<p>Line-breaks in a popup box.</p>

<button onclick="alert('Hello\nHow are you?')">Try it</button>

</body>
</html>
```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript</h2>
<p>Line-breaks in a popup box.</p>

<button onclick="alert('Hello\nHow are you?')">Try it</button>

</body>
</html>

____________________________
**JavaScript Timing Events**

The window object allows execution of code at specified time intervals.

These time intervals are called timing events.

The two key methods to use with JavaScript are:

- setTimeout(function, milliseconds): 
Executes a function, after waiting a specified number of milliseconds.

- setInterval(function, milliseconds):
Same as setTimeout(), but repeats the execution of the function continuously.

Note: The setTimeout() and setInterval() are both methods of the HTML DOM Window object.

**The setTimeout() Method**

`window.setTimeout(function, milliseconds);`

The window.setTimeout() method can be written without the window prefix.

The first parameter is a function to be executed.

The second parameter indicates the number of milliseconds before execution.
```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Timing</h2>

<p>Click "Try it". Wait 3 seconds, and the page will alert "Hello".</p>

<button onclick="setTimeout(myFunction, 3000);">Try it</button>

<script>
function myFunction() {
  alert('Hello');
}
</script>

</body>
</html>

```

<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Timing</h2>

<p>Click "Try it". Wait 3 seconds, and the page will alert "Hello".</p>

<button onclick="setTimeout(myFunction, 3000);">Try it</button>

<script>
function myFunction() {
  alert('Hello');
}
</script>

</body>
</html>

**How to Stop the Execution?**

The clearTimeout() method stops the execution of the function specified in setTimeout().

window.clearTimeout(timeoutVariable)
The window.clearTimeout() method can be written without the window prefix.

The clearTimeout() method uses the variable returned from setTimeout():

```
myVar = setTimeout(function, milliseconds);
clearTimeout(myVar);
```
If the function has not already been executed, you can stop the execution by calling the clearTimeout() method:
```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Timing</h2>

<p>Click "Try it". Wait 3 seconds. The page will alert "Hello".</p>
<p>Click "Stop" to prevent the first function to execute.</p>
<p>(You must click "Stop" before the 3 seconds are up.)</p>

<button onclick="myVar = setTimeout(myFunction, 3000)">Try it</button>

<button onclick="clearTimeout(myVar)">Stop it</button>

<script>
function myFunction() {
  alert("Hello");
}
</script>
</body>
</html>

```
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript Timing</h2>

<p>Click "Try it". Wait 3 seconds. The page will alert "Hello".</p>
<p>Click "Stop" to prevent the first function to execute.</p>
<p>(You must click "Stop" before the 3 seconds are up.)</p>

<button onclick="myVar = setTimeout(myFunction, 3000)">Try it</button>

<button onclick="clearTimeout(myVar)">Stop it</button>

<script>
function myFunction() {
  alert("Hello");
}
</script>
</body>
</html>

**The setInterval() Method**

The setInterval() method repeats a given function at every given time-interval.

`window.setInterval(function, milliseconds);`

The window.setInterval() method can be written without the window prefix.

The first parameter is the function to be executed.

The second parameter indicates the length of the time-interval between each execution.

This example executes a function called "myTimer" once every second (like a digital watch).

Example

Display the current time:
```
setInterval(myTimer, 1000);

function myTimer() {
const d = new Date();
document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}

```
**How to Stop the Execution?**

The clearInterval() method stops the executions of the function specified in the setInterval() method.

window.clearInterval(timerVariable)
The window.clearInterval() method can be written without the window prefix.

The clearInterval() method uses the variable returned from setInterval():
```
let myVar = setInterval(function, milliseconds);
clearInterval(myVar);

```

Example

Same example as above, but we have added a "Stop time" button:
```
<p id="demo"></p>

<button onclick="clearInterval(myVar)">Stop time</button>

<script>
let myVar = setInterval(myTimer, 1000);
function myTimer() {
  const d = new Date();
  document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}
</script>

```
________________________
**JavaScript Cookies**

Cookies let you store user information in web pages.

**What are Cookies?**

Cookies are data, stored in small text files, on your computer.

When a web server has sent a web page to a browser, the connection is shut down, and the server forgets everything about the user.

Cookies were invented to solve the problem "how to remember information about the user":

When a user visits a web page, his/her name can be stored in a cookie.
Next time the user visits the page, the cookie "remembers" his/her name.
Cookies are saved in name-value pairs like:

`username = John Doe`

When a browser requests a web page from a server, cookies belonging to the page are added to the request. This way the server gets the necessary data to "remember" information about users.

None of the examples below will work if your browser has local cookies support turned off.

**Create a Cookie with JavaScript**

JavaScript can create, read, and delete cookies with the `document.cookie` property.

With JavaScript, a cookie can be created like this:

`document.cookie = "username=John Doe";`

You can also add an expiry date (in UTC time). By default, the cookie is deleted when the browser is closed:

`document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC";`

**Read a Cookie with JavaScript**

With JavaScript, cookies can be read like this:

`let x = document.cookie;`

`document.cookie` will return all cookies in one string much like: cookie1=value; cookie2=value; cookie3=value;

**Change a Cookie with JavaScript**

With JavaScript, you can change a cookie the same way as you create it:

`document.cookie = "username=John Smith; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";`

The old cookie is overwritten.

**Delete a Cookie with JavaScript**

Deleting a cookie is very simple, 
you don't have to specify a cookie value when you delete a cookie.

Just set the expires parameter to a past date:

`document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";`

You should define the cookie path to ensure that you delete the right cookie.

Some browsers will not let you delete a cookie if you don't specify the path.

**The Cookie String**

The document.cookie property looks like a normal text string. But it is not.

Even if you write a whole cookie string to document.cookie, when you read it out again, you can only see the name-value pair of it.

If you set a new cookie, older cookies are not overwritten. The new cookie is added to document.cookie, so if you read document.cookie again you will get something like:

`cookie1 = value; cookie2 = value;`


**JavaScript Cookie Example**

In the example to follow, we will create a cookie that stores the name of a visitor.

The first time a visitor arrives to the web page, he/she will be asked to fill in his/her name. The name is then stored in a cookie.

The next time the visitor arrives at the same page, he/she will get a welcome message.

For the example we will create 3 JavaScript functions:

- A function to set a cookie value
- A function to get a cookie value
- A function to check a cookie value

**A Function to Set a Cookie**

First, we create a function that stores the name of the visitor in a cookie variable:

Example
```
function setCookie(cname, cvalue, exdays) {
const d = new Date();
d.setTime(d.getTime() + (exdays*24*60*60*1000));
let expires = "expires="+ d.toUTCString();
document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
```

Example explained:

The parameters of the function above are the name of the cookie (cname), the value of the cookie (cvalue), and the number of days until the cookie should expire (exdays).

The function sets a cookie by adding together the cookiename, the cookie value, and the expires string.

**A Function to Get a Cookie**

Then, we create a function that returns the value of a specified cookie:

Example

```
function getCookie(cname) {
let name = cname + "=";
let decodedCookie = decodeURIComponent(document.cookie);
let ca = decodedCookie.split(';');
for(let i = 0; i <ca.length; i++) {
let c = ca[i];
while (c.charAt(0) == ' ') {
c = c.substring(1);
}
if (c.indexOf(name) == 0) {
return c.substring(name.length, c.length);
}
}
return "";
}
```
Function explained:

Take the cookiename as parameter (cname).

Create a variable (name) with the text to search for (cname + "=").

Decode the cookie string, to handle cookies with special characters, e.g. '$'

Split document.cookie on semicolons into an array called ca (ca = decodedCookie.split(';')).

Loop through the ca array (i = 0; i < ca.length; i++), and read out each value c = ca[i]).

If the cookie is found (c.indexOf(name) == 0), return the value of the cookie (c.substring(name.length, c.length).

If the cookie is not found, return "".

**A Function to Check a Cookie**

Last, we create the function that checks if a cookie is set.

If the cookie is set it will display a greeting.

If the cookie is not set, it will display a prompt box, asking for the name of the user, and stores the username cookie for 365 days, by calling the setCookie function:
```
function checkCookie() {
let username = getCookie("username");
if (username != "") {
alert("Welcome again " + username);
} else {
username = prompt("Please enter your name:", "");
if (username != "" && username != null) {
setCookie("username", username, 365);
}
}
}
```
