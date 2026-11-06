### Dimensionality Reduction Techniques

#### 1. **Principal Component Analysis (PCA)**
- **Definition:** PCA is a linear dimensionality reduction technique that seeks to maximize variance and identify the most important features (principal components) in the data.
- **Key Points:**
  - **Variance Maximization:** Finds orthogonal components that capture the maximum variance in the data.
  - **Linear Transformation:** Projects data onto a lower-dimensional subspace.
  - **Advantages:** Reduces dimensionality while preserving most of the variation in the data.

- **Example:**
```python
from sklearn.decomposition import PCA
import numpy as np

# Sample data
X = np.array([[1, 2, 1], [2, 3, 1.5], [3, 4, 2], [4, 5, 2.5]])

# Create a PCA model
pca = PCA(n_components=2)

# Fit the model and transform the data
X_pca = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Transformed shape:", X_pca.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("PCA components (eigenvectors):\n", pca.components_)
```

#### 2. **Linear Discriminant Analysis (LDA)**
- **Definition:** LDA is both a dimensionality reduction technique and a supervised learning algorithm for classification. It finds the feature subspace that maximizes class separability.
- **Key Points:**
  - **Maximizes Class Separability:** Projects data onto a subspace that maximizes the separation between multiple classes.
  - **Supervised Technique:** Requires class labels for training.
  - **Advantages:** Effective for classification tasks, reduces dimensionality while preserving class discrimination.

- **Example:**
```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

# Sample data (with class labels)
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])  # Binary class labels

# Create an LDA model
lda = LinearDiscriminantAnalysis(n_components=1)

# Fit the model and transform the data
X_lda = lda.fit_transform(X, y)

print("Original shape:", X.shape)
print("Transformed shape:", X_lda.shape)
print("Explained variance ratio (LDA):", lda.explained_variance_ratio_)
print("LDA components (eigenvectors):\n", lda.scalings_)
```

#### 3. **t-SNE (t-Distributed Stochastic Neighbor Embedding)**
- **Definition:** t-SNE is a non-linear dimensionality reduction technique that maps high-dimensional data to a lower-dimensional space while preserving the local structure of the data.
- **Key Points:**
  - **Local Relationships Preservation:** Focuses on preserving the similarity of nearby points.
  - **Non-linear Mapping:** Captures complex structures in the data.
  - **Advantages:** Visualizes high-dimensional data effectively, useful for exploratory data analysis.

- **Example:**
```python
from sklearn.manifold import TSNE
import numpy as np

# Sample data
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])

# Create a t-SNE model
tsne = TSNE(n_components=2, perplexity=30, random_state=0)

# Fit the model and transform the data
X_tsne = tsne.fit_transform(X)

print("Original shape:", X.shape)
print("Transformed shape (t-SNE):", X_tsne.shape)
```

### Key Points:
- **PCA** is a linear technique that maximizes variance and is suitable for reducing the dimensionality of large datasets.
- **LDA** focuses on maximizing class separability and is useful for supervised dimensionality reduction.
- **t-SNE** is non-linear and effective for visualizing complex, high-dimensional data structures.

Understanding these dimensionality reduction techniques provides students with essential tools for preprocessing data, visualizing data distributions, and improving the performance of machine learning models by reducing the number of features while preserving important information.