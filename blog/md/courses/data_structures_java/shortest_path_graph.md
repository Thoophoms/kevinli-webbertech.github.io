# Shortest Path Algorithm in Graph

In **graph theory**, finding the **shortest path** between two vertices in a graph is a fundamental problem. A **shortest path** is the path that connects two vertices with the minimum possible sum of edge weights. The problem can be solved using various algorithms, depending on the type of graph and its characteristics.

### **Types of Graphs and Shortest Path Problems:**
1. **Weighted Graphs**: Graphs where edges have weights or costs associated with them.
2. **Unweighted Graphs**: Graphs where all edges have the same weight (often treated as 1).
3. **Directed Graphs**: Graphs where edges have a direction (i.e., they go from one vertex to another).
4. **Undirected Graphs**: Graphs where edges have no direction and can be traversed both ways.

### **Algorithms to Find the Shortest Path:**
1. **Dijkstra's Algorithm**:
   - **Best for**: Weighted graphs with non-negative edge weights.
   - **Method**: Dijkstra’s algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph.
   - **Time Complexity**: O(E log V) when using a priority queue (min-heap), where **E** is the number of edges and **V** is the number of vertices.

2. **Bellman-Ford Algorithm**:
   - **Best for**: Graphs with negative weight edges (but no negative weight cycles).
   - **Method**: It works by relaxing the edges repeatedly and can detect negative weight cycles.
   - **Time Complexity**: O(VE), where **V** is the number of vertices and **E** is the number of edges.

3. **Floyd-Warshall Algorithm**:
   - **Best for**: Finding shortest paths between all pairs of vertices in a graph (all-pairs shortest path).
   - **Method**: It uses dynamic programming to compute shortest paths between all pairs of vertices.
   - **Time Complexity**: O(V³), where **V** is the number of vertices.

4. **Breadth-First Search (BFS)**:
   - **Best for**: Unweighted graphs or graphs with uniform edge weights.
   - **Method**: BFS finds the shortest path in terms of the number of edges (or steps) in an unweighted graph.
   - **Time Complexity**: O(V + E), where **V** is the number of vertices and **E** is the number of edges.

### **Dijkstra's Algorithm Explanation**

Dijkstra's Algorithm is one of the most efficient algorithms for finding the shortest path in a graph with non-negative edge weights. It works by maintaining a set of vertices whose shortest distance from the source is already known and repeatedly selecting the vertex with the smallest known distance to explore its neighbors.

### **Steps of Dijkstra's Algorithm:**
1. **Initialize**:
   - Set the distance to the source vertex to 0 and the distance to all other vertices to infinity.
   - Mark all vertices as unvisited.
   - Set the source vertex as the current vertex.
   
2. **Relaxation**:
   - For the current vertex, consider all its unvisited neighbors and calculate their tentative distances through the current vertex. If the calculated distance of a vertex is less than the known distance, update the shortest distance.
   
3. **Select the Next Vertex**:
   - After processing the current vertex, mark it as visited. The algorithm then selects the unvisited vertex with the smallest tentative distance and repeats the process until all vertices have been visited.

4. **Output**:
   - After visiting all vertices, the shortest distance from the source to each vertex will be known.

### **Dijkstra’s Algorithm Example (Java Implementation)**

Below is a Java implementation of **Dijkstra’s Algorithm** using an adjacency list and a priority queue (min-heap):

