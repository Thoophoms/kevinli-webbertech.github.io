## **ResNet Pre-Trained Model**

The ResNet model is a pre-trained model that has been trained using ImageNet. You can load the ResNet50 model with the following syntax:

```python
keras.applications.resnet.ResNet50(
    include_top=True, 
    weights='imagenet', 
    input_tensor=None, 
    input_shape=None, 
    pooling=None, 
    classes=1000
)

### Parameter Descriptions

- **`include_top`**: Refers to the fully-connected layer at the top of the network.

- **`weights`**: Refers to pre-training on ImageNet.

- **`input_tensor`**: Refers to an optional Keras tensor to use as image input for the model.

- **`input_shape`**: Refers to an optional shape tuple. The default input size for this model is 224x224.

- **`classes`**: Refers to the optional number of classes to classify images.

### Step 1: Import the Modules

```python
import PIL
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
import numpy as np
from keras.applications.resnet50 import ResNet50
from keras.applications import resnet50

### Step 2: Select an Input

```python
filename = 'banana.jpg' 

# Load an image in PIL format
original = load_img(filename, target_size=(224, 224)) 
print('PIL image size', original.size)

# Display the image
plt.imshow(original) 
plt.show()

### Step 3: Convert Images into NumPy Array

```python
# Convert the PIL image to a NumPy array
numpy_image = img_to_array(original) 

# Display the NumPy image
plt.imshow(np.uint8(numpy_image)) 
plt.show()

print('numpy array size', numpy_image.shape) 
# Output: numpy array size (224, 224, 3)

# Convert the image/images into batch format
image_batch = np.expand_dims(numpy_image, axis=0) 

print('image batch size', image_batch.shape) 
# Output: image batch size (1, 224, 224, 3)

### Step 4: Model Prediction

```python
# Prepare the image for the ResNet50 model
processed_image = resnet50.preprocess_input(image_batch.copy()) 

# Create ResNet50 model with pre-trained weights
resnet_model = resnet50.ResNet50(weights='imagenet') 
# Output: Downloading data from https://github.com/fchollet/deep-learning-models/releases/download/v0.2/resnet50_weights_tf_dim_ordering_tf_kernels.h5
# 102858752/102853048 [==============================] - 33s 0us/step 

# Get the predicted probabilities for each class
predictions = resnet_model.predict(processed_image) 

# Convert the probabilities to class labels
label = decode_predictions(predictions) 
# Output: Downloading data from https://storage.googleapis.com/download.tensorflow.org/data/imagenet_class_index.json 
# 40960/35363 [==================================] - 0s 0us/step 

print(label)


### Output

```python
[
   [
      ('n07753592', 'banana', 0.99229723), 
      ('n03532672', 'hook', 0.0014551596), 
      ('n03970156', 'plunger', 0.0010738898), 
      ('n07753113', 'fig', 0.0009359837), 
      ('n03109150', 'corkscrew', 0.00028538404)
   ]
]



Here, the model predicted the image as a `banana` correctly.
