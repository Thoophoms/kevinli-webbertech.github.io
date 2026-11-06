# **Depth-First Search (DFS)**

**Depth-First Search (DFS)** is a graph traversal algorithm that explores as far down a branch (path) as possible before backtracking. DFS starts from a source node and explores all the way down to a leaf node or until it cannot go further, then backtracks and explores other unvisited nodes.

### **Key Characteristics of DFS**:
1. **Exploration by Depth**: DFS explores deeper into the graph before backtracking. It goes down one path completely before moving to another path.
2. **Uses Stack**: DFS can be implemented using a **stack** data structure (either explicitly using a stack or implicitly through recursion). The stack helps in backtracking when a path is fully explored.
3. **Recursion**: DFS is naturally implemented recursively, as each recursive call explores one branch of the graph.
4. **Search Tree**: The path taken from the starting node to the end node forms a tree-like structure.

### **DFS Algorithm**:

1. **Start from a source node** and mark it as visited.
2. **Explore** all the unvisited neighbors of the node. For each unvisited neighbor, call the DFS function recursively.
3. **Backtrack** if all neighbors of a node are visited and return to the previous node to explore other branches.
4. **Repeat** the process until all nodes are visited.

### **Time and Space Complexity**:
- **Time Complexity**: O(V + E), where **V** is the number of vertices (nodes) and **E** is the number of edges in the graph. Each vertex and edge is explored once.
- **Space Complexity**: O(V), as space is required for the stack (in the case of a recursive DFS) or for the visited nodes tracking array.

### **DFS Types**:
1. **Preorder DFS**: Process the current node before exploring its neighbors.
2. **Inorder DFS**: Process the current node between its left and right children (commonly used in binary trees).
3. **Postorder DFS**: Process the current node after exploring all its neighbors.

---

### **Example of DFS:**

#### **DFS on a Graph**:
Let’s consider a **graph represented as an adjacency list**. We will implement DFS to traverse the graph and print the nodes visited.

#### **Java Implementation**:

```java
import java.util.*;

public class DFS {

    // Method to perform DFS on the graph
    public static void dfs(int start, List<List<Integer>> graph) {
        int n = graph.size();
        boolean[] visited = new boolean[n];  // Array to track visited nodes

        // Call the recursive DFS function
        dfsRecursive(start, visited, graph);
    }

    // Recursive DFS method to explore the graph
    public static void dfsRecursive(int node, boolean[] visited, List<List<Integer>> graph) {
        visited[node] = true; // Mark the node as visited
        System.out.print(node + " "); // Print the current node

        // Explore all the neighbors of the current node
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {  // If the neighbor is unvisited, recursively explore it
                dfsRecursive(neighbor, visited, graph);
            }
        }
    }

    public static void main(String[] args) {
        // Create an undirected graph represented as an adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        
        // Add nodes and edges to the graph (for example, 0-1, 0-2, 1-3, etc.)
        for (int i = 0; i < 6; i++) {
            graph.add(new ArrayList<>());
        }
        
        // Add edges
        graph.get(0).add(1);
        graph.get(0).add(2);
        graph.get(1).add(0);
        graph.get(1).add(3);
        graph.get(2).add(0);
        graph.get(2).add(4);
        graph.get(3).add(1);
        graph.get(4).add(2);
        graph.get(5).add(5);  // Self loop for node 5

        // Perform DFS starting from node 0
        System.out.println("DFS traversal starting from node 0:");
        dfs(0, graph);
    }
}
```

#### **Explanation**:
1. **Graph Representation**: The graph is represented as an adjacency list, where each index represents a node, and each node has a list of its neighbors.
2. **dfs()**: This function initiates the DFS traversal starting from the given source node.
3. **dfsRecursive()**: This is the core recursive function that explores the graph. It marks the current node as visited, prints it, and recursively explores all its unvisited neighbors.
4. **visited[]**: An array used to track which nodes have been visited to avoid revisiting them.

