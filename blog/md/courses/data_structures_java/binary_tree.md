# Binary Tree

A **Binary Tree** is a hierarchical data structure where each node has at most two children referred to as the **left child** and the **right child**. It is widely used for searching, sorting, and hierarchical data representation.

### **Binary Tree Structure**

Each node in the tree has the following properties:
1. **Data**: The value stored in the node.
2. **Left Child**: A reference to the left child node.
3. **Right Child**: A reference to the right child node.

### **Binary Tree Implementation in Java**

Below is an example of a simple **Binary Tree** implementation in Java. It covers:
1. **Insert**: Adding elements to the tree.
2. **Traversal**: In-order, pre-order, and post-order traversals.
3. **Search**: Searching for an element in the tree.

### 1. **Binary Tree Node Class**

```java
class Node {
    int data;   // Data in the node
    Node left;  // Left child
    Node right; // Right child

    // Constructor to create a new node
    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
```

### 2. **Binary Tree Class**

```java
class BinaryTree {
    Node root; // Root node of the binary tree

    // Constructor to initialize the binary tree
    public BinaryTree() {
        root = null;  // Initially, the tree is empty
    }

    // Method to insert a node in the binary tree
    public void insert(int data) {
        root = insertRec(root, data);
    }

    // Recursive function to insert a new node with the given data
    private Node insertRec(Node root, int data) {
        // If the tree is empty, create a new node
        if (root == null) {
            root = new Node(data);
            return root;
        }

        // Otherwise, recur down the tree
        if (data < root.data) {
            root.left = insertRec(root.left, data);  // Insert in the left subtree
        } else if (data > root.data) {
            root.right = insertRec(root.right, data);  // Insert in the right subtree
        }

        // Return the unchanged root node
        return root;
    }

    // In-order traversal (Left, Root, Right)
    public void inorder() {
        inorderRec(root);
    }

    private void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);  // Traverse left subtree
            System.out.print(root.data + " ");  // Visit the root
            inorderRec(root.right); // Traverse right subtree
        }
    }

    // Pre-order traversal (Root, Left, Right)
    public void preorder() {
        preorderRec(root);
    }

    private void preorderRec(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");  // Visit the root
            preorderRec(root.left);  // Traverse left subtree
            preorderRec(root.right); // Traverse right subtree
        }
    }

    // Post-order traversal (Left, Right, Root)
    public void postorder() {
        postorderRec(root);
    }

    private void postorderRec(Node root) {
        if (root != null) {
            postorderRec(root.left);  // Traverse left subtree
            postorderRec(root.right); // Traverse right subtree
            System.out.print(root.data + " ");  // Visit the root
        }
    }

    // Search for a value in the binary tree
    public boolean search(int key) {
        return searchRec(root, key);
    }

    private boolean searchRec(Node root, int key) {
        // Base case: root is null or key is present at the root
        if (root == null) {
            return false;
        }
        if (root.data == key) {
            return true;
        }

        // Key is greater than the root's data
        if (key > root.data) {
            return searchRec(root.right, key);
        }

        // Key is smaller than the root's data
        return searchRec(root.left, key);
    }
}
```

### 3. **Main Class to Demonstrate Binary Tree Operations**

```java
public class Main {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();

        // Inserting nodes into the binary tree
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);

        // Displaying the tree using different traversals
        System.out.println("In-order traversal:");
        tree.inorder();  // Output: 20 30 40 50 60 70 80
        System.out.println();

        System.out.println("Pre-order traversal:");
        tree.preorder();  // Output: 50 30 20 40 70 60 80
        System.out.println();

        System.out.println("Post-order traversal:");
        tree.postorder();  // Output: 20 40 30 60 80 70 50
        System.out.println();

        // Searching for a value in the binary tree
        int key = 60;
        System.out.println("Is " + key + " in the tree? " + tree.search(key));  // Output: true

        key = 100;
        System.out.println("Is " + key + " in the tree? " + tree.search(key));  // Output: false
    }
}
```

### **Explanation:**
- **Node Class**: Represents each node in the tree. Each node contains data and references to its left and right child nodes.
- **BinaryTree Class**:
  - **insert()**: Adds a new node with the given value to the tree.
  - **inorder()**: Performs in-order traversal of the tree (left, root, right).
  - **preorder()**: Performs pre-order traversal of the tree (root, left, right).
  - **postorder()**: Performs post-order traversal of the tree (left, right, root).
  - **search()**: Searches for a specific value in the binary tree.
- **Main Class**: Demonstrates how to create and manipulate a binary tree, including inserting elements, performing different tree traversals, and searching for a value.

