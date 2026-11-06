## Leetcode Takeaways

LeetCode organizes its problems into various categories based on the underlying **data structures** and algorithms required to solve them. These categories help users focus on specific areas of problem-solving, improving their skills with different types of data structures and algorithms.

Here are some of the most common **LeetCode data structure categories**:

### **1. Arrays**
   - **Description**: Arrays are fundamental data structures consisting of elements of the same type, stored at contiguous memory locations. Array problems on LeetCode typically focus on manipulation, searching, sorting, and handling subarrays.
   - **Common Problems**:
     - Find the maximum sum of subarrays (e.g., **Maximum Subarray**).
     - Find duplicates, unique elements, or specific conditions (e.g., **Two Sum**, **Product of Array Except Self**).
     - Sorting and searching within arrays (e.g., **Merge Intervals**, **Rotate Image**).

### **2. Strings**
   - **Description**: Strings are sequences of characters, and operations on strings form the basis of many problems, including pattern matching, string manipulation, and comparisons.
   - **Common Problems**:
     - Reverse or manipulate strings (e.g., **Reverse String**, **Valid Palindrome**).
     - String matching and searching (e.g., **Implement strStr()**, **Substring with Concatenation of All Words**).
     - Dynamic programming with strings (e.g., **Longest Common Subsequence**, **Word Break**).

### **3. Linked Lists**
   - **Description**: Linked lists are linear data structures where each element (node) contains a value and a reference (link) to the next node in the sequence.
   - **Common Problems**:
     - Reversing or modifying linked lists (e.g., **Reverse Linked List**, **Detect Cycle in Linked List**).
     - Merging and sorting (e.g., **Merge Two Sorted Lists**, **Sort List**).
     - Middle element or intersection (e.g., **Find the Middle of a Linked List**, **Intersection of Two Linked Lists**).

### **4. Stacks**
   - **Description**: A stack is a collection of elements that follows the Last In First Out (LIFO) principle. Common applications of stacks include parsing expressions, managing function calls, and more.
   - **Common Problems**:
     - Validating parentheses (e.g., **Valid Parentheses**, **Generate Parentheses**).
     - Implementing stacks (e.g., **Min Stack**, **Daily Temperature**).
     - Reverse operations or expressions (e.g., **Evaluate Reverse Polish Notation**).

### **5. Queues**
   - **Description**: A queue follows the First In First Out (FIFO) principle. It is commonly used for scheduling tasks, managing resources, and breadth-first traversal of graphs.
   - **Common Problems**:
     - Implementing queues (e.g., **Implement Queue using Stacks**, **Design Circular Queue**).
     - Level-order traversal of trees or graphs (e.g., **Binary Tree Level Order Traversal**, **Sliding Window Maximum**).
     - Handling tasks with waiting times (e.g., **Task Scheduler**).

### **6. Hash Tables**
   - **Description**: Hash tables (or hash maps) store key-value pairs and provide fast look-up, insert, and delete operations. They are often used for tracking elements, counting frequencies, or mapping data.
   - **Common Problems**:
     - Finding duplicates or counts (e.g., **Two Sum**, **Find All Anagrams in a String**).
     - Grouping elements (e.g., **Group Anagrams**, **Intersection of Two Arrays**).
     - Storing and retrieving data efficiently (e.g., **LRU Cache**).

### **7. Trees**
   - **Description**: A tree is a hierarchical data structure consisting of nodes, with each node having a value and references to child nodes. Tree problems on LeetCode typically involve traversal, construction, or manipulation of binary or n-ary trees.
   - **Common Problems**:
     - Tree traversal (e.g., **Inorder Traversal**, **Level Order Traversal**, **Preorder Traversal**).
     - Binary Search Trees (BST) and operations (e.g., **Validate Binary Search Tree**, **Lowest Common Ancestor**).
     - Balanced trees and subtrees (e.g., **Maximum Depth of Binary Tree**, **Symmetric Tree**).

