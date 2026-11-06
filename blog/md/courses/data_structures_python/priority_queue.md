# Priority Queue

A **Priority Queue (PQ)** is a special type of **queue** where each element is associated with a **priority**. In a standard queue, elements are processed in **First In First Out (FIFO)** order, meaning the first element added is the first one removed. However, in a **Priority Queue**, elements are dequeued in order of their priority rather than their insertion order.

- **Higher priority** elements are dequeued **before** lower priority ones, regardless of the order in which they were added.
- In case of two elements having the same priority, they are dequeued based on their order of insertion (this behavior is often called "First In First Out" for equal priority elements).

### Types of Priority Queue

1. **Max Priority Queue**: In a max priority queue, the **element with the highest priority** is dequeued first.
2. **Min Priority Queue**: In a min priority queue, the **element with the lowest priority** is dequeued first.

### Operations of a Priority Queue

1. **insert(item, priority)**: Adds an item with a specific priority to the queue.
2. **extract_min()** or **extract_max()**: Removes and returns the item with the **lowest** or **highest** priority, respectively.
3. **peek()**: Returns the element with the highest (or lowest) priority without removing it.
4. **is_empty()**: Checks if the priority queue is empty.
5. **size()**: Returns the number of elements in the priority queue.

### Data Structures for Priority Queues

- **Heap**: The most common implementation of a priority queue is using a **heap** (either a **binary min-heap** or **binary max-heap**).
- **Unsorted List**: A priority queue can also be implemented using an unsorted list, but this is inefficient for extraction operations.
- **Sorted List**: A priority queue can be implemented using a sorted list, but insertions are slow (O(n)).
  
### Key Operations Time Complexity (Using Heap)

1. **Insert (enqueue)**: O(log n) – To maintain the heap property after inserting a new element.
2. **Extract (dequeue)**: O(log n) – To remove the highest or lowest priority element and reheapify.
3. **Peek**: O(1) – The highest or lowest priority element is always at the root of the heap.

### Example of Priority Queue Usage

1. **Dijkstra's Algorithm**: A priority queue is used to select the next vertex with the smallest tentative distance in the shortest path algorithm.
2. **Task Scheduling**: A priority queue can be used to schedule tasks based on their priority in operating systems.
3. **Huffman Coding**: A priority queue is used to build a Huffman tree for data compression.
4. **Load Balancing**: A priority queue can be used to manage requests based on their priority in server load balancing.

### Example Code for a Priority Queue Using Python's `heapq` (Min-Priority Queue):

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0  # Used to maintain FIFO for elements with the same priority
    
    # Insert an item into the priority queue
    def insert(self, item, priority):
        # Negate the priority for max-priority queue, for min-priority queue just use priority
        heapq.heappush(self.queue, (priority, self.counter, item))
        self.counter += 1
    
    # Remove and return the item with the highest priority (lowest number)
    def extract_min(self):
        if not self.is_empty():
            priority, counter, item = heapq.heappop(self.queue)
            return item
        return "Queue is empty"

    # Return the item with the highest priority without removing it
    def peek(self):
        if not self.is_empty():
            return self.queue[0][2]  # Return the item part of the tuple
        return "Queue is empty"
    
    # Check if the priority queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    # Get the size of the priority queue
    def size(self):
        return len(self.queue)

    # Display the current priority queue
    def display(self):
        return [item[2] for item in self.queue]  # Extract the items for display

# Example Usage
if __name__ == "__main__":
    pq = PriorityQueue()

    # Insert items into the priority queue
    pq.insert("Task 1", 2)
    pq.insert("Task 2", 1)
    pq.insert("Task 3", 3)

    # Display the priority queue
    print("Priority Queue:", pq.display())  # Output: ['Task 2', 'Task 1', 'Task 3']

    # Peek the element with the highest priority
    print("Peek:", pq.peek())  # Output: 'Task 2'

    # Extract the element with the highest priority (lowest priority number)
    print("Extracted Min:", pq.extract_min())  # Output: 'Task 2'
    print("Priority Queue after extraction:", pq.display())  # Output: ['Task 1', 'Task 3']
```

### Explanation

1. **Heap**: The queue is implemented using Python's `heapq` module, which provides an efficient **min-heap** implementation. In a min-heap, the smallest element is always at the root (index `0`), which makes it easy to extract the element with the minimum priority.

2. **`insert()`**: Inserts an item with a priority. The priority is stored along with a **counter** to ensure the FIFO behavior for items with the same priority (because heapq only compares the first element of the tuple).

3. **`extract_min()`**: Removes and returns the item with the minimum priority (highest priority element). The `heappop()` function from `heapq` is used to extract the smallest element.

4. **`peek()`**: Returns the element with the highest priority (lowest priority number) without removing it.

5. **`is_empty()`**: Returns `True` if the priority queue is empty, otherwise `False`.

6. **`display()`**: Displays the current state of the priority queue.

### Example Output

```
Priority Queue: ['Task 2', 'Task 1', 'Task 3']
Peek: Task 2
Extracted Min: Task 2
Priority Queue after extraction: ['Task 1', 'Task 3']
```

### Summary:
- A **priority queue** is a queue data structure where elements are processed based on their priority.
- **Min-priority queues** process the element with the **lowest priority** first, while **max-priority queues** process the element with the **highest priority** first.
- Priority queues can be implemented using data structures like **heaps**, **sorted lists**, or **unsorted lists**. Using a **heap** is efficient for both insertion and extraction operations.
- Python’s **`heapq`** module is used to implement a **min-priority queue** efficiently, but with a small modification, it can also be used to implement a max-priority queue.