### **Sample Output:**

```
In-order traversal:
20 30 40 50 60 70 80 

Pre-order traversal:
50 30 20 40 70 60 80 

Post-order traversal:
20 40 30 60 80 70 50 

Is 60 in the tree? true
Is 100 in the tree? false
```

### **Time Complexity:**
- **insert()**: O(h) – Where h is the height of the tree. In the worst case (for an unbalanced tree), this can be O(n), where n is the number of nodes.
- **search()**: O(h) – Similarly, searching for a value requires traversing the tree, which takes time proportional to the height of the tree.
- **inorder(), preorder(), postorder()**: O(n) – All these traversals require visiting each node once, so the time complexity is linear in terms of the number of nodes.

### **Balanced vs. Unbalanced Binary Tree**:
- The above implementation assumes the binary tree is unbalanced, meaning the tree can grow in any direction. This can lead to a skewed tree with height O(n), which would result in slower operations.
- A **Balanced Binary Search Tree (BST)**, such as an **AVL Tree** or **Red-Black Tree**, ensures that the tree remains balanced, which keeps the height logarithmic (O(log n)) and operations efficient.

## Full Binary Tree

A **Full Binary Tree** is a type of binary tree in which every node has either 0 or 2 children. In other words, each node is either a leaf node (with no children) or an internal node (with exactly two children).

### **Properties of a Full Binary Tree:**
1. **Node Degree**: Every node has either 0 or 2 children.
2. **Leaf Nodes**: All leaf nodes are at the same level.
3. **Height**: The height of a full binary tree is defined as the number of edges on the longest path from the root to a leaf node.
4. **Number of Nodes**: If the height of the tree is **h**, the number of nodes **n** in a full binary tree is always:
   \[
   n = 2^{h+1} - 1
   \]
   This means that a full binary tree always has **1, 3, 7, 15, 31...** nodes for heights **0, 1, 2, 3, 4...** respectively.

![full_binary_tree](full_binary_tree.png)

### **Full Binary Tree Implementation in Java**

A **Full Binary Tree** can be represented in a similar way as a regular binary tree. Below is a Java implementation that demonstrates:
1. **Insertion**: Adds nodes to the tree.
2. **Traversal**: In-order, pre-order, and post-order traversal to display the tree.
3. **Checking Fullness**: Verifies whether a given binary tree is full or not.

### 1. **Node Class**

```java
class Node {
    int data;  // Data in the node
    Node left, right;  // Left and right children

    // Constructor to create a new node
    public Node(int data) {
        this.data = data;
        this.left = this.right = null;
    }
}
```

### 2. **Full Binary Tree Class**

```java
class FullBinaryTree {
    private Node root;  // Root node of the tree

    // Constructor to initialize the tree with an empty root
    public FullBinaryTree() {
        root = null;
    }

    // Insert a node into the tree (simple level order insertion for a full tree)
    public void insert(int data) {
        root = insertLevelOrder(root, data);
    }

    private Node insertLevelOrder(Node root, int data) {
        if (root == null) {
            return new Node(data);  // If the tree is empty, create a new node
        }

        // Insert the node in such a way that we maintain the fullness property
        if (root.left == null) {
            root.left = new Node(data);  // Add as left child if left child is empty
        } else if (root.right == null) {
            root.right = new Node(data);  // Add as right child if right child is empty
        } else {text
    }

    // Pre-order traversal (Root, Left, Right)
    public void preorder() {
        preorderRec(root);
    }

    private void preorderRec(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");  // Visit the root
            preorderRec(root.left);  // Traverse left subtree
            preorderRec(root.right); // Traverse right subtree
        }
    }

    // Post-order traversal (Left, Right, Root)
    public void postorder() {
        postorderRec(root);
    }

    private void postorderRec(Node root) {
        if (root != null) {
            postorderRec(root.left);  // Traverse left subtree
            postorderRec(root.right); // Traverse right subtree
            System.out.print(root.data + " ");  // Visit the root
        }
    }

    // Check if the tree is full
    public boolean isFull() {
        return isFullTree(root);
    }

    private boolean isFullTree(Node node) {
        if (node == null) {
            return true;  // An empty tree is considered full
        }

        if (node.left == null && node.right == null) {
            return true;  // A leaf node is full by definition
        }

        if (node.left != null && node.right != null) {
            return isFullTree(node.left) && isFullTree(node.right);  // Both children are present, check recursively
        }

        return false;  // If only one child is missing, the tree is not full
    }
}
```

