# SQL Programming - Aggregation Function and Views

## Outline

* Aggregation Function
* Views
* Other SQL Programming Usage

## Part I Aggregation Function

* An aggregate function is a function that performs a calculation on a set of values, and returns a single value.
* Aggregate functions are often used with the GROUP BY clause of the SELECT statement.
* The **GROUP BY** clause splits the result-set into groups of values and the aggregate function can be used to return a single value for each group.
* SQL **HAVING** clause

The most commonly used SQL aggregate functions are:

MIN() - returns the smallest value within the selected column
MAX() - returns the largest value within the selected column
COUNT() - returns the number of rows in a set
SUM() - returns the total sum of a numerical column
AVG() - returns the average value of a numerical column

### MIN() and MAX()

Assuming the table `Products` already exists with the following structure, please execute it from DBeaver,

```sql
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(255),
    Price DECIMAL(10, 2)
);
```

```sql
INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
VALUES
(1, 'Chais', 1, 1, '10 boxes x 20 bags', 18.00),
(2, 'Chang', 1, 1, '24 - 12 oz bottles', 19.00),
(3, 'Aniseed Syrup', 1, 2, '12 - 550 ml bottles', 10.00),
(4, 'Chef Anton''s Cajun Seasoning', 2, 2, '48 - 6 oz jars', 22.00),
(5, 'Chef Anton''s Gumbo Mix', 2, 2, '36 boxes', 21.35);
```

**Set Column Name (Alias)**

When you use MIN() or MAX(), the returned column will not have a descriptive name. 
To give the column a descriptive name, use the AS keyword:

```sql
SELECT MIN(Price) AS SmallestPrice
FROM Products;
```

**Use MIN() with GROUP BY**
Here we use the MIN() function and the GROUP BY clause, to return the smallest price for each category in the Products table:

```sql
SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;
```

### Count()

***Syntax***

```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

***Example***
```sql
SELECT COUNT(*)
FROM Products;
```

![count.png](../../../images/database/count.png)

***Specify Column***

```sql
SELECT COUNT(ProductName)
FROM Products;
```

***Add a WHERE Clause***

```sql
SELECT COUNT(ProductID)
FROM Products
WHERE Price > 20;
```

***Ignore Duplicates***

```sql
SELECT COUNT(DISTINCT Price)
FROM Products
```

***Use an Alias***

```sql
SELECT COUNT(*) AS [Number of records]
FROM Products;
```

***Use COUNT() with GROUP BY***

```sql
SELECT COUNT(*) AS [Number of records], CategoryID
FROM Products
GROUP BY CategoryID;
```

### SUM()

Let us run the following code in DBeaver to prepare for some data to play with,

-- Assuming the table `OrderDetails` already exists with the following structure:
```sql

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);
```

```sql
INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity)
VALUES
(1, 10248, 11, 12),
(2, 10248, 42, 10),
(3, 10248, 72, 5),
(4, 10249, 14, 9),
(5, 10249, 51, 40);
```

***Syntax***

```sql
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

***Example***

Return the sum of all Quantity fields in the OrderDetails table:

```sql
SELECT SUM(Quantity)
FROM OrderDetails;
```

***Add a WHERE Clause***

```sql
SELECT SUM(Quantity)
FROM OrderDetails
WHERE ProductId = 11;
```

***Use an Alias***

Name the column "total" using `AS` keyword,

```sql
SELECT SUM(Quantity) AS total
FROM OrderDetails;
```

***Use SUM() with GROUP BY***

Here we use the SUM() function and the GROUP BY clause, to return the Quantity for each OrderID in the OrderDetails table:

```sql
SELECT OrderID, SUM(Quantity) AS [Total Quantity]
FROM OrderDetails
GROUP BY OrderID;
```

***SUM() With an Expression***

The parameter inside the SUM() function can also be an expression.

If we assume that each product in the OrderDetails column costs 10 dollars, we can find the total earnings in dollars by multiply each quantity with 10:

Use an expression inside the SUM() function:

```sql
SELECT SUM(Quantity * 10)
FROM OrderDetails;
```
We can also join the OrderDetails table to the Products table to find the actual amount, instead of assuming it is 10 dollars:

Join OrderDetails with Products, and use SUM() to find the total amount:

```sql
SELECT SUM(Price * Quantity)
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;
```

### Average()

The following examples, we will be using the same Products table above.

***Syntax***

```sql
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```

***Add a WHERE Clause***

You can add a WHERE clause to specify conditions:

Return the average price of products in category 1:

```sql
SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;
```

***Use an Alias***

Give the AVG column a name by using the AS keyword.

Name the column "average price":

```sql
SELECT AVG(Price) AS [average price]
FROM Products;
```

***Higher Than Average***

To list all records with a higher price than average, we can use the AVG() function in a sub query:

Return all products with a higher price than the average price:

```sql
SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products);
```

