TensorFlow enables us to create machine learning models for different devices.

Core TensorFlow: This is the main part of TensorFlow, where you can create and train machine learning models. It provides mathematical operations to work with data (like matrices and tensors).

Keras: Keras is a high-level API that makes it easier to build and train models in TensorFlow. It’s user-friendly and helps simplify the creation of deep learning models with just a few lines of code.

TensorFlow Lite: This helps you take the models you’ve built and run them on mobile devices or embedded systems. It's useful for making AI-powered apps that work on smartphones, tablets, or even IoT devices.

TensorFlow.js: If you want to run your machine learning models directly in a web browser, TensorFlow.js allows you to do that using JavaScript. You can use it to build AI models for websites.

TensorFlow Extended (TFX): This is a full end-to-end platform that helps manage the entire process of developing and deploying machine learning models. From data validation, model training, to serving models in production.

TensorBoard: This tool is used for visualizing what's happening inside your machine learning model. It gives you graphs and charts that show how your model is learning over time, which helps you tune and improve it.

TensorFlow Hub: A place where you can find pre-trained models built by others that you can reuse in your projects. This saves time, as you don't need to train a model from scratch.

to use Keras we need to:
- Load a  dataset either by pandas dataframes, numpy array or from tensorflow APIs
1. import library
2. load dataset and identify which is the training and testing datasets
- Build a neural network machine learning model.
1. choose the model method, input shape, activation function and layers. 
2. the model returns a vector of logits or log-odds scores for each class. 
3. choose a function that converts these logits to probabilities of each class 
4. define a loss function for training
5. configure and compile the model using keras by setting the parameters (optimizer, loss, metrics)
- Train and evaluate the model
- use model.fit(x_train,y_train, epoches=5) to adjust model parameters and minimize loss
- use model.evaluate(x_test,y_test,verbose=2) to check model's performance 
- if you want the model to return a probability, attach softmax to the trained model
  probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
  ])
  probability_model(x_test[:5])


what is a model?
what is a layer? 
layers are functions with known mathematical structure that be reused and have trainable variable. 

| model       | layers               | activation function | explain model                                                  |
|-------------|----------------------|---------------------|----------------------------------------------------------------|
| sequential  | Flatten,dense, dropout | relu              | staks layers where each layer has an input and an output tensors| 
|             |                        |                   |                                                                 |



the functions that convert logist to probabilities:
softmax

loss functions:(def: a function that takes a vector of truth values and a vector of logits and returens a scalar loss,
it equals the negative log probability of the true class. if loss is zero then model is sure of the currect class )

SparseCategoricalCrossentropy

parameters to complie and configure the model using keras:
optimizer: adam, loss function
loss:loss function
metrics: accuracy

* Pre-Processing:
- pandas dataframe
library: import pandas as pd
data loading: df=pd.read_csv('file.csv')

- numpy array
Library: import numpy as np
data loading: array=np.array(df) #here this will pack the attributes in the df to a single numpy array
- cloud

*  Model Building