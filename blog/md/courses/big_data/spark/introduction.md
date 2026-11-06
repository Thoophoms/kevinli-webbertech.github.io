# Spark Architecture

## Overview

Apache Spark is an open-source, distributed computing system designed for fast computation. It provides an interface for programming entire clusters with implicit data parallelism and fault tolerance. 

## What are the similarities between Hadoop and Spark?

Both Hadoop and Spark are distributed systems that let you process data at scale. They can recover from failure if data processing is interrupted for any reason.

**Distributed big data processing**

Big data is collected frequently, continuously, and at scale in various formats.

To store, manage, and process big data, Apache Hadoop separates datasets into smaller subsets or partitions. It then stores the partitions over a distributed network of servers. Likewise, Apache Spark processes and analyzes big data over distributed nodes to provide business insights.

Depending on the use cases, you might need to integrate both Hadoop and Spark with different software for optimum functionality.

**Fault tolerance**

Apache Hadoop continues to run even if one or several data processing nodes fail. It makes multiple copies of the same data block and stores them across several nodes. When a node fails, Hadoop retrieves the information from another node and prepares it for data processing.

Meanwhile, Apache Spark relies on a special data processing technology called Resilient Distributed Dataset (RDD). With RDD, Apache Spark remembers how it retrieves specific information from storage and can reconstruct the data if the underlying storage fails.

## Key components: Hadoop vs. Spark frameworks

Both Hadoop and Spark are made of several software modules that interact and collaborate to make the system work.

**Hadoop components**

Apache Hadoop has four main components:

Hadoop Distributed File System (HDFS) is a special file system that stores large datasets across multiple computers. These computers are called Hadoop clusters. 
Yet Another Resource Negotiator (YARN) schedules tasks and allocates resources to applications running on Hadoop.

Hadoop MapReduce allows programs to break large data processing tasks into smaller ones and runs them in parallel on multiple servers.

Hadoop Common, or Hadoop Core, provides the necessary software libraries for other Hadoop components.

**Spark components**

Apache Spark runs with the following components:

* Spark Core coordinates the basic functions of Apache Spark. These functions include memory management, data storage, task scheduling, and data processing.

* Spark SQL allows you to process data in Spark's distributed storage.

* Spark Streaming and Structured Streaming allow Spark to stream data efficiently in real time by separating data into tiny continuous blocks.

* Machine Learning Library (MLlib) provides several machine learning algorithms that you can apply to big data.

* GraphX allows you to visualize and analyze data with graphs.

![hadoop_vs_spark](../../../../images/big_data/spark/hadoop_vs_spark.png)

## Misconceptions about Hadoop and Spark

### Common misconceptions about Hadoop

**Hadoop is cheap:** Though it’s open source and easy to set up, keeping the server running can be costly. When using features like in-memory computing and network storage, big data management can cost up to USD 5,000.

**Hadoop is a database:** Though Hadoop is used to store, manage and analyze distributed data, there are no queries involved when pulling data. This makes Hadoop a data warehouse rather than a database.

**Hadoop does not help SMBs:** “Big data” is not exclusive to “big companies”. Hadoop has simple features like Excel reporting that enable smaller companies to harness its power. Having one or two Hadoop clusters can greatly enhance a small company’s performance.

**Hadoop is hard to set up:** Though Hadoop management is difficult at the higher levels, there are many graphical user interfaces (GUIs) that simplify programming for MapReduce.

### Common misconceptions about Spark

Spark is an in-memory technology: Though Spark effectively utilizes the least recently used (LRU) algorithm, it is not, itself, a memory-based technology.
Spark always performs 100x faster than Hadoop: Though Spark can perform up to 100x faster than Hadoop for small workloads, according to Apache, it typically only performs up to 3x faster for large ones (link resides outside ibm.com).
Spark introduces new technologies in data processing: Though Spark effectively utilizes the LRU algorithm and pipelines data processing, these capabilities previously existed in massively parallel processing (MPP) databases. However, what sets Spark apart from MPP is its open-source orientation.

### Ref

- https://aws.amazon.com/compare/the-difference-between-hadoop-vs-spark/
- https://www.ibm.com/think/insights/hadoop-vs-spark

## Hadoop and Spark use cases

Based on the comparative analyses and factual information provided above, the following cases best illustrate the overall usability of Hadoop versus Spark.

### Hadoop use cases

Hadoop is most effective for scenarios that involve the following:

- Processing big data sets in environments where data size exceeds available memory
- Batch processing with tasks that exploit disk read and write operations
- Building data analysis infrastructure with a limited budget
- Completing jobs that are not time-sensitive
- Historical and archive data analysis

