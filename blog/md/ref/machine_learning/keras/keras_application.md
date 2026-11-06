# Using Keras Applications for Pre-trained Models

Keras applications module is used to provide pre-trained models for deep neural networks.

## Pre-trained Models

A pre-trained model consists of two parts:
- **Model Architecture**
- **Model Weights**

Some of the popular pre-trained models are:
- ResNet
- VGG16
- MobileNet
- InceptionResNetV2
- InceptionV3

## Loading a Model

```python
import keras
import numpy as np
from keras.applications import vgg16, inception_v3, resnet50, mobilenet

# Load the VGG16 model
vgg_model = vgg16.VGG16(weights='imagenet')

# Load the InceptionV3 model
inception_model = inception_v3.InceptionV3(weights='imagenet')

# Load the ResNet50 model
resnet_model = resnet50.ResNet50(weights='imagenet')

# Load the MobileNet model
mobilenet_model = mobilenet.MobileNet(weights='imagenet')


