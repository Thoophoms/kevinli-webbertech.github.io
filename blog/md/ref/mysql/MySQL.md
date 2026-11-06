# Login to MySQL

## Log in to MySQL server

- Normal login to root of MySQL

`mysql -u root -p`

Then, enter your root password

## Reset root password in Ubuntu

***Note:*** If you forget the password for the MySQL root user, you can reset it using the following steps:

1. Stop the MySQL Server

`sudo /etc/init.d/mysql stop`

(In some cases, if /var/run/mysqld doesn't exist, you have to create it at first: 

    `sudo mkdir -v /var/run/mysqld && sudo chown mysql /var/run/mysqld`

2. Start the mysqld configuration: 

`sudo mysqld --skip-grant-tables &`

3. Login to MySQL as root: 

`mysql -u root`

4. Update Root Password: Once connected to MySQL, use the following SQL query to update the root password.

`FLUSH PRIVILEGES;`
`ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password'; `
`FLUSH PRIVILEGES;`

5. Exit MySQL

`exit;`

7. Stop MySQL Safe Mode: Stop the server started in safe mode by using one of the following command:

`sudo service mysql stop` : For systems using systemd

or

`sudo /user/local/mysql/support-files/mysql.server stop` : For systems using init.d

8. Start MySQL: Start the MySQL server as normal then enter the new password you just reset


## The MySQL CREATE DATABASE Statement
The CREATE DATABASE statement is used to create a new SQL database.

Syntax

`CREATE DATABASE databasename;`

### CREATE DATABASE Example
The following SQL statement creates a database called "testDB":

`CREATE DATABASE testDB;`

## CREATE Username and Password for the Database

After creating the database, the next step is to create a MySQL User:

`CREATE USER 'myUser'@'localhost' IDENTIFIED BY 'myPassword';`

***Note:*** 

* Replace myUser with your own username

* Replace myPassword with you own password

## Grant Privileges

`GRANT ALL PRIVILEGES ON databasename.* TO 'myUSER'@'localhost';`

***Note:*** 

* Replace databasename with your own database name that you created

* Replace myUser with you own username

### Flush Privileges

`FLUSH PRIVILEGES;`

Once a database is created, you can check it in the list of databases with the following SQL command:

`SHOW DATABASES;`

# MySQL DROP DATABASE Statement
The DROP DATABASE statement is used to drop an existing SQL database.

***Syntax***

`DROP DATABASE databasename;`

***Example***

The following SQL statement drops the existing database "testDB":

`DROP DATABASE testDB;`

## MySQL CREATE TABLE Statement

The CREATE TABLE statement is used to create a new table in a database.

***Syntax***

```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```
The column parameters specify the names of the columns of the table.

The datatype parameter specifies the type of data the column can hold (e.g. varchar, integer, date, etc.).

***Tip:*** For an overview of the available data types, go to our complete [Data Types Reference](https://www.w3schools.com/mysql/mysql_datatypes.asp)

### MySQL CREATE TABLE Example

The following example creates a table called "Persons" that contains five columns: PersonID, LastName, FirstName, Address, and City:

```
CREATE TABLE Persons (
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
);
```

The PersonID column is of type int and will hold an integer.

The LastName, FirstName, Address, and City columns are of type varchar and will hold characters, and the maximum length for these fields is 255 characters.

The empty "Persons" table will now look like this:

| PersonID | LastName | FirstName | Address | City   |
|----------|----------|-----------|---------|--------|
| &nbsp;   | &nbsp;   | &nbsp;    | &nbsp;  | &nbsp; |


### Create Table Using Another Table

A copy of an existing table can also be created using 

`CREATE TABLE`

The new table gets the same column definitions. All columns or specific columns can be selected.

If you create a new table using an existing table, the new table will be filled with the existing values from the old table.

***Syntax***

```
CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....;
```

The following SQL creates a new table called "TestTables" (which is a copy of the "Customers" table):

```
CREATE TABLE TestTable AS
    SELECT customername, contactname
    FROM customers;
```

## The MySQL DROP TABLE Statement

The DROP TABLE statement is used to drop an existing table in a database.

***Syntax***

`DROP TABLE table_name;`

***Note:*** Be careful before dropping a table. Deleting a table will result in loss of complete information stored in the table!

### MySQL DROP TABLE Example
The following SQL statement drops the existing table "Shippers":

`DROP TABLE Shippers;`

## MySQL TRUNCATE TABLE
The TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself.

***Syntax***

`TRUNCATE TABLE table_name;`

## MySQL ALTER TABLE Statement

The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.
The ALTER TABLE statement is also used to add and drop various constraints on an existing table.

### ALTER TABLE - ADD Column

To add a column in a table_name, use the following syntax:

```
ALTER TABLE table_name
ADD column_name datatype;
```

The following SQL adds an "Email" column to the "Customers" table:

```
ALTER TABLE Customers
ADD Email varchar(255);
```

### ALTER TABLE - DROP COLUMN

To delete a column in a table, use the following syntax (notice that some database systems don't allow deleting a column):

```
ALTER TABLE table_name
DROP COLUMN column_name;
```

The following SQL deletes the "Email" column from the "Customers" table:

```
ALTER TABLE Customers
DROP COLUMN Email;
```

### ALTER TABLE - MODIFY COLUMN

To change the datatype of a column in a table, use the following syntax:

```
ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

### MySQL ALTER TABLE Example
Look at the "Persons" table:

| ID | LastName  | FirstName | Address      | City      |
|----|-----------|-----------|--------------|-----------|
| 1  | Hansen    | Ola       | Timoteivn 10 | Sandnes   |
| 2  | Svendson  | Tove      | Borgvn 23    | Sandnes   |
| 3  | Pettersen | Kari      | Storgt 20    | Stavanger |

Now we want to add a column named "DateOfBirth" in the "Persons" table. We use the following SQL statement:

***Example***

```
ALTER TABLE Persons
ADD DateOfBirth date;
```

Notice that the new column, "DateOfBirth", is of type date and is going to hold a date. The data type specifies what type of data the column can hold. For a complete reference of all the data types available in MySQL, go to our complete Data Types reference.

The "Persons" table will now look like this:

| ID  | LastName  | FirstName | Address      | City      | DateOfBirth |
|-----|-----------|-----------|--------------|-----------|-------------|
| 1   | Hansen    | Ola       | Timoteivn 10 | Sandnes   | &nbsp;      |
| 2   | Svendson  | Tove      | Borgvn 23    | Sandnes   | &nbsp;      |
| 3   | Pettersen | Kari      | Storgt 20    | Stavanger | &nbsp;      |


### Change Data Type Example

Now we want to change the data type of the column named "DateOfBirth" in the "Persons" table.

We use the following SQL statement:

***Example***

```
ALTER TABLE Persons
MODIFY COLUMN DateOfBirth year;
```

Notice that the "DateOfBirth" column is now of type year and is going to hold a year in a two- or four-digit format.

### DROP COLUMN Example
Next, we want to delete the column named "DateOfBirth" in the "Persons" table.

We use the following SQL statement:

***Example***

```
ALTER TABLE Persons
DROP COLUMN DateOfBirth;
```

The "Persons" table will now look like this:

| ID | LastName  | FirstName | Address      | City      |
|----|-----------|-----------|--------------|-----------|
| 1  | Hansen    | Ola       | Timoteivn 10 | Sandnes   |
| 2  | Svendson  | Tove      | Borgvn 23    | Sandnes   |
| 3  | Pettersen | Kari      | Storgt 20    | Stavanger |


## MySQL Constraints

## SQL constraints are used to specify rules for data in a table.

### Create Constraints
Constraints can be specified when the table is create with the CREATE TABLE statement, or after the table is created with ALTER TABLE statement.

***Syntax***

```
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
   ....
);
```

### MySQL Constraints

SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

Constraints can be column level or table level. Column level constraints apply to a column, and table level constraints apply to the whole table.

The following constraints are commonly used in SQL:

  1. ***NOT NULL*** - Ensures that a column cannot have a **NULL** value
  2. ***UNIQUE*** - Ensures that all values in a column are different 
  3. ***PRIMARY KEY*** - A combination of a **NOT NULL** and **UNIQUE**. Uniquely identifies each row in a table 
  4. ***FOREIGN KEY*** - Prevents actions that would destroy links between tables 
  5. ***CHECK*** - Ensures that the values in a column satisfies a specific condition 
  6. ***DEFAULT*** - Sets a default value for a column if no value is specified 
  7. ***CREATE INDEX*** - Used to create and retrieve data from the database very quickly

# MySQL NOT NULL Constraint

By default, a column can hold NULL values.

The `NOT NULL` constraint enforces a column to NOT accept NULL values.

This enforces a field to always contain a value, which means that you cannot insert a new record, or update a record withut adding a value to this field.

### NOT NULL on CREATE TABLE

The following SQL ensures that the "ID", "LastName", and "FirstName" columns will NOT accept NULL values when the "Persons" table is created:

***Example***

``` 
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FiestName varchar(255) NOT NULL,
    Age int
);
```

### NOT NULL on ALTER TABLE

To create a `NOT NULL` constraint on the "Age" column when the "Persons" table is alreadt created, use the following SQL:

***Example***

```
ALTER TABLE Persons
MODIFY Age int NOT NULL;
```

# MySQL UNIQUE Constraint

The `UNIQUE` constraint ensures that all values in a column are different.

Both the `UNIQUE` and `PRIMARY KEY` constraints provide a guarantee for uniqueness for a column or set of columns.

A `PRIMARY KEY` constraint automatically has a `UNIQUE` constraint.

However, you can have many `UNIQUE` constraints per table, but only one `PRIMARY KEY` constraint per table.

### UNIQUE Constraint on CREATE TABLE
The following SQL creates a UNIQUE constraint on the "ID" column when the "Persons" table is created:

``` 
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    UNIQUE (ID)
);
```

To name a UNIQUE constraint, and to define a UNIQUE constraint on multiple columns, use the following SQL syntax:

``` 
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT UC_Person UNIQUE (ID,LastName)
);
```

### UNIQUE Constraint on ALTER TABLE

To create a `UNIQUE` constraint on the "ID" column when the table is already created, use the following SQL:

```
ALTER TABLE Persons
ADD UNIQUE (ID);
```

To name a `UNIQUE` constraint, and to define a `UNIQUE` constraint on multiple columns, use the following SQL syntax:

```
ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE (ID,LastName);
```

### DROP a UNIQUE Constraint

To drop a UNIQUE constraint, use the following SQL:

```
ALTER TABLE Persons
DROP INDEX UC_Person;
```

# MySQL PRIMARY KEY Constraint

The `PRIMARY KEY` constraint uniquely identifies each record in a table.

Primary keys must contain UNIQUE values, and cannot contain NULL values.

A table can have only ONE primary key; and in the table, this primary key can consist of single or multiple columns (fields).

### PRIMARY KEY on CREATE TABLE

The following SQL creates a PRIMARY KEY on the "ID" column when the "Persons" table is created:

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
```

