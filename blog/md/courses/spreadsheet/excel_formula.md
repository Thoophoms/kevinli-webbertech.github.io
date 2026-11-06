# Microsoft Office Excel - Formulas

## Objectives

The aim of this course is to show you how to.

* Work with formulas.
* Use the built-in functions to perform calculations and manipulate text.

### The Components of an Excel Formula

### Entering Formulas

### Cell References in Formulas

* Relative vs Absolute Cell Referencing

* Copying Formulas

* Editing Formulas

* Making Sense of Error Messages

## Homework 2 Work with some built-in functions

* Date(year, month, day) function

1/ Select the sell in which you want the date to appear
2/ Try to insert DATE(2008,1,35) and verify that you can see the serial number representing February 4, 2008.

* Dynamic date function

1/ Select the sell in which you want the date to appear
2/ In the cell, type: =today()
3/ Press [Enter].

* Static date function

Static dates are not updated. The date that is inserted into the cell is the date immediately after the command is entered into the cell. This can be used to enter the date when the worksheet has been
created.

1/ Select the cell in which you want the date to appear.
2/ Press [ Ctrl] and[; ].

The current date appears in the cell and will not be updated.

* Calculate the Number of Days Between Two Dates

You do not have to use the DATE function, or any other function, to calculate the number of days between two dates. Use the subtraction (-) operator to do this.

![Date difference calculation in Excel (Umulhidayah, CC BY-SA 4.0, via Wikimedia Commons)](/blog/images/spreadsheet/date_diff_excel.jpg)

Remember to change the Format for the “Days in between” cell to the number format. Select `Format > Cells` and choose the `Number` Category.

* Working with Text

UPPER, LOWER, PROPER, TRIM Functions

Syntax:
    
`UPPER(text)` Changes text to all uppercase.
`LOWER(text)` Changes text to all lowercase.
`PROPER(text)` Changes text to title case.
`TRIM(text)` where text is the text value to remove the leading and trailing spaces from.
`CONCATENATE(text1, text2)` are 1 to 30 text items to be joined into a single text item. The text items can
be text strings, numbers, or single-cell references.

![UPPER function example in Excel (Umulhidayah, CC BY-SA 4.0, via Wikimedia Commons)](/blog/images/spreadsheet/upper_function_excel.png)

- PROPER and TRIM Functions combined

Functions can be combined to complete multiple tasks at once.

![PROPER function example in Excel (Umulhidayah, CC BY-SA 4.0, via Wikimedia Commons)](/blog/images/spreadsheet/proper_function_excel.png)

- Concatenate example

![CONCATENATE function in Excel (Umulhidayah, CC BY-SA 4.0, via Wikimedia Commons)](/blog/images/spreadsheet/concatenate_excel.jpg)


The “&” operator can be used instead of CONCATENATE to join text items.

