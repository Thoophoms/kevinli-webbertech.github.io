# **Breadth-First Search (BFS)**

**Breadth-First Search (BFS)** is a graph traversal algorithm that explores all the vertices of a graph level by level. It starts from a source node and explores all of its neighbors before moving on to the next level of neighbors. BFS is often used to find the shortest path in an unweighted graph or to explore all the nodes reachable from a given node.

### **Key Characteristics of BFS**:
1. **Exploration by Levels**: BFS explores all the neighbors of a node before moving on to the next level. This ensures that nodes closer to the source are explored first.
2. **Queue-based**: BFS uses a **queue** to store the vertices to be explored next. The first node added to the queue is the first one to be explored (FIFO).
3. **Shortest Path**: In an unweighted graph, BFS guarantees finding the shortest path from the source to any other reachable node.
4. **Uses of BFS**:
   - Finding the shortest path in an unweighted graph.
   - Finding all nodes within a given distance from a source node.
   - Solving problems in puzzles, such as the "8-puzzle" or "Sudoku".
   - In network analysis, finding the number of connected components, etc.

### **BFS Algorithm:**
1. **Initialize**: Start from the source node. Mark it as visited and enqueue it.
2. **Explore**: While the queue is not empty:
   - Dequeue the front node.
   - Explore all its unvisited neighbors.
   - Mark them as visited and enqueue them.
3. **Repeat**: Continue the process until the queue is empty, indicating that all reachable nodes have been explored.

### **Time and Space Complexity**:
- **Time Complexity**: O(V + E), where:
  - **V** is the number of vertices.
  - **E** is the number of edges.
  - Each vertex and edge is processed once in BFS.
- **Space Complexity**: O(V), as the queue stores all vertices in the worst case, and we also store the visited list.

### **Java Implementation of BFS**:

Let’s consider BFS on an **undirected graph**, represented using an adjacency list.

#### **Graph Representation**:
- A graph can be represented as an adjacency list, where each node has a list of its neighbors.

#### **Java Implementation**:

```java
import java.util.*;

public class BFS {

    // Method to perform BFS on the graph
    public static void bfs(int start, List<List<Integer>> graph) {
        // Number of nodes in the graph
        int n = graph.size();

        // Array to keep track of visited nodes
        boolean[] visited = new boolean[n];

        // Create a queue for BFS
        Queue<Integer> queue = new LinkedList<>();

        // Start from the source node
        visited[start] = true;
        queue.offer(start);

        // Explore the graph
        while (!queue.isEmpty()) {
            int currentNode = queue.poll(); // Get the front element of the queue
            System.out.print(currentNode + " "); // Print the current node

            // Visit all the unvisited neighbors of the current node
            for (int neighbor : graph.get(currentNode)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true; // Mark as visited
                    queue.offer(neighbor); // Enqueue the neighbor
                }
            }
        }
    }

    public static void main(String[] args) {
        // Create an undirected graph represented as an adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        
        // Add nodes and edges to the graph
        for (int i = 0; i < 6; i++) {
            graph.add(new ArrayList<>());
        }
        
        // Add edges (for example: 0-1, 0-2, 1-2, etc.)
        graph.get(0).add(1);
        graph.get(0).add(2);
        graph.get(1).add(0);
        graph.get(1).add(2);
        graph.get(2).add(0);
        graph.get(2).add(1);
        graph.get(3).add(4);
        graph.get(4).add(3);
        graph.get(5).add(5); // self-loop

        // Perform BFS starting from node 0
        System.out.println("BFS traversal starting from node 0:");
        bfs(0, graph);
    }
}
```

#### **Explanation**:
1. **Graph Representation**: We use an adjacency list to represent the graph. Each index of the list represents a node, and each node has a list of its neighboring nodes.
2. **BFS Function**:
   - A `visited` array is used to keep track of which nodes have already been explored.
   - A queue (`Queue<Integer>`) is used to manage the exploration process. The queue stores the nodes to be visited.
   - The algorithm starts with the source node (`start`), marks it as visited, and then iterates over its neighbors. Each unvisited neighbor is enqueued and explored.
3. **Main Function**: In the `main()` method, we create a graph, add edges, and start BFS from node `0`.

#### **Sample Output**:

