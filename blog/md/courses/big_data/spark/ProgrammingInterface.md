# Programming Interface

## Spark interfaces

There are three key Spark interfaces that you should know about.

### Resilient Distributed Dataset (RDD)
Apache Spark’s first abstraction was the RDD. It is an interface to a sequence of data objects that consist of one or more
types that are located across a collection of machines (a cluster). RDDs can be created in a variety of ways and are the “lowest level” 
API available. While this is the original data structure for Apache Spark, you should focus on the DataFrame API, which is a superset of 
the RDD functionality. The RDD API is available in the Java, Python, and Scala languages.

### DataFrame
These are similar in concept to the DataFrame you may be familiar with in the pandas Python library and the R language. 
The DataFrame API is available in the Java, Python, R, and Scala languages.

### Dataset
A combination of DataFrame and RDD. It provides the typed interface that is available in RDDs while providing the convenience of the DataFrame. 
The Dataset API is available in the Java and Scala languages.

In many scenarios, especially with the performance optimizations embedded in DataFrames and Datasets, it will not be necessary to work with RDDs. 

But it is important to understand the RDD abstraction because:

The RDD is the underlying infrastructure that allows Spark to run so fast and provide data lineage. If you are diving into more advanced components of Spark, it may be necessary to use RDDs.
The visualizations within the Spark UI reference RDDs. When you develop Spark applications, you typically use DataFrames and Datasets.

## History

This tutorial provides a quick introduction to using Spark. We will first introduce the API through Spark’s interactive shell (in Python or Scala), then show how to write applications in Java, Scala, and Python.
To follow along with this guide, first, download a packaged release of Spark from the Spark website. Since we won’t be using HDFS, you can download a package for any version of Hadoop.

* Note that, before Spark 2.0, the main programming interface of Spark was the Resilient Distributed Dataset (RDD).
* After Spark 2.0, RDDs are replaced by Dataset, which is strongly-typed like an RDD, but with richer optimizations under the hood. 
* The RDD interface is still supported, and you can get a more detailed reference at the RDD programming guide. 
* However, we highly recommend you to switch to use Dataset, which has better performance than RDD. 
* See the SQL programming guide to get more information about Dataset.

## Programming support

![spark_languages.png](../../../../images/big_data/spark/spark_languages.png)


## Ref

- https://spark.apache.org/docs/latest/quick-start.html#self-contained-applications