### Spark use cases

Spark is most effective for scenarios that involve the following:

- Dealing with chains of parallel operations by using iterative algorithms
- Achieving quick results with in-memory computations
- Analyzing stream data analysis in real time
- Graph-parallel processing to model data
- All ML applications

Ref:

- https://www.ibm.com/think/insights/hadoop-vs-spark

## Advantages of Apache Spark

Spark speeds development and operations in a variety of ways. Spark will help teams:

**Accelerate app development:** Apache Spark's Streaming and SQL programming models backed by MLlib and GraphX make it easier to build apps that exploit machine learning and graph analytics.

**Innovate faster:**  APIs provide ease of use when manipulating semi-structured data and transforming data.

**Manage with ease:** A unified engine supports SQL queries, streaming data, machine learning (ML) and graph processing.

**Optimize with open technologies:** The OpenPOWER Foundation enables GPU, CAPI Flash, RDMA, FPGA acceleration and machine learning innovation to optimize performance for Apache Spark workloads.

**Process faster:** Spark can be 100x faster than Hadoop (link resides outside ibm.com) for smaller workloads because of its advanced in-memory computing engine and disk data storage.

**Speed memory access:** Spark can be used to create one large memory space for data processing, enabling more advanced users to access data via interfaces using Python, R, and Spark SQL.

Ref:

https://www.ibm.com/topics/apache-spark

## Why choose Spark over a SQL-only engine?

Apache Spark is a fast general-purpose cluster computation engine that can be deployed in a Hadoop cluster or stand-alone mode. With Spark, programmers can write applications quickly in Java, Scala, Python, R, and SQL which makes it accessible to developers, data scientists, and advanced business people with statistics experience. Using Spark SQL, users can connect to any data source and present it as tables to be consumed by SQL clients. In addition, interactive machine learning algorithms are easily implemented in Spark.

With a SQL-only engine like `Apache Impala`, `Apache Hive`, or `Apache Drill`, users can only use SQL or SQL-like languages to query data stored across multiple databases. That means that the frameworks are smaller compared to Spark.

## How are companies using Spark?

Many companies are using Spark to help simplify the challenging and computationally intensive task of processing and analyzing high volumes of real-time or archived data, both structured and unstructured. Spark also enables users to seamlessly integrate relevant complex capabilities like machine learning and graph algorithms.

### Data engineers

Data engineers use Spark for coding and building data processing jobs—with the option to program in an expanded language set.

### Data scientists

Data scientists can have a richer experience with analytics and ML using Spark with GPUs. 
The ability to process larger volumes of data faster with a familiar language can help accelerate innovation.

## Spark Key Components

### 1. **Driver Program**

- **Definition**: The main application code that drives the Spark application.
- **Responsibilities**:
  - Defines the main function, creates the SparkContext, and runs the main algorithm.
  - Converts user-written code into tasks for the executors.
  - Maintains the Spark session and context, manages transformations and actions on RDDs, and interacts with the cluster manager.

### 2. **Cluster Manager**

- **Types**:
  - **Standalone Cluster Manager**: Spark's own built-in cluster manager.
  - **Apache Mesos**: A general cluster manager that can also run Hadoop MapReduce and service applications.
  - **Hadoop YARN**: The resource manager in Hadoop 2.
  - **Kubernetes**: An open-source system for automating deployment, scaling, and management of containerized applications.
- **Responsibilities**:
  - Allocates resources across the cluster.
  - Schedules tasks on the cluster nodes.

### 3. **Executors**

- **Definition**: Distributed agents responsible for executing tasks.
- **Responsibilities**:
  - Execute code assigned to them by the driver.
  - Store data in-memory for fast data retrieval (RDD caching).
  - Report the status of the computation and storage to the driver node.

## Key Concepts

### 1. **RDD (Resilient Distributed Dataset)**

- **Definition**: An immutable, distributed collection of objects that can be processed in parallel.
- **Features**:
  - **Immutable**: Once created, RDDs cannot be changed.
  - **Distributed**: RDDs are distributed across multiple nodes in the cluster.
  - **Fault-Tolerant**: Automatically rebuilds lost data from lineage information.

### 2. **Transformations and Actions**

- **Transformations**: Operations on RDDs that return a new RDD (e.g., `map()`, `filter()`, `flatMap()`). They are lazy and executed only when an action is called.
- **Actions**: Operations that trigger the execution of transformations and return a result (e.g., `collect()`, `count()`, `first()`, `saveAsTextFile()`).

