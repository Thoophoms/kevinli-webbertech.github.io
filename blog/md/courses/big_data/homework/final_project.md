# CSIT 554 Final Project

**Topic: Machine Learning Pipeline**

## Problem Description

Instructions. Please write code with Spark DataFrame and MLlib to complete
the following tasks.

* Task 1 Data collection (10 pts). Load the “adult dataset” from [here](https://drive.google.com/file/d/1MrDQnor8jcTrB9iqYkSOpp6xvaQ9DNcg/view?usp=sharing).

* Task 2 Data cleaning (20 pts). Handle the missing values.

* Task 3 Feature engineering (20 pts). Distill the features (all columns except for income) and labels (income). Transform the features into vectors. Use one-hot encoder to process categorical features. Split the dataset into a training and testing set with a ratio of 80% v.s. 20%.

* Task 4 Training (20 pts). Build a logistic regression and a gradient-boosted tree model to fit the dataset.

* Task 5 Tuning and Evaluation (20 pts). For each model, use grid parameter search and cross validation over 5 folds to find the parameters that yields the highest areaUnderROC on the training set.

* Task 6 Prediction (10 pts). For each model, make predictions on the testing set and display the areaUnderROC.

## Submission Guideline

1. Work individually.

2. After task 1-3, execute the display() command to show the result. For task 4, simply show some model summary result. For task 5 and 6, print the areaUnderROC.

3. Please submit a .ipynb file.

4. Submit your solution on Canvas on time. No late submission will be accepted.