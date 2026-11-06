# **Amortized Analysis**

Amortized analysis is a technique in algorithm design used to determine the **average cost per operation** over a sequence of operations, especially when certain operations might have high costs, but they are infrequent. Instead of analyzing the worst-case cost of a single operation, amortized analysis provides a more realistic view of the performance of a sequence of operations by averaging out expensive steps over time.

**Amortized analysis** is a technique used to analyze the average time complexity per operation over a sequence of operations, rather than just the worst-case time complexity of a single operation. It is particularly useful when an algorithm performs a sequence of operations where some operations might be expensive but others are cheap, and you want to understand the average cost across all operations.

Amortized analysis helps to understand the average performance of an algorithm or data structure over time, providing a more accurate measure of efficiency compared to worst-case analysis. It is especially useful when the sequence of operations includes a mix of inexpensive and expensive operations, allowing us to average out the high-cost operations.


In simple terms, **amortized analysis** helps us to determine how much work (or cost) we do, on average, for each operation when performing multiple operations in sequence.

### **Types of Amortized Analysis Techniques**

1. **Aggregate Method**:
   - In this approach, we analyze the total cost of a sequence of operations and then spread that total cost evenly across all operations. 
   - For example, if performing `n` operations results in a total cost of `O(f(n))`, the amortized cost per operation is `O(f(n) / n)`.

   **Example**:
   If a sequence of `n` operations takes `O(n^2)` time in total, the amortized cost per operation would be `O(n^2 / n) = O(n)`.

2. **Accounting Method**:
   - This method involves assigning a "charge" (or "credit") to each operation. The charge is designed to accumulate over time so that it can be used to pay for expensive operations later.
   - Some operations may have a cost lower than the charge, and the difference is stored as a credit. When a more expensive operation occurs, it can use these stored credits to pay for the expensive work.
   - The key idea is that we keep track of the surplus credits that will pay for future operations.
   
   **Example**:
   For an operation that usually takes O(1) time, we might precharge it an extra O(1) time. If we then have a more expensive operation, it can "spend" the surplus credit built up in previous operations to handle the expensive work.

3. **Potential Method**:
   - The potential method is similar to the accounting method, but instead of assigning credits to individual operations, we define a **potential function** that represents the "stored work" in the data structure.
   - The potential function tracks the extra work that may be required later. It calculates how much "extra work" is left to do and helps distribute the cost of expensive operations over time.
   - The potential function allows us to reason about the cost of an operation in terms of the **change** in potential, making it possible to amortize the cost across all operations.
   
   **Example**:
   If we are managing a data structure where elements are pushed and popped, we could define a potential function that reflects the number of elements in a structure. When the number of elements increases or decreases, the potential function would capture the amount of extra work that may be required later.

### **Amortized Cost vs. Worst-Case Cost**

In some cases, an operation may have a **worst-case** cost that seems very high. However, when considering amortized analysis, the total cost of a sequence of operations is averaged, and you may find that even the worst-case operations do not significantly impact the average cost.

For example, in a **dynamic array**, **resize operations** (when the array exceeds its capacity) are expensive since they require copying all elements to a new array. The worst-case cost of resizing is O(n), where `n` is the number of elements in the array. However, resizing occurs infrequently, and over a sequence of operations, the **amortized cost per insertion** is **O(1)** because the array's size only grows exponentially, not linearly.

### **Common Examples of Amortized Analysis**

#### 1. **Dynamic Arrays** (e.g., ArrayList in Java)
   - A **dynamic array** starts with an initial capacity. When elements are inserted, the array grows by doubling its size each time it is full.
   - The worst-case cost of inserting an element during a **resize operation** is **O(n)**, where `n` is the number of elements in the array.
   - **Amortized cost**: Despite the occasional costly resize, the amortized cost of inserting an element is **O(1)** because the size of the array doubles and the number of resizes required grows logarithmically.

   **Amortized Analysis**:
   - For `n` insertions, the total cost of resizing is the sum of a geometric series, leading to an overall cost of O(n), meaning the amortized cost per insertion is **O(1)**.