To allow naming of a `PRIMARY KEY` constraint, and for defining a `PRIMARY KEY` constraint on multiple columns, use the following SQL syntax:

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CONSTRAINT PK_Person PRIMARY KEY (ID,LastName)
);
```

***Note:*** 

In the example above there is only ONE `PRIMARY KEY` (PK_Person). 
However, the VALUE of the primary key is made up of TWO COLUMNS (ID + LastName).

### PRIMARY KEY on ALTER TABLE

To create a PRIMARY KEY constraint on the "ID" column when the table is already created, use the following SQL:

```
ALTER TABLE Persons
ADD PRIMARY KEY (ID);
```

To allow naming of a `PRIMARY KEY` constraint, and for defining a `PRIMARY KEY` constraint on multiple columns, use the following SQL syntax:

```
ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName);
```

***Note:*** 

If you use ALTER TABLE to add a primary key, the primary key column(s) must have been declared to not contain NULL values (when the table was first created).

### DROP a PRIMARY KEY Constraint
To drop a PRIMARY KEY constraint, use the following SQL:

```
ALTER TABLE Persons
DROP PRIMARY KEY;
```

# MySQL FOREIGN KEY Constraint

The `FOREIGN KEY` constraint is used to prevent actions that would destroy links between tables.

A `FOREIGN KEY` is a field (or collection of fields) in one table, that refers to the `PRIMARY KEY` in another table.

The table with the foreign key is called the child table, and the table with the primary key is called the referenced or parent table.

Look at the following two tables:

### Persons Table

| PersonID | LastName  | FirstName | Age |
|----------|-----------|-----------|-----|
| 1        | Hansen    | Ola       | 30  |
| 2        | Svendson  | Tove      | 23  |
| 3        | Pettersen | Kari      | 20  |

### Orders Table

| OrderID | OrderNumber | PersonID |
|---------|-------------|----------|
| 1       | 77895       | 3        |
| 2       | 44678       | 3        |
| 3       | 22456       | 2        |
| 4       | 24562       | 1        |


Notice that the "PersonID" column in the "Orders" table points to the "PersonID" column in the "Persons" table.

The "PersonID" column in the "Persons" table is the `PRIMARY KEY` in the "Persons" table.

The "PersonID" column in the "Orders" table is a `FOREIGN KEY` in the "Orders" table.

The `FOREIGN KEY` constraint prevents invalid data from being inserted into the foreign key column, because it has to be one of the values contained in the parent table.

### FOREIGN KEY on CREATE TABLE

The following SQL creates a `FOREIGN KEY` on the "PersonID" column when the "Orders" table is created:

```
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
```

To allow naming of a `FOREIGN KEY` constraint, and for defining a `FOREIGN KEY` constraint on multiple columns, use the following SQL syntax:

```
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID)
    REFERENCES Persons(PersonID)
);
```

### FOREIGN KEY on ALTER TABLE

To create a `FOREIGN KEY` constraint on the "PersonID" column when the "Orders" table is already created, use the following SQL:

```
ALTER TABLE Orders
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
```

To allow naming of a `FOREIGN KEY` constraint, and for defining a `FOREIGN KEY` constraint on multiple columns, use the following SQL syntax:

```
ALTER TABLE Orders
    ADD CONSTRAINT FK_PersonOrder
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);
    DROP a FOREIGN KEY Constraint
