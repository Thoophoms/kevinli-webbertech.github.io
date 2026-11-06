from pyspark import SparkContext, SparkConf
import numpy as np

conf = SparkConf().setAppName("appName").set("spark.driver.bindAddress", "127.0.0.1")
#.setMaster(master)
sc = SparkContext(conf=conf)
data = np.arange(100)
rdd = sc.parallelize(data)

rdd.reduce(lambda a, b: a + b)
dataCollect = rdd.collect()

print("Number of Partitions: "+str(rdd.getNumPartitions()))
print("Action: First element: "+str(rdd.first()))
print(dataCollect)