#### **Sample Output**:

```
DFS traversal starting from node 0:
0 1 3 2 4 5 
```

The DFS starts from node `0` and explores as deep as possible before backtracking. The order of traversal depends on the adjacency list and the recursion.

---

### **Example 2: DFS for Finding a Path in a Graph**

**Problem Statement**: Given a graph, find if there is a path from a source node to a destination node.

#### **Approach**:
1. Start DFS from the source node.
2. If we reach the destination node during the DFS traversal, return true (path found).
3. If all neighbors are visited and we haven't reached the destination, return false (no path exists).

#### **Java Implementation**:

```java
import java.util.*;

public class DFSPath {

    // Method to perform DFS and find if there is a path
    public static boolean hasPath(int start, int destination, List<List<Integer>> graph) {
        int n = graph.size();
        boolean[] visited = new boolean[n];  // Array to track visited nodes
        return dfsRecursive(start, destination, visited, graph);
    }

    // Recursive DFS method to explore the graph
    public static boolean dfsRecursive(int node, int destination, boolean[] visited, List<List<Integer>> graph) {
        if (node == destination) {
            return true; // If we've reached the destination, return true
        }

        visited[node] = true; // Mark the node as visited

        // Explore all the neighbors of the current node
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {  // If the neighbor is unvisited, recursively explore it
                if (dfsRecursive(neighbor, destination, visited, graph)) {
                    return true; // If a path is found, return true
                }
            }
        }

        return false; // If no path is found
    }

    public static void main(String[] args) {
        // Create an undirected graph represented as an adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        
        // Add nodes and edges to the graph (for example, 0-1, 0-2, 1-3, etc.)
        for (int i = 0; i < 6; i++) {
            graph.add(new ArrayList<>());
        }
        
        // Add edges
        graph.get(0).add(1);
        graph.get(0).add(2);
        graph.get(1).add(0);
        graph.get(1).add(3);
        graph.get(2).add(0);
        graph.get(2).add(4);
        graph.get(3).add(1);
        graph.get(4).add(2);
        graph.get(5).add(5);  // Self loop for node 5

        // Check if there is a path from node 0 to node 4
        boolean result = hasPath(0, 4, graph);
        System.out.println("Path from node 0 to node 4: " + result);
    }
}
```

#### **Explanation**:
1. **hasPath()**: This function initiates the DFS search to check if there is a path from the source node to the destination node.
2. **dfsRecursive()**: This recursive function explores the graph, and if it reaches the destination node, it returns true. If a node’s neighbors are unexplored, it recursively explores them.

#### **Sample Output**:

```
Path from node 0 to node 4: true
```

---

### **Applications of DFS**:
1. **Pathfinding**: DFS can be used to find if there exists a path between two nodes in a graph.
2. **Topological Sorting**: DFS is used in algorithms like **Kahn's algorithm** for topological sorting of directed acyclic graphs (DAGs).
3. **Cycle Detection**: DFS can help detect cycles in directed and undirected graphs.
4. **Connected Components**: In an undirected graph, DFS can be used to find all the connected components.
5. **Solving Puzzles and Games**: DFS is often used in problems where you need to explore all possible solutions, such as solving mazes or puzzles (e.g., **Sudoku**, **8-puzzle**).

### **Time and Space Complexity**:
- **Time Complexity**: O(V + E), where **V** is the number of vertices and **E** is the number of edges. Each vertex and edge is visited once during DFS.
- **Space Complexity**: O(V), due to the recursion stack and the visited array.

### **Conclusion**:
DFS is a versatile graph traversal algorithm that is widely used for pathfinding, cycle detection, solving puzzles, and many other problems. Its ability to explore deeply through recursion makes it suitable for a variety of applications. However, it is not always the best choice for finding the shortest path in an unweighted graph, as BFS would be more efficient for that purpose.