### 3. **Directed Acyclic Graph (DAG)**

- **Definition**: A graph structure that represents the sequence of computations performed on the data.
- **Purpose**: Used by Spark to optimize the execution plan and reduce the amount of shuffling and recomputation.

### 4. **Stages and Tasks**

- **Stages**: Subdivision of the DAG into smaller sets of parallelizable tasks.
- **Tasks**: Individual units of work sent to one executor.

## Detailed Workflow

1. **Driver Program Initialization**
   - The driver program starts and initializes a SparkSession or SparkContext.
   - The user program defines transformations and actions on RDDs.

2. **Job Submission**
   - When an action is called, the driver program constructs a DAG of stages and tasks based on the transformations.
   - The DAG scheduler divides the operators into stages of tasks. A stage contains tasks based on partitions of the input data.

3. **Task Scheduling**
   - The driver program sends tasks to the cluster manager.
   - The cluster manager allocates resources and schedules the tasks to run on different executors.

4. **Task Execution**
   - Executors execute the tasks on the partitions of the data.
   - Intermediate results can be cached or stored on disk as specified by the user.

5. **Result Collection**
   - The results of the tasks are collected and sent back to the driver program.
   - The driver program can perform further computations or output the final result.

## Spark Execution Modes

### 1. **Local Mode**

- **Definition**: Runs Spark on a single machine.
- **Use Case**: Development, testing, and debugging.

### 2. **Cluster Mode**

- **Definition**: Runs Spark on a cluster of machines.
- **Types**:
  - **Client Mode**: The driver runs on the client machine.
  - **Cluster Mode**: The driver runs inside the cluster.

### 3. **YARN and Mesos Modes**

- **YARN**: Runs Spark on Hadoop YARN.
- **Mesos**: Runs Spark on Mesos, sharing resources with other applications.

### 4. **Kubernetes Mode**

- **Definition**: Runs Spark on Kubernetes, an orchestration system for automating application deployment.

## Optimizations

### 1. **Caching and Persistence**

- **Definition**: Storing RDDs in memory for faster access.
- **Methods**: `cache()`, `persist()`.
- **Benefits**: Reduces computation time for iterative algorithms.

### 2. **Broadcast Variables**

- **Definition**: Read-only variables that are cached on each machine.
- **Use Case**: Sharing large read-only data efficiently across tasks.

### 3. **Accumulators**

- **Definition**: Variables that are only added to through an associative and commutative operation.
- **Use Case**: Aggregating information from workers.

### 4. **Shuffling and Partitioning**

- **Definition**: Data is redistributed across the cluster to balance the load.
- **Optimizations**: Reducing shuffles by using narrow transformations, optimizing partition sizes.

### 5. **Speculative Execution**

- **Definition**: Running duplicate copies of slow tasks.
- **Purpose**: To handle stragglers and improve the completion time of jobs.

## Spark SQL and DataFrames

### 1. **Spark SQL**

- **Definition**: Module for working with structured data.
- **Components**:
  - **SQL Context**: Allows running SQL queries programmatically.
  - **HiveContext**: Extends SQLContext with Hive support.

### 2. **DataFrames**

- **Definition**: Distributed collections of data organized into named columns.
- **Features**:
  - Optimized execution plans.
  - Integration with Spark SQL.


## Spark Clusters

For commercial platform, you develop your code and submit the job to clusters to execute.

Good platforms are:

* Databrick

- https://www.databricks.com/resources/ebook/big-book-of-machine-learning-use-cases?scid=7018Y000001Fi0MQAS&utm_medium=paid+search&utm_source=google&utm_campaign=17114500970&utm_adgroup=147740743372&utm_content=ebook&utm_offer=big-book-of-machine-learning-use-cases&utm_ad=665885917674&utm_term=databricks%20use&gad_source=1&gclid=EAIaIQobChMIioassd-YiQMVckT_AR0ZCSrhEAAYASAAEgJx4fD_BwE
- https://www.databricks.com/spark/getting-started-with-apache-spark

![databrick1.png](../../../../images/big_data/spark/databrick1.png)

![databrick2.png](../../../../images/big_data/spark/databrick2.png)

* Cloudera

- https://www.cloudera.com/open-source.html

* Azure HDInsight

- https://learn.microsoft.com/en-us/azure/hdinsight/spark/apache-spark-overview

* AWS EMR

- https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-launch.html

* Google Dataproc

- https://cloud.google.com/dataproc

* IBM Analytics Engine

- https://www.ibm.com/topics/apache-spark