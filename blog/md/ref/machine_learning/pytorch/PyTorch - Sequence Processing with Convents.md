 # Sequence Processing with Convolutions

We propose an alternative approach which relies on a single 2D convolutional neural network across both sequences. Each layer of our network re-codes source tokens based on the output sequence produced so far. Attention-like properties are therefore pervasive throughout the network.

Here, we will focus on creating the sequential network with specific pooling from the values included in the dataset. This process is also best applied in the **Image Recognition Module**.

## Step 1: Import Modules

Import the necessary modules for performance of sequence processing using convolutional networks:

```python
import keras 
from keras.datasets import mnist 
from keras.models import Sequential 
from keras.layers import Dense, Dropout, Flatten 
from keras.layers import Conv2D, MaxPooling2D 
import numpy as np
```

## Step 2: Create a Pattern in the Sequence

Perform the necessary operations to create a pattern in the respective sequence using the following code:

```python
batch_size = 128 
num_classes = 10 
epochs = 12

# Input image dimensions
img_rows, img_cols = 28, 28

# The data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape the data
x_train = x_train.reshape(60000, 28, 28, 1) 
x_test = x_test.reshape(10000, 28, 28, 1)

print('x_train shape:', x_train.shape) 
print(x_train.shape[0], 'train samples') 
print(x_test.shape[0], 'test samples')

# Convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes) 
y_test = keras.utils.to_categorical(y_test, num_classes)
```

## Step 3: Compile and Fit the Model

Compile the model and fit the pattern in the mentioned convolutional neural network model as shown below:

```python
# Compile the model
model.compile(
    loss=keras.losses.categorical_crossentropy, 
    optimizer=keras.optimizers.Adadelta(), 
    metrics=['accuracy']
)

# Fit the model
model.fit(
    x_train, y_train, 
    batch_size=batch_size, 
    epochs=epochs, 
    verbose=1, 
    validation_data=(x_test, y_test)
)

# Evaluate the model
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0]) 
print('Test accuracy:', score[1])
```


