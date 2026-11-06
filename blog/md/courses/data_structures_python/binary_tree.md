# Binary Tree Explanation in Python

A **Binary Tree** is a hierarchical data structure where each node has at most two children: a left child and a right child.

## **Key Properties of a Binary Tree**
1. Each node contains a value and pointers to at most two child nodes.
2. The top node is called the **root**.
3. A **leaf node** has no children.
4. A **Binary Search Tree (BST)** is a special type of binary tree where:
   - Left subtree nodes contain values smaller than the parent node.
   - Right subtree nodes contain values greater than the parent node.

---

## **Binary Tree Implementation in Python**
The code you have in the document already implements a **Binary Tree** along with **Binary Search Tree (BST) insertion** and **tree traversal methods**.

## **Traversals in Binary Tree**
1. **Inorder (Left, Root, Right)** - Gives sorted order in BST.
2. **Preorder (Root, Left, Right)** - Used in expression trees.
3. **Postorder (Left, Right, Root)** - Used in deleting nodes.

Your implementation contains:
- A `TreeNode` class to define nodes.
- `insert_bst` function to insert values into BST.
- `inorder`, `preorder`, and `postorder` traversal functions.

## **Full Binary Tree**

A **Full Binary Tree** is a tree where **every node has either 0 or 2 children**. No node can have only one child.

Example:
```
       1
      / \
     2   3
    / \  / \
   4   5 6  7
```
Here, each node has either **two children or no children**.

---

## **Complete Binary Tree**

A **Complete Binary Tree** is a binary tree where:
1. All levels, except possibly the last, are **completely filled**.
2. The last level nodes are **as left as possible**.

Example:
```
       1
      / \
     2   3
    / \  /
   4   5 6
```

- The last level is **filled from left to right**.
- Node `7` is missing, but the tree is still **complete**.

---

### **Python Implementation**

```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_full_binary_tree(root):
    if root is None:
        return True
    if (root.left is None and root.right is None):
        return True
    if (root.left is not None and root.right is not None):
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    return False

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_complete_binary_tree(root, index=0, node_count=None):
    if root is None:
        return True
    if node_count is None:
        node_count = count_nodes(root)
    if index >= node_count:
        return False
    return (is_complete_binary_tree(root.left, 2 * index + 1, node_count) and
            is_complete_binary_tree(root.right, 2 * index + 2, node_count))

# Example Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print("Is Full Binary Tree?", is_full_binary_tree(root))  # Output: False
print("Is Complete Binary Tree?", is_complete_binary_tree(root))  # Output: True
```