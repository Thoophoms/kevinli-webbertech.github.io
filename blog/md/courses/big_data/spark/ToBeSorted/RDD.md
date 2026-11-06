# Introduction to RDDs

## Why RDDs Were Introduced:

**Limitations of Hadoop MapReduce**: Before Spark, Hadoop MapReduce was the dominant framework for big data processing. However, MapReduce has several limitations:

* **Performance:** MapReduce writes intermediate data to disk, leading to high I/O overhead.  
* **Complexity:** Writing complex data pipelines required chaining multiple MapReduce jobs, which was cumbersome and error-prone.  
* **Lack of Interactivity**: MapReduce jobs are batch-oriented and not suitable for interactive data exploration.  
* **Limited Fault Tolerance:** MapReduce required explicit handling of fault tolerance, making the code more complex.  

## Solution with RDDs:

RDDs were introduced in Apache Spark to address these limitations by providing:

* **In-Memory Computation:** Significantly faster than disk-based systems like Hadoop MapReduce.  
* **Ease of Use:** Simplifies the programming model with high-level APIs.  
* **Fault Tolerance:** Automatically recovers lost data due to node failures.  
* **Lazy Evaluation:** Delays computation until an action is triggered, optimizing the execution plan.
* **Rich API:** Supports a wide range of transformations and actions for complex data processing.

## What is an RDD:

* **Immutable:** Once created, the data in an RDD cannot be changed. This immutability helps with fault tolerance as the lineage(history) of transformations can be used to recompute lost data.  
* **Distributed:** RDDs are distributed across multiple nodes in a cluster, enabling parallel processing.  
* **Fault-Tolerant:** RDDs can automatically recoever from node failures by recomputing lost paritions using lineage information.  
* **Lazy Evaluation:** Transformations on RDDs are not executed immediately. Instead, Spark builds an execution plan which is triggered when an action is called.  

## Creating RDDS

**From Existing Data:**

Parallelizing a collection in the driver program:

>rdd = sc.parallelize([1,2,3,4,5])

Reading from an external storage system like HDFS, S3, or local file system:

>rdd = sc.textfile("hdfs://path/to/file.txt")

**From Other RDDs:**

Transformations on existing RDDs create new RDDs:

>rdd2 = rdd1.map(lambda x:x*2)

## Transformations and Actions  

* **Transformations:** Operations that create a new RDD from an existing one. Examples include 'map()','filter()','flatMap()', and 'reduceByKey()'.   

  * **Lazy Evaluation:** Transformations are recorded in the form of a lineage graph but are not executed until an action is called.

* **Actions:** Operations that trigger the execution of transformations to return a result to the driver or write data to storage. Examples include 'collect()','count()','first()','take()',and 'saveAsTextFile()'.

## Key Transformations

* **map():** Applies a function to each element of the RDD and returns a new RDD.
>rdd2=rdd1.map(lambda x:x*2)

* **filter():** Returns a new RDD containing only elements that satisfy a predicate.
>rdd2=rdd1.filter(lambda x:X>10)

* **flatMap():** Similar to 'map()', but each input element can be mapped to 0 or more output elements.
>rdd2 = rdd1.flatMap(lambda x:x.split(" "))

* **reduceByKey():** Aggregates values of each key using a reduce function.
>rdd2 = rdd1.reduceByKey(lambda x, y: x+y)

## Key Actions

* **collect():** Returns all elements of the RDD to the driver.
>result = rdd.collect()

* **count():** Returns the number of elements in the RDD.
>num=rdd.count()

* **first():** Returns the first element of the RDD.
>first_element=rdd.first()

* **take():** Returns the first 'n' elements of the RDD.
>some_elements = rdd.take(5)

* **saveAsTextFile():** Saves the RDD to a text file in the specified directory.
>rdd.saveASTextFile("hdfs://path/to/output")

## Caching and Persistence

* **cache():** Caches the RDD in memory. It is a shortcut for **'persist(StorageLevel.MEMORY_ONLY)'**.
>rdd.cache()

* **persist():** Persists the RDD with a specified storage level (e.g., memory, disk).
>rdd.persist(StorageLevel.MEMORY_AND_DISK)

## Partitioning

* **Default Partitioning:** When creating an RDD, Spark automatically partitions the data.
* **Custom Partitioning:** You can specify the number of partitions or provide a custom partitioner.
>rdd = rdd.repartition(10)#increase partitions
>rdd = rdd.coalesce(2)#decrease partitions

## Fault Tolerance and Lineage

* **Lineage Graph:** Spark maintains a lineage graph to record the set of transformations used to build an RDD. This graph is used to recomupte lost data in case of failures.
* **Automatic Recovery:** Spark can recompute the paritions of RDDs using the lineage information to recover from faults.