```

To drop a FOREIGN KEY constraint, use the following SQL:

```
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder;
```

# MySQL CHECK Constraint

The `CHECK` constraint is used to limit the value range that can be placed in a column.

If you define a `CHECK` constraint on a column it will allow only certain values for this column.

If you define a `CHECK` constraint on a table it can limit the values in certain columns based on values in other columns in the row.


### CHECK on CREATE TABLE
The following SQL creates a `CHECK` constraint on the "Age" column when the "Persons" table is created. The `CHECK` constraint ensures that the age of a person must be 18, or older:

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
```

To allow naming of a `CHECK` constraint, and for defining a `CHECK` constraint on multiple columns, use the following SQL syntax:

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);
```

### CHECK on ALTER TABLE
To create a `CHECK` constraint on the "Age" column when the table is already created, use the following SQL:

```
ALTER TABLE Persons
ADD CHECK (Age>=18);
```

To allow naming of a `CHECK` constraint, and for defining a `CHECK` constraint on multiple columns, use the following SQL syntax:

```
ALTER TABLE Persons
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');
```

### DROP a CHECK Constraint

To drop a CHECK constraint, use the following SQL:

```
ALTER TABLE Persons
DROP CHECK CHK_PersonAge;
```

# MySQL DEFAULT Constraint

The `DEFAULT` constraint is used to set a default value for a column.

The default value will be added to all new records, if no other value is specified.

### DEFAULT on CREATE TABLE
The following SQL sets a `DEFAULT` value for the "City" column when the "Persons" table is created:

```
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);
```

The `DEFAULT` constraint can also be used to insert system values, by using functions like CURRENT_DATE():

```
CREATE TABLE Orders (
    ID int NOT NULL,
    OrderNumber int NOT NULL,
    OrderDate date DEFAULT CURRENT_DATE()
);
```

### DEFAULT on ALTER TABLE
To create a `DEFAULT` constraint on the "City" column when the table is already created, use the following SQL:

```
ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes';
```

### DROP a DEFAULT Constraint

To drop a `DEFAULT` constraint, use the following SQL:

```
ALTER TABLE Persons
ALTER City DROP DEFAULT;
```

# MySQL CREATE INDEX Statement
The `CREATE INDEX` statement is used to create indexes in tables.

Indexes are used to retrieve data from the database more quickly than otherwise. The users cannot see the indexes, they are just used to speed up searches/queries.

***Note:*** Updating a table with indexes takes more time than updating a table without (because the indexes also need an update). So, only create indexes on columns that will be frequently searched against.

### CREATE INDEX Syntax

Creates an index on a table. Duplicate values are allowed:

```
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

### CREATE UNIQUE INDEX Syntax
Creates a unique index on a table. Duplicate values are not allowed:

```
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);
```

### MySQL CREATE INDEX Example
The SQL statement below creates an index named "idx_lastname" on the "LastName" column in the "Persons" table:

```
CREATE INDEX idx_lastname
ON Persons (LastName);
```

If you want to create an index on a combination of columns, you can list the column names within the parentheses, separated by commas:

```
CREATE INDEX idx_pname
ON Persons (LastName, FirstName);
```

### DROP INDEX Statement

The DROP INDEX statement is used to delete an index in a table.

```
ALTER TABLE table_name
DROP INDEX index_name;
```

# MySQL AUTO INCREMENT Field

Auto-increment allows a unique number to be generated automatically when a new record is inserted into a table.

Often this is the primary key field that we would like to be created automatically every time a new record is inserted.

### MySQL AUTO_INCREMENT Keyword
MySQL uses the `AUTO_INCREMENT` keyword to perform an auto-increment feature.

By default, the starting value for `AUTO_INCREMENT` is 1, and it will increment by 1 for each new record.

The following SQL statement defines the "Personid" column to be an auto-increment primary key field in the "Persons" table:

```
CREATE TABLE Persons (
    Personid int NOT NULL AUTO_INCREMENT,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (Personid)
);
```

To let the `AUTO_INCREMENT` sequence start with another value, use the following SQL statement:

`ALTER TABLE Persons AUTO_INCREMENT=100;`

When we insert a new record into the "Persons" table, we do NOT have to specify a value for the "Personid" column (a unique value will be added automatically):

```
INSERT INTO Persons (FirstName,LastName)
VALUES ('Lars','Monsen');
```

The SQL statement above would insert a new record into the "Persons" table. The "Personid" column would be assigned a unique value automatically. The "FirstName" column would be set to "Lars" and the "LastName" column would be set to "Monsen".

# MySQL Dates

*The most difficult part when working with dates is to be sure that the format of the date you are trying to insert, matches the format of the date column in the database.*

As long as your data contains only the date portion, your queries will work as expected. However, if a time portion is involved, it gets more complicated.

### MySQL Date Data Types

MySQL comes with the following data types for storing a date or a date/time value in the database:

- DATE - format YYYY-MM-DD
- DATETIME - format: YYYY-MM-DD HH:MI:SS
- TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
- YEAR - format YYYY or YY 

***Note:*** The date data type are set for a column when you create a new table in your database!

### Working with Dates

Look at the following table:

### Orders Table