```java
import java.util.*;

class Dijkstra {
    // Class to represent the graph
    static class Graph {
        private final int V;  // Number of vertices
        private final List<List<Node>> adjList;  // Adjacency list representation of the graph

        // Constructor to initialize the graph
        public Graph(int V) {
            this.V = V;
            adjList = new ArrayList<>();
            for (int i = 0; i < V; i++) {
                adjList.add(new ArrayList<>());
            }
        }

        // Add an edge to the graph
        public void addEdge(int src, int dest, int weight) {
            adjList.get(src).add(new Node(dest, weight));  // Add an edge from src to dest with weight
        }

        // Dijkstra's Algorithm to find the shortest path from source to all vertices
        public int[] dijkstra(int src) {
            int[] dist = new int[V];  // Array to store the shortest distance from source to each vertex
            Arrays.fill(dist, Integer.MAX_VALUE);  // Initialize all distances to infinity
            dist[src] = 0;  // Distance to source is 0

            PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
            pq.add(new Node(src, 0));  // Add the source vertex to the priority queue

            while (!pq.isEmpty()) {
                Node node = pq.poll();  // Get the vertex with the minimum distance
                int u = node.vertex;

                // Explore all neighbors of the current vertex
                for (Node neighbor : adjList.get(u)) {
                    int v = neighbor.vertex;
                    int weight = neighbor.weight;

                    // Relax the edge if a shorter path is found
                    if (dist[u] + weight < dist[v]) {
                        dist[v] = dist[u] + weight;
                        pq.add(new Node(v, dist[v]));  // Add the updated neighbor to the priority queue
                    }
                }
            }
            return dist;  // Return the shortest distance from source to all vertices
        }
    }

    // Class to represent a node (vertex) in the graph
    static class Node {
        int vertex, weight;

        public Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
    }

    // Utility method to print the shortest distances from the source to all vertices
    public static void printSolution(int[] dist) {
        System.out.println("Vertex Distance from Source");
        for (int i = 0; i < dist.length; i++) {
            System.out.println(i + " \t\t " + dist[i]);
        }
    }

    public static void main(String[] args) {
        // Create a graph
        Graph graph = new Graph(9);

        // Add edges to the graph
        graph.addEdge(0, 1, 4);
        graph.addEdge(0, 7, 8);
        graph.addEdge(1, 2, 8);
        graph.addEdge(1, 7, 11);
        graph.addEdge(2, 3, 7);
        graph.addEdge(2, 5, 4);
        graph.addEdge(2, 8, 2);
        graph.addEdge(3, 4, 9);
        graph.addEdge(3, 5, 14);
        graph.addEdge(4, 5, 10);
        graph.addEdge(5, 6, 2);
        graph.addEdge(6, 7, 1);
        graph.addEdge(6, 8, 6);
        graph.addEdge(7, 8, 7);

        // Find the shortest paths from vertex 0
        int[] dist = graph.dijkstra(0);

        // Print the shortest distances
        printSolution(dist);
    }
}
```

### **Explanation of Dijkstra’s Algorithm Code**:
1. **Graph Class**:
   - Represents a graph using an adjacency list. Each vertex is connected to its neighbors with a weight.
   - The `addEdge()` method adds an edge to the graph with the given source vertex, destination vertex, and weight.
   - The `dijkstra()` method implements Dijkstra’s algorithm to compute the shortest paths from the source vertex to all other vertices.

2. **Node Class**:
   - Represents a node in the graph. Each node has a vertex (the destination) and a weight (the cost of the edge).
   
3. **Priority Queue**:
   - A priority queue (min-heap) is used to efficiently get the vertex with the minimum distance during each iteration of the algorithm.

4. **printSolution()**:
   - This utility function prints the shortest distance from the source to each vertex.

### **Sample Output:**

```
Vertex Distance from Source
0 		 0
1 		 4
2 		 12
3 		 19
4 		 21
5 		 11
6 		 9
7 		 8
8 		 14
```

### **Time Complexity of Dijkstra's Algorithm:**
- **Using Min-Heap**: O(E log V), where **E** is the number of edges and **V** is the number of vertices.
  - Each edge is processed once, and each extraction from the priority queue (min-heap) takes O(log V) time.

### **Space Complexity:**
- **O(V + E)**: Space is used for the adjacency list and priority queue. The space used by the adjacency list is proportional to the number of edges **E** and the number of vertices **V**.

