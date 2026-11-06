# Layers

A Keras layer requires shape of the input (input_shape) to understand the structure of the input data, initializer to set the weight for each input and finally activators to transform the output to make it non-linear.

To summarise, Keras layer requires below minimum details to create a complete layer.

* Shape of the input data
* Number of neurons / units in the layer
* Initializers
* Regularizers
* Constraints
* Activations

Let us create a simple Keras layer using Sequential model API to get the idea of how Keras model and layer works.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 
from keras import regularizers 
from keras import constraints 

model = Sequential() 

model.add(Dense(32, input_shape=(16,), kernel_initializer = 'he_uniform', 
   kernel_regularizer = None, kernel_constraint = 'MaxNorm', activation = 'relu')) 
model.add(Dense(16, activation = 'relu')) 
model.add(Dense(8))
```

where,

Line 1-5 imports the necessary modules.

Line 7 creates a new model using Sequential API.

Line 9 creates a new Dense layer and add it into the model. Dense is an entry level layer provided by Keras, which accepts the number of neurons or units (32) as its required parameter. If the layer is first layer, then we need to provide Input Shape, (16,) as well. Otherwise, the output of the previous layer will be used as input of the next layer. All other parameters are optional.

First parameter represents the number of units (neurons).

input_shape represent the shape of input data.

kernel_initializer represent initializer to be used. he_uniform function is set as value.

kernel_regularizer represent regularizer to be used. None is set as value.

kernel_constraint represent constraint to be used. MaxNorm function is set as value.

activation represent activation to be used. relu function is set as value.

Line 10 creates second Dense layer with 16 units and set relu as the activation function.

Line 11 creates final Dense layer with 8 units.

## Basic Concept of Layers

### Input shape

In machine learning, all types of input data (text, images, videos) are first converted into arrays of numbers before being fed into algorithms. These arrays can be one-dimensional, two-dimensional (matrix), or multi-dimensional. The shape of these arrays, specified as a tuple of integers, indicates their dimensions. For example, (4,2) represents a matrix with four rows and two columns.

```python
>>> import numpy as np 
>>> shape = (4, 2) 
>>> input = np.zeros(shape) 
>>> print(input) 
[
   [0. 0.] 
   [0. 0.] 
   [0. 0.] 
   [0. 0.]
] 
>>>
```

Similarly, (3,4,2) three dimensional matrix having three collections of 4x2 matrix (two rows and four columns).

```python
>>> import numpy as np 
>>> shape = (3, 4, 2) 
>>> input = np.zeros(shape) 
>>> print(input)
[
   [[0. 0.] [0. 0.] [0. 0.] [0. 0.]] 
   [[0. 0.] [0. 0.] [0. 0.] [0. 0.]] 
   [[0. 0.] [0. 0.] [0. 0.] [0. 0.]]
]
>>>
```

### Initializers

In Machine Learning, weight will be assigned to all input data. Initializers module provides different functions to set these initial weight. Some of the Keras Initializer function are as follows −


**Zeros**

Generates 0 for all input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.Zeros() 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

Where, kernel_initializer represent the initializer for kernel of the model.

**Ones**

Generates 1 for all input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.Ones() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

**Constant**

Generates a constant value (say, 5) specified by the user for all input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.Constant(value = 0) model.add(
   Dense(512, activation = 'relu', input_shape = (784,), kernel_initializer = my_init)
)
```

where, value represent the constant value

**RandomNormal**