| OrderId | ProductName            | OrderDate  |
|---------|------------------------|------------|
| 1       | Geitost                | 2008-11-11 |
| 2       | Camembert Pierrot      | 2008-11-09 |
| 3       | Mozzarella di Giovanni | 2008-11-11 |
| 4       | Mascarpone Fabioli     | 2008-10-29 |


Now we want to select the records with an OrderDate of "2008-11-11" from the table above.

We use the following `SELECT` statement:

`SELECT * FROM Orders WHERE OrderDate='2008-11-11'`

The result-set will look like this:

| OrderId | ProductName            | OrderDate  |
|---------|------------------------|------------|
| 1       | Geitost                | 2008-11-11 |
| 3       | Mozzarella di Giovanni | 2008-11-11 |


***Note:*** Two dates can easily be compared if there is no time component involved!

Now, assume that the "Orders" table looks like this (notice the added time-component in the "OrderDate" column):

| OrderId | ProductName            | OrderDate            |
|---------|------------------------|----------------------|
| 1       | Geitost                | 2008-11-11 13:23:44  |
| 2       | Camembert Pierrot      | 2008-11-09 15:45:21  |
| 3       | Mozzarella di Giovanni | 2008-11-11 11:12:01  |
| 4       | Mascarpone Fabioli     | 2008-10-29 14:56:59  |


If we use the same `SELECT` statement as above:

`SELECT * FROM Orders WHERE OrderDate='2008-11-11'`

we will get no result! This is because the query is looking only for dates with no time portion.

***Tip:*** To keep your queries simple and easy to maintain, do not use time-components in your dates, unless you have to!



# MySQL Views

## MySQL CREATE VIEW Statement

In SQL, a view is a virtual table based on the result-set of an SQL statement.

A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

You can add SQL statements and functions to a view and present the data as if the data were coming from one single table.

A view is created with the `CREATE VIEW` statement.

### CREATE VIEW Syntax

```
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

***Note:*** A view always shows up-to-date data! The database engine recreates the view, every time a user queries it.


### MySQL CREATE VIEW Examples

The following SQL creates a view that shows all customers from Brazil:

***Example***

```
CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = 'Brazil';
```

We can query the view above as follows:

***Example***

SELECT * FROM [Brazil Customers];
The following SQL creates a view that selects every product in the "Products" table with a price higher than the average price:

```
Example
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);
```

We can query the view above as follows:

***Example***

`SELECT * FROM [Products Above Average Price];`

___


# MySQL SELECT STATEMENT

The `SELECT` statement is used to select data from a database.

The data returned is stored in a result table, called the result-set.

### SELECT Syntax

```
SELECT column1, column2, ...
FROM table_name;
```

Here, column1, column2, ... are the field names of the table you want to select data from. If you want to select all the fields available in the table, use the following syntax:

`SELECT * FROM table_name;`


### Demo Database
In this tutorial we will use the well-known Northwind sample database.

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                       | ContactName        | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|--------------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Maria Anders       | Obere Str. 57                 | Berlin       | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo       | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno     | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy       | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |
| 5          | Berglunds snabbköp                 | Christina Berglund | Berguvsvägen 8                | Luleå        | S-958 22   | Sweden   |


### SELECT Columns Example

The following SQL statement selects the "CustomerName", "City", and "Country" columns from the "Customers" table:

***Example***
`SELECT CustomerName, City, Country FROM Customers;`


### SELECT * Example

The following SQL statement selects ALL the columns from the "Customers" table:

***Example***

```SELECT * FROM Customers;```



# The MySQL SELECT DISTINCT Statement

The `SELECT DISTINCT` statement is used to return only distinct (different) values.

Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

### SELECT DISTINCT Syntax

```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

### SELECT Example Without DISTINCT
The following SQL statement selects all (including the duplicates) values from the "Country" column in the "Customers" table:

***Example***

`SELECT Country FROM Customers;`

Now, let us use the `SELECT DISTINCT` statement and see the result.


### SELECT DISTINCT Examples

The following SQL statement selects only the DISTINCT values from the "Country" column in the "Customers" table:

***Example***

`SELECT DISTINCT Country FROM Customers;`

The following SQL statement counts and returns the number of different (distinct) countries in the "Customers" table:

***Example***

`SELECT COUNT(DISTINCT Country) FROM Customers;`


# The MySQL WHERE Clause

The `WHERE` clause is used to filter records.

It is used to extract only those records that fulfill a specified condition.

### WHERE Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

***Note:*** The `WHERE` clause is not only used in `SELECT` statements, it is also used in `UPDATE`, `DELETE`, etc.!

### Demo Database
Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                       | ContactName        | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|--------------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Maria Anders       | Obere Str. 57                 | Berlin       | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo       | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno     | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy       | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |
| 5          | Berglunds snabbköp                 | Christina Berglund | Berguvsvägen 8                | Luleå        | S-958 22   | Sweden   |



### WHERE Clause Example

The following SQL statement selects all the customers from "Mexico":

***Example***

```
SELECT * FROM Customers
WHERE Country = 'Mexico';
```

### Text Fields vs. Numeric Fields


SQL requires single quotes around text values (most database systems will also allow double quotes).

However, numeric fields should not be enclosed in quotes:

***Example***

```
SELECT * FROM Customers
WHERE CustomerID = 1;
```

### Operators in The WHERE Clause

The following operators can be used in the `WHERE` clause:

| Operator | Description                                                                  |
|----------|------------------------------------------------------------------------------|
| =        | Equal                                                                        |
| >        | Greater than                                                                 |
| <        | Less than                                                                    |
| >=       | Greater than or equal                                                        |
| <=       | Less than or equal                                                           |
| <>       | Not equal. Note: In some versions of SQL this operator may be written as !=  |
| BETWEEN  | Between a certain range                                                      |
| LIKE     | Search for a pattern                                                         |
| IN       | To specify multiple possible values for a column                             |



# The MySQL AND, OR and NOT Operators

The `WHERE` clause can be combined with `AND`, `OR`, and `NOT` operators.

The `AND` and `OR` operators are used to filter records based on more than one condition:

- The `AND` operator displays a record if all the conditions separated by `AND` are TRUE.
- The `OR` operator displays a record if any of the conditions separated by `OR` is TRUE.
- The `NOT` operator displays a record if the condition(s) is `NOT` TRUE.


### AND Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

### OR Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

### NOT Syntax

