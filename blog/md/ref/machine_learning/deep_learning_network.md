## Deep Learning CNN Implementation

## Part I Build CNN from Scratch

To understand the CNN better with the mathematica and algorithms behind it, let us implement a few simple CNN using Numpy.

## One hidden layer CNN Impl

To implement a simple deep learning neural network in Python using the sigmoid activation function, you can use libraries such as `numpy` for the mathematical operations. Below is a basic implementation of a feedforward neural network with one hidden layer:

```python
import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights randomly with mean 0
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_input_hidden = np.random.uniform(-1, 1, (self.input_size, self.hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, (self.hidden_size, self.output_size))
        
        # Initialize biases
        self.bias_hidden = np.random.uniform(-1, 1, (1, self.hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (1, self.output_size))

    def feedforward(self, X):
        # Calculate the hidden layer activations
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        
        # Calculate the output layer activations
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        
        return self.final_output

    def backpropagate(self, X, y, learning_rate=0.1):
        # Compute the error at the output layer
        output_error = y - self.final_output
        output_delta = output_error * sigmoid_derivative(self.final_output)
        
        # Compute the error at the hidden layer
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)
        
        # Update the weights and biases
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs=10000, learning_rate=0.1):
        for epoch in range(epochs):
            self.feedforward(X)
            self.backpropagate(X, y, learning_rate)

# Example usage
if __name__ == "__main__":
    # Sample training data (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    y = np.array([[0], [1], [1], [0]])

    # Create and train the neural network
    nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the neural network
    output = nn.feedforward(X)
    print("Predicted Output:")
    print(output)
```

### Breakdown of the Code

1. **Sigmoid Activation Function**: The `sigmoid` function maps inputs to values between 0 and 1, which is useful for binary classification problems. The derivative of the sigmoid function is needed for backpropagation.

2. **Neural Network Class**:
   - The class `NeuralNetwork` contains methods for initializing the network, performing forward propagation (`feedforward`), and updating the weights using backpropagation (`backpropagate`).

3. **Feedforward Process**:
   - The input data is passed through the network, which computes activations for the hidden and output layers.

4. **Backpropagation Process**:
   - After computing the output, the error is propagated back to adjust the weights and biases using the derivative of the sigmoid function.

5. **Training**:
   - The `train` method runs the backpropagation process for a specified number of epochs, updating the weights after each iteration.

6. **Example**:
   - The example in the `if __name__ == "__main__":` block demonstrates how to train the neural network to solve a simple XOR problem.

### Notes

- This is a basic implementation of a neural network. In practice, you would use libraries like TensorFlow or PyTorch for large-scale and more efficient training of neural networks.

## Two hidden layer CNN Impl

```python
import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class with two hidden layers
class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        # Initialize weights randomly with mean 0
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.output_size = output_size
        
        # Initialize weights for both hidden layers and the output layer
        self.weights_input_hidden1 = np.random.uniform(-1, 1, (self.input_size, self.hidden_size1))
        self.weights_hidden1_hidden2 = np.random.uniform(-1, 1, (self.hidden_size1, self.hidden_size2))
        self.weights_hidden2_output = np.random.uniform(-1, 1, (self.hidden_size2, self.output_size))
        
        # Initialize biases
        self.bias_hidden1 = np.random.uniform(-1, 1, (1, self.hidden_size1))
        self.bias_hidden2 = np.random.uniform(-1, 1, (1, self.hidden_size2))
        self.bias_output = np.random.uniform(-1, 1, (1, self.output_size))

    def feedforward(self, X):
        # Calculate the first hidden layer activations
        self.hidden1_input = np.dot(X, self.weights_input_hidden1) + self.bias_hidden1
        self.hidden1_output = sigmoid(self.hidden1_input)
        
        # Calculate the second hidden layer activations
        self.hidden2_input = np.dot(self.hidden1_output, self.weights_hidden1_hidden2) + self.bias_hidden2
        self.hidden2_output = sigmoid(self.hidden2_input)
        
        # Calculate the output layer activations
        self.final_input = np.dot(self.hidden2_output, self.weights_hidden2_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        
        return self.final_output

    def backpropagate(self, X, y, learning_rate=0.1):
        # Compute the error at the output layer
        output_error = y - self.final_output
        output_delta = output_error * sigmoid_derivative(self.final_output)
        
        # Compute the error at the second hidden layer
        hidden2_error = output_delta.dot(self.weights_hidden2_output.T)
        hidden2_delta = hidden2_error * sigmoid_derivative(self.hidden2_output)
        
        # Compute the error at the first hidden layer
        hidden1_error = hidden2_delta.dot(self.weights_hidden1_hidden2.T)
        hidden1_delta = hidden1_error * sigmoid_derivative(self.hidden1_output)
        
        # Update the weights and biases
        self.weights_input_hidden1 += X.T.dot(hidden1_delta) * learning_rate
        self.weights_hidden1_hidden2 += self.hidden1_output.T.dot(hidden2_delta) * learning_rate
        self.weights_hidden2_output += self.hidden2_output.T.dot(output_delta) * learning_rate
        self.bias_hidden1 += np.sum(hidden1_delta, axis=0, keepdims=True) * learning_rate
        self.bias_hidden2 += np.sum(hidden2_delta, axis=0, keepdims=True) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs=10000, learning_rate=0.1):
        for epoch in range(epochs):
            self.feedforward(X)
            self.backpropagate(X, y, learning_rate)

# Example usage
if __name__ == "__main__":
    # Sample training data (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    
    y = np.array([[0], [1], [1], [0]])

    # Create and train the neural network
    nn = NeuralNetwork(input_size=2, hidden_size1=4, hidden_size2=4, output_size=1)
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the neural network
    output = nn.feedforward(X)
    print("Predicted Output:")
    print(output)
```

