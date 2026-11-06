### TensorFlow Basics

#### 1. Tensors and Operations

- **Tensors:**
  - Tensors are multi-dimensional arrays used to represent data in TensorFlow.
  - **Types of Tensors:**
    - **Scalar (0-D tensor):** Single value (e.g., a number).
    - **Vector (1-D tensor):** Array of numbers (e.g., list of numbers).
    - **Matrix (2-D tensor):** 2-dimensional array of numbers.
    - **Higher-dimensional tensors:** Tensors with more than two dimensions.

- **Operations:**
  - Operations in TensorFlow represent computations that manipulate tensors.
  - **Types of Operations:**
    - **Element-wise operations:** Operations performed element-wise on tensors (e.g., addition, multiplication).
    - **Matrix operations:** Linear algebra operations (e.g., matrix multiplication, matrix inversion).

- **Example:**
  ```python
  import tensorflow as tf
  
  # Define tensors (constants)
  scalar = tf.constant(3)  # Scalar tensor
  vector = tf.constant([1, 2, 3])  # 1D tensor (vector)
  matrix = tf.constant([[1, 2, 3], [4, 5, 6]])  # 2D tensor (matrix)
  
  # Perform operations
  result1 = scalar + 5
  result2 = tf.square(vector)
  result3 = tf.matmul(matrix, matrix)
  
  # Print results
  print("Scalar + 5 =", result1.numpy())
  print("Square of vector =", result2.numpy())
  print("Matrix multiplication =", result3.numpy())
  ```

#### 2. Computational Graph Concept

- **Computational Graph:**
  - TensorFlow programs are based on computational graphs where nodes represent operations and edges represent tensors (data).
  - **Benefits:**
    - **Optimization:** TensorFlow can optimize the execution of operations in the graph.
    - **Visualization:** Provides a clear representation of dependencies and computations.

- **Example:**
  ```python
  import tensorflow as tf
  
  # Define tensors and operations
  a = tf.constant(2)
  b = tf.constant(3)
  c = tf.add(a, b)  # Operation (addition)
  
  # Print computational graph
  print("Nodes in the graph:", tf.get_default_graph().as_graph_def())
  ```

#### 3. Sessions and Execution

- **Sessions:**
  - In TensorFlow 1.x, sessions are used to execute operations and evaluate tensors within a computational graph.
  - **Execution:**
    - TensorFlow 2.x uses eager execution by default, where operations are evaluated immediately.

- **Example (TensorFlow 1.x):**
  ```python
  import tensorflow.compat.v1 as tf
  tf.disable_v2_behavior()
  
  # Define tensors and operations
  a = tf.constant(2)
  b = tf.constant(3)
  c = tf.add(a, b)
  
  # Create session and execute graph
  with tf.Session() as sess:
      result = sess.run(c)
      print("Result:", result)
  ```

### Key Points:
- **Tensors and Operations:** Tensors are fundamental data units in TensorFlow, and operations define computations on tensors.
- **Computational Graph:** Represents operations and dependencies in TensorFlow, facilitating optimization and visualization.
- **Sessions and Execution:** TensorFlow 1.x uses sessions to execute graphs, while TensorFlow 2.x employs eager execution for immediate computation.

These foundational concepts of tensors, operations, computational graphs, and execution methods lay the groundwork for understanding how TensorFlow processes and manipulates data in machine learning applications.