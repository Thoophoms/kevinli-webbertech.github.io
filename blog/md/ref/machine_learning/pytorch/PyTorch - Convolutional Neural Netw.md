# PyTorch - Convolutional Neural Network (CNN)

Deep learning is a division of machine learning and is considered a crucial step taken by researchers in recent decades. The examples of deep learning implementations include applications like **image recognition** and **speech recognition**.
The two important types of deep neural networks are given below −

# Types of Deep Neural Networks

Deep neural networks are a class of machine learning models that have revolutionized the field of artificial intelligence. They are characterized by their deep architectures, consisting of multiple layers of neurons. Among the various types of deep neural networks, two of the most important are:

## 1. Convolutional Neural Networks (CNNs)

Convolutional Neural Networks are primarily used for processing structured grid data, such as images. They are designed to automatically and adaptively learn spatial hierarchies of features through backpropagation by using multiple building blocks, such as convolution layers, pooling layers, and fully connected layers.

**Applications of CNNs:**

- Image recognition
- Object detection
- Facial recognition
- Image segmentation

## 2. Recurrent Neural Networks (RNNs)

Recurrent Neural Networks are designed to recognize patterns in sequences of data, such as time series, spoken language, or written text. RNNs have a unique architecture that enables them to retain information from previous inputs, which makes them particularly powerful for tasks involving sequential data.

**Applications of RNNs:**

- Speech recognition
- Language modeling
- Text generation
- Time series forecasting


# Basic Concepts of Convolutional Neural Networks (CNNs)

Every Convolutional Neural Network (CNN) includes three fundamental concepts:

- **Local Receptive Fields**
- **Convolution**
- **Pooling**

## Local Receptive Fields

Neural Networks utilize spatial correlations that exist within the input data. In each of the consecutive layers of neural networks, only a subset of input neurons is connected to the neurons in the next layer. This specific region is known as the **Local Receptive Field**. It focuses only on the hidden neurons within this field. The hidden neuron processes the input data inside the mentioned field, without being affected by changes outside the specific boundary.

> The diagram representation of generating local receptive fields is mentioned below:

(*Note: Insert the diagram here*)

## Convolution

In the diagram above, we observe that each connection learns a weight associated with a hidden neuron as it moves from one layer to another. Individual neurons shift over time, and this process is referred to as **convolution**.

- The mapping of connections from the input layer to the hidden feature map is defined by **shared weights**, which ensures that the same weights are applied across different parts of the input.
- The bias added in this mapping process is called **shared bias**.

## Pooling

Convolutional Neural Networks use **pooling layers**, which are typically positioned immediately after a convolutional layer. The pooling layer takes the feature map output from the convolutional layers and creates a condensed feature map. Pooling layers help in reducing the spatial dimensions (width and height) of the input while retaining the most important features.

Pooling serves two main purposes:

1. **Reduces the computational complexity** for the upper layers.
2. **Controls overfitting** by providing an abstracted representation of the feature map.





# Implementation of PyTorch Neural Network

## Step 1: Import Necessary Packages

To begin implementing a simple neural network in PyTorch, the first step is to import the necessary packages. These packages include tools for automatic differentiation and neural network operations.

```python
from torch.autograd import Variable
import torch.nn.functional as F
```

## Step 2: Create a Class for the Convolutional Neural Network

In this step, we define a class that represents the Convolutional Neural Network (CNN) using PyTorch. The input batch shape for the network is `(3, 32, 32)`, where `3` corresponds to the number of channels (e.g., RGB for images), and `32x32` is the spatial dimension of the input.

```python
import torch

class SimpleCNN(torch.nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Input channels = 3 (e.g., RGB image), output channels = 18
        self.conv1 = torch.nn.Conv2d(3, 18, kernel_size=3, stride=1, padding=1)
        # Max pooling layer with a 2x2 window and a stride of 2
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        # Fully connected layer: 18 channels with 16x16 feature maps -> 64 features
        self.fc1 = torch.nn.Linear(18 * 16 * 16, 64)
        # Fully connected layer: 64 input features -> 10 output features (for 10 classes)
        self.fc2 = torch.nn.Linear(64, 10)
```
## Step 3: Define the Forward Pass

In this step, we define the forward pass of the Convolutional Neural Network (CNN). The forward method computes the activation of each layer and tracks the changes in the input's dimensions throughout the network.

```python
import torch.nn.functional as F

def forward(self, x):
    # Apply the first convolutional layer followed by ReLU activation
    x = F.relu(self.conv1(x))
    # Apply max pooling, which reduces the spatial dimensions
    x = self.pool(x)
    # Reshape the tensor for the fully connected layer
    x = x.view(-1, 18 * 16 * 16)
    # Apply the first fully connected layer followed by ReLU activation
    x = F.relu(self.fc1(x))
    # Compute the second fully connected layer (no activation here, applied later)
    x = self.fc2(x)
    return x
```