### Breakdown of Changes

1. **Two Hidden Layers**:
   - The network now has two hidden layers: `hidden_size1` for the first hidden layer and `hidden_size2` for the second hidden layer.
   - We initialize weights for both layers: `weights_input_hidden1`, `weights_hidden1_hidden2`, and `weights_hidden2_output`.
   - Similarly, we have biases for both hidden layers (`bias_hidden1` and `bias_hidden2`) and the output layer (`bias_output`).

2. **Feedforward Method**:
   - First, the input is passed through the first hidden layer and then through the second hidden layer before reaching the output layer.
   
3. **Backpropagation Method**:
   - The error is propagated backward from the output layer to the second hidden layer, then to the first hidden layer, and the weights and biases are updated accordingly.

4. **Training Method**:
   - The network is trained in the same way as before, but with the updated architecture (two hidden layers).

### Example Usage

- The XOR problem is used as an example, where the network is trained with inputs `[0, 0], [0, 1], [1, 0], [1, 1]` and the corresponding target outputs `[0], [1], [1], [0]`.
- The network is trained for 10,000 epochs, and the predicted output is displayed at the end.

This code demonstrates how to extend the original neural network by adding another hidden layer, making the network more capable of handling more complex problems.

## Part II Using Frameworks to build a CNN

## Use Tensorflow to build CNN

Below is a basic implementation of a Convolutional Neural Network (CNN) using TensorFlow and Keras. We'll build a simple CNN model to classify images, such as those from the MNIST dataset, which consists of handwritten digits (0-9). This code uses TensorFlow 2.x, which includes Keras as its high-level API.

### Steps

1. Import necessary libraries.
2. Load and preprocess the MNIST dataset.
3. Build the CNN model.
4. Compile the model.
5. Train the model.
6. Evaluate the model.

### Full Implementation of CNN Using TensorFlow

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# 1. Load and preprocess the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshape the data to include the color channel (grayscale images have 1 channel)
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255

# One-hot encode the labels
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. Build the CNN model
model = models.Sequential()

# Convolutional Layer 1: 32 filters, kernel size 3x3, ReLU activation
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# Max Pooling Layer 1: Pooling size 2x2
model.add(layers.MaxPooling2D((2, 2)))

# Convolutional Layer 2: 64 filters, kernel size 3x3, ReLU activation
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Max Pooling Layer 2: Pooling size 2x2
model.add(layers.MaxPooling2D((2, 2)))

# Flatten the 3D output to 1D
model.add(layers.Flatten())

# Fully connected (dense) layer with 128 neurons and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Output layer: 10 neurons (for 10 classes) with softmax activation
model.add(layers.Dense(10, activation='softmax'))

# 3. Compile the model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 4. Train the model
model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2)

