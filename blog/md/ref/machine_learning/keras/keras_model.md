# KERAS MODELS

Keras model represents the actual neural network model. Keras provides two modes to create the model: simple and easy-to-use Sequential API as well as more flexible and advanced Functional API.


## Sequential

The core idea of Sequential API is simply arranging the Keras layers in a sequential order.

- A ANN model can be created by simply calling `Sequential()` API as specified below:

```python
from keras.models import Sequential 
model = Sequential()
```

### Add Layers

To add a layer, simply create a layer using the Keras layer API and then pass the layer through the `add()` function as specified below:

```python
from keras.models import Sequential 
from keras.layers import Dense

model = Sequential() 
input_layer = Dense(32, input_shape=(8,)) 
model.add(input_layer) 
hidden_layer = Dense(64, activation='relu') 
model.add(hidden_layer) 
output_layer = Dense(8) 
model.add(output_layer)
```

### Access the Model

Keras provides a few methods to get the model information like layers, input data, and output data. They are as follows:

- **`model.layers`** − Returns all the layers of the model as a list.

```python
>>> layers = model.layers 
>>> layers 
[
   <keras.layers.core.Dense object at 0x000002C8C888B8D0>, 
   <keras.layers.core.Dense object at 0x000002C8C888B7B8>, 
   <keras.layers.core.Dense object at 0x000002C8C888B898>
]

- **`model.inputs`** − Returns all the input tensors of the model as a list.

```python
>>> inputs = model.inputs 
>>> inputs 
[<tf.Tensor 'dense_13_input:0' shape=(?, 8) dtype=float32>]

