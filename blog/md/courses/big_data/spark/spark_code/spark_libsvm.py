from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SimpleApp").config("spark.driver.bindAddress", "127.0.0.1").getOrCreate()

df = spark.read.format("libsvm").option("numFeatures", "780").load("data/mllib/sample_libsvm_data.txt")
df.show(10)