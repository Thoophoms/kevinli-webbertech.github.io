# Binary Search Tree

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



## How BST works

Let's go step by step and visualize how a **Binary Search Tree (BST)** is built and traversed.

---

### **Step 1: Insert Nodes into BST**
We insert values: **50, 30, 70, 20, 40, 60, 80** in this order.

The resulting tree structure:
```
       50
      /  \
    30    70
   /  \   /  \
 20   40 60   80
```

---

### **Step 2: Implementing Traversals**
- **Inorder Traversal (Left, Root, Right):** `20 30 40 50 60 70 80`
- **Preorder Traversal (Root, Left, Right):** `50 30 20 40 70 60 80`
- **Postorder Traversal (Left, Right, Root):** `20 40 30 60 80 70 50`

---

### **Step 3: Python Implementation**
```python
# Create root
root = TreeNode(50)
insert_bst(root, 30)
insert_bst(root, 70)
insert_bst(root, 20)
insert_bst(root, 40)
insert_bst(root, 60)
insert_bst(root, 80)

print("Inorder Traversal:")
inorder(root)  # Output: 20 30 40 50 60 70 80

print("\nPreorder Traversal:")
preorder(root)  # Output: 50 30 20 40 70 60 80

print("\nPostorder Traversal:")
postorder(root)  # Output: 20 40 30 60 80 70 50
```

```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

def insert_bst(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

# Testing Code
if __name__ == "__main__":
    # Test Linked List
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.display()
    
    # Test Stack
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.pop())
    
    # Test Queue
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    print(queue.dequeue())
    
    # Test Sorting
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print(arr)
    
    # Test Binary Tree
    root = TreeNode(50)
    insert_bst(root, 30)
    insert_bst(root, 70)
    inorder(root)
```
