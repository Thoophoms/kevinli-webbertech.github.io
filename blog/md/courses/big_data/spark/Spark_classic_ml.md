# Spark with Classic ML (Machine Learning)

## Overview

* Classification

  * Logistic regression
    * Binomial logistic regression
    * Multinomial logistic regression
  * Decision tree classifier
  * Random forest classifier
  * Gradient-boosted tree classifier
  * Multilayer perceptron classifier
  * Linear Support Vector Machine
  * One-vs-Rest classifier (a.k.a. One-vs-All)
  * Naive Bayes
  * Factorization machines classifier

* Regression

  * Linear regression
  * Generalized linear regression
    * Available families
  * Decision tree regression
  * Random forest regression
  * Gradient-boosted tree regression
  * Survival regression
  * Isotonic regression
  * Factorization machines regressor

* Linear methods
* Factorization Machines
* Decision trees
  * Inputs and Outputs
    * Input Columns
    * Output Columns

* Tree Ensembles
  * Random Forests
    * Inputs and Outputs
      * Input Columns
      * Output Columns (Predictions)
  * Gradient-Boosted Trees (GBTs)
    * Inputs and Outputs
      * Input Columns
      * Output Columns (Predictions)

## Our plan

* We are not going to go very detail in all of these, but pick a few of them to run and talk.

* We will systematically learn these during the next couple of weeks.

## Logistic regression 

A popular method to predict a categorical response. It is a special case of Generalized Linear models that predicts the probability of the outcomes. I

## Binomial Regression

LogisticRegressionTrainingSummary provides a summary for a LogisticRegressionModel. In the case of binary classification, certain additional metrics are available, e.g. ROC curve. See BinaryLogisticRegressionTrainingSummary.

> https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.classification.LogisticRegressionSummary.html
> https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.classification.LogisticRegressionModel.html
> https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.classification.BinaryLogisticRegressionTrainingSummary.html
>  full example code at "examples/src/main/python/ml/logistic_regression_with_elastic_net.py" in the Spark repo.


```python
from pyspark.ml.classification import LogisticRegression

# Load training data
training = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

# Fit the model
lrModel = lr.fit(training)

# Print the coefficients and intercept for logistic regression
print("Coefficients: " + str(lrModel.coefficients))
print("Intercept: " + str(lrModel.intercept))

# We can also use the multinomial family for binary classification
mlr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family="multinomial")

# Fit the model
mlrModel = mlr.fit(training)

# Print the coefficients and intercepts for logistic regression with multinomial family
print("Multinomial coefficients: " + str(mlrModel.coefficientMatrix))
print("Multinomial intercepts: " + str(mlrModel.interceptVector))

# Extract the summary from the returned LogisticRegressionModel instance trained
# in the earlier example
trainingSummary = lrModel.summary

# Obtain the objective per iteration
objectiveHistory = trainingSummary.objectiveHistory
print("objectiveHistory:")
for objective in objectiveHistory:
    print(objective)

# Obtain the receiver-operating characteristic as a dataframe and areaUnderROC.
trainingSummary.roc.show()
print("areaUnderROC: " + str(trainingSummary.areaUnderROC))

# Set the model threshold to maximize F-Measure
fMeasure = trainingSummary.fMeasureByThreshold
maxFMeasure = fMeasure.groupBy().max('F-Measure').select('max(F-Measure)').head()
bestThreshold = fMeasure.where(fMeasure['F-Measure'] == maxFMeasure['max(F-Measure)']) \
    .select('threshold').head()['threshold']
lr.setThreshold(bestThreshold)
```


## Ref

- https://spark.apache.org/docs/latest/ml-classification-regression.html
- https://spark.apache.org/docs/latest/mllib-linear-methods.html#logistic-regression
- https://en.wikipedia.org/wiki/Generalized_linear_model