### **8. Heaps**
   - **Description**: Heaps are specialized binary trees that satisfy the heap property (max-heap or min-heap). Heaps are typically used for priority queues, sorting, and efficient retrieval of minimum or maximum elements.
   - **Common Problems**:
     - Priority queues (e.g., **Merge k Sorted Lists**, **Find Median from Data Stream**).
     - Heap operations (e.g., **Kth Largest Element in an Array**, **Sliding Window Maximum**).
     - Sorting with heaps (e.g., **Kth Largest Element in a Stream**).

### **9. Graphs**
   - **Description**: A graph consists of nodes (vertices) and edges (connections between nodes). Graphs can be directed, undirected, weighted, or unweighted. BFS and DFS are commonly used for traversing graphs.
   - **Common Problems**:
     - Traversal algorithms (e.g., **Depth-First Search**, **Breadth-First Search**).
     - Shortest paths (e.g., **Dijkstra’s Algorithm**, **Bellman-Ford Algorithm**, **Floyd-Warshall**).
     - Cycle detection, connected components, and topological sorting (e.g., **Detect Cycle in Directed Graph**, **Topological Sort**).

### **10. Dynamic Programming**
   - **Description**: Dynamic programming is used for solving problems by breaking them down into overlapping subproblems and solving them optimally using stored results. DP is often used for optimization problems.
   - **Common Problems**:
     - Fibonacci sequence and related problems (e.g., **Climbing Stairs**, **Longest Common Subsequence**).
     - 0/1 Knapsack and related optimization problems (e.g., **Subset Sum Problem**, **Coin Change**).
     - Sequence alignment and string manipulation (e.g., **Word Break**, **Edit Distance**).

### **11. Disjoint Set (Union-Find)**
   - **Description**: The disjoint set (or union-find) data structure is used to keep track of a partition of a set into disjoint subsets and supports efficient union and find operations.
   - **Common Problems**:
     - Union-find operations (e.g., **Number of Connected Components**, **Union-Find with Path Compression**).
     - Kruskal’s algorithm for Minimum Spanning Tree (MST) (e.g., **Kruskal's Algorithm**).
     - Detecting cycles and connected components in graphs (e.g., **Redundant Connection**).

### **12. Bit Manipulation**
   - **Description**: Bit manipulation involves performing operations on the individual bits of integers. Problems often require optimizing operations on bits, such as setting, clearing, or toggling bits.
   - **Common Problems**:
     - Basic bit operations (e.g., **Single Number**, **Counting Bits**).
     - XOR tricks (e.g., **Missing Number**, **Find the Two Non-Repeated Elements**).
     - Optimization using bitwise operations (e.g., **Power of Two**, **Reverse Bits**).

### **13. Sliding Window**
   - **Description**: Sliding window problems involve maintaining a "window" over a sequence (array or list) and efficiently updating or computing values within that window as it slides.
   - **Common Problems**:
     - Finding the maximum/minimum sum of subarrays (e.g., **Maximum Subarray Sum of Size K**, **Sliding Window Maximum**).
     - Longest substring with specific properties (e.g., **Longest Substring without Repeating Characters**, **Longest Substring with At Most K Distinct Characters**).

### **14. Backtracking**
   - **Description**: Backtracking is used to solve problems where we need to explore all possibilities and prune invalid solutions. It's often used in constraint satisfaction problems.
   - **Common Problems**:
     - N-Queens problem, Sudoku solver (e.g., **N-Queens**, **Word Search**).
     - Combinations, permutations, and subsets (e.g., **Permutations**, **Subsets**).
     - Graph problems like Hamiltonian Path or Coloring.

### **15. Mathematical Problems**
   - **Description**: This category includes problems that require number theory or advanced mathematical techniques like prime factorization, combinatorics, and modular arithmetic.
   - **Common Problems**:
     - Prime numbers (e.g., **Sieve of Eratosthenes**, **Count Primes**).
     - GCD and LCM problems (e.g., **Greatest Common Divisor**, **Chinese Remainder Theorem**).
     - Combinatorial problems (e.g., **N-th Ugly Number**, **Count Numbers with Unique Digits**).

---

### **Conclusion**:

LeetCode organizes its problems based on **data structures** and **algorithms** to help developers practice and master specific areas. By working on problems from different categories, you can build a solid foundation in solving algorithmic problems and improve your coding skills. Exploring and solving problems in different categories is a great way to prepare for coding interviews and enhance your problem-solving abilities.