 # Major Mathematical Concepts for Natural Language Processing (NLP)

The major mathematical concepts of machine learning that are important from a Natural Language Processing (NLP) point of view include:
 
## Vectors

A vector is an array of numbers, either continuous or discrete, and the space it consists of is called a vector space. The dimensions of this space can be finite or infinite. Most machine learning and data science problems deal with fixed-length vectors.

### Vector Representation

Here is an example of vector representation:

```python
temp = torch.FloatTensor([23, 24, 24.5, 26, 27.2, 23.0])
temp.size()
```
**Output:**

torch.Size([6])

## Scalar

A scalar is a zero-dimensional quantity containing only one value. In PyTorch, there is no special tensor for scalars; they are represented as tensors with a single value.

### Scalar Representation

Here is an example of scalar representation:

```python
x = torch.rand(10)
x.size()
```
**Output:**
torch.Size([10])

## Matrices

Structured data is usually represented in the form of tables or matrices. For example, the Boston House Prices dataset is available in the Python `scikit-learn` library.

### Example: Boston House Prices

```python
import torch
from sklearn.datasets import load_boston

boston = load_boston()
boston_tensor = torch.from_numpy(boston.data)
boston_tensor.size()

```
