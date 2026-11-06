# Traditional Installation

1. Download Spark

Visit the Apache Spark downloads page to download Spark.

You can choose pre-packaged versions for popular Hadoop distributions or a Hadoop-free binary, allowing you to use any Hadoop version by modifying Spark’s classpath.

`wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz`

`tar -xvf spark-3.5.1-bin-hadoop3.tgz`

2. System requirements:

Spark runs on both Windows and UNIX-like systems (Linux, Mac OS) and requires a supported Java version (8, 11, or 17). Ensure Java is installed and accessible via PATH or set the JAVA_HOME environment variable to your Java installation.

`java -version`