#### 2. **Splay Trees**
   - In a **splay tree**, after every operation (insertion, deletion, or search), the tree is restructured so that the accessed element is moved to the root.
   - The **worst-case cost** for a single operation can be **O(n)** (when the tree is skewed), but splay trees maintain good **amortized time complexity**.
   - **Amortized cost**: Through amortized analysis (specifically using the **potential method**), it is shown that the amortized cost for each operation is **O(log n)**, even though individual operations might sometimes take linear time.

#### 3. **Incrementing Binary Counter**
   - Consider a binary counter that is initialized to 0. To increment the counter, you flip the rightmost 0 bit to 1 and flip all 1 bits to the right of it to 0.
   - The **worst-case cost** for an increment operation is **O(n)**, where `n` is the number of bits in the counter (when all bits are 1 and we need to flip them all).
   - **Amortized cost**: However, if you analyze a sequence of increments, each bit will be flipped only a limited number of times. Over `n` increments, the **amortized cost** of each increment is **O(1)**.

#### 4. **Binary Search Tree (BST) Rotations**
   - In certain balanced binary search trees, such as **AVL trees** or **Red-Black trees**, balancing operations like rotations are required to maintain the tree's height.
   - While a **single rotation** can take O(log n) time in the worst case, rotations are **infrequent**.
   - Over a sequence of operations, the amortized cost of maintaining balance remains **O(log n)** because rotations are distributed over many operations.

#### 5. **Union-Find (Disjoint Set Union - DSU)**
   - **Union-Find** is a data structure used to efficiently handle **union** and **find** operations on sets. It has optimizations like **path compression** and **union by rank** to keep the trees shallow.
   - While the worst-case cost for a series of `n` operations might seem high, the **amortized cost** for each operation can be shown to be nearly constant, i.e., **O(α(n))**, where α is the **inverse Ackermann function**, which grows extremely slowly and is practically constant for all reasonable values of `n`.

### **Summary of Key Concepts**:

1. **Amortized Cost**: The average cost per operation over a sequence of operations, considering the total cost of all operations.
2. **Aggregate Method**: Spread the total cost of a sequence of operations evenly over all operations.
3. **Accounting Method**: Assign charges to operations and accumulate credits to pay for expensive operations later.
4. **Potential Method**: Use a potential function to track the "stored work" in a data structure and amortize costs based on the change in potential.

## B-Tree analysis

In the context of **B-trees**, we can use amortized analysis to understand how the tree structure behaves across multiple insertions and deletions, as these operations can sometimes trigger expensive restructuring operations like node splits or merges.

### Amortized Analysis in B-trees

When analyzing **B-tree operations** (like insertions and deletions), most operations are fast — taking logarithmic time — but in some cases, restructuring operations like splitting a node or merging nodes may be required, and these restructuring steps can be expensive. However, across a sequence of operations, these expensive operations can be rare compared to the number of simple operations.

### Key Operations in B-trees and Their Amortized Cost:

1. **Insertion**:
    - **Basic Insertion**: When inserting a key, we traverse the tree and insert the key into the appropriate node. This is an O(log n) operation since the tree is balanced and has a logarithmic height.
    - **Node Split**: If the node being inserted into is full (i.e., has `2*T-1` keys), it will need to split into two nodes, and the middle key will propagate upwards. This split operation is O(T) because we have to move keys and possibly pointers. However, splits tend to occur infrequently as the tree grows.
    - **Amortized Cost**: Since splits are rare (each node can handle up to `2*T-1` keys before splitting), the average cost of insertion is still O(log n), despite occasional expensive splits. The **amortized cost** is thus **O(log n)**.

