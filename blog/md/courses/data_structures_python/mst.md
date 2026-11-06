# Minimum Spanning Tree (MST)

A **Minimum Spanning Tree (MST)** of a connected, undirected graph is a subset of the edges of the graph that connects all the vertices (nodes) together, without any cycles, and with the **minimum possible total edge weight**.

In simpler terms, a **spanning tree** is a tree that includes every vertex in the graph, and an **MST** is a spanning tree with the smallest sum of edge weights.

### Key Properties of MST:
1. **Connected**: The tree includes all the vertices of the graph.
2. **Acyclic**: There are no cycles in the tree.
3. **Minimum Weight**: The sum of the edge weights in the tree is as small as possible.
4. **Unique MST**: If all edge weights are distinct, the MST is unique. If there are edges with the same weight, there can be multiple MSTs.

### Applications of Minimum Spanning Tree:
- **Network Design**: Designing minimum-cost networks, such as communication or electrical networks, where the goal is to connect all nodes with the least possible cost.
- **Cluster Analysis**: Used in data mining and machine learning for hierarchical clustering.
- **Approximation Algorithms**: MSTs are used in algorithms for finding approximate solutions to problems like the traveling salesman problem (TSP).

### Algorithms to Find MST:
There are several well-known algorithms to find the Minimum Spanning Tree of a graph:

1. **Kruskal's Algorithm**:
   - This algorithm works by sorting all the edges in the graph by their weights. It then adds the smallest edge to the MST, ensuring no cycles are formed, and repeats the process until the tree is fully formed.

2. **Prim's Algorithm**:
   - Prim's algorithm starts from any node and grows the MST by adding the smallest edge that connects the tree to a new node (i.e., an edge with the minimum weight that doesn’t form a cycle).

### 1. **Kruskal’s Algorithm** (Greedy Approach):

**Steps**:
1. Sort all the edges in the graph in non-decreasing order of their weights.
2. Pick the smallest edge. If it doesn’t form a cycle (i.e., it connects two different components), add it to the MST.
3. Repeat the process until the MST contains `V - 1` edges, where `V` is the number of vertices.

**Time Complexity**:
- Sorting the edges takes \(O(E \log E)\), where \(E\) is the number of edges.
- Union-Find operations to check cycles and connect components are efficient with path compression and union by rank, so they take almost constant time per operation.

### 2. **Prim’s Algorithm** (Greedy Approach):

**Steps**:
1. Start from any arbitrary node and mark it as part of the MST.
2. Add the smallest edge that connects the MST to any other node not in the MST.
3. Repeat until all vertices are included in the MST.

**Time Complexity**:
- Using a priority queue (min-heap), the time complexity is \(O((V + E) \log V)\), where `V` is the number of vertices and `E` is the number of edges.

### Example: Kruskal’s Algorithm

Consider a graph with the following vertices and edges (with weights):

```
Vertices: A, B, C, D, E
Edges:
A - B (2), A - C (3), B - C (4), B - D (5), C - D (6), C - E (7), D - E (8)
```

1. **Sort the edges by weight**: 
   ```
   A - B (2), A - C (3), B - C (4), B - D (5), C - D (6), C - E (7), D - E (8)
   ```

2. **Select the edges** in order:
   - A - B (2): Add to MST.
   - A - C (3): Add to MST.
   - B - C (4): Skip, as A-B-C is already connected.
   - B - D (5): Add to MST.
   - C - D (6): Skip, as it's already connected through A-B-C-D.
   - C - E (7): Add to MST.
   - D - E (8): Skip.

3. **MST edges**: A - B, A - C, B - D, C - E. The MST has a total weight of 2 + 3 + 5 + 7 = 17.

### Python Code for Kruskal’s Algorithm:

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    mst = []
    ds = DisjointSet(len(vertices))
    
    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((vertices[u], vertices[v], weight))
    
    return mst

# Example usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [(0, 1, 2), (0, 2, 3), (1, 2, 4), (1, 3, 5), (2, 3, 6), (2, 4, 7), (3, 4, 8)]

mst = kruskal(vertices, edges)
for edge in mst:
    print(edge)
