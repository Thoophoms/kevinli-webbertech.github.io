# Enablement and Placement of JS

## Placement

**JavaScript Placement in HTML File**

There is flexibility to place JavaScript code anywhere in an HTML document. 
You would see Javascript are placed in the following scenarios,

* Script in <head>...</head> section.

* Script in <body>...</body> section.

* Script in <body>...</body> and <head>...</head> sections.

* Script in an external file and then include in <head>...</head> section.

You can follow the syntax below to add JavaScript code using the script tag.

```javascript
<script>
   // JavaScript code
</script>
```

In the following section, we will see how we can place JavaScript in an HTML file in different ways.

###  JavaScript in <head>...</head> section

If you want to have a script run on some event, such as when a user clicks somewhere,then you will place that script in the head as follows −

> Hint: This is when you define a function but you did not call it yet.


```ecma script level 4
<html>
<head>
   <script type = "text/javascript">
      function sayHello() {
	     alert("Hello World")
	  }
   </script>
</head>

<body>
   <input type = "button" onclick = "sayHello()" value = "Say Hello" />
</body>
</html>
``` 

### JavaScript in <body>...</body> section

If you need a script to run as the page loads so that the script generates content in the page, then the script goes in the <body> portion of the document. In this case, youwould not have any function defined using JavaScript. Take a look at the following code.

```ecma script level 4
<html>
<head>
</head>
<body>   
   <script type = "text/javascript">
      document.write("Hello World")
   </script>  
   <p>This is web page body </p>   
</body>
</html>
```

### JavaScript in <body> and <head> Sections

You can put your JavaScript code in <head> and <body> sections altogether as follows −

```ecma script level 4
<html>
<head>
   <script type = "text/javascript">
      function sayHello() {
	     alert("Hello World")
	  }
   </script>
</head>
  
<body>
   <script type = "text/javascript">
      document.write("Hello World")
   </script>
   <input type = "button" onclick = "sayHello()" value = "Say Hello" />
</body>
</html>
```

>Hint: How this works is that, JS is parsed line by line or say sequentially,
> then the document.write("Hello World") will go first, then the browser engine renders
> the input type of button, then it will call sayHello() function that you defined earlier.

### JavaScript in External File

As you begin to work more extensively with JavaScript, you will likely find cases where you are reusing identical JavaScript code on multiple pages of a site.

You are not restricted to be maintaining identical code in multiple HTML files. The script tag provides a mechanism to allow you to store JavaScript in an external file and then include it in your HTML files.

To use JavaScript from an external file source, you need to write all your JavaScript source code in a simple text file with the extension ".js" and then include that file as shown below.

For example, you can keep the following content in the filename.js file, and then you can use the sayHello function in your HTML file after including the filename.js file.

```ecma script level 4
function sayHello() {
   alert("Hello World")
}
```

>Hint: External JavaScript file doesn’t contain the <script> tag.
 
You can follow the below code to add multiple scripts into a single HTML file.

```ecma script level 4
<head>
  <script src = "filename1.js" ></script>
  <script src = "filename2.js" ></script>
  <script src = "filename3.js" ></script>
</head>
```

### External References

You can add an external JavaScript file in the HTML using the below 3 ways.

1. Using the full file path

When you need to add any hosted JavaScript file or a file that doesn’t exists in the same project into the HTML, you should use the full file path.

For example,

```ecma script level 4
<head>
  <script src = "C://javascript/filename.js" ></script>
</head>
```

2. Using the relative file path

If you are working on the project and JavaScript and HTML both files are in different folders, you can use the relative file path.

```ecma script level 4
<head>
  <script src = "javascript\filename.js" ></script>
</head>
```

3. Using the filename only

If HTML and JavaScript both files are in the same folder, you can use the file name.

```ecma script level 4
<head>
  <script src = "filename.js" ></script>
</head>
```

## Enablement

**JavaScript in Chrome**

Here are the steps to turn on or turn off JavaScript in Chrome −

* Click the Chrome menu at the top right-hand corner of your browser.

* Select the Settings option. 

* Click on the Privacy and Security tab from the left sidebar.

* Click Show advanced settings at the end of the page.

* Next, click on the Site Settings tab.

Now, scroll to the bottom of the page, and find the content section. Click on the JavaScript tab in the content section.

Here, you can select a radio button to turn JavaScript on or off.

**Warning for Non-JavaScript Browsers**

If you have to do something important using JavaScript, then you can display a warning message to the user using <noscript> tags.

You can add a noscript block immediately after the script block as follows −

```ecma script level 4
<html>
<head>
   <script>
      document.write("Hello World!")
   </script>
  
   <noscript>
	  Sorry...JavaScript is needed to go ahead.
   </noscript>      
</head>
<body>
</body>
</html>
```