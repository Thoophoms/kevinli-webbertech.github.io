### Scikit-learn and Machine Learning

## Takeway

- **Machine Learning**: Enables systems to learn from data.
- **Supervised Learning**: Trained on labeled data.
- **Unsupervised Learning**: Trained on unlabeled data.
- **Model Selection**: Choosing the right model for the task.
- **Evaluation Metrics**: Metrics like MSE, R-squared for regression, and accuracy, precision, recall, F1-score for classification, to evaluate model performance.

### What is Machine Learning?

**Definition:**
Machine Learning (ML) is a subset of artificial intelligence (AI) that involves the use of algorithms and statistical models to enable computers to perform specific tasks without using explicit instructions. Instead, the system learns from patterns and inferences derived from data.

**Example:**
Email spam filtering is a common example of machine learning. The system learns to classify emails as spam or not spam based on the features of the emails, such as the presence of certain keywords, the sender’s address, etc.

### Supervised vs. Unsupervised Learning

**Supervised Learning:**
In supervised learning, the model is trained on a labeled dataset, which means that each training example is paired with an output label. The goal is for the model to learn to map inputs to the correct output.

- **Example:** Predicting house prices based on features like the number of bedrooms, bathrooms, and square footage. The dataset contains labeled examples (house features and corresponding prices).

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load your own dataset
df = pd.read_csv('house_prices.csv')

# Assuming the last column is the target variable
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
```

**Unsupervised Learning:**
In unsupervised learning, the model is trained on an unlabeled dataset. The goal is to infer the natural structure present within a set of data points.

- **Example:** Customer segmentation in marketing. Here, the dataset might contain customer purchase history, and the goal is to group customers with similar behaviors without predefined labels.

```python
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your own dataset
df = pd.read_csv('customer_data.csv')

# Assuming the features are in all columns
X = df.iloc[:, :]

# Initialize the model
kmeans = KMeans(n_clusters=3, random_state=42)

# Train the model
kmeans.fit(X)

# Get cluster assignments
clusters = kmeans.labels_

# Add the cluster assignments to the original data
df['Cluster'] = clusters

# Plot the clusters
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=clusters, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Customer Segmentation')
plt.show()
```

### Model Selection and Evaluation Metrics

**Model Selection:**
Choosing the right model involves understanding the problem domain, the data, and the performance metrics. Common models include linear regression, logistic regression, decision trees, support vector machines, and neural networks.

**Evaluation Metrics:**
Evaluation metrics are used to measure the performance of a machine learning model. The choice of metric depends on the type of problem being solved (regression vs classification).

- **For Regression:**
  - **Mean Squared Error (MSE):** Measures the average of the squares of the errors. Lower values indicate better fit.
  - **R-squared:** Indicates the proportion of the variance in the dependent variable that is predictable from the independent variables.

```python
from sklearn.metrics import mean_squared_error, r2_score

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
```

- **For Classification:**
  - **Accuracy:** The proportion of correctly classified instances out of the total instances.
  - **Precision, Recall, and F1-Score:** Precision measures the proportion of true positives out of all predicted positives, recall measures the proportion of true positives out of all actual positives, and F1-score is the harmonic mean of precision and recall.

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Assuming binary classification
y_test = [0, 1, 0, 1, 0, 1, 0, 1]
predictions = [0, 1, 0, 0, 1, 1, 0, 1]

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
```