# Minimum Spanning Tree (MST)

A **Minimum Spanning Tree (MST)** is a subset of the edges of a connected, weighted graph that connects all the vertices together, without any cycles, and with the minimum possible total edge weight.

### **Properties of Minimum Spanning Tree (MST):**
1. **Spanning**: It must include all the vertices of the graph.
2. **Tree**: It must be a tree (no cycles).
3. **Minimum Weight**: The sum of the weights of the edges in the MST must be as small as possible.

### **Algorithms to Find Minimum Spanning Tree:**
There are two main algorithms for finding the Minimum Spanning Tree:

1. **Kruskal’s Algorithm**:
   - Kruskal's algorithm works by sorting the edges of the graph by weight and then adding edges to the MST as long as they do not form a cycle.
   - It uses a **Disjoint Set (Union-Find)** data structure to keep track of cycles.
   
2. **Prim’s Algorithm**:
   - Prim's algorithm grows the MST one vertex at a time, starting from an arbitrary vertex, and always selecting the edge with the smallest weight that connects a vertex in the MST to a vertex outside the MST.

### **Kruskal’s Algorithm**:
1. **Sort all edges** in the graph in non-decreasing order of their weights.
2. **Pick the smallest edge**. If adding this edge doesn't form a cycle, add it to the MST.
3. Repeat step 2 until there are **V - 1 edges** in the MST, where **V** is the number of vertices in the graph.

### **Prim’s Algorithm**:
1. **Start with any vertex** and set its key value to 0 (indicating that it will be included in the MST).
2. **Select the vertex with the minimum key value** and add it to the MST.
3. **Update the key values** of the adjacent vertices. If the weight of an edge connecting an included vertex to an excluded vertex is less than the key value of the excluded vertex, update its key value.
4. Repeat until all vertices are included in the MST.

### **Java Implementation of Kruskal’s Algorithm** (with Union-Find data structure)

Here is a simple implementation of **Kruskal’s Algorithm** in Java:

```java
import java.util.*;

class Edge {
    int src, dest, weight;

    // Constructor for the Edge class
    public Edge(int src, int dest, int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }
}

class DisjointSet {
    int[] parent, rank;

    // Constructor for the Disjoint Set
    public DisjointSet(int n) {
        parent = new int[n];
        rank = new int[n];

        // Initially, each node is its own parent
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    // Find the representative of the set containing x
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);  // Path compression
        }
        return parent[x];
    }

    // Union of two sets
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            // Union by rank
            if (rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
}

class KruskalMST {
    public static List<Edge> kruskalMST(List<Edge> edges, int V) {
        List<Edge> mst = new ArrayList<>();

        // Sort edges by weight
        Collections.sort(edges, (a, b) -> a.weight - b.weight);

        // Create a disjoint set to handle cycles
        DisjointSet ds = new DisjointSet(V);

        // Iterate over sorted edges and add to MST if no cycle is formed
        for (Edge edge : edges) {
            int rootSrc = ds.find(edge.src);
            int rootDest = ds.find(edge.dest);

            // If the source and destination have different roots, no cycle is formed
            if (rootSrc != rootDest) {
                mst.add(edge);
                ds.union(rootSrc, rootDest);  // Union the sets
            }
        }

        return mst;
    }

    public static void printMST(List<Edge> mst) {
        int totalWeight = 0;
        for (Edge edge : mst) {
            System.out.println("Edge: " + edge.src + " - " + edge.dest + " Weight: " + edge.weight);
            totalWeight += edge.weight;
        }
        System.out.println("Total weight of MST: " + totalWeight);
    }

    public static void main(String[] args) {
        // Example graph
        List<Edge> edges = new ArrayList<>();
        edges.add(new Edge(0, 1, 10));
        edges.add(new Edge(0, 2, 6));
        edges.add(new Edge(0, 3, 5));
        edges.add(new Edge(1, 3, 15));
        edges.add(new Edge(2, 3, 4));

        int V = 4;  // Number of vertices

        // Compute MST using Kruskal's Algorithm
        List<Edge> mst = kruskalMST(edges, V);

        // Print the MST
        printMST(mst);
    }
}
```

### **Explanation of Kruskal’s Algorithm:**
1. **Edge Class**: Represents an edge with a source, destination, and weight.
2. **DisjointSet Class**: This class handles the union-find operations using path compression and union by rank.
   - `find()`: Finds the representative (root) of the set containing a node.
   - `union()`: Merges two sets.
