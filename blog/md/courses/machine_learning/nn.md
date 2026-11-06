# Neural Network and Deep Learning

Artificial Intelligence is trending nowadays to a greater extent. Machine learning and deep learning constitutes artificial intelligence. The Venn diagram mentioned below explains the relationship of machine learning and deep learning.

![deep_learning](https://kevinli-webbertech.github.io/blog/images/ml/ml_deeplearning.png)

## Machine Learning

Machine learning is the art of science which allows computers to act as per the designed and programmed algorithms. Many researchers think machine learning is the best way to make progress towards human-level AI. It includes various types of patterns like −

* Supervised Learning Pattern
* Unsupervised Learning Pattern

## Deep Learning

Deep learning is a subfield of machine learning where concerned algorithms are inspired by the structure and function of the brain called Artificial Neural Networks.

Deep learning has gained much importance through supervised learning or learning from labelled data and algorithms. Each algorithm in deep learning goes through same process. It includes hierarchy of nonlinear transformation of input and uses to create a statistical model as output.

Machine learning process is defined using following steps −

* Identifies relevant data sets and prepares them for analysis.
* Chooses the type of algorithm to use.
* Builds an analytical model based on the algorithm used.
* Trains the model on test data sets, revising it as needed.
* Runs the model to generate test scores.

## Neural Network

The main principle of neural network includes a collection of basic elements, i.e., artificial neuron or perceptron. It includes several basic inputs such as x1, x2….. xn which produces a binary output if the sum is greater than the activation potential.

The schematic representation of sample neuron is mentioned below −

![neuron](https://kevinli-webbertech.github.io/blog/images/ml/neuron.png)

The output generated can be considered as the weighted sum with activation potential or bias.

![nn formula](https://kevinli-webbertech.github.io/blog/images/ml/nn_formula.png)

The typical neural network architecture is described below −

neural network architecture

![nn architecture](https://kevinli-webbertech.github.io/blog/images/ml/nn.png)

The layers between input and output are referred to as hidden layers, and the density and type of connections between layers is the configuration. For example, a fully connected configuration has all the neurons of layer L connected to those of L+1. For a more pronounced localization, we can connect only a local neighbourhood, say nine neurons, to the next layer. Figure 1-9 illustrates two hidden layers with dense connections.

## Types of NN

The various types of neural networks are as follows −

**Feedforward Neural Networks**

Feedforward neural networks include basic units of neural network family. The movement of data in this type of neural network is from the input layer to output layer, via present hidden layers. The output of one layer serves as the input layer with restrictions on any kind of loops in the network architecture.

![feedforward nn](https://kevinli-webbertech.github.io/blog/images/ml/feedforward_nn.png)

**Recurrent Neural Networks**

Recurrent Neural Networks are when the data pattern changes consequently over a period. In RNN, same layer is applied to accept the input parameters and display output parameters in specified neural network.

![recurrent1](https://kevinli-webbertech.github.io/blog/images/ml/recurrent_nn1.png)

Neural networks can be constructed using the torch.nn package.

![recurrent2](https://kevinli-webbertech.github.io/blog/images/ml/recurrent_nn2.png)

It is a simple feed-forward network. It takes the input, feeds it through several layers one after the other, and then finally gives the output.

With the help of PyTorch, we can use the following steps for typical training procedure for a neural network −

* Define the neural network that has some learnable parameters (or weights).

* Iterate over a dataset of inputs.

* Process input through the network.

* Compute the loss (how far is the output from being correct).

* Propagate gradients back into the network’s parameters.

Update the weights of the network, typically using a simple update as given below rule: 

`weight = weight -learning_rate * gradient`

### ref

- https://www.tutorialspoint.com/machine_learning/index.htm

- https://www.simplilearn.com/tutorials/deep-learning-tutorial/neural-network