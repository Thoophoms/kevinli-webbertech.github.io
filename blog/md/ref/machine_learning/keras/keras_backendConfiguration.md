# Keras Backend Configuration

Even thought Tensorflow integrates Keras lately, but Keras can configure different backend libraries, 
TensorFlow or Theano.

## TensorFlow

`pip install  TensorFlow`

Once we execute keras, we could see the configuration file is located at your home directory inside and go to .keras/keras.json.

*keras.json*

```python
{ 
   "image_data_format": "channels_last", 
   "epsilon": 1e-07, 
   "floatx": "float32", 
   "backend": "tensorflow" 
}
```

image_data_format represent the data format.

* epsilon represents numeric constant. It is used to avoid DivideByZero error.

* floatx represent the default data type float32. You can also change it to float16 or float64 using set_floatx() method.

* image_data_format represent the data format.

Suppose, if the file is not created then move to the location and create using the below steps −

```shell
> cd home 
> mkdir .keras 
> vi keras.json
```

Remember, you should specify .keras as its folder name and add the above configuration inside keras.json file. We can perform some pre-defined operations to know backend functions.

## Theano

`pip install theano`

to change the backend to theano

*keras.json*

```json
{ 
   "image_data_format": "channels_last", 
   "epsilon": 1e-07, 
   "floatx": "float32", 
   "backend": "theano" 
}
```

Now save your file, restart your terminal and start keras, your backend will be changed.

```python
>>> import keras as k 
```
using theano backend.