```
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

### Demo Database
The table below shows the complete "Customers" table from the Northwind sample database:

| CustomerID | CustomerName                         | ContactName          | Address                              | City            | PostalCode | Country     |
|------------|--------------------------------------|----------------------|--------------------------------------|-----------------|------------|-------------|
| 1          | Alfreds Futterkiste                  | Maria Anders         | Obere Str. 57                        | Berlin          | 12209      | Germany     |
| 2          | Ana Trujillo Emparedados y helados   | Ana Trujillo         | Avda. de la Constitución 2222        | México D.F.     | 05021      | Mexico      |
| 3          | Antonio Moreno Taquería              | Antonio Moreno       | Mataderos 2312                       | México D.F.     | 05023      | Mexico      |
| 4          | Around the Horn                      | Thomas Hardy         | 120 Hanover Sq.                      | London          | WA1 1DP    | UK          |
| 5          | Berglunds snabbköp                   | Christina Berglund   | Berguvsvägen 8                       | Luleå           | S-958 22   | Sweden      |
| 6          | Blauer See Delikatessen              | Hanna Moos           | Forsterstr. 57                       | Mannheim        | 68306      | Germany     |
| 7          | Blondel père et fils                 | Frédérique Citeaux   | 24, place Kléber                     | Strasbourg      | 67000      | France      |
| 8          | Bólido Comidas preparadas            | Martín Sommer        | C/ Araquil, 67                       | Madrid          | 28023      | Spain       |
| 9          | Bon app'                             | Laurence Lebihans    | 12, rue des Bouchers                 | Marseille       | 13008      | France      |
| 10         | Bottom-Dollar Marketse               | Elizabeth Lincoln    | 23 Tsawassen Blvd.                   | Tsawassen       | T2F 8M4    | Canada      |
| 11         | B's Beverages                        | Victoria Ashworth    | Fauntleroy Circus                    | London          | EC2 5NT    | UK          |
| 12         | Cactus Comidas para llevar           | Patricio Simpson     | Cerrito 333                          | Buenos Aires    | 1010       | Argentina   |
| 13         | Centro comercial Moctezuma           | Francisco Chang      | Sierras de Granada 9993              | México D.F.     | 05022      | Mexico      |
| 14         | Chop-suey Chinese                    | Yang Wang            | Hauptstr. 29                         | Bern            | 3012       | Switzerland |
| 15         | Comércio Mineiro                     | Pedro Afonso         | Av. dos Lusíadas, 23                 | São Paulo       | 05432-043  | Brazil      |
| 16         | Consolidated Holdings                | Elizabeth Brown      | Berkeley Gardens 12 Brewery          | London          | WX1 6LT    | UK          |
| 17         | Drachenblut Delikatessend            | Sven Ottlieb         | Walserweg 21                         | Aachen          | 52066      | Germany     |
| 18         | Du monde entier                      | Janine Labrune       | 67, rue des Cinquante Otages         | Nantes          | 44000      | France      |
| 19         | Eastern Connection                   | Ann Devon            | 35 King George                       | London          | WX3 6FW    | UK          |
| 20         | Ernst Handel                         | Roland Mendel        | Kirchgasse 6                         | Graz            | 8010       | Austria     |
| 21         | Familia Arquibaldo                   | Aria Cruz            | Rua Orós, 92                         | São Paulo       | 05442-030  | Brazil      |
| 22         | FISSA Fabrica Inter. Salchichas S.A. | Diego Roel           | C/ Moralzarzal, 86                   | Madrid          | 28034      | Spain       |
| 23         | Folies gourmandes                    | Martine Rancé        | 184, chaussée de Tournai             | Lille           | 59000      | France      |
| 24         | Folk och fä HB                       | Maria Larsson        | Åkergatan 24                         | Bräcke          | S-844 67   | Sweden      |
| 25         | Frankenversand                       | Peter Franken        | Berliner Platz 43                    | München         | 80805      | Germany     |
| 26         | France restauration                  | Carine Schmitt       | 54, rue Royale                       | Nantes          | 44000      | France      |
| 27         | Franchi S.p.A.                       | Paolo Accorti        | Via Monte Bianco 34                  | Torino          | 10100      | Italy       |
| 28         | Furia Bacalhau e Frutos do Mar       | Lino Rodriguez       | Jardim das rosas n. 32               | Lisboa          | 1675       | Portugal    |
| 29         | Galería del gastrónomo               | Eduardo Saavedra     | Rambla de Cataluña, 23               | Barcelona       | 08022      | Spain       |
| 30         | Godos Cocina Típica                  | José Pedro Freyre    | C/ Romero, 33                        | Sevilla         | 41101      | Spain       |
| 31         | Gourmet Lanchonetes                  | André Fonseca        | Av. Brasil, 442                      | Campinas        | 04876-786  | Brazil      |
| 32         | Great Lakes Food Market              | Howard Snyder        | 2732 Baker Blvd.                     | Eugene          | 97403      | USA         |
| 33         | GROSELLA-Restaurante                 | Manuel Pereira       | 5ª Ave. Los Palos Grandes            | Caracas         | 1081       | Venezuela   |
| 34         | Hanari Carnes                        | Mario Pontes         | Rua do Paço, 67                      | Rio de Janeiro  | 05454-876  | Brazil      |
| 35         | HILARIÓN-Abastos                     | Carlos Hernández     | Carrera 22 con Ave. Carlos Soublette | San Cristóbal   | 5022       | Venezuela   |
| 36         | Hungry Coyote Import Store           | Yoshi Latimer        | City Center Plaza 516 Main St.       | Elgin           | 97827      | USA         |
| 37         | Hungry Owl All-Night Grocers         | Patricia McKenna     | 8 Johnstown Road                     | Cork            |            | Ireland     |
| 38         | Island Trading                       | Helen Bennett        | Garden House Crowther Way            | Cowes           | PO31 7PJ   | UK          |
| 39         | Königlich Essen                      | Philip Cramer        | Maubelstr. 90                        | Brandenburg     | 14776      | Germany     |
| 40         | La corne d'abondance                 | Daniel Tonini        | 67, avenue de l'Europe               | Versailles      | 78000      | France      |
| 41         | La maison d'Asie                     | Annette Roulet       | 1 rue Alsace-Lorraine                | Toulouse        | 31000      | France      |
| 42         | Laughing Bacchus Wine Cellars        | Yoshi Tannamuri      | 1900 Oak St.                         | Vancouver       | V3F 2K1    | Canada      |
| 43         | Lazy K Kountry Store                 | John Steel           | 12 Orchestra Terrace                 | Walla Walla     | 99362      | USA         |
| 44         | Lehmanns Marktstand                  | Renate Messner       | Magazinweg 7                         | Frankfurt a.M.  | 60528      | Germany     |
| 45         | Let's Stop N Shop                    | Jaime Yorres         | 87 Polk St. Suite 5                  | San Francisco   | 94117      | USA         |
| 46         | LILA-Supermercado                    | Carlos González      | Carrera 52 con Ave. Bolívar #65-98   | Llano Largo     | 3508       | Venezuela   |
| 47         | LINO-Delicateses                     | Felipe Izquierdo     | Ave. 5 de Mayo Porlamar              | I. de Margarita | 4980       | Venezuela   |
| 48         | Lonesome Pine Restaurant             | Fran Wilson          | 89 Chiaroscuro Rd.                   | Portland        | 97219      | USA         |
| 49         | Magazzini Alimentari Riuniti         | Giovanni Rovelli     | Via Ludovico il Moro 22              | Bergamo         | 24100      | Italy       |
| 50         | Maison Dewey                         | Catherine Dewey      | Rue Joseph-Bens 532                  | Bruxelles       | B-1180     | Belgium     |
| 51         | Mère Paillarde                       | Jean Fresnière       | 43 rue St. Laurent                   | Montréal        | H1J 1C3    | Canada      |
| 52         | Morgenstern Gesundkost               | Alexander Feuer      | Heerstr. 22                          | Leipzig         | 04179      | Germany     |
| 53         | North/South                          | Simon Crowther       | South House 300 Queensbridge         | London          | SW7 1RZ    | UK          |
| 54         | Océano Atlántico Ltda.               | Yvonne Moncada       | Ing. Gustavo Moncada 8585 Piso 20-A  | Buenos Aires    | 1010       | Argentina   |
| 55         | Old World Delicatessen               | Rene Phillips        | 2743 Bering St.                      | Anchorage       | 99508      | USA         |
| 56         | Ottilies Käseladen                   | Henriette Pfalzheim  | Mehrheimerstr. 369                   | Köln            | 50739      | Germany     |
| 57         | Paris spécialités                    | Marie Bertrand       | 265, boulevard Charonne              | Paris           | 75012      | France      |
| 58         | Pericles Comidas clásicas            | Guillermo Fernández  | Calle Dr. Jorge Cash 321             | México D.F.     | 05033      | Mexico      |
| 59         | Piccolo und mehr                     | Georg Pipps          | Geislweg 14                          | Salzburg        | 5020       | Austria     |
| 60         | Princesa Isabel Vinhoss              | Isabel de Castro     | Estrada da saúde n. 58               | Lisboa          | 1756       | Portugal    |
| 61         | Que Delícia                          | Bernardo Batista     | Rua da Panificadora, 12              | Rio de Janeiro  | 02389-673  | Brazil      |
| 62         | Queen Cozinha                        | Lúcia Carvalho       | Alameda dos Canàrios, 891            | São Paulo       | 05487-020  | Brazil      |
| 63         | QUICK-Stop                           | Horst Kloss          | Taucherstraße 10                     | Cunewalde       | 01307      | Germany     |
| 64         | Rancho grande                        | Sergio Gutiérrez     | Av. del Libertador 900               | Buenos Aires    | 1010       | Argentina   |
| 65         | Rattlesnake Canyon Grocery           | Paula Wilson         | 2817 Milton Dr.                      | Albuquerque     | 87110      | USA         |
| 66         | Reggiani Caseifici                   | Maurizio Moroni      | Strada Provinciale 124               | Reggio Emilia   | 42100      | Italy       |
| 67         | Ricardo Adocicados                   | Janete Limeira       | Av. Copacabana, 267                  | Rio de Janeiro  | 02389-890  | Brazil      |
| 68         | Richter Supermarkt                   | Michael Holz         | Grenzacherweg 237                    | Genève          | 1203       | Switzerland |
| 69         | Romero y tomillo                     | Alejandra Camino     | Gran Vía, 1                          | Madrid          | 28001      | Spain       |
| 70         | Santé Gourmet                        | Jonas Bergulfsen     | Erling Skakkes gate 78               | Stavern         | 4110       | Norway      |
| 71         | Save-a-lot Markets                   | Jose Pavarotti       | 187 Suffolk Ln.                      | Boise           | 83720      | USA         |
| 72         | Seven Seas Imports                   | Hari Kumar           | 90 Wadhurst Rd.                      | London          | OX15 4NB   | UK          |
| 73         | Simons bistro                        | Jytte Petersen       | Vinbæltet 34                         | København       | 1734       | Denmark     |
| 74         | Spécialités du monde                 | Dominique Perrier    | 25, rue Lauriston                    | Paris           | 75016      | France      |
| 75         | Split Rail Beer & Ale                | Art Braunschweiger   | P.O. Box 555                         | Lander          | 82520      | USA         |
| 76         | Suprêmes délices                     | Pascale Cartrain     | Boulevard Tirou, 255                 | Charleroi       | B-6000     | Belgium     |
| 77         | The Big Cheese                       | Liz Nixon            | 89 Jefferson Way Suite 2             | Portland        | 97201      | USA         |
| 78         | The Cracker Box                      | Liu Wong             | 55 Grizzly Peak Rd.                  | Butte           | 59801      | USA         |
| 79         | Toms Spezialitäten                   | Karin Josephs        | Luisenstr. 48                        | Münster         | 44087      | Germany     |
| 80         | Tortuga Restaurante                  | Miguel Angel Paolino | Avda. Azteca 123                     | México D.F.     | 05033      | Mexico      |
| 81         | Tradição Hipermercados               | Anabela Domingues    | Av. Inês de Castro, 414              | São Paulo       | 05634-030  | Brazil      |
| 82         | Trail's Head Gourmet Provisioners    | Helvetius Nagy       | 722 DaVinci Blvd.                    | Kirkland        | 98034      | USA         |
| 83         | Vaffeljernet                         | Palle Ibsen          | Smagsløget 45                        | Århus           | 8200       | Denmark     |
| 84         | Victuailles en stock                 | Mary Saveley         | 2, rue du Commerce                   | Lyon            | 69004      | France      |
| 85         | Vins et alcools Chevalier            | Paul Henriot         | 59 rue de l'Abbaye                   | Reims           | 51100      | France      |
| 86         | Die Wandernde Kuh                    | Rita Müller          | Adenauerallee 900                    | Stuttgart       | 70563      | Germany     |
| 87         | Wartian Herkku                       | Pirkko Koskitalo     | Torikatu 38                          | Oulu            | 90110      | Finland     |
| 88         | Wellington Importadora               | Paula Parente        | Rua do Mercado, 12                   | Resende         | 08737-363  | Brazil      |
| 89         | White Clover Markets                 | Karl Jablonski       | 305 - 14th Ave. S. Suite 3B          | Seattle         | 98128      | USA         |
| 90         | Wilman Kala                          | Matti Karttunen      | Keskuskatu 45                        | Helsinki        | 21240      | Finland     |
| 91         | Wolski                               | Zbyszek              | ul. Filtrowa 68                      | Walla           | 01-012     | Poland      |


### AND Example

The following SQL statement selects all fields from "Customers" where country is "Germany" AND city is "Berlin":

***Example***

```
SELECT * FROM Customers
WHERE Country = 'Germany' AND City = 'Berlin';
```

### OR Example

The following SQL statement selects all fields from "Customers" where city is "Berlin" OR "Stuttgart":

***Example***

```
SELECT * FROM Customers
WHERE City = 'Berlin' OR City = 'Stuttgart';
```

The following SQL statement selects all fields from "Customers" where country is "Germany" OR "Spain":

***Example***

```
SELECT * FROM Customers
WHERE Country = 'Germany' OR Country = 'Spain';
```

### NOT Example

The following SQL statement selects all fields from "Customers" where country is NOT "Germany":

***Example***

```
SELECT * FROM Customers
WHERE NOT Country = 'Germany';
```


### Combining AND, OR and NOT

You can also combine the `AND`, `OR` and `NOT` operators.

The following SQL statement selects all fields from "Customers" where country is "Germany" AND city must be "Berlin" OR "Stuttgart" (use parenthesis to form complex expressions):

***Example***

```
SELECT * FROM Customers
WHERE Country = 'Germany' AND (City = 'Berlin' OR City = 'Stuttgart');
```

The following SQL statement selects all fields from "Customers" where country is NOT "Germany" and NOT "USA":

***Example***

```
SELECT * FROM Customers
WHERE NOT Country = 'Germany' AND NOT Country = 'USA';
```


# The MySQL ORDER BY Keyword

The `ORDER BY` keyword is used to sort the result-set in ascending or descending order.

The `ORDER BY` keyword sorts the records in ascending order by default. To sort the records in descending order, use the `DESC` keyword.

### ORDER BY Syntax

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

### Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                        | ContactName         | Address                              | City           | PostalCode | Country    |
|------------|-------------------------------------|---------------------|--------------------------------------|----------------|------------|------------|
| 1          | Alfreds Futterkiste                 | Maria Anders        | Obere Str. 57                        | Berlin         | 12209      | Germany    |
| 2          | Ana Trujillo Emparedados y helados  | Ana Trujillo        | Avda. de la Constitución 2222        | México D.F.    | 05021      | Mexico     |
| 3          | Antonio Moreno Taquería             | Antonio Moreno      | Mataderos 2312                       | México D.F.    | 05023      | Mexico     |
| 4          | Around the Horn                     | Thomas Hardy        | 120 Hanover Sq.                      | London         | WA1 1DP    | UK         |
| 5          | Berglunds snabbköp                  | Christina Berglund  | Berguvsvägen 8                       | Luleå          | S-958 22   | Sweden     |


### ORDER BY Example

The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" column:

***Example***

```
SELECT * FROM Customers
ORDER BY Country;
```

### ORDER BY DESC Example

The following SQL statement selects all customers from the "Customers" table, sorted DESCENDING by the "Country" column:

***Example***

```
SELECT * FROM Customers
ORDER BY Country DESC;
```

### ORDER BY Several Columns Example

The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" and the "CustomerName" column. This means that it orders by Country, but if some rows have the same Country, it orders them by CustomerName:

***Example***

```
SELECT * FROM Customers
ORDER BY Country, CustomerName;
```

### ORDER BY Several Columns Example 2

The following SQL statement selects all customers from the "Customers" table, sorted ascending by the "Country" and descending by the "CustomerName" column:

***Example***

```
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
```


### The MySQL INSERT INTO Statement

The `INSERT INTO` statement is used to insert new records in a table.

### INSERT INTO Syntax

It is possible to write the `INSERT INTO` statement in two ways:

- Specify both the column names and the values to be inserted:

```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

