# Control Flow

Javascript control flow is similar to other programming language such as Java, Python and C. The core idea are the following parts,

* if/else, switch branches
* loop, break, continue
* switch and goto labels

## if/else

First, let us take a look at `if/else` structure.

A program can have the following situations,

* only use `if(...){}`
* use `if(...){} else{}` structure
* use `if(...){} else if(...){}` structure
* use `if(...){} else if(...){} and else{}` structure

**Example 1**

```javascript
<!DOCTYPE html>
<html>
<body>
<h2>JavaScript if(){}_else{}/else_if(){}/else{}</h2>
<p>This program is to test our if else logics</p>
<p id="demo">Good Evening!</p>

<script>
    var currentTime = new Date().getHours(); // based in 24 hrs format
    document.write("<h2>This is an complete example of using, only if</h2>");
    if (currentTime < 13) { // fasting at 4 PM
        document.getElementById("demo").innerHTML = "You see this message";
    } else if (currentTime < 18) {
       
    }
    else if (currentTime < 23 ) {
         // let say currentTime is 22.
        // skip the above blocks,
        // it is actually  currentTime>=18 && currentTime< 23
        document.write("debug here....");
        console.log("debugging on the web page");
    }
</script>
</body>
</html>
```

**Example 2**

```javascript
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript if(){}_else{}/else_if(){}/else{}</h2>
<p>This program is to test our if else logics</p>
<p id="demo">Good Evening!</p>
<script>
    var currentTime = new Date().getHours(); // based in 24 hrs format
    document.write("<h2>This is an complete example of using, only if</h2>");
    if (currentTime < 16) { // fasting at 4 PM
        document.getElementById("demo").innerHTML = "Reminder to eat your brunch!!";
    } else {
        document.getElementById("demo").innerHTML = "Reminder to eat your dinner!!";
    }
</script>
</body>
</html>
```

**Example 3**

```javascript
<!DOCTYPE html>
<html>
<body>
<h2>JavaScript if(){}_else{}/else_if(){}/else{}</h2>
<p>This program is to test our if else logics</p>
<p id="demo">Good Evening!</p>

<script>
    var currentTime = new Date().getHours(); // based in 24 hrs format
    document.write(<h2>This is an complete example of using, if else + else if + else</h2>);
    if (currentTime < 12) {
        document.getElementById("demo").innerHTML = "Good morning!";
    } else if (currentTime < 18) { // sunset time
        document.getElementById("demo").innerHTML = "Good afternoon!";
    } else {
        document.getElementById("demo").innerHTML = "Good evening!";
    }
</script>

<script>
  document.write("<h2>This is an complete example of using, only if</h2>");
    if (currentTime < 16) { // fasting at 4 PM
        document.getElementById("demo").innerHTML = "Reminder to eat your brunch!!";
    } else {
        document.getElementById("demo").innerHTML = "Reminder to eat your dinner!!";
    }
    </script>
</body>
</html>
```

## Loops

The most import loop is `for` and `while` loop.

Here we can take a look at for loop,

**Example 1 For loop with index variable**

```javascript
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript For Loop</h2>

<p id="demo"></p>

<script>
const cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];

var text = "";

// 0, 1, 2, 3, 4, 5
for (var i = 0; i < cars.length; i++) {

    if (i % 2 == 0) {
      text += cars[i] + "<br>";
    } else {
        text += cars[i] + "&nbsp&nbsp";
    }
}

document.getElementById("demo").innerHTML = text;
</script>

</body>
</html>
```

**For Example2**

There are two usages,

* `for ... in`, the var is the index

* `for ... of`, the var is the object

```javascript
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript For In Loop</h2>
<p>The for in statement loops through the properties of an object:</p>

<p id="demo"></p>

<script>


const person = {fname:"John", lname:"Doe", age:25}; 

let txt = "";
for (let x in person) {
  txt += person[x] + " ";
}

document.getElementById("demo").innerHTML = txt;

const fruits = ["orange", "apple", "kiwi"];

// this is the index
for (let f in fruits) {
    document.write(f + "<br>");
}


document.write("<h2>examples of loop in</h2>");

// to show element in an array you can do this,


for (let f in fruits) {
    document.write(fruits[f] + "<br>");
}

document.write("<h2>examples of loop of</h2>");

// if you don't want to use the index, and just use it as other programming like python or java, 
// then you can still do this,

const cars = ["BMW", "Volvo", "Mini"];

let text = "";
for (let x of cars) {
  text += x + "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
}
document.write(text);

document.write("<h2>This is another example not using += operator</h2>");
text="";
for (let x of cars) {
  text = text + x + "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
}
document.write(text);


document.write("<h2>Object array examples</h2>");
// objects array

const students = [
  {"first_name": "Kevin", "last_name": "li", "age": 10},
  {"first_name": "Tom", "last_name": "Jr", "age": 12},
  {"first_name": "Jake", "last_name": "Blake", "age": 22},
];


for (let s of students) {
    document.write(JSON.stringify(s) + "<br/>");
}


</script>

</body>
</html>
```
