# Decision Trees and Ensemble Methods

## Takeaway

- **Decision Trees** provide intuitive decision-making based on feature splits.
- **Random Forests** improve upon decision trees by combining multiple trees and randomization.
- **Gradient Boosting** builds strong predictive models by sequentially improving upon the errors of previous models.

## **Decision Trees**
- **Definition:** Decision trees are supervised learning models used for both classification and regression tasks. They recursively split the data into subsets based on features to create a tree-like structure of decisions.
- **Key Points:**
  - **Tree Structure:** Nodes represent features, edges represent decisions.
  - **Leaf Nodes:** Terminal nodes representing final predictions.
  - **Splitting Criteria:** Maximizing information gain (for classification) or minimizing variance (for regression).
  - **Advantages:** Intuitive, easy to interpret, handles non-linear relationships.

- **Example:**
```python
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels

# Create a decision tree classifier
tree_clf = DecisionTreeClassifier()

# Fit the model
tree_clf.fit(X, y)

# Predict
x_test = np.array([[5, 6]])
prediction = tree_clf.predict(x_test)

print("Feature Importances:", tree_clf.feature_importances_)
print("Prediction for [5, 6]:", prediction)
```

## **Random Forests**
- **Definition:** Random forests are ensemble learning methods that construct multiple decision trees during training and output the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.
- **Key Points:**
  - **Ensemble of Trees:** Combines multiple decision trees to improve generalization and robustness.
  - **Random Feature Subsets:** Each tree is trained on a random subset of features.
  - **Bootstrap Aggregation (Bagging):** Random sampling with replacement to create diverse trees.
  - **Advantages:** Reduces overfitting, handles high-dimensional data, robust to outliers.

- **Example:**
```python
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels

# Create a random forest classifier
rf_clf = RandomForestClassifier()

# Fit the model
rf_clf.fit(X, y)

# Predict
x_test = np.array([[5, 6]])
prediction = rf_clf.predict(x_test)

print("Feature Importances:", rf_clf.feature_importances_)
print("Prediction for [5, 6]:", prediction)
```

## **Gradient Boosting**
- **Definition:** Gradient boosting is an ensemble technique where models are added sequentially, with each new model correcting errors made by the previous ones, thereby reducing the overall bias.
- **Key Points:**
  - **Boosting Technique:** Builds trees sequentially, each focusing on improving upon the mistakes of its predecessor.
  - **Gradient Descent:** Optimizes a loss function (e.g., squared error for regression, deviance for classification) in the gradient direction.
  - **Examples:** AdaBoost, XGBoost, LightGBM.
  - **Advantages:** Produces strong predictive performance, handles complex interactions in data.

- **Example (AdaBoost Classifier):**
```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels

# Create a base decision tree classifier
base_clf = DecisionTreeClassifier(max_depth=1)

# Create an AdaBoost classifier
adaboost_clf = AdaBoostClassifier(base_estimator=base_clf, n_estimators=50)

# Fit the model
adaboost_clf.fit(X, y)

# Predict
x_test = np.array([[5, 6]])
prediction = adaboost_clf.predict(x_test)

print("Prediction for [5, 6]:", prediction)
```
