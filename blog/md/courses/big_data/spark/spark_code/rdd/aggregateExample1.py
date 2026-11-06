import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkBySession').config("spark.driver.bindAddress", "127.0.0.1").getOrCreate()
listRdd = spark.sparkContext.parallelize(range(1000))
#aggregate
seqOp = (lambda x, y: x**2 + y**2)
combOp = (lambda x, y: x + y)
agg=listRdd.aggregate(0, seqOp, combOp)
print(agg/1000000) # output 20

