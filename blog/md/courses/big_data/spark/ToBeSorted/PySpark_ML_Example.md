This example demonstrates the full cycle of building, training, evaluating, deploying, and using a machine learning model in a real-time environment with PySpark.

### Step 1: Setting Up the Environment

#### Initializing Spark
First, you need to set up your Spark environment and create a Spark session.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RealTimeML") \
    .getOrCreate()
```

#### Loading Data
For this example, we'll use a sample CSV dataset. Load the data into a DataFrame.

```python
data = spark.read.csv("path/to/your/dataset.csv", header=True, inferSchema=True)
data.show()
```

### Step 2: Data Preprocessing

#### Cleaning the Data
Handle any missing values or irrelevant columns.

```python
data = data.dropna()
```

#### Feature Engineering
Convert categorical features to numerical ones using `StringIndexer` and assemble features using `VectorAssembler`.

```python
from pyspark.ml.feature import StringIndexer, VectorAssembler

indexer = StringIndexer(inputCol="categorical_column", outputCol="categorical_index")
data = indexer.fit(data).transform(data)

assembler = VectorAssembler(inputCols=["numerical_column1", "numerical_column2", "categorical_index"], outputCol="features")
data = assembler.transform(data)
```

#### Splitting the Data
Split the data into training and test sets.

```python
train_data, test_data = data.randomSplit([0.8, 0.2], seed=1234)
```

### Step 3: Model Training

#### Building a Machine Learning Pipeline
Create a pipeline with the necessary stages including the logistic regression model.

```python
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

lr = LogisticRegression(featuresCol="features", labelCol="label")
pipeline = Pipeline(stages=[indexer, assembler, lr])
```

#### Training the Model
Fit the pipeline to the training data.

```python
model = pipeline.fit(train_data)
```

### Step 4: Model Evaluation

#### Evaluating the Model Performance
Evaluate the model using the test data.

```python
predictions = model.transform(test_data)
predictions.select("label", "prediction").show()

from pyspark.ml.evaluation import BinaryClassificationEvaluator

evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction", labelCol="label")
accuracy = evaluator.evaluate(predictions)
print(f"Test Accuracy: {accuracy}")
```

### Step 5: Model Deployment

#### Saving the Model
Save the trained model for later use.

```python
model.save("path/to/save/model")
```

#### Loading the Model
Load the saved model when needed.

```python
from pyspark.ml.pipeline import PipelineModel

loaded_model = PipelineModel.load("path/to/save/model")
```

### Step 6: Real-Time Predictions

#### Setting Up a Real-Time Data Stream
Assume we're reading real-time data from a Kafka stream.

```python
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

schema = StructType([
    StructField("numerical_column1", DoubleType()),
    StructField("numerical_column2", DoubleType()),
    StructField("categorical_column", StringType())
])

kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "real_time_topic") \
    .load()

value_df = kafka_stream.selectExpr("CAST(value AS STRING)")
json_df = value_df.select(from_json(col("value"), schema).alias("data")).select("data.*")
```

#### Applying the Model to the Data Stream
Apply the loaded model to the incoming data stream.

```python
stream_predictions = loaded_model.transform(json_df)

query = stream_predictions.select("prediction").writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
```

