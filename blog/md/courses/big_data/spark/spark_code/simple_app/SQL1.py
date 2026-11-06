"""SimpleApp.py"""
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()
df = spark.read.json("examples/people.json")
df.show()

# spark, df are from the previous example
# Print the schema in a tree format
df.printSchema()

# Select only the "name" column
df.select("name").show()

# Select everybody, but increment the age by 1
df.select(df['name'], df['age'] + 1).show()

# Select people older than 21
df.filter(df['age'] > 21).show()

# Count people by age
df.groupBy("age").count().show()

spark.stop()


