# Feature Extraction in Convolutional Neural Networks (CNNs)

Convolutional Neural Networks (CNNs) are particularly powerful for feature extraction from images. They automatically learn to extract hierarchical features that are crucial for tasks such as image classification, object detection, and more.

## Step 1: Import Necessary Libraries and Models

To create a feature extraction model using PyTorch, the first step is to import the necessary libraries and pre-trained models from the `torchvision` library.

```python
import torch
import torch.nn as nn
from torchvision import models
```
## Step 2: Create a Feature Extractor Class

In this step, we create a class for feature extraction, which can be utilized as needed during the network's forward pass. The feature extractor will capture the output from specified layers in the CNN.

```python
import torch
import torch.nn as nn

# Define the Feature Extractor class
class Feature_extractor(nn.Module):
    def forward(self, input):
        self.feature = input.clone()
        return input

# Initialize the new network and move it to GPU (if available)
new_net = nn.Sequential().cuda()

# Specify the layers from which you want to extract features
target_layers = ["conv_1", "conv_2", "conv_4"]

# Iterate over the layers of the original CNN
i = 1
for layer in list(cnn):
    if isinstance(layer, nn.Conv2d):
        name = "conv_" + str(i)
        new_net.add_module(name, layer)
        if name in target_layers:
            # Insert the feature extractor after the target layer
            new_net.add_module("extractor_" + str(i), Feature_extractor())
        i += 1
    elif isinstance(layer, nn.ReLU):
        name = "relu_" + str(i)
        new_net.add_module(name, layer)
    elif isinstance(layer, nn.MaxPool2d):
        name = "pool_" + str(i)
        new_net.add_module(name, layer)

# Forward pass with the image through the new network
new_net.forward(your_image)

# Print the extracted features from the specified layer
print(new_net.extractor_3.feature)
```

# PyTorch - Visualization of Convolutional Neural Networks (CNNs)

Visualization is a powerful tool for understanding and interpreting the inner workings of Convolutional Neural Networks (CNNs). This process helps to inspect what the network is learning at each layer and how it is transforming the input data.

## Step 1: Import Necessary Modules

To begin the visualization of CNNs, you need to import several essential modules, including those for handling data, performing computations, and building models.

```python
import os
import numpy as np
import pandas as pd
from scipy.misc import imread
from sklearn.metrics import accuracy_score

import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten, Activation, Input
from keras.layers import Conv2D, MaxPooling2D

import torch
```
## Step 2: Load and Prepare the Dataset

To ensure consistency in training and testing, it's essential to control potential randomness. In this step, we'll load the dataset and prepare it for visualization.

```python
# Set a seed to ensure reproducibility
seed = 128
rng = np.random.RandomState(seed)

# Define the directory where the dataset is located
data_dir = "../../datasets/MNIST"

# Load the training and testing datasets
train = pd.read_csv('../../datasets/MNIST/train.csv')
test = pd.read_csv('../../datasets/MNIST/Test_fCbTej3.csv')

# Randomly select an image from the training dataset
img_name = rng.choice(train.filename)

# Construct the file path to the selected image
filepath = os.path.join(data_dir, 'train', img_name)

# Load the image and flatten it into a 2D array
img = imread(filepath, flatten=True)
```



## Step 3: Plot the Images

To verify that the training and testing data are correctly loaded and represented, you can visualize some images. This step will help ensure that the images are properly formatted and suitable for training and testing your model.

```python
import pylab

# Display the image using matplotlib
pylab.imshow(img, cmap='gray')
pylab.axis('off')  # Hide the axis for better visualization
pylab.show()       # Show the image
```