2. **Deletion**:
    - **Basic Deletion**: Similar to insertion, deletion involves finding the key and possibly restructuring the tree to maintain balance. If the key is found in a leaf node, it’s simply removed, which takes O(log n) time.
    - **Merging Nodes**: If a node has fewer than `T` keys after deletion, it may require merging with a sibling. Merging nodes involves copying keys and child pointers, which can be an expensive operation. 
    - **Amortized Cost**: Merges are costly, but they are not performed after every deletion. The amortized cost over a sequence of deletions remains O(log n), because the number of merges is proportional to the height of the tree, which grows logarithmically.

3. **Splits and Merges**:
    - **Splits**: Each time a node exceeds its capacity (`2*T-1` keys), it will split, and the middle key moves up. A split happens in O(T) time, but the number of splits is relatively infrequent in a growing tree. The total number of splits that occur for `n` insertions is O(n / T), so the amortized cost per insertion is O(log n).
    - **Merges**: Similarly, when a node underflows (has fewer than `T` keys), it may be merged with a sibling, which involves a similar cost of O(T). The number of merges is proportional to the height of the tree, so the total number of merges over a series of deletions is also proportional to O(log n). Again, the amortized cost per deletion is O(log n).

### Potential Amortized Analysis Techniques:

1. **Accounting Method**:
    - In the accounting method, we assign a "charge" (or "credit") to each operation, which accumulates over time and can be used to pay for expensive operations later. For example, when splitting a node, we could pre-charge the nodes slightly more than the actual cost of a basic insertion. This way, we can "pay" for future splits with the credit accumulated from previous cheap insertions.
    - For each insertion, we could amortize the cost of future splits, so the cost per insertion stays proportional to O(log n), despite occasional expensive splits.

2. **Aggregate Analysis**:
    - In aggregate analysis, we look at the total cost of a sequence of operations and spread it evenly across all operations. In the case of insertions in a B-tree, although some insertions involve splitting nodes, these splits are infrequent. Over a large number of insertions, the total number of splits is proportional to O(n / T). Thus, even though each split operation is O(T), the total cost of splits is O(n), leading to an amortized cost of O(log n) per insertion.

3. **Potential Method**:
    - The potential method involves defining a potential function that measures the "extra work" stored in the tree (e.g., the number of extra nodes or the size of nodes that may need restructuring). When an operation is performed, we calculate the change in potential. This helps account for the restructuring operations like splits and merges that might not occur in every operation, but their cost is accounted for in the potential.

### **Why Amortized Cost is O(log n) for B-trees**:

- **Insertions**: Inserting a key generally requires O(log n) time, as we only need to traverse down the tree. Splitting nodes is expensive but rare, so when amortized over a series of insertions, the average cost of each insertion remains O(log n).
  
- **Deletions**: Deletions involve finding the key and potentially merging nodes or redistributing keys. Even though node merging is costly, it is infrequent. The total number of merges across a sequence of deletions is logarithmic in the height of the tree, and thus, the amortized cost of deletion is O(log n).

- **Amortized Analysis of Splits and Merges**: When splitting or merging nodes, we perform these operations relatively infrequently. Each split or merge operation affects only a small portion of the tree (i.e., it only affects the node being split and possibly its parent), and the number of splits or merges grows slowly compared to the total number of operations.

### Summary of Amortized Costs:
- **Insertion**: Amortized cost of **O(log n)** per insertion.
- **Deletion**: Amortized cost of **O(log n)** per deletion.
- **Overall**: The amortized cost for both insertion and deletion operations in a B-tree is **O(log n)**, thanks to the rare restructuring operations like splits and merges.

### Conclusion:

Amortized analysis allows us to understand the average cost of operations over time, especially in the presence of expensive operations like node splits or merges. In the case of B-trees, even though certain operations can be costly, they are rare and infrequent, leading to an amortized time complexity of **O(log n)** for both insertions and deletions, making B-trees efficient for managing large datasets.
