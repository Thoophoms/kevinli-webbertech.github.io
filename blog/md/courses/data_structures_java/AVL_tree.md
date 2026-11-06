An **AVL Tree** (Adelson-Velsky and Landis Tree) is a self-balancing **Binary Search Tree (BST)**, where the difference in heights of the left and right subtrees of any node (called the **balance factor**) is at most 1. This ensures that the tree remains balanced, providing an efficient structure for searching, insertion, and deletion operations.

### **AVL Tree Properties:**
1. **Balanced**: For any node in the tree, the height difference between its left and right subtrees must not exceed 1.
2. **Height**: The height of a node is the number of edges on the longest path from the node to a leaf.
3. **Balance Factor**: The balance factor of a node is the difference between the height of its left subtree and right subtree:
   \[
   \text{Balance Factor} = \text{Height of Left Subtree} - \text{Height of Right Subtree}
   \]
   - If the balance factor is **1**, the node is left-heavy.
   - If the balance factor is **-1**, the node is right-heavy.
   - If the balance factor is **0**, the node is perfectly balanced.

### **AVL Tree Operations:**
1. **Insertion**: After inserting a node, we check if the tree is still balanced. If it's not balanced, we perform rotations to restore balance.
2. **Deletion**: After deleting a node, we may need to re-balance the tree using rotations.
3. **Rotations**: There are four types of rotations that can be used to maintain balance:
   - **Left Rotation (LL)**: Used when the left child is too tall.
   - **Right Rotation (RR)**: Used when the right child is too tall.
   - **Left-Right Rotation (LR)**: A combination of left and right rotations used when the left subtree is right-heavy.
   - **Right-Left Rotation (RL)**: A combination of right and left rotations used when the right subtree is left-heavy.

### **AVL Tree Implementation in Java**

Here is a Java implementation of an AVL Tree with basic operations such as insertion, deletion, rotations, and balance factor management.

### 1. **Node Class**

```java
class Node {
    int data;  // Data stored in the node
    Node left, right;  // Left and right children
    int height;  // Height of the node

    // Constructor to create a new node
    public Node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
        this.height = 1;  // Initially, the height is 1
    }
}
```

### 2. **AVL Tree Class**

```java
class AVLTree {
    Node root;  // Root of the AVL tree

    // Constructor to initialize the tree
    public AVLTree() {
        root = null;
    }

    // Get the height of a node
    private int height(Node node) {
        if (node == null) {
            return 0;
        }
        return node.height;
    }

    // Update the height of a node
    private void updateHeight(Node node) {
        node.height = 1 + Math.max(height(node.left), height(node.right));
    }

    // Get the balance factor of a node
    private int getBalanceFactor(Node node) {
        if (node == null) {
            return 0;
        }
        return height(node.left) - height(node.right);
    }

    // Right rotation
    private Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform the rotation
        x.right = y;
        y.left = T2;

        // Update heights
        updateHeight(y);
        updateHeight(x);

        return x;  // New root
    }

    // Left rotation
    private Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        // Perform the rotation
        y.left = x;
        x.right = T2;

        // Update heights
        updateHeight(x);
        updateHeight(y);

        return y;  // New root
    }

    // Insert a node into the AVL tree
    public void insert(int data) {
        root = insertRec(root, data);
    }

    // Recursive function to insert a node
    private Node insertRec(Node node, int data) {
        // 1. Perform the normal BST insertion
        if (node == null) {
            return new Node(data);
        }

        if (data < node.data) {
            node.left = insertRec(node.left, data);
        } else if (data > node.data) {
            node.right = insertRec(node.right, data);
        } else {  // Duplicates are not allowed
            return node;
        }

        // 2. Update the height of this node
        updateHeight(node);

        // 3. Get the balance factor to check whether this node became unbalanced
        int balance = getBalanceFactor(node);

        // 4. Perform rotations to balance the tree if needed
        if (balance > 1 && data < node.left.data) {
            return rightRotate(node);  // Left-Left case
        }

        if (balance < -1 && data > node.right.data) {
            return leftRotate(node);  // Right-Right case
        }

        if (balance > 1 && data > node.left.data) {
            node.left = leftRotate(node.left);  // Left-Right case
            return rightRotate(node);
        }

        if (balance < -1 && data < node.right.data) {
            node.right = rightRotate(node.right);  // Right-Left case
            return leftRotate(node);
        }

        // Return the (unchanged) node pointer
        return node;
    }

    // Perform in-order traversal of the AVL tree
    public void inorder() {
        inorderRec(root);
    }

    private void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }

    // Search for a node with the given value
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

        // Key is greater than root's data
        if (key > root.data) {
            return searchRec(root.right, key);
        }

        // Key is smaller than root's data
        return searchRec(root.left, key);
    }

    // Delete a node from the AVL tree
    public void delete(int data) {
        root = deleteRec(root, data);
    }

    private Node deleteRec(Node root, int key) {
        // Step 1: Perform the normal BST deletion
        if (root == null) {
            return root;
        }

        if (key < root.data) {
            root.left = deleteRec(root.left, key);
        } else if (key > root.data) {
            root.right = deleteRec(root.right, key);
        } else {
            // Node with only one child or no child
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            // Node with two children: Get the inorder successor (smallest in the right subtree)
            root.data = minValue(root.right);

            // Delete the inorder successor
            root.right = deleteRec(root.right, root.data);
        }

        // Step 2: Update the height of the current node
        updateHeight(root);

        // Step 3: Get the balance factor to check whether the node became unbalanced
        int balance = getBalanceFactor(root);

        // Step 4: Perform rotations to balance the tree
        if (balance > 1 && getBalanceFactor(root.left) >= 0) {
            return rightRotate(root);  // Left-Left case
        }

        if (balance < -1 && getBalanceFactor(root.right) <= 0) {
            return leftRotate(root);  // Right-Right case
        }

        if (balance > 1 && getBalanceFactor(root.left) < 0) {
            root.left = leftRotate(root.left);  // Left-Right case
            return rightRotate(root);
        }

        if (balance < -1 && getBalanceFactor(root.right) > 0) {
            root.right = rightRotate(root.right);  // Right-Left case
            return leftRotate(root);
        }

        return root;
    }

    // Find the minimum value node in the tree (used for deletion)
    private int minValue(Node root) {
        int minValue = root.data;
        while (root.left != null) {
            root = root.left;
            minValue = root.data;
        }
        return minValue;
    }
}
```