# 5. Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
```

### Explanation

1. **Dataset Loading and Preprocessing**
   - The MNIST dataset is loaded using `tensorflow.keras.datasets.mnist`. The training and test sets are divided into images and labels.
   - Images are reshaped to have a channel dimension (`28x28x1`), indicating a grayscale image.
   - The pixel values are scaled between 0 and 1 by dividing by 255.
   - Labels are one-hot encoded to create a binary matrix for classification.

2. **CNN Architecture**
   - **Conv2D**: This is a convolutional layer that applies 2D convolutions to the input data (e.g., images). It uses filters (kernels) to extract features from the image. The `relu` activation function is used after each convolution to introduce non-linearity.
   - **MaxPooling2D**: This layer reduces the spatial dimensions (height and width) by applying a max pooling operation. It helps to reduce computational load and capture the most important features.
   - **Flatten**: After the convolutional and pooling layers, we flatten the 3D output into a 1D vector to feed it into fully connected layers.
   - **Dense**: Fully connected layers are added for classification. The last layer has 10 neurons corresponding to the 10 classes, and we use the `softmax` activation to output a probability distribution for each class.

3. **Model Compilation**
   - The model is compiled using the `Adam` optimizer, which is efficient for training deep learning models. The `categorical_crossentropy` loss function is used because it's a multi-class classification problem.
   - The model's accuracy is tracked during training and evaluation.

4. **Training**
   - The model is trained for 5 epochs with a batch size of 64. We use a validation split of 20% to monitor performance on a validation set during training.

5. **Evaluation**
   - The model is evaluated on the test set using the `evaluate()` method, and the test accuracy is printed.

### Output

After training, you should see output similar to this:

```shell
Epoch 1/5
750/750 [==============================] - 12s 16ms/step - loss: 0.1853 - accuracy: 0.9441 - val_loss: 0.0618 - val_accuracy: 0.9810
Epoch 2/5
750/750 [==============================] - 12s 16ms/step - loss: 0.0484 - accuracy: 0.9857 - val_loss: 0.0414 - val_accuracy: 0.9871
...
Test accuracy: 0.9910
```

This shows the loss and accuracy on both the training and validation data at each epoch, and the final test accuracy.

### Notes

- The above model is quite simple and can be extended to more complex CNN architectures for larger or more complex datasets (e.g., CIFAR-10, ImageNet).

- You can modify the number of convolutional layers, their filters, kernel sizes, pooling layers, etc., to improve model performance or adapt it to different tasks.

## Use Pytorch to build CNN

Certainly! Below is an implementation of a Convolutional Neural Network (CNN) using **PyTorch**. We will use the **MNIST dataset** for this example, similar to the TensorFlow example, to classify handwritten digits (0-9).

### Steps

1. Import necessary libraries.
2. Load and preprocess the MNIST dataset.
3. Define the CNN model.
4. Define the loss function and optimizer.
5. Train the model.
6. Evaluate the model.

### Full Implementation of CNN Using PyTorch

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 1. Load and preprocess the MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Load the training and testing datasets
train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# DataLoader for batching the data
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 2. Define the CNN model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        
        # Convolutional Layer 1: 1 input channel (grayscale), 32 output channels, 3x3 kernel
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 2)
        
        # Convolutional Layer 2: 32 input channels, 64 output channels, 3x3 kernel
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2, 2)
        
        # Fully Connected Layer 1
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.relu3 = nn.ReLU()
        
        # Fully Connected Layer 2 (Output layer)
        self.fc2 = nn.Linear(128, 10)  # 10 classes (digits 0-9)
    
    def forward(self, x):
        # Forward pass through convolutional layers
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        
        # Flatten the output of the last pooling layer
        x = x.view(-1, 64 * 7 * 7)
        
        # Forward pass through fully connected layers
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        
        return x

# 3. Initialize the model, loss function, and optimizer
model = CNN()

# Loss function (Cross Entropy Loss for classification)
criterion = nn.CrossEntropyLoss()

# Optimizer (Adam optimizer)
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Train the model
def train_model(model, train_loader, criterion, optimizer, epochs=5):
    model.train()
    
    for epoch in range(epochs):
        running_loss = 0.0
        for images, labels in train_loader:
            # Zero the parameter gradients
            optimizer.zero_grad()
            
            # Forward pass
            outputs = model(images)
            
            # Compute the loss
            loss = criterion(outputs, labels)
            
            # Backward pass and optimization
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}")

# 5. Evaluate the model
def evaluate_model(model, test_loader):
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for images, labels in test_loader:
            # Forward pass
            outputs = model(images)
            
            # Get predicted labels
            _, predicted = torch.max(outputs, 1)
            
            # Count correct predictions
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy = 100 * correct / total
    print(f"Test Accuracy: {accuracy:.2f}%")

# Train and evaluate the model
train_model(model, train_loader, criterion, optimizer, epochs=5)
evaluate_model(model, test_loader)
```

### Explanation

