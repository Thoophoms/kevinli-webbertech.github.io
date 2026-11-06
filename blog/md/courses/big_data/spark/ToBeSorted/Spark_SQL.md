# Introduction to Spark SQL

## Overview:

* Spark SQL is a spark module for structured data processing.
* It provides a programming abstraction called DataFrame and can also act as a distributed SQL query engine.
* Spark SQL integrates relational processing with Spark's functional programming API.

## Key Features:

* Allows execution of SQL queries with Spark Programs.
* Provides a unified interface for processing structured data.
* Can read data from various data sources such as JSON, Parquet, Avro, ORC, Hive tables, and more.

## Working with DataFrames

* **Creation of Data Frames:** 
   * From JSON:
     ```python
     df = spark.read.json("path/to/json/file")
     ```
   * From CSV:
     ```python
     df = spark.read.csv("path/to/csv/file",header=True, inferSchema=True)
     ```
   * From Parquet:
     ```python
     df = spark.read.parquet("path/to/parquet/file")
     ```
* **Basic Operations:**
   * **select():** Selects a subset of columns:
     ```python
     df.select("column_name").show()
     ```
   * **filter():** Filters rows based on a condition.
     ```python
     df.filter(df["column_name"]>100.show()
     ```
   * **groupBy() and agg():** Groups the data by a column and performs aggregate operations.
     ```python
     df.groupBy("column_name").agg({"another_column":"sum"}).show()
     ```
   * **withColumn():** Adds a new column or replaces an existing column.
     ```python
     df.withColumn("new_column",df["existing_column"]+1).show()
     ```
   * **drop():** Drops a column from the DataFrame.
     ```python
     df.drop("column_name").show()
     ```
* **DataFrame Methods:**
   * **show():** Displays the content of the DataFrame.
     ```python
     df.show()
     ```
   * **printSchema():** Prints the schema of the DataFrame.
     ```python
     df.printSchema()
     ```
   * **describe():** Computes basic statistics for numeric columns.
     ```python
     df.describe().show()
     ```

## Using Datasets

* **Datasets:**

  * A dataset is a distributed collection of data.
  * Datasets are strongly-typed and provide the benefits of RDDs with the optimatizations of DataFrames.
  * In Python, DataFrames are considered as a type of Dataset with Row objects.

## Running SQL Queries

* **SQL Queries in Spark:**

  * You can run SQL queries directly against DataFrames or create temporary views to use SQL queries.
  * **spark.sql():** Executes SQL query.
    ```python
    df.createOrReplaceTempView("table_name")  
    result=spark.sql("SELECT * FROM table_name")  
    result.show()  
    ```
  
## Advanced Sprak SQL Operations

* **Joins:**

  * Different types of joins: inner, outer, left, right, and cross joins.
  * **join():** Performs joins on DataFrames.
    ```python
    df1.join(df2, df1["id"]==df2["id"], "inner").show()
    ```
  
* **Window Functions:**

  * Used for operations like ranking, cumulative sum, moving averages, etc.
  * **window():** Defines a window specification.
    ```python
    from pyspark.sql.window import Window  
    from pyspark.sql.functions import row_number  
    windowSpec = Window.partitionBy("column").orderBy("column")
    df.withColumn("row_number",row_number().over(windowSpec)).show()
    ```
  
* **UDFs(User-Defined Functions):
  * Allows you to define custom functions to use in SQL queries or DataFrame operations.
  * **udf():** Registers a Python function as a UDF.
     ```python
    from pyspark.sql.functions import udf  
    from pyspark.sql.types import StringType  
    def upper_case(name):  
         return name.upper() 
    my_udf = udf(my_function, StringType())  
    df.withColumn("new_column", my_udf(df["existing_column"])).show()
     ```
## Optimizations and Performance Tuning

* **Catalyst Optimizer:**

  * Spark SQL uses the Catalyst optimizer for query optimization, which applied rules to improve the execution plan.

* **Tungsten Execution Engine:**

  * Improves the efficiency of memory and CPU utilization.

* **Persisting DataFrame:**

  * Use **'cache()'** or **'persist()'** to store DataFrames in memory, which is beneficial for iterative algorithms.
   ```python
   df.cache()  
   df.persist()
  ```
  
* **Broadcast Joins:**

  * Efficient for joining a large DataFrame with a small DataFrame.
  * **broadcast():** Marks a DataFrame as broadcastable.
    ```python
    from pyspark.sql.functions import broadcast  
    df1.join(broadcast(df2), df1["id"]==df2["id]).show() 
    ```
    
# Handling Data Soruces

* **Reading from Databases:**

  * You can read data from various databases using JDBC.
    ```python
    jdbcDF=spark.read.format("jdbc").option("url","jdbc:postgresql://host:port/database").option("dbtable","table_name").option("user","username").option("password","password").load()  
    ```

* **Writing DataFrames:**

  * **write():** Saves the DataFrame to a specified format.
    ```python
    df.write.csv("path/to/output.csv")  
    df.write.parquet("path/to/output.parquet")  
    df.write.json("path/to/output.json")  
    ```

## Example Code

Here is a comprehensive example demonstarting the usage of Spark SQL in Python:
```python
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SparkSQLExample").getOrCreate()

# Read data into DataFrame
df = spark.read.json("path/to/json/file")

# Perform basic operations
df.select("name", "age").show()  
df.filter(df["age"] > 21).show()  
df.groupBy("age").agg({"salary": "avg"}).show()  

# Register DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")

# Run SQL query
result = spark.sql("SELECT * FROM people WHERE age > 21")  
result.show()

# Use window functions
from pyspark.sql.window import Window  
from pyspark.sql.functions import rank  

windowSpec = Window.partitionBy("department").orderBy("salary")  
df.withColumn("rank", rank().over(windowSpec)).show()  

# Define and use a UDF
from pyspark.sql.functions import udf  
from pyspark.sql.types import StringType  

def upper_case(name):  
    return name.upper()  

upper_case_udf = udf(upper_case, StringType())  
df.withColumn("upper_name", upper_case_udf(df["name"])).show()  

# Save DataFrame to Parquet
df.write.parquet("path/to/output.parquet")  

# Stop Spark session
spark.stop()  
```