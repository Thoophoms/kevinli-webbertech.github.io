# Red-Black Tree

A **Red-Black Tree** is a type of self-balancing binary search tree (BST) that ensures efficient searching, insertion, and deletion operations. It's widely used in computer science and has practical applications in various data structures and algorithms. Let's break down its use and benefits:

## Properties of a Red-Black Tree

A Red-Black Tree has several key properties that guarantee balanced behavior:

1. **Binary Search Tree Property**: Like all binary search trees, for any given node:
   - The left child contains values less than the node.
   - The right child contains values greater than the node.

2. **Coloring of Nodes**: Every node in the tree is colored either **red** or **black**.

3. **Properties for Balance**:
   - **Root property**: The root is always black.
   - **Red node property**: No red node can have a red child (i.e., red nodes cannot be adjacent).
   - **Black height property**: Every path from a given node to its descendant null node must have the same number of black nodes.
   - **Leaf property**: Every leaf (null child) is considered black.
   
4. **Height Balance**: The tree maintains a balance, meaning the path from the root to any leaf (or null) is always logarithmic in length. This ensures that the tree doesn't become unbalanced (e.g., degenerating into a linked list).

## Advantages of Red-Black Trees

1. **Balanced Structure**: The red-black tree ensures that the tree stays balanced, preventing it from degenerating into a linear structure (which can happen in a regular binary search tree).
2. **Efficient Operations**: 
   - **Search, insertion, and deletion operations** are all guaranteed to run in \( O(\log n) \) time in the worst case due to the balanced nature of the tree.
   - This makes red-black trees suitable for scenarios where efficient lookups, insertions, and deletions are necessary.
3. **Self-Balancing**: After each insertion or deletion, the red-black tree automatically rebalances itself through rotations and recoloring, ensuring it remains balanced without the need for additional manual intervention.

## Applications of Red-Black Trees

Red-Black Trees are used in situations where balanced trees are essential for maintaining efficiency. Some notable applications include:

1. **Associative Containers in STL (C++)**:
   - **C++ Standard Template Library (STL)** makes use of red-black trees in its **map**, **set**, **multimap**, and **multiset** containers. These containers need to allow efficient insertion, deletion, and searching, and red-black trees provide the necessary balance to guarantee that operations are performed in \( O(\log n) \) time.
  
2. **Implementing Dictionaries and Symbol Tables**:
   - Red-Black Trees are frequently used to implement **dictionaries** or **symbol tables** where key-value pairs need to be stored and accessed efficiently. This is useful in many algorithms, including those in compilers, databases, and file systems.
  
3. **Memory Management**:
   - In systems that implement memory allocation, such as **allocators**, red-black trees can be used to maintain free memory blocks. The ability to quickly insert, delete, and search for available blocks is crucial for efficient memory management.

4. **Priority Queues**:
   - A **priority queue** is a data structure that supports inserting and extracting the "maximum" or "minimum" element efficiently. A red-black tree can be used to implement a priority queue since it provides efficient insertion and extraction operations.

5. **Network Routing Algorithms**:
   - Red-Black Trees can be used in network routing algorithms where efficient path lookups are required, ensuring that data is transmitted through the shortest or most efficient path.

6. **Database Indexing**:
   - Red-Black Trees are used in databases for indexing data, where each row in a table might be indexed by a key. The database can quickly find records based on the key and keep the index balanced.

7. **Sorted Data Maintenance**:
   - Red-Black Trees are useful in applications that require maintaining a collection of **sorted data** while providing efficient operations for insertions and deletions.

## How Does the Red-Black Tree Work?

1. **Insertion**:
   - Insertions in a red-black tree start similarly to a standard binary search tree. After the new node is inserted, it is initially colored **red**.
   - The tree is then checked for violations of red-black properties (such as two adjacent red nodes), and necessary **recoloring** and **rotations** are performed to restore the properties.