- If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the `INSERT INTO` syntax would be as follows:

```
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```

### Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                        | ContactName         | Address                              | City           | PostalCode | Country    |
|------------|-------------------------------------|---------------------|--------------------------------------|----------------|------------|------------|
| 89         | White Clover Markets                | Karl Jablonski      | 305 - 14th Ave. S. Suite 3B          | Seattle        | 98128      | USA        |
| 90         | Wilman Kala                         | Matti Karttunen     | Keskuskatu 45                        | Helsinki       | 21240      | Finland    |
| 91         | Wolski                              | Zbyszek             | ul. Filtrowa 68                      | Walla          | 01-012     | Poland     |


### INSERT INTO Example

The following SQL statement inserts a new record in the "Customers" table:

***Example***

```
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
```

The selection from the "Customers" table will now look like this:

| CustomerID | CustomerName         | ContactName     | Address                     | City      | PostalCode | Country |
|------------|----------------------|-----------------|-----------------------------|-----------|------------|---------|
| 89         | White Clover Markets | Karl Jablonski  | 305 - 14th Ave. S. Suite 3B | Seattle   | 98128      | USA     |
| 90         | Wilman Kala          | Matti Karttunen | Keskuskatu 45               | Helsinki  | 21240      | Finland |
| 91         | Wolski               | Zbyszek         | ul. Filtrowa 68             | Walla     | 01-012     | Poland  |
| 92         | Cardinal             | Tom B. Erichsen | Skagen 21                   | Stavanger | 4006       | Norway  |