### 3. **Main Class to Demonstrate Full Binary Tree Operations**

```java
public class Main {
    public static void main(String[] args) {
        FullBinaryTree tree = new FullBinaryTree();

        // Inserting nodes into the Full Binary Tree
        tree.insert(1);
        tree.insert(2);
        tree.insert(3);
        tree.insert(4);
        tree.insert(5);
        tree.insert(6);
        tree.insert(7);

        // Display the tree using different traversal methods
        System.out.println("In-order traversal:");
        tree.inorder();  // Output: 4 2 5 1 6 3 7
        System.out.println();

        System.out.println("Pre-order traversal:");
        tree.preorder();  // Output: 1 2 4 5 3 6 7
        System.out.println();

        System.out.println("Post-order traversal:");
        tree.postorder();  // Output: 4 5 2 6 7 3 1
        System.out.println();

        // Checking if the tree is a full binary tree
        System.out.println("Is the tree full? " + tree.isFull());  // Output: true
    }
}
```

### **Explanation:**
1. **Node Class**: Represents each node in the tree. It contains data and references to the left and right children.
2. **FullBinaryTree Class**:
   - **insert()**: Adds nodes to the tree. It ensures that the tree remains full by inserting nodes into a level-order fashion. If a node has only one child, the tree will not be considered full.
   - **inorder(), preorder(), postorder()**: These are different tree traversal methods. In-order, pre-order, and post-order traversals are implemented recursively.
   - **isFull()**: Checks whether the tree is full by recursively ensuring that each internal node has exactly two children and every leaf node has no children.
3. **Main Class**: Demonstrates how to use the Full Binary Tree by performing insertion, tree traversal, and checking whether the tree is full.

### **Sample Output:**

```
In-order traversal:
4 2 5 1 6 3 7 

Pre-order traversal:
1 2 4 5 3 6 7 

Post-order traversal:
4 5 2 6 7 3 1 

Is the tree full? true
```

### **Time Complexity:**
- **insert()**: O(n) – Inserting a node requires traversing the tree to find an empty spot.
- **search()**: O(n) – Searching in a full binary tree can take linear time since the structure is not necessarily balanced.
- **isFull()**: O(n) – Checking if the tree is full involves recursively checking all the nodes to ensure they satisfy the fullness property.
- **Traversal**: O(n) – Tree traversal (in-order, pre-order, post-order) visits every node exactly once.

### **Space Complexity:**
- The space complexity is O(n), where n is the number of nodes in the tree. Each node requires space for its data and child references.

### **Conclusion:**
The Full Binary Tree ensures that each internal node has exactly two children, making it a highly structured type of binary tree. However, the key disadvantage is that it may not always be perfectly balanced (e.g., the number of leaf nodes could be imbalanced). For practical purposes, a **Complete Binary Tree** or **Balanced Binary Tree** (like AVL or Red-Black trees) is often preferred in dynamic applications.

## Complete Binary Tree

A **Complete Binary Tree** is a type of binary tree where all levels are completely filled except possibly the last level. At the last level, all nodes are as far left as possible. This structure ensures that the tree is balanced, and the tree remains compact.

### **Properties of a Complete Binary Tree:**
1. **Perfectly Balanced**: All levels are filled except the last one.
2. **Last Level**: All nodes at the last level are filled from left to right.
3. **Height**: The height of a complete binary tree is **log(n)**, where **n** is the number of nodes.
4. **Efficient Memory Use**: Since all nodes are filled left to right, there are no gaps, and the tree uses memory efficiently.

### **Difference Between Full and Complete Binary Trees:**
- **Full Binary Tree**: Every node has either 0 or 2 children.
- **Complete Binary Tree**: All levels are filled except possibly the last, and the last level is filled from left to right.

### **Complete Binary Tree Implementation in Java**

Here, we will implement a **Complete Binary Tree** with basic operations like insertion and traversal. We will use an **array-based** representation to ensure that the nodes are filled left to right, which naturally fits the structure of a complete binary tree.

### 1. **CompleteBinaryTree Class**

