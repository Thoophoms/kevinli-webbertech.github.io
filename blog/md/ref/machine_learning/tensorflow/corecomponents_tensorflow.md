### Core Components of TensorFlow

#### 1. Variables and Constants

- **Constants:**
  - Constants in TensorFlow are immutable tensors with fixed values.
  - **Example:**
    ```python
    import tensorflow as tf
    
    # Define a constant tensor
    a = tf.constant(5)
    print("Constant tensor 'a':", a.numpy())
    ```

- **Variables:**
  - Variables are mutable tensors that hold values that can change during execution.
  - **Example:**
    ```python
    import tensorflow as tf
    
    # Define a variable initialized to zero
    b = tf.Variable(0, name='my_variable')
    print("Initial value of variable 'b':", b.numpy())
    
    # Update the variable's value
    b.assign(10)
    print("Updated value of variable 'b':", b.numpy())
    ```

#### 2. Placeholders and Feeding Data

- **Placeholders (Deprecated in TensorFlow 2.x):**
  - In TensorFlow 1.x, placeholders are used to feed data into the computational graph during execution.
  - **Example (TensorFlow 1.x):**
    ```python
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
    
    # Define a placeholder for a single value
    x = tf.placeholder(tf.float32)
    y = 2 * x
    
    # Execute the graph and feed data into placeholder
    with tf.Session() as sess:
        result = sess.run(y, feed_dict={x: 3.0})
        print("Result:", result)
    ```

- **Feeding Data in TensorFlow 2.x:**
  - TensorFlow 2.x uses Python variables or NumPy arrays directly with eager execution for dynamic computation.
  - **Example (TensorFlow 2.x):**
    ```python
    import tensorflow as tf
    
    # Define a function using TensorFlow operations
    def compute_result(x):
        return 2 * x
    
    # Execute the function with a Python variable
    result = compute_result(3.0)
    print("Result:", result.numpy())
    ```

#### 3. Graphs and Operations

- **Graphs:**
  - TensorFlow programs are structured as computational graphs where nodes represent operations and edges represent data tensors (inputs/outputs).
  - **Example:**
    ```python
    import tensorflow as tf
    
    # Define tensors and operations
    a = tf.constant(2)
    b = tf.constant(3)
    c = tf.add(a, b)
    
    # Print computational graph
    print("Nodes in the graph:", tf.get_default_graph().as_graph_def())
    ```

- **Operations:**
  - Operations in TensorFlow define computations that manipulate tensors.
  - **Example:**
    ```python
    import tensorflow as tf
    
    # Define tensors and operations
    a = tf.constant(2)
    b = tf.constant(3)
    c = tf.add(a, b)
    
    # Execute the operation and print result
    print("Result of addition:", c.numpy())
    ```

### Key Points:
- **Variables and Constants:** Constants are immutable tensors with fixed values, while variables are mutable and can change during execution.
- **Placeholders and Feeding Data:** TensorFlow 1.x uses placeholders for dynamic input data, while TensorFlow 2.x employs Python variables or NumPy arrays with eager execution.
- **Graphs and Operations:** TensorFlow programs are represented as computational graphs where nodes are operations and edges are tensors, facilitating optimization and execution.

These core components provide the foundation for understanding how TensorFlow manages data flow, computations, and dynamic inputs in machine learning applications.