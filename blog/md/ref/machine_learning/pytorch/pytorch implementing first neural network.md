# Implementation of Neural Network in PyTorch

PyTorch provides robust features for creating and implementing neural networks. In this chapter, we will create a simple neural network with one hidden layer and a single output unit.

## Step 1

Import the PyTorch library using the following commands:

```python
import torch
import torch.nn as nn
```

## Step 2

Define all the layers and the batch size to start executing the neural network.

```python
# Defining input size, hidden layer size, output size, and batch size
n_in, n_h, n_out, batch_size = 10, 5, 1, 10
```

## Step 3

As a neural network includes a combination of input data to get the respective output data, follow the procedure below:

```python
# Create dummy input and target tensors (data)
x = torch.randn(batch_size, n_in)
y = torch.tensor([[1.0], [0.0], [0.0], 
                  [1.0], [1.0], [1.0], 
                  [0.0], [0.0], [1.0], 
                  [1.0]])

```

## Step 4

Create a sequential model using built-in functions. Use the following lines of code to create the model:

```python
# Create a model
model = nn.Sequential(
    nn.Linear(n_in, n_h),  # Input layer to hidden layer
    nn.ReLU(),             # ReLU activation function
    nn.Linear(n_h, n_out), # Hidden layer to output layer
    nn.Sigmoid()           # Sigmoid activation function for the output
)
```
## Step 5

Construct the loss function and optimizer as shown below:

```python
# Construct the loss function
criterion = torch.nn.MSELoss()

# Construct the optimizer (Stochastic Gradient Descent in this case)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

## Step 6

Implement the gradient descent model with an iterating loop using the following lines of code:

```python
# Gradient Descent
for epoch in range(50):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x)

    # Compute and print loss
    loss = criterion(y_pred, y)
    print('epoch:', epoch, 'loss:', loss.item())

    # Zero gradients, perform a backward pass, and update the weights
    optimizer.zero_grad()
    
    # Perform a backward pass (backpropagation)
    loss.backward()
    
    # Update the parameters
    optimizer.step()
```

## Step 7

The output generated is as follows:
epoch: 0 loss: 0.2545787990093231
epoch: 1 loss: 0.2545052170753479
epoch: 2 loss: 0.254431813955307
epoch: 3 loss: 0.25435858964920044
epoch: 4 loss: 0.2542854845523834
epoch: 5 loss: 0.25421255826950073
epoch: 6 loss: 0.25413978099823
epoch: 7 loss: 0.25406715273857117
epoch: 8 loss: 0.2539947032928467
epoch: 9 loss: 0.25392240285873413
epoch: 10 loss: 0.25385022163391113
epoch: 11 loss: 0.25377824902534485
epoch: 12 loss: 0.2537063956260681
epoch: 13 loss: 0.2536346912384033
epoch: 14 loss: 0.25356316566467285
epoch: 15 loss: 0.25349172949790955
epoch: 16 loss: 0.25342053174972534
epoch: 17 loss: 0.2533493936061859
epoch: 18 loss: 0.2532784342765808
epoch: 19 loss: 0.25320762395858765
epoch: 20 loss: 0.2531369626522064
epoch: 21 loss: 0.25306645035743713
epoch: 22 loss: 0.252996027469635
epoch: 23 loss: 0.2529257833957672
epoch: 24 loss: 0.25285571813583374
epoch: 25 loss: 0.25278574228286743
epoch: 26 loss: 0.25271597504615784
epoch: 27 loss: 0.25264623761177063
epoch: 28 loss: 0.25257670879364014
epoch: 29 loss: 0.2525072991847992
epoch: 30 loss: 0.2524380087852478
epoch: 31 loss: 0.2523689270019531
epoch: 32 loss: 0.25229987502098083
epoch: 33 loss: 0.25223103165626526
epoch: 34 loss: 0.25216227769851685
epoch: 35 loss: 0.252093642950058
epoch: 36 loss: 0.25202515721321106
epoch: 37 loss: 0.2519568204879761
epoch: 38 loss: 0.251888632774353
epoch: 39 loss: 0.25182053446769714
epoch: 40 loss: 0.2517525553703308
epoch: 41 loss: 0.2516847252845764
epoch: 42 loss: 0.2516169846057892
epoch: 43 loss: 0.2515493929386139
epoch: 44 loss: 0.25148195028305054
epoch: 45 loss: 0.25141456723213196
epoch: 46 loss: 0.2513473629951477
epoch: 47 loss: 0.2512802183628082
epoch: 48 loss: 0.2512132525444031
epoch: 49 loss: 0.2511464059352875