### **Advantages of Dijkstra’s Algorithm:**
1. **Efficient for Non-Negative Weights**: Dijkstra’s algorithm works efficiently for graphs with non-negative edge weights.
2. **Minimizes the Shortest Path**: It guarantees finding the shortest path from the source to all other vertices in O(E log V) time.
3. **Widely Used**: It is used in network routing protocols and pathfinding algorithms (e.g., in GPS systems).

### **Disadvantages of Dijkstra’s Algorithm:**
1. **Not Suitable for Negative Weights**: It doesn’t handle negative edge weights well. For graphs with negative weights, the **Bellman-Ford algorithm** is preferred.
2. **Greedy Nature**: The algorithm greedily picks the closest vertex, which works well for most cases but may not always yield the correct result if there are negative weights.

### **Conclusion:**
Dijkstra’s Algorithm is an efficient and widely-used algorithm for finding the shortest paths from a source vertex to all other vertices in a graph with non-negative edge weights. It runs in O(E log V) time when using a priority queue, making it suitable for sparse and dense graphs. For graphs with negative weights, **Bellman-Ford** is a better choice.

## **Bellman-Ford**

The **Bellman-Ford Algorithm** is a graph algorithm used for finding the **shortest path** from a **single source vertex** to all other vertices in a **weighted graph**. It is particularly useful when the graph has **negative weight edges** but no negative weight cycles.

### **Bellman-Ford Algorithm Overview:**
1. **Handle Negative Weights**: Unlike Dijkstra's algorithm, which assumes all edge weights are non-negative, Bellman-Ford works with graphs containing negative edge weights.
2. **Detect Negative Cycles**: One of the unique features of the Bellman-Ford algorithm is that it can detect **negative weight cycles** in the graph. A negative weight cycle is a cycle where the sum of the edge weights is negative, and repeatedly traversing this cycle will decrease the total path cost indefinitely.

### **Steps of the Bellman-Ford Algorithm:**
1. **Initialization**:
   - Set the distance to the source vertex as 0 and the distance to all other vertices as infinity.
   
2. **Relaxation**:
   - For each edge in the graph, check if the distance to the destination vertex can be minimized by going through the source vertex. This is done by updating the distance to the destination vertex if the current path offers a shorter path than the known path.
   - Repeat this process for **V - 1 iterations**, where **V** is the number of vertices. This ensures that the shortest paths are found for all vertices.

3. **Negative Cycle Detection**:
   - After the **V - 1 iterations**, perform one more iteration to check if any distance can be further minimized. If so, a negative weight cycle exists in the graph.

### **Bellman-Ford Algorithm Pseudocode:**
1. Initialize the distance of all vertices to infinity, except the source vertex, which is set to 0.
2. For each edge `(u, v)` with weight `w`, if `distance[u] + w < distance[v]`, update `distance[v]`.
3. Repeat the process for `V - 1` times.
4. Check for negative cycles by iterating over all edges again.

### **Time Complexity of Bellman-Ford Algorithm:**
- **Time Complexity**: O(V * E), where **V** is the number of vertices and **E** is the number of edges in the graph.
  - For each edge, we perform relaxation, and we repeat this process **V - 1** times.
- **Space Complexity**: O(V), since we need to store the distance for each vertex.

### **Java Implementation of Bellman-Ford Algorithm:**

Here’s how you can implement **Bellman-Ford** in Java:

```java
import java.util.*;

class BellmanFord {
    // Class to represent an edge in the graph
    static class Edge {
        int src, dest, weight;

        public Edge(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
    }

    // Method to perform the Bellman-Ford algorithm
    public static void bellmanFord(List<Edge> edges, int V, int source) {
        int[] dist = new int[V];  // Array to store the shortest distance from source to each vertex

        // Step 1: Initialize distances
        Arrays.fill(dist, Integer.MAX_VALUE);  // Set all distances to infinity
        dist[source] = 0;  // Distance to the source is 0

        // Step 2: Relax all edges V-1 times
        for (int i = 1; i < V; i++) {
            for (Edge edge : edges) {
                int u = edge.src;
                int v = edge.dest;
                int weight = edge.weight;

                if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                }
            }
        }

        // Step 3: Check for negative-weight cycles
        for (Edge edge : edges) {
            int u = edge.src;
            int v = edge.dest;
            int weight = edge.weight;

            if (dist[u] != Integer.MAX_VALUE && dist[u] + weight < dist[v]) {
                System.out.println("Graph contains negative weight cycle");
                return;
            }
        }

        // Step 4: Print the shortest distances
        printSolution(dist);
    }

    // Utility method to print the solution
    public static void printSolution(int[] dist) {
        System.out.println("Vertex Distance from Source");
        for (int i = 0; i < dist.length; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                System.out.println(i + " \t\t INF");
            } else {
                System.out.println(i + " \t\t " + dist[i]);
            }
        }
    }

    public static void main(String[] args) {
        // Example graph with 5 vertices (0 to 4)
        int V = 5;
        List<Edge> edges = new ArrayList<>();

        // Add edges to the graph
        edges.add(new Edge(0, 1, -1));
        edges.add(new Edge(0, 2, 4));
        edges.add(new Edge(1, 2, 3));
        edges.add(new Edge(1, 3, 2));
        edges.add(new Edge(1, 4, 2));
        edges.add(new Edge(3, 2, 5));
        edges.add(new Edge(3, 1, 1));
        edges.add(new Edge(4, 3, -3));

        // Perform Bellman-Ford algorithm from source vertex 0
        bellmanFord(edges, V, 0);
    }
}
```

### **Explanation of the Code:**

1. **Edge Class**: Represents an edge in the graph with a source vertex, destination vertex, and the edge weight.

2. **bellmanFord()**:
   - **Step 1**: Initialize the `dist[]` array with **infinity** for all vertices, except for the source vertex, which is set to **0**.
   - **Step 2**: Perform relaxation for all edges **V - 1** times. For each edge `(u, v)`, if the distance to vertex `v` can be shortened by going through `u`, update `dist[v]`.
   - **Step 3**: After **V - 1** iterations, perform one more iteration to check for negative weight cycles. If an edge can still be relaxed, then there is a negative weight cycle.
   - **Step 4**: If no negative weight cycle is detected, print the shortest distances from the source vertex to all other vertices.

3. **printSolution()**: Prints the shortest distance from the source vertex to all other vertices in the graph.

4. **main()**: Creates an example graph with 5 vertices (0 to 4) and edges with weights, then runs the **Bellman-Ford** algorithm from source vertex 0.

### **Sample Output:**

```
Vertex Distance from Source
0 	     0
1 	     -1
2 	     2
3 	     -2
4 	     1
```

### **Time Complexity of Bellman-Ford Algorithm:**
- **O(V * E)**: We relax each edge **V-1** times, and each relaxation step takes **O(E)** time, where **V** is the number of vertices and **E** is the number of edges.

### **Space Complexity:**
- **O(V)**: Space is required to store the distance of each vertex from the source and the edges list.

### **Advantages of Bellman-Ford Algorithm:**
1. **Handles Negative Weight Edges**: Unlike Dijkstra’s algorithm, Bellman-Ford can handle graphs with negative weight edges.
2. **Cycle Detection**: Bellman-Ford can also detect negative weight cycles, which is useful in many applications, such as detecting arbitrage opportunities in currency exchange rates.

### **Disadvantages of Bellman-Ford Algorithm:**
1. **Inefficient for Dense Graphs**: The algorithm has a time complexity of O(V * E), which makes it inefficient for large graphs with many edges.
2. **Slower than Dijkstra’s Algorithm**: Dijkstra’s algorithm is generally faster for graphs with non-negative edge weights and is more commonly used in practice for such graphs.

### **Conclusion:**
The **Bellman-Ford Algorithm** is useful when working with graphs that contain negative weight edges, or when detecting negative weight cycles is important. However, it is not as efficient as Dijkstra's algorithm for graphs with non-negative edge weights due to its higher time complexity. For graphs without negative weight cycles, **Dijkstra’s Algorithm** is generally preferred.