1. **Dataset Loading and Preprocessing**:
   - We load the MNIST dataset using `torchvision.datasets.MNIST`. The dataset is transformed using `transforms.ToTensor()` to convert images to PyTorch tensors, and `transforms.Normalize()` normalizes the pixel values to a range of -1 to 1.
   - We use `DataLoader` to create batches and shuffle the training data.

2. **Model Definition**:
   - The model is defined as a class `CNN` that inherits from `nn.Module`. It includes two convolutional layers (`conv1`, `conv2`), each followed by ReLU activation (`relu1`, `relu2`) and max-pooling (`pool1`, `pool2`).
   - After the convolutional layers, we flatten the output to feed it into fully connected layers (`fc1` and `fc2`), where `fc2` has 10 output units corresponding to the 10 digits (0-9).

3. **Loss Function and Optimizer**:
   - The `CrossEntropyLoss` function is used for multi-class classification.
   - The `Adam` optimizer is chosen for its efficiency and is set to learn the model parameters.

4. **Training Loop**:
   - The training loop iterates over the dataset for a specified number of epochs (5 in this case).
   - For each batch, the model performs a forward pass, the loss is computed, and gradients are backpropagated to update the model's weights.

5. **Evaluation**:
   - After training, the model is evaluated on the test dataset to calculate the accuracy by comparing predicted labels with the actual labels.

### Output

During training, you will see loss values printed for each epoch. After training, the test accuracy will be printed:

```shell
Epoch 1/5, Loss: 0.2154
Epoch 2/5, Loss: 0.0593
Epoch 3/5, Loss: 0.0380
Epoch 4/5, Loss: 0.0273
Epoch 5/5, Loss: 0.0197
Test Accuracy: 98.60%
```

### Notes

- This is a simple CNN model. You can experiment by adding more convolutional layers, changing the filter sizes, or adding dropout layers to prevent overfitting.

- You can also try training on different datasets, like CIFAR-10, to extend this model's capabilities.

- PyTorch's dynamic computation graph allows you to easily modify the model and experiment with different architectures.

## Comparing Tensorflow and PyTorch

Both **TensorFlow** and **PyTorch** are powerful deep learning frameworks that are widely used in the machine learning and artificial intelligence community. Each has its own strengths and weaknesses, making them more suitable for different use cases. Below is a comparison of TensorFlow and PyTorch, highlighting their **pros** and **cons**.

---

### **TensorFlow**:
**Pros**:
1. **Mature and Stable**: TensorFlow has been around since 2015, and over the years, it has become a very stable and mature framework. It’s widely adopted in production environments, particularly in large-scale systems.
   
2. **Ecosystem**: TensorFlow has a rich ecosystem, including libraries like `Keras` (high-level API), `TensorFlow Lite` (for mobile and embedded devices), `TensorFlow.js` (for running models in the browser), and `TensorFlow Extended (TFX)` (for production pipelines).
   
3. **Scalability**: TensorFlow is designed for scaling. It supports distributed training and large-scale machine learning models efficiently. TensorFlow’s `TF Distributed` allows you to scale models across multiple GPUs or machines seamlessly.
   
4. **Deployment and Production**: TensorFlow offers strong deployment options, such as TensorFlow Serving (for serving models), TensorFlow Lite (for mobile), and TensorFlow.js (for web applications). It’s well-suited for production environments and is often preferred in industries requiring model deployment at scale.
   
5. **Graph-based Computation (Static Computation Graph)**: TensorFlow uses a static computation graph, which allows for optimizations, such as graph pruning, that make it highly efficient in terms of execution. TensorFlow also supports optimizing models for inference, which can be beneficial when working on production systems.

6. **TensorFlow 2.0**: In 2019, TensorFlow released TensorFlow 2.0, which made the framework more user-friendly by incorporating Keras as its high-level API and emphasizing eager execution (dynamic computation graph).

**Cons**:
1. **Steeper Learning Curve**: Although TensorFlow 2.0 improved the user experience, it still has a steeper learning curve compared to PyTorch, especially for beginners. The static computation graph model can make debugging and development less intuitive.
   
2. **Verbose Syntax**: TensorFlow, prior to TensorFlow 2.0, was often criticized for its verbose and complex syntax. While TensorFlow 2.0 improved this with Keras integration, it’s still not as easy to use as PyTorch for some tasks.

3. **Less Pythonic**: TensorFlow is often considered less "Pythonic" than PyTorch, meaning it feels more like a specialized library and less like an extension of the Python language. Some developers find it harder to debug and prototype in TensorFlow compared to PyTorch.

