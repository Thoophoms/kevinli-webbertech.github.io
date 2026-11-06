# Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a type of binary tree in which each node has at most two children, referred to as the **left** and **right** child. The key characteristic of a binary search tree is that it maintains a specific order among the nodes, which allows for efficient searching, insertion, and deletion operations.

### Properties of a Binary Search Tree:
1. **Binary Tree Structure**: Each node has at most two children.
   - The **left child** of a node contains values **less than** the node’s value.
   - The **right child** of a node contains values **greater than** the node’s value.
   
2. **Recursive Definition**: A BST is a tree where:
   - The **left subtree** of a node contains only nodes with values **less than** the node's value.
   - The **right subtree** of a node contains only nodes with values **greater than** the node's value.
   - Both the left and right subtrees are themselves BSTs.

3. **No Duplicate Values**: Typically, binary search trees do not allow duplicate values, although variations of BSTs may allow them with certain rules for placement.

4. **Search Property**: Due to the order property, searching for an element in a BST can be done efficiently by traversing the tree:
   - If the value to be searched is smaller than the node, the search proceeds to the **left** subtree.
   - If the value to be searched is larger, the search proceeds to the **right** subtree.
   - This process continues recursively until the value is found or the search reaches a leaf node.

### Example of a Binary Search Tree:
Let's say we have the following numbers to insert into an empty binary search tree: **50, 30, 70, 20, 40, 60, 80**.

After inserting them into the tree one by one, the tree would look like this:

```
       50
      /  \
    30    70
   /  \   /  \
 20   40 60   80
```

In this tree:
- The **left subtree** of `50` contains values smaller than `50` (`30`, `20`, `40`).
- The **right subtree** of `50` contains values larger than `50` (`70`, `60`, `80`).
- This order ensures efficient searching: if you are searching for `60`, you would go to the right of `50`, then go to the left of `70` to find it.

### Operations on a Binary Search Tree:
1. **Search**: To search for a value, start at the root and recursively move to the left or right child based on whether the target value is smaller or larger than the current node’s value.
   
   - **Time Complexity**: On average, the search operation has a time complexity of \(O(\log n)\) in a balanced BST. However, in the worst case (if the tree is unbalanced), it can degrade to \(O(n)\).

2. **Insertion**: To insert a value into the tree, start at the root and traverse left or right based on the value being inserted. Once you find a **null** child (a position where there is no node), you insert the new node.

3. **Deletion**: Deleting a node from a BST requires careful handling of three cases:
   - **Node with no children** (leaf node): Simply remove the node.
   - **Node with one child**: Remove the node and link its parent to its only child.
   - **Node with two children**: Find the **in-order successor** (the smallest node in the right subtree) or **in-order predecessor** (the largest node in the left subtree) and replace the node to be deleted with this successor/predecessor.

4. **Traversal**: There are several ways to traverse a BST:
   - **In-order**: Visit the left subtree, then the current node, then the right subtree. This traversal visits nodes in **ascending order**.
   - **Pre-order**: Visit the current node first, then recursively visit the left and right subtrees.
   - **Post-order**: Visit the left subtree, then the right subtree, and finally the current node.
   
   Example of in-order traversal for the BST above would give the sorted list: **20, 30, 40, 50, 60, 70, 80**.

### Advantages of a Binary Search Tree:
- **Efficient Search**: With a balanced BST, searching for a value can be very efficient.
- **Ordered Structure**: In-order traversal of a BST produces the values in sorted order, which is useful for sorting algorithms and searching for ranges of values.
- **Dynamic Insertion/Deletion**: BSTs allow for dynamic insertion and deletion of values while maintaining their ordered structure.

### Time Complexity of Operations:
- **Search, Insert, and Delete**: In a balanced BST, the time complexity for these operations is \(O(\log n)\), where `n` is the number of nodes in the tree.
- However, in the worst case, if the tree becomes unbalanced (degenerates into a linked list), the time complexity can degrade to \(O(n)\).

### Balanced vs Unbalanced BST:
- A **balanced BST** (like an AVL Tree or Red-Black Tree) ensures that the height of the tree is logarithmic, maintaining \(O(\log n)\) time complexity for operations.
- An **unbalanced BST** can degrade into a **linear structure** (like a linked list), where the height of the tree is \(O(n)\), making operations inefficient.

---

### Summary:
A **Binary Search Tree (BST)** is a binary tree where each node follows the property that its left children are smaller and right children are larger than the node. This structure allows for efficient search, insertion, and deletion operations. Balanced BSTs ensure that these operations remain efficient with a time complexity of \(O(\log n)\), while unbalanced trees can degrade to linear time complexity.


