### Advanced Neural Networks

#### 1. Convolutional Neural Networks (CNNs)

- **Definition:**
  - CNNs are specialized neural networks designed for processing grid-like data, such as images.

- **Architecture and Layers:**
  - **Convolutional Layers:** Perform feature extraction by applying filters (kernels) across the input.
  - **Pooling Layers:** Reduce the spatial dimensions of the feature map, reducing computation and controlling overfitting.

- **Example: Image Classification (MNIST Dataset)**

  ```python
  import tensorflow as tf
  from tensorflow.keras import datasets, layers, models
  import matplotlib.pyplot as plt
  
  # Load and preprocess MNIST dataset
  (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
  train_images, test_images = train_images / 255.0, test_images / 255.0
  
  # Reshape images for CNN input (add channel dimension for grayscale)
  train_images = train_images.reshape(-1, 28, 28, 1)
  test_images = test_images.reshape(-1, 28, 28, 1)
  
  # Define CNN architecture
  model = models.Sequential([
      layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
      layers.MaxPooling2D((2, 2)),
      layers.Conv2D(64, (3, 3), activation='relu'),
      layers.MaxPooling2D((2, 2)),
      layers.Conv2D(64, (3, 3), activation='relu'),
      layers.Flatten(),
      layers.Dense(64, activation='relu'),
      layers.Dense(10, activation='softmax')
  ])
  
  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
  
  # Train the model
  history = model.fit(train_images, train_labels, epochs=10,
                      validation_data=(test_images, test_labels))
  
  # Evaluate the model
  test_loss, test_acc = model.evaluate(test_images, test_labels)
  print(f'Test accuracy: {test_acc}')
  
  # Plot accuracy and loss curves
  plt.plot(history.history['accuracy'], label='accuracy')
  plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend(loc='lower right')
  plt.show()
  ```

#### 2. Recurrent Neural Networks (RNNs)

- **Definition:**
  - RNNs are designed to capture sequential dependencies in data, making them suitable for tasks like time series prediction, text analysis, and speech recognition.

- **Architecture and Layers:**
  - **LSTM (Long Short-Term Memory):** A type of RNN cell that mitigates the vanishing gradient problem, allowing for learning long-term dependencies.
  - **GRU (Gated Recurrent Unit):** Another variant of RNNs that simplifies the architecture while maintaining effectiveness in learning sequential data.

- **Example: Text Generation**

  ```python
  import tensorflow as tf
  from tensorflow.keras.layers import Embedding, LSTM, Dense
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.preprocessing.text import Tokenizer
  from tensorflow.keras.preprocessing.sequence import pad_sequences
  import numpy as np
  
  # Example text data
  corpus = [
      'Hello, how are you?',
      'I am doing great!',
      'What are you up to?',
      'Let us meet tomorrow.'
  ]
  
  # Tokenize and pad sequences
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(corpus)
  total_words = len(tokenizer.word_index) + 1
  
  input_sequences = []
  for line in corpus:
      token_list = tokenizer.texts_to_sequences([line])[0]
      for i in range(1, len(token_list)):
          n_gram_sequence = token_list[:i+1]
          input_sequences.append(n_gram_sequence)
  
  max_sequence_len = max([len(x) for x in input_sequences])
  input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
  
  # Create predictors and label
  predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
  label = tf.keras.utils.to_categorical(label, num_classes=total_words)
  
  # Define RNN model
  model = Sequential()
  model.add(Embedding(total_words, 64, input_length=max_sequence_len-1))
  model.add(LSTM(150))
  model.add(Dense(total_words, activation='softmax'))
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  
  # Train the model
  history = model.fit(predictors, label, epochs=100, verbose=1)
  
  # Generate text
  seed_text = "Hello,"
  next_words = 5
  
  for _ in range(next_words):
      token_list = tokenizer.texts_to_sequences([seed_text])[0]
      token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
      predicted = model.predict_classes(token_list, verbose=0)
      
      output_word = ""
      for word, index in tokenizer.word_index.items():
          if index == predicted:
              output_word = word
              break
      seed_text += " " + output_word
  
  print(seed_text)
  ```

### Key Points:
- **Convolutional Neural Networks (CNNs):** Specialized for spatial data like images, leveraging convolutional and pooling layers for feature extraction and spatial reduction.
- **Recurrent Neural Networks (RNNs):** Effective for sequential data processing, utilizing LSTM and GRU layers to capture temporal dependencies.
- **Examples:** Hands-on implementation of image classification with CNNs using the MNIST dataset and text generation with RNNs, demonstrating practical applications and architectures.

These advanced neural network concepts and examples provide a deeper understanding of how TensorFlow can be utilized for complex tasks like image classification and sequential data processing, preparing us to explore and implement sophisticated machine learning models effectively.