4. **Slower Development Cycle**: Because TensorFlow focuses a lot on stability and production readiness, new features might take longer to appear in TensorFlow as compared to PyTorch, which is more agile in terms of rapid prototyping.

---

### **PyTorch**:
**Pros**:
1. **Dynamic Computation Graph (Eager Execution)**: PyTorch uses a dynamic computation graph, meaning the graph is built on the fly as operations are executed. This makes it easier to work with and more intuitive for beginners. It allows for flexible model design, debugging, and prototyping.
   
2. **Pythonic and Intuitive**: PyTorch feels like an extension of Python. It is much more "Pythonic" than TensorFlow, making it easier for Python developers to learn and use. Debugging is straightforward because the execution model is similar to regular Python code.
   
3. **Excellent for Research and Prototyping**: PyTorch is favored in academic research and by people working on new models and techniques. Its dynamic graph makes it great for experimentation and rapid prototyping.
   
4. **Seamless Integration with Python**: Since PyTorch is designed to be a deep learning library for Python, it integrates seamlessly with Python tools and libraries, such as NumPy, SciPy, and scikit-learn.
   
5. **Better Debugging Support**: Due to its dynamic graph, debugging with PyTorch is straightforward and intuitive. You can use Python’s built-in debugging tools (like `pdb`) directly, which makes finding and fixing issues easier.

6. **Active Community and Rapid Development**: PyTorch has a vibrant community, and its development cycle is very fast. New features and updates are often rolled out quickly.

**Cons**:
1. **Limited Ecosystem**: Although PyTorch has been making strides in its ecosystem, it is still behind TensorFlow in terms of available production tools. For example, while TensorFlow has robust support for mobile deployment, PyTorch is still catching up in this area.
   
2. **Deployment Challenges**: Although PyTorch has added support for deployment through tools like `TorchServe`, it is still not as mature or optimized for large-scale production systems as TensorFlow. PyTorch is often used in research, but TensorFlow is more common in production.

3. **Slower Performance in Some Cases**: In certain scenarios (e.g., distributed training, large-scale model training), TensorFlow’s optimizations for production may offer better performance than PyTorch, especially in TensorFlow 2.0's optimized static graph.
   
4. **Less Support for Mobile and Embedded Devices**: While PyTorch does offer solutions like `TorchScript` for exporting models and using them in production, TensorFlow's `TensorFlow Lite` is much more mature for deploying models on mobile and embedded devices.

---

### **Summary Table:**

| Feature                     | TensorFlow                             | PyTorch                                 |
|-----------------------------|----------------------------------------|-----------------------------------------|
| **Ease of Use**             | Steeper learning curve, especially pre-TF 2.0 | More intuitive and Pythonic             |
| **Computation Graph**       | Static graph (TensorFlow 1.x), Dynamic graph (TensorFlow 2.0) | Dynamic computation graph (eager execution) |
| **Prototyping & Flexibility** | Slower prototyping, more suitable for production | Great for prototyping and experimentation |
| **Deployment**              | Robust production tools (TensorFlow Serving, TensorFlow Lite, etc.) | Limited production tools, but improving with TorchServe |
| **Performance**             | Often optimized for production workloads | May be slower in large-scale systems, but improving |
| **Community & Research**    | Large community, widely used in industry | Preferred by researchers, very active community |
| **Mobile & Embedded**       | Excellent support (TensorFlow Lite)    | Limited support (but improving)         |
| **Support for Other Languages** | Excellent support for languages like C++, Java, and JavaScript | Primarily focused on Python            |

---

### **Which Should You Choose?**

- **If you’re a researcher** or someone who needs flexibility and a fast development cycle for experimentation, **PyTorch** is usually the better choice. Its dynamic nature and ease of debugging make it great for prototyping new algorithms or models.
  
- **If you’re working on a large-scale production system** that requires optimized deployment, scalability, and an established ecosystem, **TensorFlow** might be the better choice. TensorFlow is highly optimized for deployment and often preferred in industries that require scaling and cross-platform support.

- **For mobile or edge deployment**, TensorFlow is more mature, but PyTorch is catching up with tools like `TorchServe` and `TorchScript`.

In conclusion, both frameworks are excellent choices, and the best one depends on your use case, with TensorFlow excelling in production and PyTorch being more suited for research and rapid prototyping.


## Ref of Githubs

- https://github.com/ashishpatel26/Andrew-NG-Notes/blob/master/andrewng-p-1-neural-network-deep-learning.md
- https://github.com/amanchadha/coursera-deep-learning-specialization