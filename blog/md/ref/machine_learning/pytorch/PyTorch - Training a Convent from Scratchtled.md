# Training a Convent from Scratch

This involves creating a convolutional network or sample neural network with PyTorch.

## Step 1: Create the Neural Network Class

Define a class with the necessary parameters. The parameters include weights initialized with random values.

```python
import torch
import torch.nn as nn

class Neural_Network(nn.Module):
    def __init__(self):
        super(Neural_Network, self).__init__()
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        
        # Initialize weights
        self.W1 = torch.randn(self.inputSize, self.hiddenSize)  # 3 x 2 tensor
        self.W2 = torch.randn(self.hiddenSize, self.outputSize)  # 3 x 1 tensor

    def forward(self, x):
        # Define the forward pass (for demonstration purposes)
        pass
```
## Step 2: Create the Feed Forward Pattern

Define a feed-forward pattern function using sigmoid activation functions, and implement the backward pass for gradient computation.

```python
import torch
import torch.nn as nn

class Neural_Network(nn.Module):
    def __init__(self):
        super(Neural_Network, self).__init__()
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        
        # Initialize weights
        self.W1 = torch.randn(self.inputSize, self.hiddenSize)  # 2 x 3 tensor
        self.W2 = torch.randn(self.hiddenSize, self.outputSize)  # 3 x 1 tensor

    def forward(self, X):
        self.z = torch.matmul(X, self.W1)  # Matrix multiplication
        self.z2 = self.sigmoid(self.z)  # Apply sigmoid activation function
        self.z3 = torch.matmul(self.z2, self.W2)  # Matrix multiplication
        o = self.sigmoid(self.z3)  # Apply final activation function
        return o

    def sigmoid(self, s):
        return 1 / (1 + torch.exp(-s))

    def sigmoidPrime(self, s):
        # Derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        self.o_error = y - o  # Error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o)  # Derivative of sigmoid to error
        self.z2_error = torch.matmul(self.o_delta, torch.t(self.W2))
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += torch.matmul(torch.t(X), self.z2_delta)  # Update weights W1
        self.W2 += torch.matmul(torch.t(self.z2), self.o_delta)  # Update weights W2
```
## Step 3: Create a Training and Prediction Model

Define the training function, save the model weights, and implement a prediction method.

```python
class Neural_Network(nn.Module):
    # Other methods (init, forward, backward, etc.) go here

    def train(self, X, y):
        # Forward and backward pass for training
        o = self.forward(X)
        self.backward(X, y, o)
        
    def saveWeights(self, model):
        # Implement PyTorch internal storage functions
        torch.save(model.state_dict(), "NN_weights.pth")
        # You can reload the model with all the weights using:
        # model.load_state_dict(torch.load("NN_weights.pth"))
        
    def predict(self, xPredicted):
        print("Predicted data based on trained weights:")
        print("Input (scaled): \n" + str(xPredicted))
        print("Output: \n" + str(self.forward(xPredicted)))
```