```
- **`model.outputs`** − Returns all the output tensors of the model as a list.

```python
>>> outputs = model.outputs 
>>> outputs 
<tf.Tensor 'dense_15/BiasAdd:0' shape=(?, 8) dtype=float32>]
```

- **`model.get_weights()`** − Returns all the weights as NumPy arrays.

- **`model.set_weights(weight_numpy_array)`** − Sets the weights of the model.

### Serialize the Model

Keras provides methods to serialize the model into an object as well as JSON, and load it again later. They are as follows:

- **`get_config()`** − Returns the model configuration as an object.

## Serialize the Model

Keras provides methods to serialize the model into an object as well as JSON and YAML, and load it again later. They are as follows:

- **`get_config()`** − Returns the model configuration as an object.

    ```python
    config = model.get_config()
    ```

- **`from_config()`** − Accepts the model configuration object as an argument and creates the model accordingly.

    ```python
    new_model = Sequential.from_config(config)
    ```

- **`to_json()`** − Returns the model as a JSON object.

    ```python
    >>> json_string = model.to_json() 
    >>> json_string 
    '{"class_name": "Sequential", "config": {"name": "sequential_10", "layers": [{"class_name": "Dense", "config": {"name": "dense_13", "trainable": true, "batch_input_shape": [null, 8], "dtype": "float32", "units": 32, "activation": "linear", "use_bias": true, "kernel_initializer": {"class_name": "VarianceScaling", "config": {"scale": 1.0, "mode": "fan_avg", "distribution": "uniform", "seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_14", "trainable": true, "dtype": "float32", "units": 64, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "VarianceScaling", "config": {"scale": 1.0, "mode": "fan_avg", "distribution": "uniform", "seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_15", "trainable": true, "dtype": "float32", "units": 8, "activation": "linear", "use_bias": true, "kernel_initializer": {"class_name": "VarianceScaling", "config": {"scale": 1.0, "mode": "fan_avg", "distribution": "uniform", "seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}]}, "keras_version": "2.2.5", "backend": "tensorflow"}'
    ```

- **`model_from_json()`** − Accepts the JSON representation of the model and creates a new model.

    ```python
    from keras.models import model_from_json 
    new_model = model_from_json(json_string)
    ```

- **`to_yaml()`** − Returns the model as a YAML string.

    ```python
    >>> yaml_string = model.to_yaml() 
    >>> yaml_string 
    'backend: tensorflow\nclass_name: Sequential\nconfig:\n layers:\n - class_name: Dense\n config:\n activation: linear\n activity_regularizer: null\n batch_input_shape: !!python/tuple\n - null\n - 8\n bias_constraint: null\n bias_initializer:\n class_name: Zeros\n config: {}\n bias_regularizer: null\n dtype: float32\n kernel_constraint: null\n kernel_initializer:\n class_name: VarianceScaling\n config:\n distribution: uniform\n mode: fan_avg\n scale: 1.0\n seed: null\n kernel_regularizer: null\n name: dense_13\n trainable: true\n units: 32\n use_bias: true\n - class_name: Dense\n config:\n activation: relu\n activity_regularizer: null\n bias_constraint: null\n bias_initializer:\n class_name: Zeros\n config: {}\n bias_regularizer: null\n dtype: float32\n kernel_constraint: null\n kernel_initializer:\n class_name: VarianceScaling\n config:\n distribution: uniform\n mode: fan_avg\n scale: 1.0\n seed: null\n kernel_regularizer: null\n name: dense_14\n trainable: true\n units: 64\n use_bias: true\n - class_name: Dense\n config:\n activation: linear\n activity_regularizer: null\n bias_constraint: null\n bias_initializer:\n class_name: Zeros\n config: {}\n bias_regularizer: null\n dtype: float32\n kernel_constraint: null\n kernel_initializer:\n class_name: VarianceScaling\n config:\n distribution: uniform\n mode: fan_avg\n scale: 1.0\n seed: null\n kernel_regularizer: null\n name: dense_15\n trainable: true\n units: 8\n use_bias: true\n name: sequential_10\nkeras_version: 2.2.5\n'
    ```

- **`model_from_yaml()`** − Accepts the YAML representation of the model and creates a new model.

    ```python
    from keras.models import model_from_yaml 
    new_model = model_from_yaml(yaml_string)
    ```

### Summarize the Model

Understanding the model is a crucial phase to properly use it for training and prediction purposes. Keras provides a simple method, `summary()`, to get the full information about the model and its layers.

A summary of the model created in the previous section is as follows:

```python
>>> model.summary()
Model: "sequential_10"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_13 (Dense)             (None, 32)                288       
_________________________________________________________________
dense_14 (Dense)             (None, 64)                2112      
_________________________________________________________________
dense_15 (Dense)             (None, 8)                 520       
=================================================================
Total params: 2,920
Trainable params: 2,920
Non-trainable params: 0
_________________________________________________________________
```
### Train and Predict the Model

The model provides functions for training, evaluation, and prediction processes. They are as follows:

- **`compile`**: Configure the learning process of the model.
- **`fit`**: Train the model using the training data.
- **`evaluate`**: Evaluate the model using the test data.
- **`predict`**: Predict the results for new input.



## Functional API

The Sequential API is used to create models layer-by-layer. The Functional API is an alternative approach for creating more complex models. With the Functional API, you can define multiple inputs or outputs that share layers. 

In this approach, you first create an instance of the model and then connect the layers to define the inputs and outputs of the model. This section provides a brief explanation of the Functional API.


### Create a Model

To create a model using the Functional API, follow these steps:

1. Import the input layer using the following module:

    ```python
    from keras.layers import Input
    ```

2. Create an input layer by specifying the input dimension shape for the model using the following code:

    ```python
    data = Input(shape=(2, 3))
    ```


### Define Layer for the Input

To define a layer for the input, follow these steps:

1. Import the `Dense` layer using the following module:

    ```python
    from keras.layers import Dense
    ```

2. Add a `Dense` layer to the input using the following line of code:

    ```python
    layer = Dense(2)(data)
    ```

3. Print the layer to see its details:

    ```python
    print(layer)
    ```

   Output:

    ```
    Tensor("dense_1/add:0", shape=(?, 2, 2), dtype=float32)
    ```


### Define Model

To define a model, use the following module:

```python
from keras.models import Model
```

### Create a Functional Model

To create a model in a functional way by specifying both the input and output layers, use the following code:

```python
model = Model(inputs=data, outputs=layer)
```
## Complete Code to Create a Simple Model

The complete code to create a simple model is shown below:

```python
from keras.layers import Input
from keras.models import Model
from keras.layers import Dense

# Define the input layer
data = Input(shape=(2, 3))

# Define the Dense layer
layer = Dense(2)(data)

# Create the model
model = Model(inputs=data, outputs=layer)

# Print the model summary
model.summary()

_________________________________________________________________
Layer (type)               Output Shape               Param #   
=================================================================
input_2 (InputLayer)       (None, 2, 3)               0         
_________________________________________________________________
dense_2 (Dense)            (None, 2, 2)               8         
=================================================================
Total params: 8
Trainable params: 8
Non-trainable params: 0
_________________________________________________________________
_________________________________________________________________
Layer (type)               Output Shape               Param #   
=================================================================
input_2 (InputLayer)       (None, 2, 3)               0         
_________________________________________________________________
dense_2 (Dense)            (None, 2, 2)               8         
=================================================================
Total params: 8
Trainable params: 8
Non-trainable params: 0
_________________________________________________________________
```