```java
class CompleteBinaryTree {
    private int[] tree;  // Array to store tree elements
    private int size;    // Number of nodes in the tree
    private int capacity; // Maximum capacity of the tree

    // Constructor to initialize the tree with a fixed capacity
    public CompleteBinaryTree(int capacity) {
        this.capacity = capacity;
        this.tree = new int[capacity];
        this.size = 0;
    }

    // Insert a new element into the complete binary tree
    public void insert(int value) {
        if (size >= capacity) {
            System.out.println("Tree is full. Cannot insert " + value);
            return;
        }
        tree[size] = value; // Insert value at the next available position
        size++;  // Increment the size of the tree
    }

    // Perform in-order traversal (Left, Root, Right)
    public void inorder() {
        inorderRec(0); // Start traversal from the root (index 0)
    }

    private void inorderRec(int index) {
        if (index >= size) {
            return; // If index is out of bounds, return
        }
        inorderRec(2 * index + 1); // Traverse left child
        System.out.print(tree[index] + " ");  // Visit the root
        inorderRec(2 * index + 2); // Traverse right child
    }

    // Perform pre-order traversal (Root, Left, Right)
    public void preorder() {
        preorderRec(0); // Start traversal from the root (index 0)
    }

    private void preorderRec(int index) {
        if (index >= size) {
            return; // If index is out of bounds, return
        }
        System.out.print(tree[index] + " ");  // Visit the root
        preorderRec(2 * index + 1); // Traverse left child
        preorderRec(2 * index + 2); // Traverse right child
    }

    // Perform post-order traversal (Left, Right, Root)
    public void postorder() {
        postorderRec(0); // Start traversal from the root (index 0)
    }

    private void postorderRec(int index) {
        if (index >= size) {
            return; // If index is out of bounds, return
        }
        postorderRec(2 * index + 1); // Traverse left child
        postorderRec(2 * index + 2); // Traverse right child
        System.out.print(tree[index] + " ");  // Visit the root
    }

    // Check if the tree is full
    public boolean isFull() {
        return size == capacity;
    }

    // Get the number of nodes in the tree
    public int getSize() {
        return size;
    }
}
```

### 2. **Main Class to Demonstrate Complete Binary Tree Operations**

```java
public class Main {
    public static void main(String[] args) {
        // Create a Complete Binary Tree with capacity 7
        CompleteBinaryTree tree = new CompleteBinaryTree(7);

        // Insert elements into the tree
        tree.insert(10);
        tree.insert(20);
        tree.insert(30);
        tree.insert(40);
        tree.insert(50);
        tree.insert(60);
        tree.insert(70);

        // Try to insert another element (this should fail as the tree is full)
        tree.insert(80);

        // Display the tree using different traversals
        System.out.println("In-order traversal:");
        tree.inorder();  // Output: 40 20 50 10 60 30 70
        System.out.println();

        System.out.println("Pre-order traversal:");
        tree.preorder();  // Output: 10 20 40 50 30 60 70
        System.out.println();

        System.out.println("Post-order traversal:");
        tree.postorder();  // Output: 40 50 20 60 70 30 10
        System.out.println();

        // Check if the tree is full
        System.out.println("Is the tree full? " + tree.isFull());  // Output: true

        // Get the number of nodes in the tree
        System.out.println("Size of the tree: " + tree.getSize());  // Output: 7
    }
}
```

### **Explanation:**
1. **CompleteBinaryTree Class**:
   - **insert()**: Adds a new node to the tree, placing it in the first available spot (in left-to-right order). If the tree is full, it prints an error message.
   - **inorder(), preorder(), postorder()**: These methods perform the respective tree traversals (left-to-right, root-left-right, left-right-root).
   - **isFull()**: Checks whether the tree has reached its maximum capacity.
   - **getSize()**: Returns the number of nodes in the tree.

2. **Main Class**: This class demonstrates how to create a **Complete Binary Tree**, insert nodes into the tree, and perform various tree operations (in-order, pre-order, post-order traversal).

### **Sample Output:**

```
In-order traversal:
40 20 50 10 60 30 70 

Pre-order traversal:
10 20 40 50 30 60 70 

Post-order traversal:
40 50 20 60 70 30 10 

Is the tree full? true
Size of the tree: 7
```

### **Time Complexity:**
- **Insertion**: O(1) – Inserting a node into a complete binary tree is always done at the next available position (the next level in the tree).
- **Traversal**: O(n) – Traversing the entire tree (in-order, pre-order, or post-order) requires visiting every node exactly once.
- **isFull()**: O(1) – Checking if the tree is full is a constant-time operation since we simply check if the size equals the capacity.

### **Space Complexity:**
- The space complexity is O(n), where **n** is the number of nodes in the tree. The tree is stored in an array, and the space required is proportional to the number of elements.

### **Conclusion:**
The **Complete Binary Tree** structure ensures that the tree remains compact, with all levels completely filled except possibly the last, which is filled from left to right. This is ideal for applications like **binary heaps** (used in priority queues) and other scenarios where efficient memory usage and balanced tree structure are essential.
