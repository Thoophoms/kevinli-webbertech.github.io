# AVL Tree

## Definition of an AVL Tree:

An **AVL Tree** is a **self-balancing binary search tree (BST)** in which the difference in heights between the left and right subtrees of any node (called the **balance factor**) is at most **1**. This property ensures that the tree remains balanced, providing efficient performance for operations such as insertion, deletion, and search.

### Key Characteristics of an AVL Tree:
1. **Binary Search Tree (BST) Property**: Like any BST, for every node:
   - The **left child** contains values smaller than the node.
   - The **right child** contains values greater than the node.

2. **Balance Factor**: The balance factor of any node is defined as:
   ```
   Balance Factor = Height of Left Subtree - Height of Right Subtree
   ```
   - For an AVL tree to remain balanced, the balance factor of every node must be either **-1**, **0**, or **1**.
   - If a node’s balance factor becomes less than -1 or greater than 1, the tree is considered unbalanced, and rotations are needed to restore balance.

3. **Rotations**: When the tree becomes unbalanced due to an insertion or deletion, the tree can be rebalanced using **rotations**. There are four types of rotations:
   - **Left Rotation (LL Rotation)**: Applied when a node becomes unbalanced due to the left child of its left subtree.
   - **Right Rotation (RR Rotation)**: Applied when a node becomes unbalanced due to the right child of its right subtree.
   - **Left-Right Rotation (LR Rotation)**: A combination of a left rotation followed by a right rotation, applied when a node becomes unbalanced due to the right child of its left subtree.
   - **Right-Left Rotation (RL Rotation)**: A combination of a right rotation followed by a left rotation, applied when a node becomes unbalanced due to the left child of its right subtree.

4. **Height Calculation**: The height of a node is the length of the longest path from that node to a leaf node. The height is used to calculate the balance factor of nodes.

### Example of AVL Tree:

Let’s consider the following numbers: **30, 20, 40, 10, 25, 50**. After inserting these numbers into an AVL tree, it would look like this:

```
       30
      /  \
    20    40
   /  \     \
 10   25    50
```

In this example, the tree is balanced because the balance factor of every node is either -1, 0, or 1.

---

### Operations on an AVL Tree:

1. **Insertion**: 
   - Inserting a new node into an AVL tree follows the same rules as a regular binary search tree.
   - After insertion, you check the balance factor of the nodes, and if any node has a balance factor of **-2** or **+2**, you perform the appropriate rotation to restore balance.

2. **Deletion**:
   - Deleting a node follows the standard binary search tree deletion process.
   - After deletion, you may need to check and restore the balance of the tree by performing rotations, similar to insertion.

3. **Searching**:
   - Searching in an AVL tree is similar to searching in a regular binary search tree. The difference is that, due to the self-balancing property, the height of the tree is guaranteed to remain logarithmic, ensuring that the search operation is efficient.

### Example of Rotations:

1. **Left Rotation (LL Rotation)**: If a node becomes unbalanced because the left subtree is too tall (left-heavy), a left rotation is performed to restore balance.

   Before Left Rotation:
   ```
        30
       /
     20
    /
   10
   ```

   After Left Rotation:
   ```
        20
       /  \
     10    30
   ```

2. **Right Rotation (RR Rotation)**: If a node becomes unbalanced because the right subtree is too tall (right-heavy), a right rotation is performed to restore balance.

   Before Right Rotation:
   ```
        10
          \
           20
             \
              30
   ```

   After Right Rotation:
   ```
        20
       /  \
     10    30
   ```

3. **Left-Right (LR) Rotation**: When the left child of a node is unbalanced due to its right subtree, a combination of **left rotation** followed by a **right rotation** is performed.

4. **Right-Left (RL) Rotation**: When the right child of a node is unbalanced due to its left subtree, a combination of **right rotation** followed by a **left rotation** is performed.

---

### Uses of AVL Trees:

1. **Efficient Search Operations**:
   - The primary use of AVL trees is in scenarios where efficient searching is needed. Because AVL trees are balanced, they guarantee that search operations will be performed in \( O(\log n) \) time, where `n` is the number of nodes in the tree. This makes AVL trees suitable for applications like dictionary lookups, symbol tables, and more.

2. **Self-Balancing Data Structure**:
   - AVL trees are used in applications where data is frequently inserted and deleted. Since the tree remains balanced after every operation (through rotations), the search, insertion, and deletion operations always take logarithmic time, making AVL trees ideal for applications that require fast, dynamic data access.

3. **Database Indexing**:
   - In databases, indexing is crucial for fast data retrieval. AVL trees are used for indexing because of their balanced nature, which ensures that queries (such as searching for records) are executed in \( O(\log n) \) time.

4. **Memory Management**:
   - In memory allocators and deallocators, AVL trees can be used to efficiently manage free blocks of memory. The tree structure allows quick insertion and deletion of memory blocks while keeping the available memory sorted.

5. **Operating Systems**:
   - AVL trees are used in operating systems for managing resources such as processes, tasks, or memory segments, ensuring efficient allocation and access.

6. **Network Routing**:
   - AVL trees can be used in network routing algorithms, where maintaining an efficient and balanced structure is important for quickly determining the best path or routing decisions.