### 3. **Main Class to Demonstrate AVL Tree Operations**

```java
public class Main {
    public static void main(String[] args) {
        AVLTree tree = new AVLTree();

        // Inserting nodes into the AVL tree
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);

        // Display the tree using in-order traversal (sorted order)
        System.out.println("In-order traversal of the AVL tree:");
        tree.inorder();  // Output: 20 30 40 50 60 70 80
        System.out.println();

        // Searching for values in the AVL tree
        System.out.println("Is 60 in the tree? " + tree.search(60));  // Output: true
        System.out.println("Is 25 in the tree? " + tree.search(25));  // Output: false

        // Deleting a node from the AVL tree
        tree.delete(20);
        System.out.println("In-order traversal after deletion of 20:");
        tree.inorder();  // Output: 30 40 50 60 70 80
    }
}
```

### **Explanation:**
1. **Node Class**: Represents each node in the AVL tree with data, left and right children, and height.
2. **AVLTree Class**: Manages the AVL tree with operations such as insertion, deletion, search, and tree traversal.
   - **insert()**: Inserts a node and ensures that the tree remains balanced by using rotations.
   - **delete()**: Deletes a node and re-balances the tree if necessary.
   - **search()**: Searches for a value in the tree.
   - **inorder()**: Displays the tree in sorted order using in-order traversal.
   - **Rotation Methods**: Perform rotations (left and right) to maintain balance in the tree.
3. **Main Class**: Demonstrates how to use the AVL Tree by performing insertion, deletion, search, and displaying the tree.

### **Sample Output:**

```
In-order traversal of the AVL tree:
20 30 40 50 60 70 80 

Is 60 in the tree? true
Is 25 in the tree? false
In-order traversal after deletion of 20:
30 40 50 60 70 80 
```

### **Time Complexity:**
- **Insert**: O(log n) – Insertion is efficient in AVL trees, as the height is kept balanced at log(n).
- **Delete**: O(log n) – Deletion involves finding the node and potentially re-balancing the tree.
- **Search**: O(log n) – Searching is efficient due to the tree's balanced structure.
- **Traversal (in-order)**: O(n) – In-order traversal visits each node exactly once.

AVL trees provide **logarithmic time complexity** for all major operations (search, insertion, deletion), making them efficient for large datasets where frequent updates and queries are required.