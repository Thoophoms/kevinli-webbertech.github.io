# Queue

A **queue** is a **linear data structure** that follows the **First In First Out (FIFO)** principle. This means that the first element inserted into the queue will be the first one to be removed. A queue operates like a real-life queue, such as a line at a ticket counter or a line of people waiting to board a bus.

## Queue Operations

1. **enqueue(item)**: Adds an item to the back of the queue.
2. **dequeue()**: Removes and returns the item from the front of the queue.
3. **peek()**: Returns the item at the front of the queue without removing it.
4. **is_empty()**: Checks if the queue is empty.
5. **size()**: Returns the number of elements in the queue.

## Queue Implementation in Python

A queue can be implemented using various data structures such as a list, deque, or linked list. Here, we will implement it using **Python’s `collections.deque`** (double-ended queue), which is optimized for efficient insertion and removal of elements from both ends.

### Python Code for Queue Implementation

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize an empty deque to represent the queue

    # Add an element to the back of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # Remove and return the front element of the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    # Return the front element without removing it
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Return the size of the queue
    def size(self):
        return len(self.queue)

    # Display the current state of the queue
    def display(self):
        return list(self.queue)


# Example usage
if __name__ == "__main__":
    q = Queue()

    # Enqueue elements to the queue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueue operations:", q.display())  # Output: [10, 20, 30]

    # Peek the front element
    print("Front element:", q.peek())  # Output: 10

    # Dequeue an element from the queue
    print("Dequeued element:", q.dequeue())  # Output: 10
    print("Queue after dequeue operation:", q.display())  # Output: [20, 30]

    # Check if the queue is empty
    print("Is the queue empty?", q.is_empty())  # Output: False

    # Get the size of the queue
    print("Size of the queue:", q.size())  # Output: 2
```

### Explanation

1. **`__init__()`**: Initializes the queue using `deque()`. The `deque` class from the `collections` module is efficient for operations that involve appending or popping elements from both ends.
2. **`enqueue(item)`**: Adds an item to the back of the queue using the `append()` method of `deque`.
3. **`dequeue()`**: Removes and returns the item from the front of the queue using the `popleft()` method of `deque`. If the queue is empty, it returns a message indicating that the queue is empty.
4. **`peek()`**: Returns the front item of the queue without removing it by accessing the first element (`queue[0]`). It checks if the queue is empty before accessing the front element.
5. **`is_empty()`**: Checks whether the queue is empty by checking if the length of the `queue` is zero.
6. **`size()`**: Returns the number of elements in the queue by using the `len()` function.
7. **`display()`**: Converts the `deque` object to a list and returns it, making it easier to visualize the state of the queue.

### Example Output

```
Queue after enqueue operations: [10, 20, 30]
Front element: 10
Dequeued element: 10
Queue after dequeue operation: [20, 30]
Is the queue empty? False
Size of the queue: 2
```

### Advantages of Using `deque`

- **Efficient Operations**: `deque` is optimized for fast `append` and `popleft` operations, both of which have **O(1)** time complexity.
- **Flexible**: While we only use it for a queue (FIFO), it can also efficiently function as a stack (LIFO), or for double-ended operations.

### Summary

- A **queue** follows the **FIFO** principle, where the first element added is the first to be removed.
- This implementation uses the **`deque`** class from the `collections` module, which is efficient for adding and removing elements from both ends of the queue.
- The time complexity of the key operations (enqueue, dequeue, peek, is_empty, and size) is **O(1)**.