***Use AVG() with GROUP BY***

Here we use the AVG() function and the GROUP BY clause, to return the average price for each category in the Products table:

Example

```sql
SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;
```

## HAVING Clause

***HAVING Syntax***

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```

**Demo Database**

|CustomerID|CustomerName|ContactName|Address|City|PostalCode|Country|
|----------|------------|-----------|-------|----|----------|-------|
|1|Alfreds Futterkiste|Maria Anders|Obere Str. 57|Berlin|12209|Germany|
|2|Ana Trujillo Emparedados y helados|Ana Trujillo|Avda. de la Constitución 2222|México D.F.|05021|Mexico|
|3|Antonio Moreno Taquería|Antonio Moreno|Mataderos|2312 México D.F.|05023|Mexico|
|4|Around the Horn|Thomas Hardy|120 Hanover Sq.|London|WA1|1DP|UK|
|5|Berglunds snabbköp|Christina Berglund|Berguvsvägen 8|Luleå|S-958 22|Sweden|

**SQL HAVING Examples**

```sql
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
```

> Hint: To run this example, please create a table, and then insert the above data into the table, and run the above select.

> Hint: The reason why you can't use `WHERE` instead of using `HAVING` is that you had used a `COUNT` which is an aggregation function already. `WHERE` keyword is used for those plain column attribute for simplicity.

## Part II Views

* In SQL, a view is a virtual table based on the result-set of an SQL statement.

* A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

* You can add SQL statements and functions to a view and present the data as if the data were coming from one single table.

### Create View

***CREATE VIEW Syntax***

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**SQL CREATE VIEW Examples**

```sql
CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = 'Brazil';
```

We can query the view above as follows:

```sql
SELECT * FROM [Brazil Customers];
```

The following SQL creates a view that selects every product in the "Products" table with a price higher than the average price:

```sql
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
```

We can query the view above as follows:

`SELECT * FROM [Products Above Average Price];`

### Update View

***SQL CREATE OR REPLACE VIEW Syntax***

```sql
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

***Example***

```sql
CREATE OR REPLACE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = 'Brazil';
```

### SQL Dropping a View

***Drop view Syntax***

`DROP VIEW view_name;`

## Part III Others Operators

### `In` Operator

* The IN operator allows you to specify multiple values in a WHERE clause.

* The IN operator is a shorthand for multiple OR conditions.

***Syntax***

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

***Example***

```sql
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');
```

**NOT IN**

***Example***

```sql
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK');
```

**IN (SELECT)**

You can also use IN with a subquery in the WHERE clause.

```sql
SELECT * FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);
```

**NOT IN (SELECT)**

Similar to the above one,

```sql
SELECT * FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);
```

## `Between` Operator

* The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.

* The BETWEEN operator is inclusive: begin and end values are included.

```sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
```

**NOT BETWEEN**

Similar to the above example,

```sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;
```

**BETWEEN with IN**

```sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID IN (1,2,3);
```

**BETWEEN Text Values**

```sql
SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;
```

```sql
SELECT * FROM Products
WHERE ProductName BETWEEN "Carnarvon Tigers" AND "Chef Anton's Cajun Seasoning"
ORDER BY ProductName;
```

**NOT BETWEEN Text Values**

```sql
SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY ProductName;
```

**BETWEEN Dates**

```sql
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;
```

or 

```sql
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
```

### `Alias`

**Alias on column name**

```sql
SELECT column_name AS alias_name
FROM table_name;
```

* An alias is created with the `AS` keyword. But it can be optional.

```sql
SELECT CustomerID AS ID
FROM Customers;
```

The following works too without `AS`,

```sql
SELECT CustomerID ID
FROM Customers;
```

Another example,

```sql
SELECT CustomerID AS ID, CustomerName AS Customer
FROM Customers;
```

**Alias on table name**

***Syntax***

```sql
SELECT column_name(s)
FROM table_name AS alias_name;
```

Example,

```sql
SELECT * FROM Customers AS Persons;
```

It is normally used in a complex query where you use the new alias in the `where` statement.

```sql
SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName='Around the Horn' AND c.CustomerID=o.CustomerID;
```

Of course, it works without alias too with their original table name,

```sql
SELECT Orders.OrderID, Orders.OrderDate, Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerName='Around the Horn' AND Customers.CustomerID=Orders.CustomerID;
```

**Using Aliases With a Space Character**

If your new name contains whitespace, then it should be the following,

```sql
SELECT ProductName AS [My Great Products]
FROM Products;
```

or,

```sql
SELECT ProductName AS "My Great Products"
FROM Products;
```

At anytime, you have to put the into a bracket, [] or ""

**Concatenate Columns**

Repurpose one column for a new column like the following,

```sql
SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country AS Address
FROM Customers;
```

or you can use `concat` function,

```sql
SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;
```

### Ref

- https://www.w3schools.com
