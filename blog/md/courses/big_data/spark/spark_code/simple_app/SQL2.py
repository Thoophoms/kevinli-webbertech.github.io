"""SimpleApp.py"""
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()
df = spark.read.json("examples/people.json")

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()


spark.stop()