Generates value using normal distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.RandomNormal(mean=0.0, 
stddev = 0.05, seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

where,

`mean` represent the mean of the random values to generate

`stddev` represent the standard deviation of the random values to generate

`seed` represent the values to generate random number

**RandomUniform**

Generates value using uniform distribution of input data.

```python
from keras import initializers 

my_init = initializers.RandomUniform(minval = -0.05, maxval = 0.05, seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

where,

`minval` represent the lower bound of the random values to generate

`maxval` represent the upper bound of the random values to generate

**TruncatedNormal**

Generates value using truncated normal distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.TruncatedNormal(mean = 0.0, stddev = 0.05, seed = None
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

**VarianceScaling**

Generates value based on the input shape and output shape of the layer along with the specified scale.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.VarianceScaling(
   scale = 1.0, mode = 'fan_in', distribution = 'normal', seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   skernel_initializer = my_init))
```

where,

`scale` represent the scaling factor

`mode` represent any one of fan_in, fan_out and fan_avg values

`distribution` represent either of normal or uniform

**VarianceScaling**

It finds the stddev value for normal distribution using below formula and then find the weights using normal distribution,

`stddev = sqrt(scale / n)`

where n represent,

number of input units for mode = fan_in

number of out units for mode = fan_out

average number of input and output units for mode = fan_avg

Similarly, it finds the limit for uniform distribution using below formula and then find the weights using uniform distribution,

`limit = sqrt(3 * scale / n)`

**lecun_normal**

Generates value using lecun normal distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.RandomUniform(minval = -0.05, maxval = 0.05, seed = None)
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

It finds the stddev using the below formula and then apply normal distribution

`stddev = sqrt(1 / fan_in)`

where, fan_in represent the number of input units.

**lecun_uniform**

Generates value using lecun uniform distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.lecun_uniform(seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

It finds the limit using the below formula and then apply uniform distribution

`limit = sqrt(3 / fan_in)`

where,

`fan_in` represents the number of input units

`fan_out` represents the number of output units

**glorot_normal**

Generates value using glorot normal distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.glorot_normal(seed=None) model.add(
   Dense(512, activation = 'relu', input_shape = (784,), kernel_initializer = my_init)
)
```

It finds the stddev using the below formula and then apply normal distribution

`stddev = sqrt(2 / (fan_in + fan_out))`

where,

`fan_in` represents the number of input units

`fan_out` represents the number of output units

**glorot_uniform**

Generates value using glorot uniform distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.glorot_uniform(seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

It finds the limit using the below formula and then apply uniform distribution

`limit = sqrt(6 / (fan_in + fan_out))`

where,

`fan_in` represent the number of input units.

`fan_out` represents the number of output units

**he_normal**

Generates value using he normal distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.RandomUniform(minval = -0.05, maxval = 0.05, seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

It finds the stddev using the below formula and then apply normal distribution.

`stddev = sqrt(2 / fan_in)`

where, fan_in represent the number of input units.

**he_uniform**

Generates value using he uniform distribution of input data.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.he_normal(seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

It finds the limit using the below formula and then apply uniform distribution.

`limit = sqrt(6 / fan_in)`

where, fan_in represent the number of input units.

**Orthogonal**

Generates a random orthogonal matrix.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.Orthogonal(gain = 1.0, seed = None) 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init))
```

where, gain represent the multiplication factor of the matrix.

**Identity**

Generates identity matrix.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.Identity(gain = 1.0) model.add(
   Dense(512, activation = 'relu', input_shape = (784,), kernel_initializer = my_init)
)
```

### Constraints

In machine learning, a constraint will be set on the parameter (weight) during optimization phase. <>Constraints module provides different functions to set the constraint on the layer. Some of the constraint functions are as follows.

**NonNeg**

Constrains weights to be non-negative.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import initializers 

my_init = initializers.Identity(gain = 1.0) model.add(
   Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_initializer = my_init)
)
```

where, kernel_constraint represent the constraint to be used in the layer.

**UnitNorm**

Constrains weights to be unit norm.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import constraints 

my_constrain = constraints.UnitNorm(axis = 0) 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_constraint = my_constrain))
```

**MaxNorm**

Constrains weight to norm less than or equals to the given value.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import constraints 

my_constrain = constraints.MaxNorm(max_value = 2, axis = 0) 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_constraint = my_constrain))
```

where,

`max_value` represent the upper bound