2. **Deletion**:
   - Deletion from a red-black tree is more complicated than insertion. After removing a node, the tree might violate red-black properties, and the tree must undergo a series of **recoloring** and **rotations** to restore balance.

3. **Rotations**:
   - A **rotation** is an operation that moves nodes in the tree to maintain balance. There are two types of rotations:
     - **Left Rotation**: A node is rotated to the left to adjust the tree structure.
     - **Right Rotation**: A node is rotated to the right.

   Rotations help in maintaining the tree’s balanced height and are essential for ensuring that the tree does not become unbalanced during insertion and deletion.

---

## Example of Red-Black Tree

Here’s a small example to illustrate how nodes are inserted into a red-black tree:

1. Insert `10` into an empty tree. The tree has only one node, so it becomes the root and is colored **black**.
2. Insert `20`. It's added as a red node. Since no red-red violations occur, the tree remains balanced.
3. Insert `15`. The tree will color and rotate nodes to ensure balance, and after a rotation, it may look something like this:

   ```
         15(B)
        /    \
      10(R)  20(R)
   ```
   After inserting `15`, it ensures the black height property is maintained.

---

## Summary:
- **Red-Black Trees** are a type of self-balancing binary search tree with important properties that ensure balanced search times for insertion, deletion, and search operations.
- They maintain an efficient time complexity of \( O(\log n) \) for these operations, even in the worst case.
- **Practical Uses** include implementing associative containers, dictionaries, priority queues, and memory management systems, among others.


## **Java Implementation of a Red-Black Tree**

The implementation includes the following operations:
1. **Insert**: Inserts a new node into the tree while ensuring that the Red-Black Tree properties are maintained.
2. **Left and Right Rotations**: To maintain balance during insertion and deletion.
3. **Fixing Violations**: After insertion, the tree might violate one or more of the Red-Black Tree properties, which are corrected through specific fixes (recoloring and rotations).

### 1. **Red-Black Tree Node Class**

```java
class Node {
    int data;
    Node parent, left, right;
    int color; // 1 for Red, 0 for Black

    // Constructor for the node
    public Node(int data) {
        this.data = data;
        this.parent = null;
        this.left = null;
        this.right = null;
        this.color = 1; // New nodes are always red
    }
}
```

### 2. **Red-Black Tree Class**

```java
class RedBlackTree {
    private Node root;
    private Node TNULL; // Sentinel node

    // Constructor to initialize the tree
    public RedBlackTree() {
        TNULL = new Node(0);
        TNULL.color = 0; // TNULL is always black
        root = TNULL;
    }

    // Left rotate operation
    private void leftRotate(Node x) {
        Node y = x.right;
        x.right = y.left;
        if (y.left != TNULL) {
            y.left.parent = x;
        }
        y.parent = x.parent;
        if (x.parent == null) {
            root = y;
        } else if (x == x.parent.left) {
            x.parent.left = y;
        } else {
            x.parent.right = y;
        }
        y.left = x;
        x.parent = y;
    }

    // Right rotate operation
    private void rightRotate(Node x) {
        Node y = x.left;
        x.left = y.right;
        if (y.right != TNULL) {
            y.right.parent = x;
        }
        y.parent = x.parent;
        if (x.parent == null) {
            root = y;
        } else if (x == x.parent.right) {
            x.parent.right = y;
        } else {
            x.parent.left = y;
        }
        y.right = x;
        x.parent = y;
    }

    // Fix the tree after insertion
    private void fixInsert(Node k) {
        Node u;
        while (k.parent.color == 1) {
            if (k.parent == k.parent.parent.right) {
                u = k.parent.parent.left;
                if (u.color == 1) {
                    u.color = 0;
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    k = k.parent.parent;
                } else {
                    if (k == k.parent.left) {
                        k = k.parent;
                        rightRotate(k);
                    }
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    leftRotate(k.parent.parent);
                }
            } else {
                u = k.parent.parent.right;
                if (u.color == 1) {
                    u.color = 0;
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    k = k.parent.parent;
                } else {
                    if (k == k.parent.right) {
                        k = k.parent;
                        leftRotate(k);
                    }
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    rightRotate(k.parent.parent);
                }
            }
            if (k == root) {
                break;
            }
        }
        root.color = 0;
    }

    // Insert a new node
    public void insert(int key) {
        Node node = new Node(key);
        node.parent = null;
        node.data = key;
        node.left = TNULL;
        node.right = TNULL;
        node.color = 1; // New node is always red

        Node y = null;
        Node x = root;

        while (x != TNULL) {
            y = x;
            if (node.data < x.data) {
                x = x.left;
            } else {
                x = x.right;
            }
        }

        node.parent = y;
        if (y == null) {
            root = node;
        } else if (node.data < y.data) {
            y.left = node;
        } else {
            y.right = node;
        }

        if (node.parent == null) {
            node.color = 0;
            return;
        }

        if (node.parent.parent == null) {
            return;
        }

        fixInsert(node);
    }

    // In-order traversal
    public void inorder() {
        inorderHelper(this.root);
    }

    private void inorderHelper(Node node) {
        if (node != TNULL) {
            inorderHelper(node.left);
            System.out.print(node.data + " ");
            inorderHelper(node.right);
        }
    }

    // Search for a node
    public boolean search(int key) {
        return searchTreeHelper(this.root, key);
    }

    private boolean searchTreeHelper(Node node, int key) {
        if (node == TNULL) {
            return false;
        }
        if (key == node.data) {
            return true;
        }

        if (key < node.data) {
            return searchTreeHelper(node.left, key);
        }
        return searchTreeHelper(node.right, key);
    }
}
```

