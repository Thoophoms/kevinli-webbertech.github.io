# Clustering Algorithms

## Takeaway
- **K-means Clustering** partitions data into \( k \) clusters based on centroids.
- **Hierarchical Clustering** creates a tree of clusters, useful for visualizing relationships.
- **DBSCAN** identifies clusters based on density, handling arbitrary shapes and noisy data.

These clustering algorithms provide powerful tools for exploring and analyzing unlabeled data, uncovering patterns and structures that can aid in various domains of data analysis and machine learning.

## **K-means Clustering**
- **Definition:** K-means clustering is an unsupervised learning algorithm that partitions data into \( k \) clusters based on similarity of features.
- **Key Points:**
  - **Centroid-based:** Clusters are defined by their centroids (means).
  - **Iterative Refinement:** Alternates between assigning data points to the nearest centroid and recalculating centroids based on the assigned points.
  - **Advantages:** Simple, efficient for large datasets, scales well.

- **Example:**
```python
from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Create a K-means clustering model
kmeans = KMeans(n_clusters=2)

# Fit the model
kmeans.fit(X)

# Get cluster labels and centroids
cluster_labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("Cluster Labels:", cluster_labels)
print("Centroids:", centroids)
```

## **Hierarchical Clustering**
- **Definition:** Hierarchical clustering creates a hierarchy of clusters by either recursively merging or splitting clusters based on distance metrics.
- **Key Points:**
  - **Agglomerative vs. Divisive:** Agglomerative starts with each point as its own cluster and merges them, while divisive starts with one cluster and splits it.
  - **Dendrogram:** Visual representation of the hierarchy.
  - **Advantages:** No need to specify the number of clusters beforehand, interpretable dendrogram.

- **Example:**
```python
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np

# Sample data
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Perform hierarchical clustering
linked = linkage(X, 'single')  # Single linkage (other options: complete, average)

# Plot dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=[f'Point {i+1}' for i in range(len(X))],
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()
```

## **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
- **Definition:** DBSCAN is a density-based clustering algorithm that groups together points that are closely packed together (dense regions) and marks points as outliers (noise) that lie alone in low-density regions.
- **Key Points:**
  - **Core Points, Border Points, Noise:** Defined based on density (number of points within a specified radius \( \epsilon \)).
  - **No Need for Specifying Number of Clusters:** Automatically determines the number of clusters based on data density.
  - **Advantages:** Robust to noise and outliers, handles non-linear boundaries well.

- **Example:**
```python
from sklearn.cluster import DBSCAN
import numpy as np

# Sample data
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Create a DBSCAN clustering model
dbscan = DBSCAN(eps=2, min_samples=2)

# Fit the model
dbscan.fit(X)

# Get cluster labels
cluster_labels = dbscan.labels_

print("Cluster Labels:", cluster_labels)
```