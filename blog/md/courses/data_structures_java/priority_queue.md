# **Priority Queue**

A **Priority Queue** is a special type of queue where each element is assigned a priority. Elements are dequeued in order of their priority, with higher-priority elements being removed before lower-priority ones. If two elements have the same priority, they are dequeued in the order they were added, which is known as **FIFO** for elements with the same priority.

In Java, the **PriorityQueue** class is part of the **java.util** package and implements the **Queue** interface. The priority of elements is determined by their natural ordering (if the elements implement `Comparable`) or by a **Comparator** provided at the time of the queue's creation.

### 1. **PriorityQueue Class Implementation** (Using Java’s built-in PriorityQueue)

Here is an example of how to use the **PriorityQueue** class in Java:

```java
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // Creating a priority queue with natural ordering (min-heap by default)
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        // Adding elements to the priority queue
        pq.add(10);
        pq.add(30);
        pq.add(20);
        pq.add(50);
        pq.add(40);

        System.out.println("Priority Queue (Min-Heap):");
        while (!pq.isEmpty()) {
            // Remove and print elements from the priority queue (min element first)
            System.out.println(pq.poll());
        }

        // Creating a priority queue with a custom comparator (max-heap)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);

        // Adding elements to the max-heap priority queue
        maxHeap.add(10);
        maxHeap.add(30);
        maxHeap.add(20);
        maxHeap.add(50);
        maxHeap.add(40);

        System.out.println("\nPriority Queue (Max-Heap):");
        while (!maxHeap.isEmpty()) {
            // Remove and print elements from the max-heap priority queue (max element first)
            System.out.println(maxHeap.poll());
        }
    }
}
```

### **Explanation:**

1. **Min-Heap PriorityQueue**: By default, the `PriorityQueue` in Java uses the **natural ordering** of the elements, meaning the smallest element has the highest priority.
   - The `poll()` method removes the smallest element from the queue.
   - The queue is a **min-heap** (the smallest element is always at the front).

2. **Max-Heap PriorityQueue**: You can create a max-heap by providing a custom comparator. In the example, the comparator `(a, b) -> b - a` ensures that the larger element has higher priority.
   - The `poll()` method removes the largest element from the queue.
   - The queue behaves as a **max-heap** (the largest element is always at the front).

### **Sample Output:**

```
Priority Queue (Min-Heap):
10
20
30
40
50

Priority Queue (Max-Heap):
50
40
30
20
10
```

### 2. **PriorityQueue with Custom Objects (Using Comparator)**

If you need a priority queue to handle custom objects, you can implement a custom comparator that determines the order of elements in the queue.

Here’s an example of using a **PriorityQueue** to store objects based on their priority:

```java
import java.util.PriorityQueue;

class Task {
    String name;
    int priority;

    // Constructor
    public Task(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    // Getter methods
    public String getName() {
        return name;
    }

    public int getPriority() {
        return priority;
    }

    // Override toString method to display Task details
    @Override
    public String toString() {
        return "Task{name='" + name + "', priority=" + priority + "}";
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating a priority queue with a custom comparator (to order tasks by priority)
        PriorityQueue<Task> taskQueue = new PriorityQueue<>((task1, task2) -> task2.getPriority() - task1.getPriority());

        // Adding tasks to the priority queue
        taskQueue.add(new Task("Task1", 3));
        taskQueue.add(new Task("Task2", 1));
        taskQueue.add(new Task("Task3", 4));
        taskQueue.add(new Task("Task4", 2));

        // Removing and displaying tasks from the queue (highest priority first)
        System.out.println("Tasks in order of priority:");
        while (!taskQueue.isEmpty()) {
            System.out.println(taskQueue.poll());
        }
    }
}
```

### **Explanation:**
- **Task Class**: A custom class that has a name and a priority. The priority determines the order of the tasks in the queue.
- **Comparator**: We create a comparator `(task1, task2) -> task2.getPriority() - task1.getPriority()` to order tasks by their priority in descending order (higher priority tasks come first).
- **PriorityQueue**: The `PriorityQueue` will order the tasks based on their priority, removing the task with the highest priority first.

### **Sample Output:**

```
Tasks in order of priority:
Task{name='Task3', priority=4}
Task{name='Task1', priority=3}
Task{name='Task4', priority=2}
Task{name='Task2', priority=1}
```

### **Time Complexity:**

- **Insertion (`add()`)**: O(log n) – Each insertion operation takes logarithmic time because the priority queue maintains a heap structure.
- **Removal (`poll()`)**: O(log n) – Removing the element with the highest priority also takes logarithmic time, as the heap must be restructured.
- **Peek (`peek()`)**: O(1) – Accessing the element with the highest priority is done in constant time.

### **Important Notes:**
- The `PriorityQueue` class in Java does **not** allow `null` elements. If you attempt to insert `null`, a `NullPointerException` will be thrown.
- By default, Java's `PriorityQueue` uses a **min-heap**, but you can create a **max-heap** by using a custom comparator.
- **PriorityQueue** is not thread-safe. If multiple threads access the queue concurrently, you should synchronize access to it or use the **PriorityBlockingQueue** for thread-safe operations.