```

### Example Output:

```
('A', 'B', 2)
('A', 'C', 3)
('B', 'D', 5)
('C', 'E', 7)
```

### Summary:
- **Minimum Spanning Tree (MST)** is a tree that spans all vertices of a graph with the minimum sum of edge weights.
- **Kruskal’s Algorithm** works by sorting all edges and adding the smallest edge that doesn’t form a cycle. It uses the **Union-Find** (Disjoint Set) data structure to manage connected components.
- **Prim’s Algorithm** starts from any node and grows the MST by adding the smallest edge that connects the tree to a new node.

Both algorithms are greedy in nature and guarantee the minimum spanning tree with a time complexity of \( O(E \log E) \) for Kruskal’s and \( O((V + E) \log V) \) for Prim’s.


## Kruskal’s Algorithm vs. Prim’s Algorithm

Both **Kruskal’s Algorithm** and **Prim’s Algorithm** are popular **greedy algorithms** for finding the **Minimum Spanning Tree (MST)** of a connected, undirected graph. While they both aim to find the MST, they approach the problem in different ways.

#### 1. **Kruskal’s Algorithm**:

**Approach**: Kruskal’s algorithm works by sorting all the edges of the graph by weight and adding edges to the MST in increasing order of weight, ensuring no cycles are formed.

- **Steps**:
  1. Sort all the edges in non-decreasing order of their weights.
  2. Iterate over the sorted edges and add each edge to the MST if it does not form a cycle (using a **Union-Find** or **Disjoint Set** structure).
  3. Stop when the MST contains `V-1` edges, where `V` is the number of vertices.

- **Key Data Structure**: **Disjoint Set (Union-Find)**, to efficiently check if two vertices are in the same component and to perform the union operation.

- **Time Complexity**:
  - **Sorting** the edges: \( O(E \log E) \), where \(E\) is the number of edges.
  - **Union-Find operations**: \( O(\alpha(V)) \), where \( \alpha \) is the inverse Ackermann function, which is almost constant for practical inputs.

  So, the overall time complexity is **O(E log E)**.

- **When to Use**:
  - **Edge-based approach**: Kruskal’s algorithm works well when the graph is sparse or when you have many edges.
  - Efficient for **disjoint edge sets**.
  - **Edge list representation** is more natural for Kruskal's.

- **Memory Usage**: Kruskal’s algorithm stores edges and uses the **Union-Find** structure, so it requires space for edges and additional space for the union-find data structure.

#### 2. **Prim’s Algorithm**:

**Approach**: Prim’s algorithm works by growing the MST starting from any vertex, repeatedly adding the smallest edge that connects a vertex in the tree to a vertex outside the tree.

- **Steps**:
  1. Start from an arbitrary vertex.
  2. Grow the MST by adding the smallest edge that connects a vertex in the MST to a vertex outside the MST (edge with the least weight).
  3. Repeat until all vertices are in the MST.

- **Key Data Structure**: **Priority Queue (Min-Heap)**, to efficiently fetch the minimum edge that connects the current tree to a new vertex.

- **Time Complexity**:
  - **Priority Queue Operations**: \( O((V + E) \log V) \), where \(V\) is the number of vertices and \(E\) is the number of edges.

  So, the overall time complexity is **O((V + E) log V)**.

- **When to Use**:
  - **Vertex-based approach**: Prim’s algorithm is more suitable when the graph is dense (i.e., has many edges).
  - It works better when the graph is represented as an **adjacency matrix** or an **adjacency list**.

- **Memory Usage**: Prim’s algorithm uses a **priority queue** for managing the vertices and edges, and needs an array for tracking the minimum weight edge for each vertex.

---

### Comparison of Kruskal’s Algorithm and Prim’s Algorithm

| Aspect                        | **Kruskal's Algorithm**                                   | **Prim's Algorithm**                                  |
|-------------------------------|-----------------------------------------------------------|-------------------------------------------------------|
| **Approach**                   | Edge-based (works by sorting edges)                      | Vertex-based (grows the MST one vertex at a time)     |
| **Graph Representation**       | Works better with edge list representation               | Works better with adjacency matrix or adjacency list  |
| **Data Structure**             | Disjoint Set (Union-Find) for cycle detection             | Priority Queue (Min-Heap) for selecting minimum edges |
| **Time Complexity**            | \( O(E \log E) \)                                        | \( O((V + E) \log V) \)                               |
| **Space Complexity**           | \( O(E + V) \) (for edges and Union-Find structure)      | \( O(V) \) (for storing vertex weights and the heap)   |
| **Suitable For**               | Sparse graphs with fewer edges                           | Dense graphs with many edges                          |
| **Handling of Cycles**         | Uses Union-Find to avoid cycles                          | Avoids cycles naturally during the process            |
| **Starting Point**             | Starts with all edges sorted, can start from any edge    | Starts with any vertex                                |
| **Efficiency with Dense Graphs**| Less efficient, slower in dense graphs                   | More efficient in dense graphs                        |
| **Efficiency with Sparse Graphs**| More efficient in sparse graphs                         | Less efficient in sparse graphs                       |

### Example:

Consider a graph with the following vertices and edges:

```
Vertices: A, B, C, D
Edges:
A - B (1), A - C (4), A - D (3)
B - C (2), B - D (5), C - D (6)
```

For **Kruskal’s Algorithm**, we would:
1. Sort the edges by weight: `A-B(1)`, `B-C(2)`, `A-D(3)`, `A-C(4)`, `B-D(5)`, `C-D(6)`.
2. Add the edges to the MST in this order, avoiding cycles: `A-B(1)`, `B-C(2)`, `A-D(3)` (edges `B-D(5)` and `C-D(6)` would form cycles).

For **Prim’s Algorithm**, starting from `A`:
1. Start with `A`. The smallest edge is `A-B(1)`, add `B`.
2. The smallest edge that connects the MST to a new vertex is `B-C(2)`, add `C`.
3. The smallest edge connecting `A-B-C` to another vertex is `A-D(3)`, add `D`.

In this case, both algorithms will produce the same MST with edges `A-B(1)`, `B-C(2)`, `A-D(3)`.

### Summary:

- **Kruskal’s Algorithm** is better when you have a sparse graph, and the graph is represented by an edge list.
- **Prim’s Algorithm** is more efficient for dense graphs and when using an adjacency matrix or list representation.
- Both are greedy algorithms and guarantee the same result for the MST, but they have different performance characteristics depending on the graph structure.

