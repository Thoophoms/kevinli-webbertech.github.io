import pyspark
from pyspark.sql import SparkSession
import numpy as np

spark = SparkSession.builder.appName('SparkBySession').config("spark.driver.bindAddress", "127.0.0.1").getOrCreate()
sc=spark.sparkContext
data = np.arange(100)
rdd = sc.parallelize(data)
rdd.reduce(lambda a, b: a + b)
dataCollect = rdd.collect()

print("Number of Partitions: "+str(rdd.getNumPartitions()))
print("Action: First element: "+str(rdd.first()))
print(dataCollect)
