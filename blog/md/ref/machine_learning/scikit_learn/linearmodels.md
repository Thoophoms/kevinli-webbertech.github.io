# Linear Models with Scikit-Learn

## Takeway

- **Linear regression** predicts continuous outcomes using a linear equation.
- **Ridge and Lasso regression** add regularization to linear regression to handle multicollinearity and prevent overfitting.
- **Logistic regression** predicts binary outcomes or probabilities using logistic function.
  
These foundational models are essential tools in data analysis and machine learning, providing a versatile toolkit for predictive modeling across various domains.

## **Linear Regression**
- **Definition:** Linear regression models the relationship between a dependent variable \( y \) and one or more independent variables \( X \) by fitting a linear equation to observed data.
- **Usage:** Predicting continuous outcomes.
- **Example:**
  ```python
  from sklearn.linear_model import LinearRegression
  import numpy as np

  # Sample data
  X = np.array([[1], [2], [3], [4]])
  y = np.array([2, 3.5, 4.2, 5.0])

  # Create a linear regression model
  model = LinearRegression()

  # Fit the model
  model.fit(X, y)

  # Predict
  x_test = np.array([[5]])
  prediction = model.predict(x_test)

  print("Coefficient:", model.coef_)
  print("Intercept:", model.intercept_)
  print("Prediction for x=5:", prediction)
  ```

## **Ridge Regression**
- **Definition:** Ridge regression adds a penalty equivalent to the square of the magnitude of coefficients to the linear regression, helping to reduce overfitting.
- **Usage:** Handling multicollinearity and preventing overfitting in linear regression.
- **Example:**
  ```python
  from sklearn.linear_model import Ridge
  import numpy as np

  # Sample data
  X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
  y = np.array([5, 6, 7, 8])

  # Create a ridge regression model
  alpha = 0.1  # Regularization strength
  ridge_model = Ridge(alpha=alpha)

  # Fit the model
  ridge_model.fit(X, y)

  # Predict
  x_test = np.array([[5, 6]])
  prediction = ridge_model.predict(x_test)

  print("Coefficients:", ridge_model.coef_)
  print("Intercept:", ridge_model.intercept_)
  print("Prediction for [5, 6]:", prediction)
  ```

## **Lasso Regression**
- **Definition:** Lasso regression adds a penalty equivalent to the absolute value of the magnitude of coefficients to the linear regression, promoting sparsity and feature selection.
- **Usage:** Feature selection in high-dimensional datasets.
- **Example:**
  ```python
  from sklearn.linear_model import Lasso
  import numpy as np

  # Sample data
  X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
  y = np.array([5, 6, 7, 8])

  # Create a Lasso regression model
  alpha = 0.1  # Regularization strength
  lasso_model = Lasso(alpha=alpha)

  # Fit the model
  lasso_model.fit(X, y)

  # Predict
  x_test = np.array([[5, 6]])
  prediction = lasso_model.predict(x_test)

  print("Coefficients:", lasso_model.coef_)
  print("Intercept:", lasso_model.intercept_)
  print("Prediction for [5, 6]:", prediction)
  ```

## **Logistic Regression**
- **Definition:** Logistic regression is used for binary classification, estimating the probability of a binary outcome based on one or more predictor variables.

- **Usage:** Predicting binary outcomes or probabilities.

- **Example:**
  ```python
  from sklearn.linear_model import LogisticRegression
  import numpy as np

  # Sample data
  X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
  y = np.array([0, 0, 1, 1])  # Binary classification labels

  # Create a logistic regression model
  logistic_model = LogisticRegression()

  # Fit the model
  logistic_model.fit(X, y)

  # Predict probabilities
  x_test = np.array([[5, 6]])
  probabilities = logistic_model.predict_proba(x_test)
  prediction = logistic_model.predict(x_test)

  print("Coefficients:", logistic_model.coef_)
  print("Intercept:", logistic_model.intercept_)
  print("Class Probabilities:", probabilities)
  print("Prediction for [5, 6]:", prediction)
  ```