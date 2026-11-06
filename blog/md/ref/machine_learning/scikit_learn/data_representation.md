# Data Representation in Machine Learning

## Takeaway

- **Loading Datasets**: Understand how to load datasets from CSV files and scikit-learn's built-in datasets.
- **Preprocessing Data**: Learn to scale, encode, and impute data to prepare it for machine learning models.
- **Train-Test Split**: Split data into training and testing sets to evaluate model performance.


## Loading Datasets

**Loading Datasets from CSV Files**

To work with datasets, one of the common formats is CSV (Comma-Separated Values). Using Python and the `pandas` library, you can easily load CSV files.

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('your_dataset.csv')

# Display the first few rows
print(df.head())
```

**Example:**
```python
# Sample code to load a CSV file
import pandas as pd

# Load the dataset
df = pd.read_csv('students_performance.csv')

# Display the first few rows
print(df.head())
```

**Loading Datasets from Scikit-learn**

Scikit-learn provides several built-in datasets that are useful for practice and learning. These datasets are available through the `sklearn.datasets` module.

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Features and target variable
X = iris.data
y = iris.target

print("Feature matrix shape:", X.shape)
print("Target vector shape:", y.shape)
```

## Preprocessing Data

Preprocessing is a crucial step in preparing data for machine learning models. This includes tasks such as scaling, encoding categorical variables, and handling missing values.

**Scaling**

Scaling ensures that the features are on a similar scale, which is essential for algorithms that rely on distance calculations.

```python
from sklearn.preprocessing import StandardScaler

# Create a scaler object
scaler = StandardScaler()

# Fit and transform the data
X_scaled = scaler.fit_transform(X)

print("Scaled data:", X_scaled[:5])
```

**Encoding Categorical Variables**

Categorical variables need to be converted into a numerical format. One common method is one-hot encoding.

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load dataset with categorical variables
df = pd.read_csv('students_performance.csv')

# Create a OneHotEncoder object
encoder = OneHotEncoder()

# Fit and transform the categorical data
encoded_features = encoder.fit_transform(df[['gender', 'race/ethnicity']])

print("Encoded features shape:", encoded_features.shape)
```

**Imputation**

Handling missing values is essential for maintaining the integrity of the dataset. Imputation can be used to fill in missing values.

```python
from sklearn.impute import SimpleImputer

# Create an imputer object
imputer = SimpleImputer(strategy='mean')

# Fit and transform the data
X_imputed = imputer.fit_transform(X)

print("Data after imputation:", X_imputed[:5])
```

## Train-Test Split

To evaluate the performance of a machine learning model, it's important to split the data into training and testing sets. This allows for an unbiased evaluation of the model's performance on unseen data.

```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
```

### Example: Complete Workflow

Here's an example that integrates loading a dataset, preprocessing, and splitting the data.

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('students_performance.csv')

# Separate features and target variable
X = df.drop(columns=['math_score'])
y = df['math_score']

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X.select_dtypes(include=['float64', 'int64']))

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Encode categorical features
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(X.select_dtypes(include=['object']))

# Combine numerical and categorical features
import numpy as np
X_preprocessed = np.hstack((X_scaled, encoded_features.toarray()))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_preprocessed, y, test_size=0.2, random_state=42)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
```