***Did you notice that we did not insert any number into the CustomerID field?***
The CustomerID column is an auto-increment field and will be generated automatically when a new record is inserted into the table.


### Insert Data Only in Specified Columns

It is also possible to only insert data in specific columns.

The following SQL statement will insert a new record, but only insert data in the "CustomerName", "City", and "Country" columns (CustomerID will be updated automatically):

***Example***

```
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
```

The selection from the "Customers" table will now look like this:

| CustomerID | CustomerName         | ContactName     | Address                     | City      | PostalCode | Country |
|------------|----------------------|-----------------|-----------------------------|-----------|------------|---------|
| 89         | White Clover Markets | Karl Jablonski  | 305 - 14th Ave. S. Suite 3B | Seattle   | 98128      | USA     |
| 90         | Wilman Kala          | Matti Karttunen | Keskuskatu 45               | Helsinki  | 21240      | Finland |
| 91         | Wolski               | Zbyszek         | ul. Filtrowa 68             | Walla     | 01-012     | Poland  |
| 92         | Cardinal             | null            | null                        | Stavanger | null       | Norway  |



# MySQL NULL Values

A field with a NULL value is a field with no value.

If a field in a table is optional, it is possible to insert a new record or update a record without adding a value to this field. Then, the field will be saved with a NULL value.

