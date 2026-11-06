# Shortest Path Algorithm in Graph

## Shortest Path Algorithm in Graph

In graph theory, a **shortest path algorithm** is used to find the shortest path between two vertices in a graph. These algorithms are essential for applications such as navigation systems (finding the shortest route), network routing, and even in social networks (finding the shortest connection between users).

### Types of Graphs

1. **Weighted Graphs**: Graphs where edges have weights (costs or distances).
2. **Unweighted Graphs**: Graphs where edges do not have any specific weight, and all edges are assumed to have equal weight.

### Popular Shortest Path Algorithms

1. **Dijkstra's Algorithm** (For graphs with non-negative weights)
2. **Bellman-Ford Algorithm** (For graphs with negative weights)
3. **A* Search Algorithm** (Optimized version of Dijkstra, typically used in pathfinding)
4. **Floyd-Warshall Algorithm** (For finding shortest paths between all pairs of vertices)

We'll focus on **Dijkstra’s Algorithm** and **Bellman-Ford Algorithm** as the most commonly used algorithms.

---

### 1. **Dijkstra’s Algorithm** (for non-negative weights):

**Dijkstra's Algorithm** is a greedy algorithm that finds the shortest path from a single source node to all other nodes in a graph with non-negative edge weights.

**Steps**:
1. Initialize the distance to the source node as 0 and all other nodes as infinity (`∞`).
2. Add the source node to a priority queue (min-heap) with a distance of 0.
3. While the queue is not empty:
   - Extract the node with the minimum distance from the queue.
   - For each neighbor of this node, calculate the tentative distance. If it's smaller than the current known distance, update the distance and add the neighbor to the queue.
4. Continue until all nodes have been processed or the queue is empty.

**Time Complexity**:
- Using a **min-heap (priority queue)**, the time complexity is \( O((V + E) \log V) \), where `V` is the number of vertices and `E` is the number of edges.

### Python Implementation of Dijkstra’s Algorithm

```python
import heapq

def dijkstra(graph, start):
    # Priority queue to hold (distance, vertex) tuples
    min_heap = [(0, start)]
    # Dictionary to store the shortest distance to each node
    distances = {start: 0}
    # Set of processed nodes
    visited = set()
    
    while min_heap:
        # Pop the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(min_heap)
        
        # If the node is already visited, skip it
        if current_vertex in visited:
            continue
        
        # Mark the current node as visited
        visited.add(current_vertex)
        
        # Explore neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If the new distance is shorter, update it
            if neighbor not in visited and (neighbor not in distances or distance < distances[neighbor]):
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances

# Example Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {distances}")
```

**Output**:
```
Shortest distances from A: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

In the example above, we compute the shortest distances from node `'A'` to all other nodes.

### 2. **Bellman-Ford Algorithm** (for graphs with negative weights):

**Bellman-Ford Algorithm** can handle graphs with negative edge weights, but it is slower than Dijkstra's algorithm. It can also detect negative-weight cycles in the graph.

**Steps**:
1. Initialize the distance to the source node as 0 and all other nodes as infinity (`∞`).
2. Relax all edges `(V-1)` times (where `V` is the number of vertices):
   - For each edge `(u, v)` with weight `w`, if the distance to `u` plus `w` is less than the distance to `v`, update the distance to `v`.
3. After `(V-1)` iterations, check for negative-weight cycles by performing one more relaxation. If any distance can still be updated, it indicates a negative-weight cycle.

**Time Complexity**:
- **O(V * E)**, where `V` is the number of vertices and `E` is the number of edges.

### Python Implementation of Bellman-Ford Algorithm

```python
def bellman_ford(graph, start):
    # Step 1: Initialize distances from the source node to all other nodes
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Step 2: Relax all edges (V-1) times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Step 3: Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                print("Graph contains a negative weight cycle")
                return None
    
    return distances

# Example Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = bellman_ford(graph, start_node)
if distances:
    print(f"Shortest distances from {start_node}: {distances}")
```

**Output**:
```
Shortest distances from A: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

### When to Use Each Algorithm

1. **Dijkstra’s Algorithm**:
   - Best suited for graphs with **non-negative edge weights**.
   - Very efficient with a time complexity of \( O((V + E) \log V) \) using a priority queue.
   - Not suitable for graphs with negative edge weights.

2. **Bellman-Ford Algorithm**:
   - Can handle **graphs with negative edge weights**.
   - Slower than Dijkstra’s with a time complexity of \( O(V * E) \).
   - Useful when you need to **detect negative-weight cycles** in a graph.

### Summary

- **Dijkstra’s Algorithm** is ideal for **non-negative weight graphs**, offering an efficient solution for finding the shortest path from a source node to all other nodes.
- **Bellman-Ford Algorithm** is more general and can handle **negative edge weights**, and it can also detect negative weight cycles, but it is less efficient than Dijkstra’s algorithm.