3. **KruskalMST Class**: Implements Kruskal’s algorithm.
   - `kruskalMST()`: Sorts edges by weight and uses the disjoint set to check if adding an edge will form a cycle. If not, it adds the edge to the MST.
   - `printMST()`: Prints the edges in the MST and the total weight.
4. **main()**: Initializes an example graph, computes the MST using Kruskal’s algorithm, and prints the result.

### **Sample Output:**

```
Edge: 2 - 3 Weight: 4
Edge: 0 - 3 Weight: 5
Edge: 0 - 1 Weight: 10
Total weight of MST: 19
```

### **Time Complexity of Kruskal's Algorithm:**
- **Sorting edges**: O(E log E), where **E** is the number of edges.
- **Union-Find operations**: O(E α(V)), where α is the inverse Ackermann function (which grows very slowly and can be considered constant for practical purposes).

Thus, the overall time complexity of Kruskal's algorithm is **O(E log E)**.

### **Space Complexity:**
- **O(V + E)**: Space is used for storing the edges and the disjoint set data structure.

### **Prim’s Algorithm:**
Alternatively, **Prim’s Algorithm** can also be used to find the Minimum Spanning Tree. While Kruskal’s Algorithm works well with edge-based representation, Prim's Algorithm is more efficient for dense graphs. It grows the MST one vertex at a time, always choosing the edge with the minimum weight connecting a vertex in the MST to a vertex outside the MST.

### **Conclusion:**
- **Kruskal’s Algorithm** is efficient for sparse graphs and uses a union-find structure to detect cycles.
- **Prim’s Algorithm** is often more efficient for dense graphs and uses a priority queue to select the minimum edge connecting the MST to the rest of the graph.

## **Prim’s Algorithm**

**Prim’s Algorithm** is another popular algorithm used to find the **Minimum Spanning Tree (MST)** of a graph. Unlike **Kruskal’s Algorithm**, which works by sorting the edges, **Prim’s Algorithm** starts from a single vertex and grows the MST by adding the smallest edge that connects a vertex in the MST to a vertex outside the MST. It works well for dense graphs, especially when the graph is represented by an adjacency matrix.

### **Prim’s Algorithm Overview:**
1. **Start with an arbitrary node** and add it to the MST.
2. **Choose the smallest edge** that connects a vertex in the MST to a vertex outside the MST.
3. **Add the selected edge** and the connected vertex to the MST.
4. **Repeat** steps 2 and 3 until all vertices are included in the MST.

### **Prim's Algorithm Approach:**
1. **Initialization**:
   - Start with an arbitrary node and mark it as part of the MST.
   - Maintain a priority queue (min-heap) to store the edges, ordered by their weights. The key operation is to extract the minimum-weight edge that connects a vertex in the MST to a vertex outside it.
   
2. **Main Process**:
   - Extract the minimum edge from the priority queue.
   - If the edge connects a vertex outside the MST to a vertex inside the MST, add it to the MST.
   - Mark the vertex as visited, and push all the edges that connect the newly added vertex to other unvisited vertices into the priority queue.
   
3. **Repeat** until all vertices are included in the MST.

### **Prim's Algorithm Pseudocode:**
1. Initialize a priority queue with edges.
2. Set the key value of the starting node to 0.
3. Iterate over all vertices, extracting the minimum key value from the priority queue.
4. For each extracted vertex, update the key values of adjacent vertices if a smaller edge weight is found.
5. Stop when all vertices are included in the MST.

### **Java Implementation of Prim’s Algorithm:**

Here is the Java implementation of **Prim’s Algorithm** using an adjacency list representation and a **min-heap** (priority queue).

