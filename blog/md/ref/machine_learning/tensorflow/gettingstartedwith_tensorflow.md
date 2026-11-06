### Getting Started with TensorFlow

#### 1. Installation and Setup

- **Installation:**
  - TensorFlow can be installed using pip, Anaconda, or Docker depending on your system and requirements.
  - Preferred installation for TensorFlow 2.x:
    ```
    pip install tensorflow
    ```
    This command installs the latest stable version of TensorFlow.

- **Setup:**
  - Verify installation:
    ```python
    import tensorflow as tf
    
    # Check TensorFlow version
    print("TensorFlow version:", tf.__version__)
    
    # Check if GPU is available (optional)
    print("GPU available:", tf.config.list_physical_devices('GPU'))
    ```

- **System Requirements:**
  - TensorFlow supports various platforms including Windows, macOS, and Linux.
  - Utilizing GPU for accelerated computations requires compatible NVIDIA GPUs and CUDA toolkit installation.

#### 2. Hello World Example (TensorFlow Program Structure)

- **TensorFlow Program Structure:**
  - TensorFlow programs typically involve defining computational graphs using tensors (multi-dimensional arrays) and operations.

- **Example:**
  ```python
  import tensorflow as tf
  
  # Define constants
  a = tf.constant(2)
  b = tf.constant(3)
  
  # Perform addition
  c = tf.add(a, b)
  
  # Print the result
  print("Sum of a and b:", c.numpy())
  ```
  
### Explanation:

- **Installation and Setup:** Ensure TensorFlow is properly installed and verify the version to confirm functionality.
  
- **Hello World Example:** Introduces the basic TensorFlow operations:
  - **Constants (`tf.constant`):** Immutable tensors with fixed values.
  - **Operations (`tf.add`):** Defines computation within the TensorFlow graph.
  - **Execution (`c.numpy()`):** Computes and retrieves the result using eager execution in TensorFlow 2.x.

### Key Points:
- **Installation:** Install TensorFlow using pip and verify installation with a simple import statement.
- **Hello World Example:** Illustrates the fundamental structure of TensorFlow programs with constants and operations.

These foundational concepts and examples serve as a starting point for us to begin experimenting and building more complex machine learning models using TensorFlow.