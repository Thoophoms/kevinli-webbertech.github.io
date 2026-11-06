from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SimpleApp").config("spark.driver.bindAddress", "127.0.0.1").getOrCreate()
df = spark.read.format("image").option("dropInvalid", True).load("data/mllib/images/origin/kittens")
df.select("image.origin", "image.width", "image.height").show(truncate=False)