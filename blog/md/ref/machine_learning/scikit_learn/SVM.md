# Support Vector Machines (SVM)

## Takeaway
- **Linear SVM** finds optimal linear boundaries between classes.
- **Kernel SVM** extends to non-linear boundaries using kernel functions.
- **GridSearchCV** optimizes SVM performance by searching through specified hyperparameters.

These concepts and examples provide a solid foundation for understanding SVMs and their practical applications in classification tasks, including handling linearly and non-linearly separable datasets effectively.

## **Linear SVM**
- **Definition:** Linear SVM is a supervised learning algorithm used for classification tasks where it tries to find the optimal hyperplane that best separates the classes in the feature space.
- **Key Points:**
  - Finds the best linear separator for the data.
  - Effective for linearly separable data.
  - Maximizes the margin between classes.

- **Example:**
```python
from sklearn.svm import SVC
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels

# Create a linear SVM model
linear_svm = SVC(kernel='linear')

# Fit the model
linear_svm.fit(X, y)

# Predict
x_test = np.array([[5, 6]])
prediction = linear_svm.predict(x_test)

print("Support Vectors:", linear_svm.support_vectors_)
print("Coefficients:", linear_svm.coef_)
print("Intercept:", linear_svm.intercept_)
print("Prediction for [5, 6]:", prediction)
```

## **Kernel SVM**
- **Definition:** Kernel SVM extends linear SVM by using a kernel function to map the input data into a higher-dimensional space where classes can be separated by a linear hyperplane.
- **Key Points:**
  - Handles non-linearly separable data by transforming it into a higher-dimensional space.
  - Common kernel functions: polynomial, radial basis function (RBF), sigmoid, etc.
  - Allows complex decision boundaries.

- **Example (RBF Kernel):**
```python
from sklearn.svm import SVC
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels

# Create a kernel SVM model (RBF kernel)
rbf_svm = SVC(kernel='rbf')

# Fit the model
rbf_svm.fit(X, y)

# Predict
x_test = np.array([[5, 6]])
prediction = rbf_svm.predict(x_test)

print("Support Vectors:", rbf_svm.support_vectors_)
print("Prediction for [5, 6]:", prediction)
```

## **Hyperparameter Tuning with GridSearchCV**
- **Definition:** GridSearchCV is a method to systematically work through multiple combinations of hyperparameters, cross-validating as it goes to determine which parameters optimize the performance of a model.
- **Key Points:**
  - Helps in finding the best set of hyperparameters for a model.
  - Improves model performance and generalization.
  - Reduces the risk of overfitting.

- **Example (GridSearchCV for SVM):**
```python
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary classification labels

# Define parameter grid
param_grid = {'C': [0.1, 1, 10], 'gamma': [0.1, 1, 10], 'kernel': ['rbf', 'linear']}

# Create a SVM model
svm_model = SVC()

# Instantiate GridSearchCV
grid_search = GridSearchCV(estimator=svm_model, param_grid=param_grid, cv=3, verbose=2)

# Fit GridSearchCV
grid_search.fit(X, y)

# Best parameters and best score
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)
```