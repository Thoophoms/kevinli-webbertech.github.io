# Tree

## Basic Level Order Implementation

**BFS** can be used to traverse a tree level wise. One key point to note is that we can control which way we want to traverse
(either left to right or right to left) by deciding what goes inside queue first.

**DFS** can also be used to solve these type of problems by adding a level variable.

- 102. Binary Tree Level Order Traversal
       https://leetcode.com/problems/binary-tree-level-order-traversal

- 107. Binary Tree Bottom up Level Order Traversal
       https://leetcode.com/problems/binary-tree-level-order-traversal-ii

- 108. N-ary Tree Level Order Traversal
       https://leetcode.com/problems/n-ary-tree-level-order-traversal

- 109. Average of Levels in Binary Tree
       https://leetcode.com/problems/average-of-levels-in-binary-tree

- 110. Binary Tree Zigzag Level Order Traversal
       https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

- 111. Add One Row at a given Level in a binary Tree
       https://leetcode.com/problems/add-one-row-to-tree

- 112. Reverse Odd Levels of Binary Tree
       https://leetcode.com/problems/reverse-odd-levels-of-binary-tree

- 113. Minimum Number of Operations to Sort a Binary Tree by Level CyclicSort+BFS
       https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level

## Tree construction

Note:
Inorder + Preorder => Unique tree
Inorder + Postorder => Unique tree
Postorder + Preorder => Multiple Trees possible

- 105. Construct Binary Tree from Preorder and Inorder Traversal
       https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
- 106. Construct Binary Tree from Inorder and Postorder Traversal
       https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
- 107. Construct Binary Tree from Preorder and Postorder Traversal
       https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
- 108. Construct String from Binary Tree
       https://leetcode.com/problems/construct-string-from-binary-tree
- 109. Maximum Binary Tree
       https://leetcode.com/problems/maximum-binary-tree

## Depth/Height based

Note: Always check height is 0 or 1 indexed.

- 104. Maximum Depth of Binary Tree Classic DFS
       https://leetcode.com/problems/maximum-depth-of-binary-tree
- 111. Minimum Depth of Binary Tree BFS intuitive
       https://leetcode.com/problems/minimum-depth-of-binary-tree
- 559. Maximum Depth of N-ary Tree
       https://leetcode.com/problems/maximum-depth-of-n-ary-tree

## Counting

Note:

- Count nodes with some condition
- Count Trees or subtrees

- 222. Count Complete Tree Nodes
       https://leetcode.com/problems/count-complete-tree-nodes

- 223. Count Good Nodes in Binary Tree
       https://leetcode.com/problems/count-good-nodes-in-binary-tree

- 224. Count Nodes Equal to Average of Subtree
       https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

- 250. Count Univalue Subtrees [Premium]
       https://leetcode.com/problems/count-univalue-subtrees

## Comparison on Two Trees

Note: In these types of problem we generally run dfs/bfs simultaneously on both trees

- 100. Same Tree
       https://leetcode.com/problems/same-tree

- 101. Symmetric Tree
       https://leetcode.com/problems/symmetric-tree

- 102. Leaf-Similar Trees
       https://leetcode.com/problems/leaf-similar-trees

- 103. Subtree of Another Tree
       https://leetcode.com/problems/subtree-of-another-tree

## Path

Note:
Total number of paths between any two nodes in a binary tree with n nodes is:
n×(n−1) ​/2. For each starting node, there are n−1 other nodes in the tree to which it can connect, forming n−1 paths.

- 687. Longest Univalue Path
       https://leetcode.com/problems/longest-univalue-path

- 688. Binary Tree Maximum Path Sum H
       https://leetcode.com/problems/binary-tree-maximum-path-sum

### Rooted Path (Root to leaves)

Note:
When a path starts from root and ends at leaf node

- 1022. Sum of Root To Leaf Binary Numbers path forms a binary number
        https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

- 1023. Sum Root to Leaf Numbers path forms a number
        https://leetcode.com/problems/sum-root-to-leaf-numbers

- 1024. Binary Tree Paths Backtracking
        https://leetcode.com/problems/binary-tree-paths

- 1025. Smallest String Starting From Leaf
        https://leetcode.com/problems/smallest-string-starting-from-leaf

- 1026. Path Sum
        https://leetcode.com/problems/path-sum

### Tree Leaves

Note: Operations done on leaf nodes

- 404. Sum of Left Leaves
       https://leetcode.com/problems/sum-of-left-leaves

- 405. Deepest Leaves Sum
       https://leetcode.com/problems/deepest-leaves-sum

## Ancestor

- 236. Lowest Common Ancestor of a Binary Tree
       https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

- 237. Lowest Common Ancestor of Deepest Leaves
       https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
- 238. Kth Ancestor of a Tree Node
       https://leetcode.com/problems/kth-ancestor-of-a-tree-node
- 239. Maximum Difference Between Node and Ancestor
       https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

## Iterative Tree Traversals

- 94. Binary Tree Inorder Traversal
      https://leetcode.com/problems/binary-tree-inorder-traversal/

- 95. Binary Tree Preorder Traversal
      https://leetcode.com/problems/binary-tree-preorder-traversal

- 96. Binary Tree Postorder Traversal
      https://leetcode.com/problems/binary-tree-postorder-traversal/description/

- 97. Graph Creation
      Note: Use this option when you need more freedom to move inside a tree

- 98. All Nodes Distance K in Binary Tree better alternatives might be available
      https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

## BST

Note: Inorder Traversal of a BST is always sorted so keep that in mind while solving bst problems.

- 700. Search in a Binary Search Tree
       https://leetcode.com/problems/search-in-a-binary-search-tree
- 701. Validate Binary Search Tree
       https://leetcode.com/problems/validate-binary-search-tree
- 702. Find Mode in Binary Search Tree
       https://leetcode.com/problems/find-mode-in-binary-search-tree
- 703. Two Sum IV - Input is a BST
       https://leetcode.com/problems/two-sum-iv-input-is-a-bst
- 704. Increasing Order Search Tree
       https://leetcode.com/problems/increasing-order-search-tree
- 705. Range Sum of BST
       https://leetcode.com/problems/range-sum-of-bst
- 706. Convert Sorted Array to Binary Search Tree
       https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
- 70- 7. Convert Sorted List to Binary Search Tree
  https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
- 708. Minimum Absolute Difference in BST
       https://leetcode.com/problems/minimum-absolute-difference-in-bst
- 709. All Elements in Two Binary Search Trees
       https://leetcode.com/problems/all-elements-in-two-binary-search-trees
- 710. Kth Smallest Element in a BST
       https://leetcode.com/problems/kth-smallest-element-in-a-bst
- 711. Trim a Binary Search Tree
       https://leetcode.com/problems/trim-a-binary-search-tree
- 712. Construct Binary Search Tree from Preorder Traversal
       https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal
- 713. Unique Binary Search Trees
       https://leetcode.com/problems/unique-binary-search-trees

- 714. Delete Node in a BST
       https://leetcode.com/problems/delete-node-in-a-bst
- 715. Insert into a Binary Search Tree
       https://leetcode.com/problems/insert-into-a-binary-search-tree
- 716. Lowest Common Ancestor of a Binary Search Tree
       https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
