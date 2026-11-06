**Neural Networks**

Neural Network consists of:

- input layer (root nodes)

-hidden layers

-output layer (terminal nodes)

**1-Input Data (perceptrons)**

input data (texts, numbers, pictures..etc) are converted to numbers.

_1.1-numeric data types:_

scalar: single value

vectors: 1D array of values

matrix: 2D array of values

Tensor: 3D or more array of values

_1.2-Normalization/standarization:_

sometimes the numbers need to normalized or standardized, which means the numbers are converted to be around zero with
standard deviation of 1 on each side of the mean. 

_1.3- input data packages:_
Numpy and Tensorflow.keras

**2- Layers**

if the neural network consists of one or more hidden layers then we're dealing with deep learning. 

_2.1 Fully connected Neural network FCNN (Dense layers) (from tensorflow.keras.layers import Dense)_

every node in the layer is connected to every node in the following layer 
- use add() method to the class object Dense() with 10 nodes in the first layer (model.add(Dense(10,input_shape=(13,))))
- add a second layer and a third with 10,1 in order nodes (model.add(Dense(10)), model.add(Dense(1))

_2.2 feed forward networks:_

FNN: data moves through the network sequentially in one direction from the input (as parameters) to the hidden layers 
(where action happen to them) then to the output layer (as results).

_2.2.1: sequential API method (from tensorflow.keras import Sequential)_
- create an empty FFN with sequential class object (model=Sequential ())
- add one layer at a time until the output layer (model.add(..the first layer) and so on)

_2.2.2: Functional API method_ 

suitable for the construction of models that are non-sequential in flow like branches, skip links
and multiple inputs and outputs.
- Build layers separately (input=layers.(.. the first layer) and so on)
- tie the layers (model=Model(input, output))

_2.3: input Layer (from tensorflow.keras import Input)_

construct an input vector of one dimensional array with 13 elements (features) (Input(shape=(?,13)))
each node in the input vector will be connected to each node in the input layer.

_2.4: weight and bias (threshold)_

def:
weight is the connection value between each node in the input layer and the input vector. represents how strong the input 
value will contribute in the model prediction.
bias is a value each input layer node has.

each node is a linear regression model composed of input data, weight, bias and output.

how does it work?

the node is connected with several nodes and each connection has a certain weight, when data is received via each connection,
the node will multiply it with the associated weight and add the results yielding a single number. if the number is 
below a threshold value, the node fires (sends the single number to all its outgoing connections).

∑wixi + bias = w1x1 + w2x2 + w3x3 + bias

output = f(x) = 1 if ∑w1x1 + b>= 0; 0 if ∑w1x1 + b < 0

how is it setup and trained?

initially weights and thresholds are set to random values. during the training, the weights and thresholds are continually
adjusted till training data with the same labels keep on yielding similar outputs.
Training data is fed to the bottom layer — the input layer — and it passes through the succeeding layers, getting
multiplied and added together in complex ways, until it finally arrives, radically transformed, at the output layer.

the weight and bias (NN parameters) are what the NN will learn during the training
the number of parameters is the inputs nodes * dense + bias

_2.5: Activation Functions_

functions that occur to the data in a layer where the results are passed to the following layer. 
the functions are used in the learning process handling linear and non linear relationships. where they assist in
the non-linear separation and corresponding clustering nodes within input sequences which learn the near linear
relationships to the output.

the activation function can either be added on its own with .add(activation fn) method 
or through the dense(#,input_shape,activation) in each layer.

the Activation functions:
- the rectified linear unit (ReLu):
most used and produces best result in model training
R(z)=max(0,z) :passes values greater than zero unchanged otherwise zero 
model.add(ReLu()) : pass the output from the current layer to the next one using ReLu funtcion.
- Sigmoid
- Softmax

**3. Evaluation**

the regressor:

the neural network calculates the errors in the predicted results (loss) from the actual values (labels)
and uses the information to adjust weights and biases of the nodes (learning)
as the FNN is a regressor, the loss function is the Mean Square Error (MSE) 
the compile() method takes a keyword(loss function) to calculate it so in a FNN we can write MSE

the optimizer:

based on the gradiant descent algorithm. where each time the loss function is calculated, we decide how much to change the weights and biases in the layers. the process is done gradually to get closer to the correct weight and bias values to enhance the prediction which is defined by convergence.

the goal is minimize the loss function to ensure correctness of fit where the model uses cost function and reinforcement learning to reach the point of convergence(local min).

backward propagation/ model.compile(loss='mse',optimizer='rmsprop'):

backpropagation allows  the model to calculate the error associated with each neuron to adjust the parameters by passing data backwards from output to input

**4. types of Neural networks:**

- Feedforward NN or multi-layer perceptrons (used for computer vision, NLP)
- Convolutional NN (CNN) (used for image recognition, pattern recognition,computer vision)
- Recurrent NN(RNN)/feedback loops: works with sequential data (used for time series, speech recognition, translation, NLP)

**5. Artificial intelligence AI**

machines that mimic humans intelligence functions like problem-solving and learning

AI categories:

Artificial narrow intelligence (ANI)

Artificial general intelligence (AGI)

Artificial super intelligence (ASI)

6. machine learning vs Deep learning

|                   | ML                                                          | DL                                      |
|-------------------|-------------------------------------------------------------|-----------------------------------------|
| learn             | statistical algorithms                                      | ANN architecture                        |
| dataset amount    | smaller                                                     | larger                                  |
| label task        | better for low label tasks                                  | better for complex label task           |
| training time     | less time                                                   | more time                               |
| relevant features | model is created by relevant features extracted from images | relevant features extracted from images |
| complexity        | less complex, easy result interpretation                    | more complex (black box)                |
| computer power    | CPU, less power                                             | GPU, high performance computer          |

**7. Deep learning**

Branch of machine learning that is based on artificial neural network architecture. used for supervised, unsupervised and reinforcement learning.

_7.1 DL in supervised machine learning_

Neural networks learn to make predictions or classification based on labelled datasets. Neural network makes predictions based on the error/cost/loss function evaluation.

models used: CNN, RNN

applications: image classification and recognition, sentiment analysis, language translation;

_7.2 DL in unsupervised learning_

Neural networks learn to discover the pattern or to cluster the dataset based on unlabelled datasets.

**Models:** clustering, dimensionality reduction, anomaly detection.

**Applications:** autoencoders and generative models.

_7.3 DL in reinforcement learning_

agent learns to make decisions in an environment to maximize a reward signal by taking action and observe the resulting 
rewards. deep learning used to learn policies, set of actions to maximize the cumulative reward over time

Models: Deep Q networkds, deep deterministic policy gradiant

Applications: robotics and game playing

_7.4 Deep learning applications_ 

- computer vision

object detection and recognition (used for self driving cars, surveillance, robotics)

image classification (used for medical imaging, quality control,image retrieval)

image segmentation(identify features in an image)

- Natural Language Processing (NLP)

Automatic text generation

**Language translation**

sentiment analysis/determines whether text is positive, negative or neutral  (customer service, social media monitoring, political analysis)

Speech recognition (speech to text conversion, voice search, voice controlled device)

- reinforcement learning

game playing/learns how to beat humans experts at games (go, chess, atari)

robotics/train robots to perform complex tasks (grasping objects, navigation, manipulation)

control systems(power grids, traffic management, supply chain optimization)

8. The Transform Model

A machine learning system used to understand and process sequences of information, like sentences in a language.

Unlike older methods that read sequences one step at a time (like reading a sentence word by word), the Transformer looks at all parts of the sequence at once.

This makes it much faster and better at understanding long-distance relationships between words or data points.

8.1 model characteristics:

- Self-Attention: The Transformer checks how each part of a sequence is related to every other part.

For example,  when translating a sentence, it looks at all the words together to figure out their connections.

- Multi-head attention: It does this multiple times in parallel to catch different patterns and relationships at once,
making it more accurate.

- No Recurrence or Convolution: Unlike older systems that had to read through sequences one-by-one, the Transformer processes everything at the same time, which speeds things up.

8.2 Model Architecture

Most neural models for tasks like translation use an encoder-decoder structure.
The encoder takes the input sequence  (like words in a sentence) and converts it into continuous data representations.
Then, the decoder uses this data to generate the output sequence (like the translated sentence), one element at a time.
At each step, the decoder uses the previous output as input for the next.

The Transformer model follows this same structure but replaces traditional methods with self-attention and fully 
connected layers in both the encoder and decoder, allowing for faster and more efficient processing.

- encoder has 6 identical layers, each has two parts:
1- multi-head self-attention: model looks at different parts of input sequence at the same time
2- feed-forward network: fully connected network processes each position seperately.

- decoder has 6 identical layers:
1- multi-head self-attention 2-feed-forward network 3-multi-head attention that looks at encoder output each part has residual connection helps model learn by skipping layers and layer normalization to speed up training.

**Attention:**

helps the model decide which parts of the input to focus on when making predictions. how?
- it compares a query (what you're looking for) with keys (features of input)
- it assigns weights to the values ( the information being processed) based on how well they match.

**methods:**
- multi-head attention, compares multiple times in parallel to capture different patterns making the model better at focusing on important information. 
- Scaled dot-product attention, compares the query and keys, divides by the square root of their size for stability and uses softmax function to assign attention weights to make the process faster and efficient.

The transformer uses attention in three ways:

- encoder-decoder attention: decoder focuses on different parts of the encoder output
- encoder self-attention: each part of the input can attend to every other part in the encoder.
- decoder self-attention: each part of the output can attend to earlier parts while generating the output sequence but not future ones to ensure proper prediction order. 

The position-wise-feedforward networks in encoder and decoder layers process (through math operations) each position in the input separately (each word). They
consist of two linear transformations with a ReLu activation in between. the process:

- input is transformed using two linear layers: FFN(x)=max(0,xW1 + b1)W2 + b2.
- these transformations apply across all positions but each layer has its own unique parameters. 
- the input and output dimensions (d_model) are 512 while the inner layer dimension (inner processing space d_ff) is 2048.

**Embedding and softmax**

- The model uses embeddings to convert words/tokens into numerical vectors.
- on output side, model uses linear transformation and softmax function to predict the next word. the softmax function converts numbers into probabilities, helping the model decide which word is likely to come next.
- the model shares the same weight matrix for both the input and output embeddings and pre-softmax transformation. the sharing helps make the model more efficient
- the weights are scaled by square root of d_model.

**Neural machine Translation**

A modern approach to translate languages that differs from traditional methods. it uses a single
large NN that learns to translate by reading a whole sentence at once.

NMT maximizes the probability of a correct translation to find best translation where it learns from sentence pairs (source and target language).

- RNN encoder-decoder framework: the encoder reads, compresses the sentence into a vector and decode generates translation
- alignment and attention mechanism: instead of encoding a whole sentence into a vector, the system creates a series of vectors and chooses the most relevant ones as it translates so the model handles longer sentences effectively and translation performance is improved.
- Bidirectional RNNs: reads the sentence forward and backward summerizing information from the entire sentence so the model can generate more accurate translations by considering all parts of the sentence.

**Retrieval-Augmented generation (RAG)**

LLMs is a technology powering intellegent chatbots and NLP applications to answer questions, translate.. but the source of information for LLMs could be non-authorative so the information could be false.

RAG came to solve this problem of LLMs to retrieve relevant information from authorative knowledge sources.

**why are RAG good?**

1- chatbots development via foundation models, foundation models are retrained based on an organization. however, that expensive. RAG works on Gen AI and new data introduction with a more cost-effective approach.

2- its challenging to maintain relevancy  even if training data sources are suitable for an LLM. RAG provides latest statistics and news to generative models as it connects LLM to live soial media feed, news sites and updated info sources.

3- RAG references the sources in output for more accuracy

4- RAG allows applications to be developed, LLMs information sources can be updated, sensitive
information can be restricted.

**how does RAG work?**

LLMs create response based on information it was trained on. what does RAG do?

- RAG uses the user input to pull information from a new data source
- the user Query is pre-processed (i.e tokenization, stemming and stop words removal) then converted to a numerical vector and matched with vector databases via an embedding language model
- the relevancy is calculated and established using mathematical vector calculations and representations
- the highly relevant documents vectors to the query vector will be retrieved.
- examples of data sources: APIs, databases, document repositories and storage examples: files, database records,long form texts)
- RAG model adds the user query (input or prompt) to the relevant retrieved data using prompt engineering techniques and communicated it with the LLM and LLM uses the new knowledge and trained data to create a better response. 

**Semantic Search**
a technology that does all the work of knowledge based preperations (word embedding, document chunking,,,) as well as generating semantically relevant passages and token words ordered by relevance to maximize the quality of RAG payload on its own without the need to developers.

**AWS**
- Amazon Bedrock :connect FMs to data sources for RAG in few clicks where vector conversions, retrievals and improved output generation are handled automatically.
- Amazon Kendra: provides optimized retreieved API with high accuracy.

**Google cloud**
- vertex AI search
- vertex AI vector search
- BigQuery

**Navida:**
- launchPad Lab

**IBM:**
- open book