### TensorFlow 2.x Features and Updates

#### 1. Eager Execution Mode

- **Eager Execution:**
  - Eager execution is a mode in TensorFlow 2.x where operations are evaluated immediately, allowing for more intuitive Python programming and easier debugging.

- **Example:**

  ```python
  import tensorflow as tf
  
  # Enable eager execution (enabled by default in TensorFlow 2.x)
  tf.config.experimental_run_functions_eagerly(True)
  
  # Define tensors and operations
  x = tf.constant([1, 2, 3])
  y = tf.constant([4, 5, 6])
  z = tf.add(x, y)
  
  # Print results immediately
  print(z.numpy())
  ```

#### 2. Keras Integration and High-Level API

- **Keras Integration:**
  - TensorFlow 2.x integrates the Keras API as its high-level API for building and training deep learning models, providing simplicity and ease of use.

- **Example: Building a Simple Neural Network using Keras**

  ```python
  import tensorflow as tf
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Dense
  
  # Define a Sequential model
  model = Sequential([
      Dense(64, activation='relu', input_shape=(784,)),
      Dense(64, activation='relu'),
      Dense(10, activation='softmax')
  ])
  
  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
  
  # Print model summary
  model.summary()
  ```

#### 3. TensorFlow Hub for Reusable Machine Learning Components

- **TensorFlow Hub:**
  - TensorFlow Hub is a library and platform for publishing, discovering, and reusing machine learning components (modules, models, embeddings).

- **Example: Using a Pretrained Model from TensorFlow Hub**

  ```python
  import tensorflow as tf
  import tensorflow_hub as hub
  
  # Load a pretrained model from TensorFlow Hub
  embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
  
  # Define a list of sentences
  sentences = ["Hello, how are you?", "I am doing great!", "What are you up to?"]
  
  # Compute embeddings for sentences
  embeddings = embed(sentences)
  
  # Print embeddings
  print(embeddings)
  ```

### Key Points:
- **Eager Execution Mode:** Allows for immediate evaluation of operations, enhancing flexibility and ease of debugging in TensorFlow 2.x.
- **Keras Integration and High-Level API:** TensorFlow 2.x integrates the Keras API as its primary high-level API, offering simplicity and modularity for building neural networks.
- **TensorFlow Hub:** Facilitates the reuse of pretrained models and components, streamlining the development and deployment of machine learning applications.

These TensorFlow 2.x features and updates empower students with modern tools and capabilities for developing and deploying machine learning models effectively, leveraging intuitive APIs and reusable components for enhanced productivity and flexibility.