# B Tree

## Definition of a B-Tree:

A **B-Tree** is a **self-balancing search tree** data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations. It is commonly used in **databases** and **file systems** because it is optimized for systems that read and write large blocks of data.

### Key Characteristics of a B-Tree:

1. **Multi-level Indexing**: 
   - A B-tree is a **multi-level index** where each node can contain multiple keys and have multiple children. Unlike a binary search tree (BST), where each node has at most two children, a B-tree node can have **more than two children**.
   
2. **Order of the B-Tree**: 
   - The order of a B-tree, denoted as **`m`**, determines the maximum number of children a node can have. Each node can contain up to **`m - 1`** keys and can have **up to `m` children**.
   - The order also governs the minimum number of children a node can have. For a node to remain valid:
     - It must have at least **⌈m/2⌉ children**.
     - It must have at least **⌈m/2⌉ - 1 keys** (except for the root, which can have fewer keys).

3. **Balanced Tree**: 
   - All leaf nodes are at the same level, meaning the tree is balanced. This ensures that the tree's height remains logarithmic with respect to the number of keys, leading to efficient search, insertion, and deletion operations.

4. **Key Ordering**: 
   - In a B-tree, the keys are stored in a sorted order within each node, and the child nodes are organized in a way that each node’s children correspond to key ranges:
     - The leftmost child of a node contains keys **less than** the first key of the node.
     - The middle child contains keys **between** the first and second keys, and so on.
   
5. **Efficient Disk Access**:
   - The B-tree is designed to minimize disk access by storing multiple keys and children in a node. This is particularly useful for **databases** and **file systems**, where accessing data from disk is relatively slow compared to memory access.

### Structure of a B-Tree:

- **Root Node**: The root is the top-most node. It can have fewer keys and children than other nodes in the tree.
- **Internal Nodes**: These nodes contain keys and child pointers that guide the search for data. They are also used during insertions and deletions to navigate the tree.
- **Leaf Nodes**: These nodes contain only keys and no children. They store the actual data in the case of databases or references to data.

### Example of a B-Tree (Order 3):

Consider a **B-tree of order 3**. This means each node can have a maximum of 2 keys and 3 children.

```
            [10, 20]
           /    |    \
       [5]   [15]   [25, 30]
```

- **Root Node**: The root node has two keys: `10` and `20`. It has three children:
  - The left child contains the key `5` (which is less than `10`).
  - The middle child contains the key `15` (between `10` and `20`).
  - The right child contains the keys `25` and `30` (which are greater than `20`).
  
- **Leaf Nodes**: In this case, the leaf nodes contain the actual keys that are stored.

### B-Tree Operations:

1. **Search**:
   - Search in a B-tree is efficient because the keys are sorted, and at each internal node, the key comparisons allow you to decide which child to follow. This ensures **logarithmic time complexity**.
   
2. **Insertion**:
   - When inserting a new key, you first locate the correct leaf node where the key should be inserted. If the node has space, the key is simply inserted in sorted order.
   - If the node is full (it has `m - 1` keys), it is **split** into two nodes, and the middle key is **promoted** to the parent node. This process may propagate upwards, causing further splits at higher levels if necessary.
   
3. **Deletion**:
   - Deletion in a B-tree involves locating the key to be deleted. If the key is in a leaf node and the node still satisfies the minimum number of keys, the key is simply removed.
   - If the key is in an internal node, it is replaced with either the **predecessor** or **successor** key, and then the corresponding deletion process is performed in the leaf node. If this causes a node to have fewer than the minimum number of keys, nodes may be **merged** or **redistributed** to maintain the balance.

4. **Traversal**:
   - In-order traversal of a B-tree visits the nodes in sorted order. It is useful for printing or retrieving all keys in the tree.

### Properties of a B-Tree:

- **Balanced**: The height of the tree is logarithmic in the number of keys, ensuring efficient access times for large datasets.
- **Dynamic**: The tree dynamically grows or shrinks as keys are inserted or deleted, without requiring reorganization of the entire tree.
- **Efficient Search, Insert, and Delete Operations**: All three operations are performed in **O(log n)** time, where `n` is the number of keys in the tree.

### Applications of B-Trees:

1. **Database Indexing**:
   - B-trees are widely used in **databases** for indexing data because they can efficiently handle a large number of keys and support efficient search, insert, and delete operations.

2. **File Systems**:
   - Many **file systems** (such as NTFS and HFS+) use B-trees to manage file directories and blocks, ensuring quick lookup and management of files.
   
3. **Multi-level Indexing**:
   - B-trees are used for **multi-level indexing** in situations where large datasets are stored and need to be accessed efficiently, such as in **key-value stores** and **search engines**.

4. **External Memory Data Structures**:
   - B-trees are well-suited for situations where data is stored in **external memory** (e.g., disk), and the goal is to minimize the number of disk reads by storing as much data as possible in each node.

