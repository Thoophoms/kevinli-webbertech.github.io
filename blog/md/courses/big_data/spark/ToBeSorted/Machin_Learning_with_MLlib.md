### Machine Learning with MLlib

#### Overview of MLlib
- **What is MLlib?**:
  - MLlib is Spark’s scalable machine learning library.
  - It provides various tools and utilities for machine learning, including algorithms for classification, regression, clustering, and collaborative filtering.
  - MLlib also offers feature extraction and transformation tools, as well as utilities for creating machine learning pipelines.

- **Advantages**:
  - Built for scalability and speed.
  - Seamlessly integrates with other Spark components.
  - Provides a simple API for a wide range of machine learning tasks.

#### Supported Algorithms

##### Classification
- **Logistic Regression**:
  - Used for binary classification problems.
  - Estimates the probability that a given input point belongs to a certain class.
  ```python
  from pyspark.ml.classification import LogisticRegression

  lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
  model = lr.fit(trainingData)
  ```

- **Decision Tree**:
  - A non-parametric supervised learning method used for classification and regression.
  - Splits the data into subsets based on the value of input features.
  ```python
  from pyspark.ml.classification import DecisionTreeClassifier

  dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
  model = dt.fit(trainingData)
  ```

##### Regression
- **Linear Regression**:
  - Models the relationship between a scalar response and one or more explanatory variables.
  ```python
  from pyspark.ml.regression import LinearRegression

  lr = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
  model = lr.fit(trainingData)
  ```

- **Generalized Linear Regression**:
  - Extends linear regression to models with a non-normal distribution.
  ```python
  from pyspark.ml.regression import GeneralizedLinearRegression

  glr = GeneralizedLinearRegression(family="gaussian", link="identity", maxIter=10, regParam=0.3)
  model = glr.fit(trainingData)
  ```

##### Clustering
- **KMeans**:
  - A clustering algorithm that partitions the data into K distinct clusters based on their features.
  ```python
  from pyspark.ml.clustering import KMeans

  kmeans = KMeans().setK(2).setSeed(1)
  model = kmeans.fit(dataset)
  ```

- **Gaussian Mixture**:
  - A probabilistic model for representing normally distributed subpopulations within an overall population.
  ```python
  from pyspark.ml.clustering import GaussianMixture

  gmm = GaussianMixture().setK(2).setSeed(1)
  model = gmm.fit(dataset)
  ```

##### Collaborative Filtering
- **Alternating Least Squares (ALS)**:
  - Used for recommendation systems.
  - Factorizes the user-item interaction matrix.
  ```python
  from pyspark.ml.recommendation import ALS

  als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating")
  model = als.fit(trainingData)
  ```

#### Creating Pipelines
- **What are Pipelines?**:
  - Pipelines in MLlib provide a way to combine multiple processing stages into a single workflow.
  - Simplifies machine learning workflows by chaining together transformers and estimators.

- **Components**:
  - **Transformers**:
    - Transform the input data into another form.
    - Example: `Tokenizer`, `VectorAssembler`.
  - **Estimators**:
    - Learn from the input data and produce a model.
    - Example: `LinearRegression`, `DecisionTreeClassifier`.

- **Example**:
  ```python
  from pyspark.ml import Pipeline
  from pyspark.ml.feature import Tokenizer, VectorAssembler
  from pyspark.ml.classification import LogisticRegression

  # Define the stages of the pipeline
  tokenizer = Tokenizer(inputCol="text", outputCol="words")
  assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
  lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

  # Create a pipeline
  pipeline = Pipeline(stages=[tokenizer, assembler, lr])

  # Fit the pipeline to training data
  model = pipeline.fit(trainingData)

  # Make predictions
  predictions = model.transform(testData)
  ```

#### Feature Extraction and Transformation
- **StringIndexer**:
  - Encodes a string column of labels to a column of label indices.
  ```python
  from pyspark.ml.feature import StringIndexer

  indexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
  indexed = indexer.fit(df).transform(df)
  ```

- **OneHotEncoder**:
  - Maps a column of label indices to a column of binary vectors.
  ```python
  from pyspark.ml.feature import OneHotEncoder

  encoder = OneHotEncoder(inputCol="categoryIndex", outputCol="categoryVec")
  encoded = encoder.fit(df).transform(df)
  ```

- **StandardScaler**:
  - Standardizes features by removing the mean and scaling to unit variance.
  ```python
  from pyspark.ml.feature import StandardScaler

  scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures", withStd=True, withMean=False)
  scalerModel = scaler.fit(df)
  scaledData = scalerModel.transform(df)
  ```

### Example Code for Feature Extraction and Transformation

```python
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler

# Initialize Spark session
spark = SparkSession.builder.appName("MLlibExample").getOrCreate()

# Sample DataFrame
data = spark.createDataFrame([
    (0, "cat", 1.0),
    (1, "dog", 0.0),
    (2, "cat", 1.0),
    (3, "cat", 1.0),
    (4, "dog", 0.0)
], ["id", "category", "value"])

# StringIndexer
indexer = StringIndexer(inputCol="category", outputCol="categoryIndex")
indexed = indexer.fit(data).transform(data)

# OneHotEncoder
encoder = OneHotEncoder(inputCol="categoryIndex", outputCol="categoryVec")
encoded = encoder.fit(indexed).transform(indexed)

# VectorAssembler
assembler = VectorAssembler(inputCols=["value", "categoryVec"], outputCol="features")
assembled = assembler.transform(encoded)

# StandardScaler
scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures")
scalerModel = scaler.fit(assembled)
scaledData = scalerModel.transform(assembled)

scaledData.show()

# Stop Spark session
spark.stop()
```

