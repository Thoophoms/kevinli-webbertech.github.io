# Neural Networks

## Principle of Neural Network

A neural network is composed of a collection of basic elements known as artificial neurons or perceptrons. Each neuron processes inputs to generate an output. The basic structure includes several inputs, such as `x1`, `x2`, ..., `xn`, which are weighted and summed. If this weighted sum exceeds a certain threshold, known as the activation potential, the neuron produces a binary output.

### Basic Structure of a Perceptron

- **Inputs**: `x1`, `x2`, ..., `xn`
- **Weights**: `w1`, `w2`, ..., `wn`
- **Bias**: `b`
- **Output**: `y`

### Mathematical Representation

The output `y` of a perceptron can be mathematically represented as:

Output=∑jwjxj+Bias
schematic representation of sample neuron
# Typical Neural Network Architecture

A neural network typically consists of several layers that process the data sequentially from input to output. The layers between the input and output are referred to as **hidden layers**. The density and type of connections between these layers define the network's configuration.

## Hidden Layers and Connections

- **Hidden Layers**: Layers between the input and output layers.
- **Connections**: The manner in which neurons are connected between layers.

### Example: Fully Connected Configuration

In a **fully connected** configuration, every neuron in one layer is connected to every neuron in the next layer. For example, in layer `L`, all the neurons are connected to the neurons in layer `L+1`.

However, for more pronounced localization, you might connect only a local neighborhood of neurons. For instance, only nine neurons from layer `L` might be connected to the next layer `L+1`.

### Illustration

Below is an illustration showing two hidden layers with dense connections.

![Neural Network Architecture](path/to/your/diagram.png)

*Figure 1-9*: Two hidden layers with dense connections.

> **Note:** Replace `path/to/your/diagram.png` with the actual path to your diagram image file.


# Types of Neural Networks

## Feedforward Neural Networks

Feedforward Neural Networks (FNNs) are the most basic units of the neural network family. In this type of neural network, data flows in one direction: from the **input layer** to the **output layer**, passing through any **hidden layers** that may be present.

### Key Characteristics:

- **Data Flow**: The movement of data is unidirectional, from the input layer to the output layer.
- **No Loops**: There are restrictions on any kind of loops or cycles in the network architecture.
- **Layer Structure**: The output of one layer serves as the input to the next layer.

### Illustration

Below is an illustration of a Feedforward Neural Network.

![Feedforward Neural Network](path/to/your/diagram.png)

*Figure 2-1*: A Feedforward Neural Network with one hidden layer.

> **Note:** Replace `path/to/your/diagram.png` with the actual path to your diagram image file.

### How It Works

In a feedforward neural network:

1. **Input Layer**: Receives the input data.
2. **Hidden Layers**: Process the data with weighted connections.
3. **Output Layer**: Produces the final output based on the processed information.

The absence of loops makes FNNs relatively simple and efficient for various applications, such as classification and regression tasks.



# Types of Neural Networks

## Recurrent Neural Networks (RNNs)

Recurrent Neural Networks (RNNs) are used when the data pattern changes sequentially over a period. Unlike feedforward neural networks, RNNs apply the same layer multiple times to accept input parameters and generate output parameters, allowing the network to maintain a form of memory by using its previous outputs as part of its input.

### Key Characteristics:

- **Sequential Data Handling**: Ideal for tasks where the input data has a sequential nature, such as time series analysis, language modeling, or speech recognition.
- **Recurrent Connections**: The output from one step is fed as input to the next step, enabling the network to capture temporal dependencies.

### Illustration

Below is an illustration of a Recurrent Neural Network.

![Recurrent Neural Network](path/to/your/diagram.png)

*Figure 3-1*: A Recurrent Neural Network with one hidden layer and recurrent connections.

> **Note:** Replace `path/to/your/diagram.png` with the actual path to your diagram image file.

## Constructing Neural Networks with PyTorch

Neural networks can be constructed using the `torch.nn` package in PyTorch. Below is a typical training procedure for a neural network using PyTorch:

### Steps for Training a Neural Network

1. **Define the Neural Network**: Define the architecture that includes some learnable parameters (or weights).

   ```python
   import torch.nn as nn

   class SimpleRNN(nn.Module):
       def __init__(self):
           super(SimpleRNN, self).__init__()
           self.rnn = nn.RNN(input_size=..., hidden_size=..., num_layers=...)
           self.fc = nn.Linear(..., ...)

       def forward(self, x):
           out, _ = self.rnn(x)
           out = self.fc(out)
           return out
```


