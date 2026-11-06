### Graph Processing with GraphX

#### Introduction to GraphX
- **Overview**:
  - GraphX is Spark's API for graph and graph-parallel computation.
  - Combines the advantages of both data-parallel and graph-parallel systems by allowing users to view data as graphs and tables.
  - Provides a unified abstraction for modeling user-defined graphs and applying graph algorithms.

#### Graph Abstraction
- **Vertex RDD**:
  - Represents the set of vertices in the graph.
  - Each vertex has a unique identifier and can have user-defined properties.
  ```scala
  val vertices = sc.parallelize(Array((1L, "Alice"), (2L, "Bob"), (3L, "Charlie")))
  ```

- **Edge RDD**:
  - Represents the set of edges in the graph.
  - Each edge connects two vertices and can have user-defined properties.
  ```scala
  val edges = sc.parallelize(Array(Edge(1L, 2L, "is friends with"), Edge(2L, 3L, "likes")))
  ```

- **Graph Object**:
  - Combines Vertex RDD and Edge RDD into a property graph.
  - Supports user-defined properties for both vertices and edges.
  ```scala
  val graph = Graph(vertices, edges)
  ```

#### Common Graph Algorithms
- **PageRank**:
  - Measures the importance of each vertex within the graph based on the structure of incoming links.
  ```scala
  val ranks = graph.pageRank(0.0001).vertices
  ```

- **Connected Components**:
  - Identifies connected subgraphs within a graph.
  ```scala
  val cc = graph.connectedComponents().vertices
  ```

- **Triangle Counting**:
  - Counts the number of triangles passing through each vertex.
  ```scala
  val triangles = graph.triangleCount().vertices
  ```

#### Using GraphFrames
- **What are GraphFrames?**:
  - A higher-level API for graph processing built on top of Spark DataFrames.
  - Provides seamless integration with Spark SQL and DataFrames.

- **Creating a GraphFrame**:
  - Uses DataFrames for vertices and edges.
  ```python
  from graphframes import GraphFrame

  vertices = spark.createDataFrame([
      ("1", "Alice", 34),
      ("2", "Bob", 36),
      ("3", "Charlie", 30)
  ], ["id", "name", "age"])

  edges = spark.createDataFrame([
      ("1", "2", "friend"),
      ("2", "3", "follow"),
      ("3", "1", "follow")
  ], ["src", "dst", "relationship"])

  g = GraphFrame(vertices, edges)
  ```

- **Common Operations**:
  - **Finding Motifs**:
    - Complex patterns in the graph can be found using a motif-finding API.
    ```python
    motifs = g.find("(a)-[e]->(b)")
    motifs.show()
    ```
  - **PageRank**:
    - Calculates the PageRank of each vertex.
    ```python
    results = g.pageRank(resetProbability=0.15, maxIter=10)
    results.vertices.select("id", "pagerank").show()
    ```
  - **Connected Components**:
    - Identifies connected components within the graph.
    ```python
    result = g.connectedComponents()
    result.select("id", "component").show()
    ```
  - **Triangle Counting**:
    - Counts the number of triangles passing through each vertex.
    ```python
    results = g.triangleCount()
    results.select("id", "count").show()
    ```