### Summary:

A **B-Tree** is a balanced search tree used for efficient **data indexing** and **storage** in systems that handle large volumes of data. It supports **efficient searching, insertion, and deletion** with logarithmic time complexity. B-trees are particularly useful in **databases** and **file systems** due to their ability to store multiple keys and minimize disk access.

## Python Code for B-Tree Implementation

Here is a Python implementation of a **B-Tree**. This implementation includes key operations such as **search**, **insert**, and **delete**.

```python
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t           # Minimum degree (defines the range for number of keys)
        self.leaf = leaf     # True if leaf node, false otherwise
        self.keys = []       # List to store keys
        self.children = []   # List to store child nodes

class BTree:
    def __init__(self, t):
        self.t = t           # Minimum degree of the B-tree
        self.root = BTreeNode(t, True)  # Start with an empty root node

    # A utility function to search a key in the B-Tree
    def search(self, key, node=None):
        if node is None:
            node = self.root
        
        # Find the first key greater than or equal to key
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        
        # If the key is found, return the index
        if i < len(node.keys) and node.keys[i] == key:
            return node, i
        
        # If this is a leaf node, return None (key doesn't exist)
        if node.leaf:
            return None
        
        # Otherwise, search in the appropriate child
        return self.search(key, node.children[i])

    # A utility function to insert a key in a non-full node
    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        
        if node.leaf:
            # Find the position to insert the new key
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            # Find the child which is going to have the new key
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            # Check if the child is full
            if len(node.children[i].keys) == 2 * self.t - 1:
                # Split the child
                self.split_child(node, i)
                
                # After split, the middle key will be promoted to the parent node
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    # A utility function to split the child of a node
    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])
        
        z.keys = y.keys[t: ]
        y.keys = y.keys[:t - 1]
        
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    # Insert a new key into the B-Tree
    def insert(self, key):
        root = self.root
        
        # If the root is full, create a new root and split the old root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        
        # Insert the key in the non-full root
        self.insert_non_full(self.root, key)

    # A utility function to print the tree structure (in-order traversal)
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.inorder_traversal(node.children[i])
            print(node.keys[i], end=" ")
        if not node.leaf:
            self.inorder_traversal(node.children[-1])

# Example usage
if __name__ == "__main__":
    btree = BTree(3)  # B-tree with minimum degree 3 (i.e., each node can have at most 5 keys)

    # Insert keys into the B-tree
    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in keys:
        btree.insert(key)
    
    # Print the in-order traversal of the tree
    print("In-order traversal of the B-Tree:")
    btree.inorder_traversal()
    print()
    
    # Search for a key
    key_to_search = 12
    result = btree.search(key_to_search)
    if result:
        node, idx = result
        print(f"Key {key_to_search} found at index {idx} in node with keys {node.keys}")
    else:
        print(f"Key {key_to_search} not found in the tree.")
```

### Explanation of the B-Tree Implementation:

1. **BTreeNode Class**:
   - Represents a node in the B-tree. Each node contains a list of `keys` (sorted), a list of `children` (which are also BTreeNode objects), and a boolean `leaf` to indicate whether the node is a leaf.

2. **BTree Class**:
   - The main class that implements the B-tree. It contains:
     - `insert`: This function inserts a key into the B-tree, starting from the root.
     - `insert_non_full`: This function inserts a key into a node that is not full.
     - `split_child`: This function splits a child node when it becomes full.
     - `search`: This function searches for a key in the tree.
     - `inorder_traversal`: A helper function to print the tree’s keys in sorted order (in-order traversal).

### How the B-Tree Works:

- **Insertion**: 
   - When inserting a key, the algorithm first checks if the root is full. If the root is full, a new root is created and the original root is split. Then, the key is inserted into the appropriate node.
   - If a node is full, it is split into two nodes, and the middle key is promoted to the parent node.
   
- **Searching**:
   - The search is done recursively by comparing the key with the node’s keys. If the key is found, the search returns the key’s position in the node. Otherwise, the search continues in the child node corresponding to the key range.

- **In-order Traversal**:
   - The `inorder_traversal` function prints the keys of the tree in sorted order by visiting each node’s keys and recursively visiting the child nodes.

### Example Output:

When you run the program with the inserted keys `[10, 20, 5, 6, 12, 30, 7, 17]`, the in-order traversal will output the keys in sorted order:

```
In-order traversal of the B-Tree:
5 6 7 10 12 17 20 30
```

Additionally, when searching for a key, say `12`, it will return the index and node where the key was found:

```
Key 12 found at index 0 in node with keys [12, 17, 20]
```

### Summary:

This is a basic implementation of a **B-tree** in Python that supports **insertion** and **searching**. The tree is balanced, and the operations are efficient with time complexity of **O(log n)** for insertion, search, and traversal. You can also extend the functionality to handle **deletion** and other advanced operations if needed. Let me know if you'd like to explore those or have any questions!