```
BFS traversal starting from node 0:
0 1 2 3 4 5 
```

In this output, BFS starts at node `0` and explores all reachable nodes in a breadth-first manner.

---

### **Example 2: BFS for Shortest Path in an Unweighted Graph**

**Problem Statement**: Find the shortest path from a source node to all other nodes in an unweighted graph using BFS.

#### **Approach**:
1. Use BFS starting from the source node.
2. Keep track of the distance from the source to each node. The first time a node is visited, its distance is recorded.
3. The distance of each node from the source is the number of edges in the shortest path from the source to that node.

#### **Java Implementation**:

```java
import java.util.*;

public class BFSShortestPath {

    // Method to find the shortest path using BFS
    public static void bfsShortestPath(int start, List<List<Integer>> graph) {
        int n = graph.size();
        int[] distance = new int[n];
        Arrays.fill(distance, -1); // Initialize distances to -1 (unreachable)
        Queue<Integer> queue = new LinkedList<>();

        // Start from the source node
        distance[start] = 0;
        queue.offer(start);

        while (!queue.isEmpty()) {
            int currentNode = queue.poll();

            // Explore all the unvisited neighbors of the current node
            for (int neighbor : graph.get(currentNode)) {
                if (distance[neighbor] == -1) { // If the node is unvisited
                    distance[neighbor] = distance[currentNode] + 1; // Update distance
                    queue.offer(neighbor); // Enqueue the neighbor
                }
            }
        }

        // Print the shortest distances from the start node
        System.out.println("Shortest distances from node " + start + ":");
        for (int i = 0; i < n; i++) {
            System.out.println("Distance to node " + i + ": " + distance[i]);
        }
    }

    public static void main(String[] args) {
        // Create an undirected graph represented as an adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        
        for (int i = 0; i < 6; i++) {
            graph.add(new ArrayList<>());
        }
        
        // Add edges
        graph.get(0).add(1);
        graph.get(0).add(2);
        graph.get(1).add(0);
        graph.get(1).add(2);
        graph.get(2).add(0);
        graph.get(2).add(1);
        graph.get(3).add(4);
        graph.get(4).add(3);
        graph.get(5).add(5);

        // Find shortest paths from node 0
        bfsShortestPath(0, graph);
    }
}
```

#### **Explanation**:
- The `bfsShortestPath()` function computes the shortest distance from the `start` node to all other nodes in the graph.
- The distance for each node is stored in the `distance[]` array. Initially, all distances are set to `-1` (indicating the node is not reachable).
- During BFS, the `distance[]` array is updated with the number of edges from the source node.
- At the end of BFS, the `distance[]` array contains the shortest distances from the source to all reachable nodes.

#### **Sample Output**:

```
Shortest distances from node 0:
Distance to node 0: 0
Distance to node 1: 1
Distance to node 2: 1
Distance to node 3: -1
Distance to node 4: -1
Distance to node 5: -1
```

This output shows the shortest distance from node `0` to all other nodes in the graph. Nodes that are not reachable from node `0` have a distance of `-1`.

---

### **Applications of BFS**:
1. **Shortest Path in Unweighted Graphs**: BFS is optimal for finding the shortest path in unweighted graphs.
2. **Level-order Traversal**: BFS can be used to perform a level-order traversal of a tree or graph.
3. **Connected Components**: BFS can be used to find all nodes reachable from a given node in a connected graph.
4. **Finding the Minimum Number of Moves**: BFS can solve problems like "minimum number of moves to reach the target" in puzzles like **the 8-puzzle**, **chessboard problems**, etc.

### **Time and Space Complexity**:
- **Time Complexity**: O(V + E), where:
  - **V** is the number of vertices (nodes).
  - **E** is the number of edges in the graph.
  - BFS explores each vertex and edge at most once.
  
- **Space Complexity**: O(V), as we need space for the visited list, the queue, and possibly a distance array (for storing the shortest paths).

---

### **Conclusion**:
**Breadth-First Search (BFS)** is a versatile and efficient graph traversal algorithm, particularly useful for finding the shortest path in unweighted graphs and for solving problems where level-wise exploration is required. Its time complexity of O(V + E) makes it suitable for graphs with a large number of vertices and edges.