***Note:*** A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation!

### How to Test for NULL Values?
It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

We will have to use the IS `NULL` and IS `NOT NULL` operators instead.

### IS NULL Syntax

```
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

### IS NOT NULL Syntax

```
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```

### Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                        | ContactName        | Address                       | City         | PostalCode | Country  |
|------------|-------------------------------------|--------------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                 | Maria Anders       | Obere Str. 57                 | Berlin       | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados  | Ana Trujillo       | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería             | Antonio Moreno     | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                     | Thomas Hardy       | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |
| 5          | Berglunds snabbköp                  | Christina Berglund | Berguvsvägen 8                | Luleå        | S-958 22   | Sweden   |



# MySQL UPDATE Statement

The `UPDATE` statement is used to modify the existing records in a table.

### UPDATE Syntax

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

***Note:*** Be careful when updating records in a table! Notice the WHERE clause in the `UPDATE` statement. The `WHERE` clause specifies which record(s) that should be updated. If you omit the `WHERE` clause, all records in the table will be updated!

### Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                       | ContactName    | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|----------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Maria Anders   | Obere Str. 57                 | Berlin       | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy   | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |


### UPDATE Table

The following SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city.

***Example***

```
UPDATE Customers
SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
WHERE CustomerID = 1;
```

The selection from the "Customers" table will now look like this:

| CustomerID | CustomerName                       | ContactName    | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|----------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Alfred Schmidt | Obere Str. 57                 | Frankfurt    | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy   | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |


### UPDATE Multiple Records

It is the `WHERE` clause that determines how many records will be updated.

The following SQL statement will update the PostalCode to 00000 for all records where country is "Mexico":

***Example***

```
UPDATE Customers
SET PostalCode = 00000
WHERE Country = 'Mexico';
```

The selection from the "Customers" table will now look like this:

| CustomerID | CustomerName                       | ContactName    | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|----------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Alfred Schmidt | Obere Str. 57                 | Frankfurt    | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Avda. de la Constitución 2222 | México D.F.  | 00000      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mataderos 2312                | México D.F.  | 00000      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy   | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |


## Update Warning!
Be careful when updating records. If you omit the `WHERE` clause, ALL records will be updated!

***Example***

```
UPDATE Customers
SET PostalCode = 00000;
```

The selection from the "Customers" table will now look like this:

| CustomerID | CustomerName                       | ContactName    | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|----------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Alfred Schmidt | Obere Str. 57                 | Frankfurt    | 00000      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Avda. de la Constitución 2222 | México D.F.  | 00000      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mataderos 2312                | México D.F.  | 00000      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy   | 120 Hanover Sq.               | London       | 00000      | UK       |



# MySQL DELETE Statement
The `DELETE` statement is used to delete existing records in a table.

### DELETE Syntax

`DELETE FROM table_name WHERE condition;`

***Note:*** Be careful when deleting records in a table! Notice the `WHERE` clause in the `DELETE` statement. The `WHERE` clause specifies which record(s) should be deleted. If you omit the `WHERE` clause, all records in the table will be deleted!

### Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName                       | ContactName        | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|--------------------|-------------------------------|--------------|------------|----------|
| 1          | Alfreds Futterkiste                | Maria Anders       | Obere Str. 57                 | Berlin       | 12209      | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo       | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno     | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy       | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |
| 5          | Berglunds snabbköp                 | Christina Berglund | Berguvsvägen 8                | Luleå        | S-958 22   | Sweden   |


### SQL DELETE Example

The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:

***Example***

`DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';`

The "Customers" table will now look like this:

| CustomerID | CustomerName                       | ContactName        | Address                       | City         | PostalCode | Country  |
|------------|------------------------------------|--------------------|-------------------------------|--------------|------------|----------|
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo       | Avda. de la Constitución 2222 | México D.F.  | 05021      | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno     | Mataderos 2312                | México D.F.  | 05023      | Mexico   |
| 4          | Around the Horn                    | Thomas Hardy       | 120 Hanover Sq.               | London       | WA1 1DP    | UK       |
| 5          | Berglunds snabbköp                 | Christina Berglund | Berguvsvägen 8                | Luleå        | S-958 22   | Sweden   |

### Delete All Records

It is possible to delete all rows in a table without deleting the table. This means that the table structure, attributes, and indexes will be intact:

`DELETE FROM table_name;`

The following SQL statement deletes all rows in the "Customers" table, without deleting the table:

***Example***

`DELETE FROM Customers;`


___

## MySQL Joining Tables
A `JOIN` clause is used to combine rows from two or more tables, based on a related column between them.

Let's look at a selection from the "Orders" table:

| OrderID | CustomerID | OrderDate   |
|---------|------------|-------------|
| 10308   | 2          | 1996-09-18  |
| 10309   | 37         | 1996-09-19  |
| 10310   | 77         | 1996-09-20  |

Then, look at a selection from the "Customers" table:

| CustomerID | CustomerName                       | ContactName    | Country  |
|------------|------------------------------------|----------------|----------|
| 1          | Alfreds Futterkiste                | Maria Anders   | Germany  |
| 2          | Ana Trujillo Emparedados y helados | Ana Trujillo   | Mexico   |
| 3          | Antonio Moreno Taquería            | Antonio Moreno | Mexico   |


Notice that the "CustomerID" column in the "Orders" table refers to the "CustomerID" in the "Customers" table. The relationship between the two tables above is the "CustomerID" column.

Then, we can create the following SQL statement (that contains an `INNER JOIN`), that selects records that have matching values in both tables:

***Example***

```
SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
```

and it will produce something like this:

| OrderID | CustomerName                       | OrderDate  |
|---------|------------------------------------|------------|
| 10308   | Ana Trujillo Emparedados y helados | 9/18/1996  |
| 10365   | Antonio Moreno Taquería            | 11/27/1996 |
| 10383   | Around the Horn                    | 12/16/1996 |
| 10355   | Around the Horn                    | 11/15/1996 |
| 10278   | Berglunds snabbköp                 | 8/12/1996  |


# Supported Types of Joins in MySQL
- INNER JOIN: Returns records that have matching values in both tables
- LEFT JOIN: Returns all records from the left table, and the matched records from the right table
- RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
- CROSS JOIN: Returns all records from both tables

Reference: https://www.w3schools.com/mysql/