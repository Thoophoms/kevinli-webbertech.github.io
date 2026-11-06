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


```python
class RedBlackNode:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(None, "black")
        self.root = self.NIL
    
    def insert(self, data):
        new_node = RedBlackNode(data)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root
        
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        new_node.color = "red"
        self.fix_insert(new_node)
    
    def fix_insert(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"
    
    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child
    
    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder_traversal(self, node):
        if node != self.NIL:
            self.inorder_traversal(node.left)
            print(node.data, "(", node.color, ")", end=" -> ")
            self.inorder_traversal(node.right)

# Testing Huffman Encoding and Decoding
if __name__ == "__main__":
    
    # Testing Red-Black Tree
    rbt = RedBlackTree()
    for num in [20, 15, 25, 10, 5, 1]:
        rbt.insert(num)
    print("\nRed-Black Tree Inorder Traversal:")
    rbt.inorder_traversal(rbt.root)
```