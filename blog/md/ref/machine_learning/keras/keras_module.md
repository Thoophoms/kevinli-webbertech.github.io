# KERAS MODULES

# Keras Modules Documentation

## Initializers

Provides a list of initializers functions. We can learn about them in detail in the Keras Layers chapter during the model creation phase of machine learning.

## Regularizers

Provides a list of regularizers functions. We can learn about them in detail in the Keras Layers chapter.

## Constraints

Provides a list of constraints functions. We can learn about them in detail in the Keras Layers chapter.

## Activations

Provides a list of activation functions. We can learn about them in detail in the Keras Layers chapter.

## Losses

Provides a list of loss functions. We can learn about them in detail in the Model Training chapter.

## Metrics

Provides a list of metrics functions. We can learn about them in detail in the Model Training chapter.

## Optimizers

Provides a list of optimizer functions. We can learn about them in detail in the Model Training chapter.

## Callback

Provides a list of callback functions. We can use these during the training process to print intermediate data as well as to stop the training itself (e.g., EarlyStopping method) based on some condition.

## Text Processing

Provides functions to convert text into NumPy arrays suitable for machine learning. We can use these in the data preparation phase of machine learning.

## Image Processing

Provides functions to convert images into NumPy arrays suitable for machine learning. We can use these in the data preparation phase of machine learning.

## Sequence Processing

Provides functions to generate time-based data from the given input data. We can use these in the data preparation phase of machine learning.

## Backend

Provides functions for backend operations like TensorFlow and Theano. By default, Keras runs on top of the TensorFlow backend. If desired, you can switch to other backends like Theano or CNTK. The default backend configuration is defined in the `.keras/keras.json` file in your root directory.
Keras backend module can be imported using below code
```python
 from keras import backend as k



>>> k.get_uid(prefix='')


>>> k.get_uid(prefix='')
```
## Utilities

Provides various utility functions useful in deep learning.

## `reset_uids`

The `reset_uids()` function resets the UID value.

```python
>>> k.reset_uids()

Now, again execute the get_uid(). This will be reset and change again to 1.

>>> k.get_uid(prefix='') 
```

## `placeholder`

The `placeholder` function instantiates a placeholder tensor. Here is an example of creating a simple placeholder with a 3-D shape:

```python
>>> data = k.placeholder(shape=(1, 3, 3))
>>> data
<tf.Tensor 'Placeholder_9:0' shape=(1, 3, 3) dtype=float32>


If you use int_shape(), it will show the shape. 

>>> k.int_shape(data) (1, 3, 3)
```
## `dot`

The `dot` function is used to multiply two tensors. 

Consider `a` and `b` are two tensors, and `c` will be the outcome of multiplying `a` and `b`. For example, with shapes `(4, 2)` for `a` and `(2, 3)` for `b`, the operation is defined as follows:

```python
>>> a = k.placeholder(shape=(4, 2))
>>> b = k.placeholder(shape=(2, 3))
>>> c = k.dot(a, b)
>>> c
<tf.Tensor 'MatMul_3:0' shape=(4, 3) dtype=float32>
```
## `ones`

The `ones` function initializes a tensor with all values set to one.

```python
>>> res = k.ones(shape=(2, 2))

# Print the value
>>> k.eval(res)
array([[1., 1.],
       [1., 1.]], dtype=float32)
```
## `batch_dot`

The `batch_dot` function performs the product of two tensors in batches. The input dimensions must be 2 or higher.

```python
>>> a_batch = k.ones(shape=(2, 3))
>>> b_batch = k.ones(shape=(3, 2))
>>> c_batch = k.batch_dot(a_batch, b_batch)
>>> c_batch
<tf.Tensor 'ExpandDims:0' shape=(2, 1) dtype=float32>
```
## `variable`

The `variable` function initializes a variable. Here is an example of performing a simple transpose operation with this variable:

```python
>>> data = k.variable([[10, 20, 30, 40], [50, 60, 70, 80]])
# Variable initialized here
>>> result = k.transpose(data)
>>> print(result)
Tensor("transpose_6:0", shape=(4, 2), dtype=float32)
>>> print(k.eval(result))
[[10. 50.]
 [20. 60.]
 [30. 70.]
 [40. 80.]]
```
### Accessing from NumPy

To work with NumPy arrays and convert them into Keras variables:

```python
>>> data = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])

>>> print(np.transpose(data))
[[10 50]
 [20 60]
 [30 70]
 [40 80]]

>>> res = k.variable(value=data)
>>> print(res)
<tf.Variable 'Variable_7:0' shape=(2, 4) dtype=float32_ref>

## `is_sparse(tensor)`

The `is_sparse` function checks whether a tensor is sparse.

```python
>>> a = k.placeholder((2, 2), sparse=True)

>>> print(a)
SparseTensor(indices=
   Tensor("Placeholder_8:0",
   shape=(?, 2), dtype=int64),
values=Tensor("Placeholder_7:0", shape=(,),
dtype=float32), dense_shape=Tensor("Const:0", shape=(2,), dtype=int64))

>>> print(k.is_sparse(a))
True
```
## `to_dense()`

The `to_dense` function converts a sparse tensor into a dense tensor.

```python
>>> b = k.to_dense(a)
>>> print(b)
Tensor("SparseToDense:0", shape=(2, 2), dtype=float32)

>>> print(k.is_sparse(b))
False
```
## `random_uniform_variable`

The `random_uniform_variable` function initializes a variable using a uniform distribution.

### Parameters

- **shape**: Denotes the rows and columns in the format of tuples.
- **low**: The lower bound of the uniform distribution.
- **high**: The upper bound of the uniform distribution.

### Example Usage

```python
>>> a = k.random_uniform_variable(shape=(2, 3), low=0, high=1)
>>> b = k.random_uniform_variable(shape=(3, 2), low=0, high=1)
>>> c = k.dot(a, b)
>>> k.int_shape(c)
(2, 2)

```

## `HDF5Matrix`

The `HDF5Matrix` function is used to represent input data in HDF5 format.

```python
from keras.utils import HDF5Matrix
data = HDF5Matrix('data.hdf5', 'data')
```
## `to_categorical`

The `to_categorical` function converts a class vector into a binary class matrix.

```python
>>> from keras.utils import to_categorical
>>> labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> to_categorical(labels)
array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]], dtype=float32)
```
## `print_summary`

The `print_summary` function is used to print the summary of a Keras model.

### Example Usage

```python
from keras.utils import print_summary

print_summary(model)
```
## `plot_model`

The `plot_model` function creates a visual representation of a Keras model in dot format and saves it to a file.

### Example Usage

```python
from keras.utils import plot_model

plot_model(model, to_file='rdesktop1.png')
```
This plot_model will generate an image to understand the performance of model.


