# Mathematical Building Blocks of Neural Networks

Understanding the major mathematical concepts of machine learning is crucial, especially from a Natural Language Processing (NLP) point of view
## Vectors

A vector is an array of numbers, which can be either continuous or discrete. The space that the vector occupies is known as a vector space. The dimensions of this space can be finite or infinite. 

Most machine learning and data science problems deal with fixed-length vectors.

### Example: Vector Representation in PyTorch

In PyTorch, a vector can be represented and its size can be checked as follows:

```python
temp = torch.FloatTensor([23, 24, 24.5, 26, 27.2, 23.0])
temp.size()
```

## Scalars

A scalar is a zero-dimensional value, meaning it contains only one value. In PyTorch, there is no special tensor type specifically for scalars; instead, they are represented as tensors with a single value.

### Example: Scalar Representation in PyTorch

In PyTorch, a scalar can be represented as follows:

```python
x = torch.rand(10)
x.size()
```

## Matrices

Structured data is often represented in the form of tables or matrices. A matrix is a two-dimensional array where each element is identified by two indices, typically representing rows and columns.

For example, the Boston House Prices dataset, available in the Python scikit-learn library, can be converted into a PyTorch tensor as follows:

### Example: Matrix Representation in PyTorch

```python
from sklearn.datasets import load_boston
import torch

boston = load_boston()
boston_tensor = torch.from_numpy(boston.data)
boston_tensor.size()
```

