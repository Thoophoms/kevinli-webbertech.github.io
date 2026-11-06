# APACHE SPARK INSTALLATION

Spark is Hadoop's sub-project. Therefore, it is better to install Spark into a Linux based system. The following steps show how to install Apache Spark.

## Step 1

Java installation is one of the mandatory things in installing Spark. Try the following command to verify the JAVA version.

> $java -version

If Java is already, installed on your system, you get to see the following response −

>java version "1.7.0_71"   
Java(TM) SE Runtime Environment (build 1.7.0_71-b13)
Java HotSpot(TM) Client VM (build 25.0-b02, mixed mode)  

In case you do not have Java installed on your system, then Install Java before proceeding to next step.

## Step 2

As we're not using Scala, we will directly proceed to Spark Installation

Download the latest version of Spark by visiting the following link [Download Spark](https://spark.apache.org/downloads.html) For this tutorial, we are using spark-3.5.1-bin-hadoop3 version. After downloading it, you will find the Spark tar file in the download folder.

## Step 4: Define Spark Home

1. Make sure Java is installed
2. Go to your bash profile for editing

>nano ~/.bashrc

3. Check the 'export' commands

Ensure that the 'export' commands for **'SPARK_HOME'** and **'PATH'** are correctly formatted. They should look something like this:

>export SPARK_HOME=/Path-to-the-spark-3.5.1-bin-hadoop3  
export PATH=$SPARK_HOME/bin:$PATH

Tip: If it's not reading the path, add double quotes around the path to handle spaced properly

>export SPARK_HOME="/Path-to-the-spark-3.5.1-bin-hadoop3"  
export PATH="$SPARK_HOME/bin:$PATH"

save the ~/.bashrc file and source it again.

> source ~/.bashrc

Tip: Commands

'ctrl+o' to save the file, then 'Enter'.  
Press 'ctrl + x' to exit 'nano'

Now, try running 'spark-shell' again (to check did we downloaded it correctly or not)

> spark-shell