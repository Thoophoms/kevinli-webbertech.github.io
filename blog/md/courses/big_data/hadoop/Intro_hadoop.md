# Introduction to Hadoop

## Outline

* Part I: What is hadoop?
* Part II: Distributed Computing Background

## Part II Hadoop

Hadoop is an Apache open source framework written in java that allows distributed processing of large datasets across clusters of computers using simple programming models.

* Hadoop is designed to scale up from single server to thousands of machines, each offering local computation and storage.

* The Hadoop framework application works in an environment that provides distributed storage and computation across clusters of computers.

### Hadoop Architecture

* Processing/Computation layer (MapReduce), and
* Storage layer (Hadoop Distributed File System).
* Hadoop Common − These are Java libraries and utilities required by other Hadoop modules.
* Hadoop YARN − This is a framework for job scheduling and cluster resource management.

![architecture](https://kevinli-webbertech.github.io/blog/images/big_data/hadoop/architecture.png)

### MapReduce

MapReduce is a parallel programming model for writing distributed applications devised at Google for efficient processing of large amounts of data (multi-terabyte data-sets), on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner. The MapReduce program runs on Hadoop which is an Apache open-source framework.

### Hadoop Distributed File System (DFS)

The Hadoop Distributed File System (HDFS) is based on the Google File System (GFS) and provides a distributed file system that is designed to run on commodity hardware.

It is highly fault-tolerant and is designed to be deployed on low-cost hardware.

## Distributed computing History and Backgound

### A distributed computing metaphor and framework- MPI

MPI (message passing interface), a famous distributed computing technology and libaries in early days and still being used in high performance computer or distributed computer clusters. It is implemented in C programming language.

### Distributed Math computing framework

* Lapack (Linear Algegra package), written in C and fortran programming languages. This is a non-distributed version.

* Scalapack (Scalable Lapack), written in C language, Intel Numerical Library for parallelism.

### Takeaway

***How does Hadoop work?***

* Written in Java.
* Master/Slaves, one master, rest of slaves.
* HDFS, being on top of the local file system, supervises the processing.
* Data is initially divided into directories and files.
  Files are divided into uniform sized blocks of 128M and 64M (preferably 128M). These files are then distributed across various cluster nodes for further processing.
* Blocks are replicated for handling hardware failure.
* Checking that the code was executed successfully.
* Performing the sort that takes place between the map and reduce stages.
* Sending the sorted data to a certain computer.
* Writing the debugging logs for each job.