### 1. **BST Node Class**

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

### 2. **Binary Search Tree Class**

```java
class BinarySearchTree {
    Node root; // Root node of the binary search tree

    // Constructor to initialize the BST
    public BinarySearchTree() {
        root = null; // Initially, the tree is empty
    }

    // Insert a node with the given data
    public void insert(int data) {
        root = insertRec(root, data);
    }

    // Recursive function to insert a new node
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

    // Search for a node with the given key
    public boolean search(int key) {
        return searchRec(root, key);
    }

    // Recursive function to search for a node with the given key
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

    // Delete a node with the given key
    public void delete(int key) {
        root = deleteRec(root, key);
    }

    // Recursive function to delete a node with the given key
    private Node deleteRec(Node root, int key) {
        // Base case: root is null
        if (root == null) {
            return root;
        }

        // Traverse the tree to find the node to be deleted
        if (key < root.data) {
            root.left = deleteRec(root.left, key); // Key is smaller, search in left subtree
        } else if (key > root.data) {
            root.right = deleteRec(root.right, key); // Key is greater, search in right subtree
        } else {
            // Node to be deleted is found
            // Case 1: Node has no child (leaf node)
            if (root.left == null && root.right == null) {
                return null;
            }
            // Case 2: Node has one child
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }

            // Case 3: Node has two children
            root.data = minValue(root.right);  // Get the inorder successor
            root.right = deleteRec(root.right, root.data); // Delete the inorder successor
        }

        return root;
    }

    // Find the minimum value node in the tree (used for deletion)
    private int minValue(Node root) {
        int minValue = root.data;
        while (root.left != null) {
            minValue = root.left.data;
            root = root.left;
        }
        return minValue;
    }

    // In-order traversal of the BST (Left, Root, Right)
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

    // Pre-order traversal of the BST (Root, Left, Right)
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

    // Post-order traversal of the BST (Left, Right, Root)
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
}
```

### 3. **Main Class to Demonstrate BST Operations**

```java
public class Main {
    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();

        // Inserting nodes into the BST
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);

        // Display the tree using different traversals
        System.out.println("In-order traversal:");
        tree.inorder();  // Output: 20 30 40 50 60 70 80
        System.out.println();

        System.out.println("Pre-order traversal:");
        tree.preorder();  // Output: 50 30 20 40 70 60 80
        System.out.println();

        System.out.println("Post-order traversal:");
        tree.postorder();  // Output: 20 40 30 60 80 70 50
        System.out.println();

        // Searching for a value in the binary search tree
        int key = 60;
        System.out.println("Is " + key + " in the tree? " + tree.search(key));  // Output: true

        key = 100;
        System.out.println("Is " + key + " in the tree? " + tree.search(key));  // Output: false

        // Deleting a node from the tree
        System.out.println("Deleting node with value 20");
        tree.delete(20);

        // Display the tree after deletion
        System.out.println("In-order traversal after deletion:");
        tree.inorder();  // Output: 30 40 50 60 70 80
    }
}
```

### **Explanation:**
- **Node Class**: Represents each node in the tree. Each node contains data and references to its left and right children.
- **BinarySearchTree Class**:
  - **insert()**: Adds a new node to the tree while maintaining the BST property.
  - **search()**: Searches for a value in the BST.
  - **delete()**: Removes a node from the tree and handles three cases: no children, one child, or two children.
  - **inorder(), preorder(), postorder()**: Perform different types of tree traversal.
- **Main Class**: Demonstrates the creation of a BST, insertion, deletion, searching, and traversal operations.

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
Deleting node with value 20
In-order traversal after deletion:
30 40 50 60 70 80 
```

### **Time Complexity:**
- **insert()**: O(h) – Where h is the height of the tree. In the worst case (for an unbalanced tree), this can be O(n), where n is the number of nodes.
- **search()**: O(h) – Searching takes time proportional to the height of the tree.
- **delete()**: O(h) – Deletion also takes time proportional to the height of the tree.
- **Traversal (inorder, preorder, postorder)**: O(n) – All tree traversal operations visit every node once.

### **Balanced vs. Unbalanced BST**:
- If the tree becomes unbalanced, the height can grow to O(n), which means operations can degrade to O(n).
- A **Balanced Binary Search Tree (BST)** (such as an **AVL Tree** or **Red-Black Tree**) ensures that the tree remains balanced, keeping the height logarithmic (O(log n)) and ensuring that operations remain efficient.

Let me know if you'd like to explore **AVL trees**, **Red-Black trees**, or other advanced topics!