```java
import java.util.*;

class PrimMST {
    // Class to represent an edge in the graph
    static class Edge {
        int dest, weight;
        public Edge(int dest, int weight) {
            this.dest = dest;
            this.weight = weight;
        }
    }

    // Method to perform Prim's Algorithm
    public static void primMST(List<List<Edge>> graph, int V) {
        // Priority queue to store the vertex and its key value
        // The key value is the minimum edge weight to connect the vertex to the MST
        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.weight));

        // Array to store the parent of each vertex in the MST
        int[] parent = new int[V];
        // Array to store the minimum edge weight for each vertex
        int[] key = new int[V];
        // Array to check if a vertex is included in the MST
        boolean[] inMST = new boolean[V];

        // Initialize the key values of all vertices to infinity and parent to -1
        Arrays.fill(key, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);

        // Start with vertex 0 and set its key value to 0
        key[0] = 0;
        pq.offer(new Edge(0, 0));

        // Iterate until the priority queue is empty
        while (!pq.isEmpty()) {
            // Get the vertex with the minimum key value
            Edge minEdge = pq.poll();
            int u = minEdge.dest;
            inMST[u] = true;

            // Explore the neighbors of the current vertex
            for (Edge edge : graph.get(u)) {
                int v = edge.dest;
                int weight = edge.weight;

                // If the vertex v is not in MST and weight of edge is smaller than current key value
                if (!inMST[v] && key[v] > weight) {
                    key[v] = weight;
                    parent[v] = u;
                    pq.offer(new Edge(v, key[v]));
                }
            }
        }

        // Print the MST
        printMST(parent, key);
    }

    // Utility method to print the MST
    private static void printMST(int[] parent, int[] key) {
        int totalWeight = 0;
        System.out.println("Edge \tWeight");
        for (int i = 1; i < parent.length; i++) {
            System.out.println(parent[i] + " - " + i + "\t" + key[i]);
            totalWeight += key[i];
        }
        System.out.println("Total weight of MST: " + totalWeight);
    }

    public static void main(String[] args) {
        int V = 5; // Number of vertices in the graph
        List<List<Edge>> graph = new ArrayList<>();
        
        // Initialize the adjacency list
        for (int i = 0; i < V; i++) {
            graph.add(new ArrayList<>());
        }

        // Add edges to the graph
        graph.get(0).add(new Edge(1, 2));
        graph.get(0).add(new Edge(3, 6));
        graph.get(1).add(new Edge(0, 2));
        graph.get(1).add(new Edge(2, 3));
        graph.get(1).add(new Edge(3, 8));
        graph.get(2).add(new Edge(1, 3));
        graph.get(2).add(new Edge(3, 5));
        graph.get(3).add(new Edge(0, 6));
        graph.get(3).add(new Edge(1, 8));
        graph.get(3).add(new Edge(2, 5));
        
        // Perform Prim's Algorithm to find the MST
        primMST(graph, V);
    }
}
```

### **Explanation of Prim’s Algorithm:**
1. **Edge Class**: This represents an edge in the graph, where `dest` is the destination vertex and `weight` is the weight of the edge.
   
2. **primMST()**:
   - **PriorityQueue (min-heap)**: A priority queue is used to store the edges and vertices, where the edge with the minimum weight is always extracted first.
   - **Key Array**: This array stores the minimum weight of the edge that connects a vertex to the MST.
   - **Parent Array**: This array stores the parent of each vertex in the MST, which helps to reconstruct the MST after the algorithm finishes.
   - **InMST Array**: This array tracks whether a vertex is already included in the MST or not.

3. **Main Logic**:
   - The algorithm starts with vertex 0 and adds it to the MST.
   - Then, it explores the neighbors of the current vertex, and if the weight of an edge is smaller than the current key value for a neighbor, the key is updated.
   - This process continues until all vertices are included in the MST.

4. **printMST()**:
   - This method prints the edges of the MST, along with their weights and the total weight of the MST.

### **Sample Output:**

```
Edge    Weight
0 - 1    2
1 - 2    3
0 - 3    6
Total weight of MST: 11
```

### **Time Complexity of Prim’s Algorithm:**
- **Using Min-Heap**: O(E log V), where **E** is the number of edges and **V** is the number of vertices. This is because each edge is processed once and each extraction from the priority queue takes **O(log V)** time.
- **Using an Adjacency List**: The graph is typically represented using an adjacency list, which allows efficient exploration of neighbors.

### **Space Complexity:**
- **O(V + E)**: The space complexity is O(V + E) for storing the graph, the key array, the parent array, and the priority queue.

### **Advantages of Prim’s Algorithm:**
1. **Efficient for Dense Graphs**: Prim’s algorithm works well on dense graphs, as it uses an adjacency list and processes vertices efficiently using a priority queue.
2. **Consistent Time Complexity**: It provides a predictable time complexity of O(E log V) when using a priority queue.

### **Disadvantages of Prim’s Algorithm:**
1. **Memory Usage**: It requires extra memory for storing key values, parent values, and the priority queue.
2. **Not Efficient for Sparse Graphs**: For sparse graphs, Kruskal’s algorithm may be more efficient.

### **Conclusion:**
Prim's Algorithm is a reliable and efficient way to find the Minimum Spanning Tree of a graph, especially for dense graphs. It is particularly useful when the graph is represented by an adjacency matrix or when you want to incrementally build the MST by starting from an arbitrary vertex.