axis represent the dimension in which the constraint to be applied. e.g. in Shape (2,3,4) axis 0 denotes first dimension, 1 denotes second dimension and 2 denotes third dimension

**MinMaxNorm**

Constrains weights to be norm between specified minimum and maximum values.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import constraints 

my_constrain = constraints.MinMaxNorm(min_value = 0.0, max_value = 1.0, rate = 1.0, axis = 0) 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_constraint = my_constrain))
```

where, rate represent the rate at which the weight constrain is applied.

### Regularizers

In machine learning, regularizers are used in the optimization phase. It applies some penalties on the layer parameter during optimization. Keras regularization module provides below functions to set penalties on the layer. Regularization applies per-layer basis only.

**L1 Regularizer**

It provides L1 based regularization.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import regularizers 

my_regularizer = regularizers.l1(0.) 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_regularizer = my_regularizer))
```

where, kernel_regularizer represent the rate at which the weight constrain is applied.

**L2 Regularizer**

It provides L2 based regularization.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import regularizers 

my_regularizer = regularizers.l2(0.) 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,), 
   kernel_regularizer = my_regularizer))
```

**L1 and L2 Regularizer**

It provides both L1 and L2 based regularization.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
from keras import regularizers 

my_regularizer = regularizers.l2(0.) 
model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,),
   kernel_regularizer = my_regularizer))
```

### Activations

In machine learning, activation function is a special function used to find whether a specific neuron is activated or not. Basically, the activation function does a nonlinear transformation of the input data and thus enable the neurons to learn better. Output of a neuron depends on the activation function

result = Activation(SUMOF(input * weight) + bias)

**linear**

Applies Linear function. Does nothing.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'linear', input_shape = (784,)))
```

Where, activation refers the activation function of the layer. It can be specified simply by the name of the function and the layer will use corresponding activators.

**elu**
Applies Exponential linear unit.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'elu', input_shape = (784,)))
```

**selu**

Applies Scaled exponential linear unit.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'selu', input_shape = (784,)))
```

**relu**

Applies Rectified Linear Unit.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'relu', input_shape = (784,)))
```

**softmax**

Applies Softmax function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'softmax', input_shape = (784,)))
```

**softplus**

Applies Softplus function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'softplus', input_shape = (784,)))
```

**softsign**

Applies Softsign function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'softsign', input_shape = (784,)))
```

**tanh**

Applies Hyperbolic tangent function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 
model = Sequential() 
model.add(Dense(512, activation = 'tanh', input_shape = (784,)))
```

**sigmoid**

Applies Sigmoid function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'sigmoid', input_shape = (784,)))
```

**hard_sigmoid**

Applies Hard Sigmoid function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'hard_sigmoid', input_shape = (784,)))
```

**exponential**

Applies exponential function.

```python
from keras.models import Sequential 
from keras.layers import Activation, Dense 

model = Sequential() 
model.add(Dense(512, activation = 'exponential', input_shape = (784,)))
```

**Sr.No Layers & Description**

`Dense Layer`

Dense layer is the regular deeply connected neural network layer.

`Dropout Layers`

Dropout is one of the important concept in the machine learning.

`Flatten Layers`

Flatten is used to flatten the input.

`Reshape Layers`

Reshape is used to change the shape of the input.

`Permute Layers`

Permute is also used to change the shape of the input using pattern.

`RepeatVector Layers`

RepeatVector is used to repeat the input for set number, n of times.

`Lambda Layers`

Lambda is used to transform the input data using an expression or function.

`Convolution Layers`

Keras contains a lot of layers for creating Convolution based ANN, popularly called as Convolution Neural Network (CNN).

`Pooling Layer`

It is used to perform max pooling operations on temporal data.

`Locally connected layer`

Locally connected layers are similar to Conv1D layer but the difference is Conv1D layer weights are shared but here weights are unshared.

`Merge Layer`

It is used to merge a list of inputs.

`Embedding Layer`

It performs embedding operations in input layer.