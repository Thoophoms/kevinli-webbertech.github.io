# Spark Tutorial

## What is Spark

 Text: ChatGPT

## Spark Architecture

1/ Relationship with Haddoop (images)

![maven run]https://kevinli-webbertech.github.io/blog/images/big_data/spark/mvn_run.png)

2/ Comparison with Hadoop, Limitation of Hadoop MapReduce

## Spark Installation

Step 1: go to https://spark.apache.org/downloads.html

Step 2: pip install pyspark

```
Install with 'pip'
$ pip install pyspark
$ pyspark
```

Docker Use without installation
```
$ docker run -it --rm spark:python3 /opt/spark/bin/pyspark
```

## Spark Toolset

From pdf from Dr Dong

### Ref

- https://www.tutorialspoint.com/apache_spark/apache_spark_introduction.htm

- https://www.tutorialspoint.com/apache_spark/apache_spark_rdd.htm

- https://www.tutorialspoint.com/apache_spark/apache_spark_core_programming.htm

- https://www.tutorialspoint.com/apache_spark/apache_spark_deployment.htm (jar file)

- https://www.tutorialspoint.com/apache_spark/advanced_spark_programming.htm


Example of 

1/ CSV

2/ Machine learning

3/ Analytics and Data Science

4/ SQL
$ docker run -it --rm spark /opt/spark/bin/spark-sql
spark-sql>

SELECT
  name.first AS first_name,
  name.last AS last_name,
  age
FROM json.`logs.json`
  WHERE age > 21;

References

Explore this a little bit,

https://spark.apache.org/docs/latest/


Deployment
https://youtu.be/k1LaWFNOa68?si=kBwp4Cc886eiZLdz (Hive)
https://github.com/amplab/spark-ec2
https://spark.apache.org/docs/latest/running-on-kubernetes.html
https://spark.apache.org/docs/latest/running-on-yarn.html
https://spark.apache.org/docs/latest/configuration.html