7. **Autocompletion and Auto-suggestions**:
   - In search engines, web browsers, and text editors, AVL trees are used to efficiently store and retrieve data for autocompletion and auto-suggestions. The tree allows fast retrieval of suggestions based on user input.

---

### Advantages of AVL Trees:
1. **Efficient Operations**: The self-balancing property ensures that search, insertion, and deletion operations are always performed in \( O(\log n) \) time, even in the worst case.
2. **Logarithmic Height**: AVL trees maintain a logarithmic height, ensuring that the tree does not become skewed or degenerate into a linked list, which can happen in unbalanced binary search trees.
3. **Predictable Performance**: Unlike unbalanced binary search trees, the AVL tree guarantees consistent performance due to its balanced nature.

### Disadvantages of AVL Trees:
1. **Complexity in Implementation**: AVL trees are more complex to implement compared to simple binary search trees because of the need to calculate balance factors and perform rotations after each operation.
2. **Higher Overhead**: Maintaining balance during insertion and deletion requires additional operations (rotations), which can make these operations more expensive compared to a simpler BST. However, this is still \( O(\log n) \), and the extra complexity provides a significant performance improvement in the long run.

---

### Summary:

An **AVL Tree** is a **self-balancing binary search tree** that guarantees logarithmic time complexity for search, insert, and delete operations by ensuring the balance factor of every node is between **-1** and **+1**. It is used in applications that require fast dynamic data access and sorting, such as databases, memory management, and network routing. Although the tree is more complex to implement than a standard binary search tree, it ensures consistently efficient operations, making it a valuable data structure in many real-world applications.

## Python Implementation

Here's a Python implementation of an **AVL Tree**. This includes methods for **insertion**, **rotation**, and **balancing** the tree. After that, we’ll also include the **in-order traversal** method to visualize the tree’s structure.

### Python Code for AVL Tree Implementation:

```python
class Node:
    def __init__(self, key):
        self.key = key  # Node value
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Initial height of the node

class AVLTree:
    def __init__(self):
        self.root = None  # The root of the AVL tree

    # Get the height of a node
    def height(self, node):
        if not node:
            return 0
        return node.height

    # Get the balance factor of a node
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Perform a right rotation (single rotation)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        # Return the new root
        return x

    # Perform a left rotation (single rotation)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        # Return the new root
        return y

    # Insert a node into the AVL Tree
    def insert(self, node, key):
        # Step 1: Perform normal BST insertion
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Step 2: Update height of this ancestor node
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Step 3: Get the balance factor of this node to check whether this node became unbalanced
        balance = self.balance_factor(node)

        # Step 4: If the node becomes unbalanced, then there are 4 cases

        # Left Left Case (Single right rotation)
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case (Single left rotation)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case (Double rotation: Left rotation followed by Right rotation)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case (Double rotation: Right rotation followed by Left rotation)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the (unchanged) node pointer
        return node

    # Function to insert a new key
    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    # In-order traversal of the tree (for visualization)
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print(root.key, end=" ")
        self.in_order(root.right)

# Example usage:
if __name__ == "__main__":
    tree = AVLTree()

    # Insert keys into the AVL tree
    keys = [20, 10, 30, 5, 15, 25, 35, 40, 50]
    for key in keys:
        tree.insert_key(key)

    # Print in-order traversal of the AVL tree
    print("In-order traversal of the AVL tree:")
    tree.in_order(tree.root)
```

### Explanation of the AVL Tree Implementation:

1. **Node Class**: 
   - Each node has a `key` (value), a left and right child, and a `height` property. The height of a node is essential for calculating the balance factor.

2. **AVLTree Class**: 
   - The `AVLTree` class contains the methods for inserting a node, performing rotations (left and right), and maintaining balance.
   
3. **Insertion**: 
   - When a new key is inserted, it’s placed just like a regular binary search tree insertion. After insertion, the tree is rebalanced by checking the balance factor of each node starting from the newly inserted node up to the root.

4. **Rotations**: 
   - **Right Rotate**: A right rotation is done when the left subtree of a node is too high (left-heavy).
   - **Left Rotate**: A left rotation is done when the right subtree of a node is too high (right-heavy).
   - **Left-Right Rotate**: When the left child of the left subtree is not balanced, a left-right rotation is performed.
   - **Right-Left Rotate**: When the right child of the right subtree is not balanced, a right-left rotation is performed.

5. **In-Order Traversal**: 
   - The `in_order` method prints the keys of the AVL tree in sorted order (ascending), which helps visualize the tree structure.

### Example Output:

If you run the example code with the keys `[20, 10, 30, 5, 15, 25, 35, 40, 50]`, the **in-order traversal** will output:

```
In-order traversal of the AVL tree:
5 10 15 20 25 30 35 40 50
```

The AVL tree ensures that the keys are always balanced and displayed in sorted order when traversed in-order.

### Summary of Operations:
- **Insertion**: Inserts elements while keeping the tree balanced.
- **Rotations**: Ensures the AVL tree remains balanced after insertion or deletion.
- **In-Order Traversal**: Helps to visualize the sorted structure of the tree.

This AVL tree implementation guarantees \( O(\log n) \) time complexity for insertion, deletion, and searching, thanks to its self-balancing property. The rotations keep the tree balanced during each insertion.