### 3. **Main Class to Demonstrate Red-Black Tree Operations**

```java
public class Main {
    public static void main(String[] args) {
        RedBlackTree tree = new RedBlackTree();

        // Insert nodes into the Red-Black Tree
        tree.insert(10);
        tree.insert(20);
        tree.insert(30);
        tree.insert(15);
        tree.insert(25);
        tree.insert(5);

        // Display the tree in in-order (sorted) traversal
        System.out.println("In-order traversal of the Red-Black Tree:");
        tree.inorder();  // Output: 5 10 15 20 25 30
        System.out.println();

        // Searching for a value
        System.out.println("Is 15 in the tree? " + tree.search(15));  // Output: true
        System.out.println("Is 40 in the tree? " + tree.search(40));  // Output: false
    }
}
```

### **Explanation:**
1. **Node Class**: Represents each node in the tree. It includes data, parent, left, and right pointers. It also has a `color` field where `1` represents red and `0` represents black.
2. **RedBlackTree Class**:
   - **insert()**: Inserts a node into the tree, ensuring the Red-Black Tree properties are maintained. It uses the `fixInsert()` function to correct any violations after insertion.
   - **fixInsert()**: Ensures that the tree properties are maintained after insertion by performing appropriate rotations and recoloring.
   - **rotations**: Left and right rotations are used to maintain balance.
   - **inorder()**: Displays the tree in sorted order using in-order traversal.
   - **search()**: Searches for a specific value in the tree.
3. **Main Class**: Demonstrates how to insert nodes into the tree, perform a traversal, and search for a value.

### **Sample Output:**

```
In-order traversal of the Red-Black Tree:
5 10 15 20 25 30 

Is 15 in the tree? true
Is 40 in the tree? false
```

### **Time Complexity:**
- **Insert**: O(log n) – The height of the tree is kept balanced, ensuring efficient insertions.
- **Search**: O(log n) – Searching is efficient due to the balanced structure.
- **Traversal**: O(n) – Traversing the entire tree takes linear time.

### **Rotations Overview:**
- **Left Rotation**: Used when the right subtree of a node becomes too heavy (right-right or right-left case).
- **Right Rotation**: Used when the left subtree of a node becomes too heavy (left-left or left-right case).

These rotations are key to maintaining the balance in the Red-Black Tree, which ensures that all operations (insertion, deletion, and search) remain efficient.