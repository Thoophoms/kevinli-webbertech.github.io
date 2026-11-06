# Anomaly Detection Techniques

## Takeaway
- **One-class SVM** learns the boundaries of normal data and identifies outliers.
- **Isolation Forests** use ensemble of decision trees to isolate anomalies based on their path lengths.
- Both techniques are effective for anomaly detection in various domains, providing robust solutions for identifying unusual patterns in data.

Understanding these anomaly detection techniques equips us with essential tools for detecting outliers and anomalies in real-world datasets, crucial for tasks such as fraud detection, network security, and quality control.

## **One-class SVM (Support Vector Machine)**
- **Definition:** One-class SVM is an unsupervised learning algorithm that learns a decision function for anomaly detection: it learns the properties of normal instances and classifies new data points as either normal or anomalies (outliers).
- **Key Points:**
  - **Unsupervised Learning:** Only normal instances are used for training.
  - **Kernel Trick:** Can use kernel functions to handle non-linear boundaries.
  - **Advantages:** Effective for high-dimensional data, handles skewed data distributions.

- **Example:**
```python
from sklearn.svm import OneClassSVM
import numpy as np

# Sample data (normal data)
X_train = 0.3 * np.random.randn(100, 2)

# Create a One-class SVM model
svm = OneClassSVM(nu=0.05)  # nu is an upper bound on the fraction of outliers

# Fit the model
svm.fit(X_train)

# Generate test data (including outliers)
X_test = np.r_[0.3 * np.random.randn(20, 2), np.random.uniform(low=-6, high=6, size=(5, 2))]

# Predict outliers (anomalies)
y_pred = svm.predict(X_test)

print("Predicted labels (-1 for outliers, 1 for inliers):", y_pred)
```

## **Isolation Forests**
- **Definition:** Isolation Forests are ensemble learning methods for anomaly detection that isolate anomalies by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature.
- **Key Points:**
  - **Ensemble of Decision Trees:** Each tree partitions the data recursively.
  - **Path Length:** Anomalies are expected to have shorter average path lengths in the tree.
  - **Advantages:** Effective for high-dimensional data, scalable to large datasets.

- **Example:**
```python
from sklearn.ensemble import IsolationForest
import numpy as np

# Sample data (normal data)
X_train = 0.3 * np.random.randn(100, 2)

# Create an Isolation Forest model
isoforest = IsolationForest(contamination=0.05)  # contamination is the expected proportion of outliers

# Fit the model
isoforest.fit(X_train)

# Generate test data (including outliers)
X_test = np.r_[0.3 * np.random.randn(20, 2), np.random.uniform(low=-6, high=6, size=(5, 2))]

# Predict outliers (anomalies)
y_pred = isoforest.predict(X_test)

print("Predicted labels (-1 for outliers, 1 for inliers):", y_pred)
```