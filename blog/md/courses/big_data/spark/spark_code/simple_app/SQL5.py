from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.functions import count
from pyspark.sql.functions import avg
from pyspark.sql.functions import max
from pyspark.sql.functions import min
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("SQLExample")
                    .config("spark.driver.bindAddress", "127.0.0.1")
                    .getOrCreate()
data = [("John", "Hardware", 1000),
("Sara", "Software", 2000),
("Mike", "Hardware", 3000),
("Lisa", "Hardware", 4000),
("David", "Software", 5000)]

df = spark.createDataFrame(data, ["name", "category", "sales"])
df.select(sum("sales")).show()
df.select(count("sales")).show()
df.select(avg("sales")).show()
df.select(max("sales")).show()
df.select(min("sales")).show()
df.groupBy("category").agg(avg("sales")).show()