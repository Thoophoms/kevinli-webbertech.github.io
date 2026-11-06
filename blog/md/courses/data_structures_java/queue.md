# **Queue**

A **Queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. This means that the element added first to the queue will be the first one to be removed. A queue supports the following main operations:
1. **Enqueue**: Adds an element to the back of the queue.
2. **Dequeue**: Removes and returns the element at the front of the queue.
3. **Peek**: Returns the element at the front without removing it.
4. **isEmpty**: Checks if the queue is empty.
5. **size**: Returns the number of elements in the queue.

Here is a simple implementation of a **Queue** using an **array** in Java.

### 1. **Queue Class Implementation**

```java
class Queue {
    private int front;  // Index of the front element
    private int rear;   // Index of the rear element
    private int size;   // Current size of the queue
    private int capacity; // Maximum capacity of the queue
    private int[] queueArray; // Array to hold the elements of the queue

    // Constructor to initialize the queue with a specified capacity
    public Queue(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.front = 0;
        this.rear = capacity - 1;  // Rear is initialized to the last index
        this.queueArray = new int[capacity];
    }

    // Method to add an element to the queue
    public void enqueue(int item) {
        if (isFull()) {
            System.out.println("Queue is full. Cannot enqueue " + item);
            return;
        }
        // Increment rear and add the item
        rear = (rear + 1) % capacity;
        queueArray[rear] = item;
        size++;
        System.out.println(item + " enqueued to queue.");
    }

    // Method to remove and return the element from the front of the queue
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty. Cannot dequeue.");
            return -1;  // Returning -1 to indicate the queue is empty
        }
        int item = queueArray[front];
        front = (front + 1) % capacity;  // Move front to the next element
        size--;
        System.out.println(item + " dequeued from queue.");
        return item;
    }

    // Method to return the front element without removing it
    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty. Cannot peek.");
            return -1;
        }
        return queueArray[front];
    }

    // Method to check if the queue is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Method to check if the queue is full
    public boolean isFull() {
        return size == capacity;
    }

    // Method to return the current size of the queue
    public int size() {
        return size;
    }

    // Method to display the elements of the queue
    public void display() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        int i = front;
        for (int j = 0; j < size; j++) {
            System.out.print(queueArray[i] + " ");
            i = (i + 1) % capacity;  // Circular increment to move to the next element
        }
        System.out.println();
    }
}
```

### 2. **Main Class to Demonstrate Queue Operations**

```java
public class Main {
    public static void main(String[] args) {
        Queue queue = new Queue(5); // Creating a queue with a capacity of 5

        // Enqueue elements
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.enqueue(40);
        queue.enqueue(50);

        // Trying to enqueue when the queue is full
        queue.enqueue(60);

        // Display the elements of the queue
        System.out.println("Queue elements after enqueues:");
        queue.display();  // Output: 10 20 30 40 50

        // Dequeue elements
        queue.dequeue();
        queue.dequeue();

        // Display the elements of the queue after dequeues
        System.out.println("Queue elements after dequeues:");
        queue.display();  // Output: 30 40 50

        // Peek the front element
        System.out.println("Front element: " + queue.peek());  // Output: 30

        // Checking the size of the queue
        System.out.println("Queue size: " + queue.size());  // Output: 3

        // Check if the queue is empty
        System.out.println("Is the queue empty? " + queue.isEmpty());  // Output: false

        // Dequeue all remaining elements
        queue.dequeue();
        queue.dequeue();
        queue.dequeue();

        // Trying to dequeue from an empty queue
        queue.dequeue();
    }
}
```

### **Explanation:**
- **Queue Class**:
  - **enqueue()**: Adds an element to the back of the queue. If the queue is full, it prints an error message.
  - **dequeue()**: Removes and returns the front element from the queue. If the queue is empty, it prints an error message and returns -1.
  - **peek()**: Returns the front element without removing it. If the queue is empty, it prints an error message.
  - **isEmpty()**: Returns `true` if the queue is empty, otherwise returns `false`.
  - **isFull()**: Returns `true` if the queue is full, otherwise returns `false`.
  - **size()**: Returns the number of elements currently in the queue.
  - **display()**: Displays the elements in the queue in FIFO order.

- **Main Class**: Demonstrates the functionality of the queue with operations like enqueue, dequeue, peek, and display.

### **Sample Output:**

```
10 enqueued to queue.
20 enqueued to queue.
30 enqueued to queue.
40 enqueued to queue.
50 enqueued to queue.
Queue is full. Cannot enqueue 60
Queue elements after enqueues:
10 20 30 40 50 
10 dequeued from queue.
20 dequeued from queue.
Queue elements after dequeues:
30 40 50 
Front element: 30
Queue size: 3
Is the queue empty? false
30 dequeued from queue.
40 dequeued from queue.
50 dequeued from queue.
Queue is empty. Cannot dequeue.
```

### **Time Complexity:**
- **enqueue()**: O(1) – Adding an element to the back of the queue takes constant time.
- **dequeue()**: O(1) – Removing the front element takes constant time.
- **peek()**: O(1) – Returning the front element without removing it takes constant time.
- **isEmpty()**: O(1) – Checking if the queue is empty takes constant time.
- **isFull()**: O(1) – Checking if the queue is full takes constant time.
- **display()**: O(n) – Displaying all elements in the queue takes linear time, where n is the number of elements.

### **Notes:**
- This queue implementation uses a **circular array**. By using modulo arithmetic (`(rear + 1) % capacity`), we can ensure that the rear index wraps around to the beginning of the array when it reaches the end.
- If you need a more flexible implementation with automatic resizing, you can implement a **dynamic array-based queue** or use a **LinkedList**. However, the circular array implementation is efficient in terms of space.