# SASS

A Sass can be compiled into a CSS files making it writing many files easy.If you are using create react app you are in luck because the processing part is already taken care of for you. If not you can use Grunt or Gulp to process your Sass/SCSS files into CSS.

There are an endless number of frameworks built with Sass. Bootstrap, Bourbon, and Susy just to name a few.

## Syntax SCSS vs SASS

SASS is a pre-processor scripting language that will be compiled or interpreted into CSS. SassScript is itself a scripting language whereas SCSS is the main syntax for the SASS which builds on top of the existing CSS syntax.

What’s the difference between Sass and SCSS. Well, both of them can be compiled into CSS. The real difference is in syntax. SCSS uses mostly the same syntax of CSS while Sass takes away curly braces and semi-colons. In both you can use the additional features that Sass provides.

**SCSS SYNTAX**

```css
$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

**SASS SYNTAX**

```css
$font-stack:    Helvetica, sans-serif
$primary-color: #333

body
  font: 100% $font-stack
  color: $primary-color
```

## Variables

If you use any coding language you know what a variable is. So I won’t go too in depth with this. Essentially Sass finally allows you to define variables so that if you decide to change say a color you don’t have to change it 1000 times. You can just change your primary color variable in one place and you’re good to go

```css
$primary-color: #333;
body {
  background-color: $primary-color;
}
.text {
  color: $primary-color;
}
```

## Nesting

In CSS you cannot nest. Let’s take a look at these two selectors. There is nothing terribly wrong with this. But we are repeating code.

```css
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
```

We can nest in Sass like so. This looks much cleaner.

```css
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }
}
```

## Partials (_, modular css file)

Partials are Sass or Scss files that have an underscore in the front of the filename. For example. “_test.scss”. What does this do? It denote’s that this particular file should not be turned into CSS when the time comes. These files will contain snippets of CSS that can then be imported by other SCSS files.

This is a great way to modularize your CSS and keep things easier to maintain. For example you may want to store variables that will be used in multiple files. This is the way to do it.

## Mixins

Mixins are interesting because they add a coding language-like feature. You will immediately recognize what I mean upon seeing the code:

```css
@mixin transform($property) {
  -webkit-transform: $property;
  -ms-transform: $property;
  transform: $property;
}
.box { @include transform(rotate(30deg)); }
```

Instead of typing out “rotate(30deg)” 3 times. You can create what essentially feels like a function and sort of acts like one. You pass in the property to the transform() mixin.

## Installation

* NPM installation

Three ways to install, but npm is slower because this is the node implementation of sass binary.

`npm install -g sass`

* Install on Windows (Chocolatey)

`choco install sass`

* Install on Mac OS X or Linux (Homebrew)

`brew install sass/sass/sass`

## Usage

`sass source/stylesheets/index.scss build/stylesheets/index.css`

## Parsing

* InputEncoding: default to UTF-8.

* Parse Errors: When Sass encounters invalid syntax in a stylesheet, parsing will fail and an error will be presented to the user with information about the location of the invalid syntax and the reason it was invalid.

## Statements

Universal StatementsUniversal Statements permalink
These types of statements can be used anywhere in a Sass stylesheet:

Variable declarations, like $var: value.
Flow control at-rules, like @if and @each.
The @error, @warn, and @debug rules.

CSS StatementsCSS Statements permalink
These statements produce CSS. They can be used anywhere except within a @function:

Style rules, like h1 { /* ... */ }.
CSS at-rules, like @media and @font-face.
Mixin uses using @include.
The @at-root rule.

Top-Level StatementsTop-Level Statements permalink
These statements can only be used at the top level of a stylesheet, or nested within a CSS statement at the top level:

Module loads, using @use.
Imports, using @import.
Mixin definitions using @mixin.
Function definitions using @function.

## Expressions

An expression is anything that goes on the right-hand side of a property or variable declaration. Each expression produces a value. Any valid CSS property value is also a Sass expression, but Sass expressions are much more powerful than plain CSS values. They’re passed as arguments to mixins and functions, used for control flow with the @if rule, and manipulated using arithmetic. We call Sass’s expression syntax SassScript.

LiteralsLiterals permalink
The simplest expressions just represent static values:

Numbers, which may or may not have units, like 12 or 100px.
Strings, which may or may not have quotes, like "Helvetica Neue" or bold.
Colors, which can be referred to by their hex representation or by name, like #c6538c or blue.
The boolean literals true or false.
The singleton null.
Lists of values, which may be separated by spaces or commas and which may be enclosed in square brackets or no brackets at all, like 1.5em 1em 0 2em, Helvetica, Arial, sans-serif, or [col1-start].
Maps that associate values with keys, like ("background": red, "foreground": pink).

Operations

Sass defines syntax for a number of operations:

== and != are used to check if two values are the same.
+, -, *, /, and % have their usual mathematical meaning for numbers, with special behaviors for units that matches the use of units in scientific math.
<, <=, >, and >= check whether two numbers are greater or less than one another.
and, or, and not have the usual boolean behavior. Sass considers every value "true" except for false and null.
+, -, and / can be used to concatenate strings.
( and ) can be used to explicitly control the precedence order of operations.

Other ExpressionsOther Expressions permalink
Variables, like $var.
Function calls, like nth($list, 1) or var(--main-bg-color), which may call Sass core library functions or user-defined functions, or which may be compiled directly to CSS.
Special functions, like calc(1px + 100%) or url(http://myapp.com/assets/logo.png), that have their own unique parsing rules.
The parent selector, &.
The value !important, which is parsed as an unquoted string.

## Documentation Comments

## Ref

- https://sass-lang.com/install/
- https://sass-lang.com/documentation/syntax/