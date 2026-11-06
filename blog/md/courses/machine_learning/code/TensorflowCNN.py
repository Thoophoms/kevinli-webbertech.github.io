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