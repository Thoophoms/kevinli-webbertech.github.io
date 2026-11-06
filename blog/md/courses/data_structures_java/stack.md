# Stack

## Array-based Stack Implementation

A **stack** is a data structure that follows the **Last In, First Out (LIFO)** principle. This means that the last element added to the stack is the first one to be removed. The two main operations that a stack supports are:

1. **Push**: Adds an element to the top of the stack.
2. **Pop**: Removes the top element from the stack.
   
Here's a basic implementation of a stack in Java using an array-based approach:

### 1. **Stack Class Implementation**

```java
class Stack {
    private int maxSize;
    private int top;
    private int[] stackArray;

    // Constructor to initialize the stack
    public Stack(int size) {
        maxSize = size;  // Maximum size of the stack
        stackArray = new int[maxSize];  // Array to hold stack elements
        top = -1;  // Top of the stack is initialized to -1 (empty stack)
    }

    // Push operation to add an element to the stack
    public void push(int value) {
        if (top < maxSize - 1) {
            stackArray[++top] = value;  // Increment top and add the element
            System.out.println(value + " pushed to stack.");
        } else {
            System.out.println("Stack is full, cannot push " + value);
        }
    }

    // Pop operation to remove an element from the stack
    public int pop() {
        if (top >= 0) {
            int poppedValue = stackArray[top--];  // Remove the top element and decrement top
            System.out.println(poppedValue + " popped from stack.");
            return poppedValue;
        } else {
            System.out.println("Stack is empty, cannot pop.");
            return -1;  // Return a default value indicating an empty stack
        }
    }

    // Peek operation to view the top element without removing it
    public int peek() {
        if (top >= 0) {
            return stackArray[top];  // Return the top element without removing it
        } else {
            System.out.println("Stack is empty, cannot peek.");
            return -1;  // Return a default value indicating an empty stack
        }
    }

    // Check if the stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Check if the stack is full
    public boolean isFull() {
        return top == maxSize - 1;
    }

    // Get the size of the stack
    public int size() {
        return top + 1;  // The number of elements in the stack
    }
}
```

### 2. **Main Class to Demonstrate Stack Operations**

```java
public class Main {
    public static void main(String[] args) {
        Stack stack = new Stack(5); // Create a stack of size 5

        // Pushing elements onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);
        stack.push(40);
        stack.push(50);

        // Trying to push another element into a full stack
        stack.push(60);

        // Peeking the top element
        System.out.println("Top element is: " + stack.peek());

        // Popping elements from the stack
        stack.pop();
        stack.pop();

        // Checking if the stack is empty
        System.out.println("Is stack empty? " + stack.isEmpty());

        // Checking the current size of the stack
        System.out.println("Current stack size: " + stack.size());

        // Popping all remaining elements
        stack.pop();
        stack.pop();
        stack.pop();

        // Trying to pop from an empty stack
        stack.pop();
    }
}
```

### Explanation:
- **Stack Class**: The `Stack` class has:
  - **maxSize**: The maximum size of the stack.
  - **stackArray**: An array used to store stack elements.
  - **top**: An integer that keeps track of the index of the top element in the stack.
  - **push()**: Adds a value to the stack. If the stack is full, it displays a message indicating that the stack cannot accommodate more elements.
  - **pop()**: Removes the top element and returns it. If the stack is empty, it indicates that no elements are available for removal.
  - **peek()**: Returns the top element without removing it.
  - **isEmpty()**: Checks whether the stack is empty.
  - **isFull()**: Checks whether the stack is full.
  - **size()**: Returns the number of elements in the stack.

- **Main Class**: This class demonstrates various operations like `push()`, `pop()`, `peek()`, and checks for stack status (`isEmpty()`, `isFull()`) as well as the stack's size.

### Sample Output:
```
10 pushed to stack.
20 pushed to stack.
30 pushed to stack.
40 pushed to stack.
50 pushed to stack.
Stack is full, cannot push 60
Top element is: 50
50 popped from stack.
40 popped from stack.
Is stack empty? false
Current stack size: 3
30 popped from stack.
20 popped from stack.
10 popped from stack.
Stack is empty, cannot pop.
```

### Time Complexity:
- **Push**: O(1) – Constant time to add an element to the stack.
- **Pop**: O(1) – Constant time to remove the top element.
- **Peek**: O(1) – Constant time to view the top element.
- **isEmpty**: O(1) – Constant time to check if the stack is empty.
- **isFull**: O(1) – Constant time to check if the stack is full.
- **size**: O(1) – Constant time to get the size of the stack.

## **Dynamic Array Implementation in Java**

A **dynamic array** is an array that automatically resizes itself when elements are added or removed, unlike a static array that has a fixed size. The main advantage of dynamic arrays is that they provide flexibility in terms of size, while still maintaining efficient access to elements.

In Java, you can implement a dynamic array using an array as the underlying storage, and resizing it when necessary (usually doubling the size when the array reaches capacity).

Here's a basic implementation of a **dynamic array**:

### 1. **DynamicArray Class Implementation**

```java
class DynamicArray {
    private int size;      // Number of elements in the array
    private int capacity;  // Total capacity of the array
    private int[] array;   // The underlying array to store elements

    // Constructor to initialize the dynamic array
    public DynamicArray() {
        capacity = 10;  // Initial capacity
        size = 0;       // Initially, the array is empty
        array = new int[capacity];  // Allocate the array with the initial capacity
    }

    // Method to add an element to the array
    public void add(int value) {
        // If the array is full, resize it by doubling the capacity
        if (size == capacity) {
            resize();
        }
        array[size++] = value;  // Add the element and increment the size
    }

    // Method to resize the array when it reaches full capacity
    private void resize() {
        capacity *= 2;  // Double the capacity
        int[] newArray = new int[capacity];  // Create a new array with doubled capacity
        
        // Copy all elements from the old array to the new array
        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }
        
        array = newArray;  // Make the new array the underlying array
    }

    // Method to get the element at a specific index
    public int get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        return array[index];
    }

    // Method to set the value of an element at a specific index
    public void set(int index, int value) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }
        array[index] = value;
    }

    // Method to remove an element from the array (shift elements to the left)
    public void remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds");
        }

        // Shift all elements after the index to the left
        for (int i = index; i < size - 1; i++) {
            array[i] = array[i + 1];
        }
        
        // Nullify the last element and decrement size
        array[size - 1] = 0;
        size--;
    }

    // Method to return the current size of the dynamic array
    public int size() {
        return size;
    }

    // Method to check if the array is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Method to display the dynamic array's elements
    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
}
```

### 2. **Main Class to Demonstrate Dynamic Array Operations**

```java
public class Main {
    public static void main(String[] args) {
        DynamicArray dynamicArray = new DynamicArray();

        // Add elements to the dynamic array
        dynamicArray.add(10);
        dynamicArray.add(20);
        dynamicArray.add(30);
        dynamicArray.add(40);
        dynamicArray.add(50);

        System.out.println("Dynamic Array after adding elements:");
        dynamicArray.display();  // Output: 10 20 30 40 50

        // Get an element at a specific index
        System.out.println("Element at index 2: " + dynamicArray.get(2));  // Output: 30

        // Set a new value at a specific index
        dynamicArray.set(2, 35);
        System.out.println("Dynamic Array after setting value at index 2 to 35:");
        dynamicArray.display();  // Output: 10 20 35 40 50

        // Remove an element at a specific index
        dynamicArray.remove(3);  // Remove the element at index 3 (value 40)
        System.out.println("Dynamic Array after removing element at index 3:");
        dynamicArray.display();  // Output: 10 20 35 50

        // Check the size of the dynamic array
        System.out.println("Size of dynamic array: " + dynamicArray.size());  // Output: 4

        // Check if the dynamic array is empty
        System.out.println("Is dynamic array empty? " + dynamicArray.isEmpty());  // Output: false
    }
}
```

### **Explanation:**
- **DynamicArray Class**:
  - **add()**: Adds an element to the dynamic array. If the array is full, it triggers a resize operation.
  - **resize()**: Doubles the capacity of the underlying array and copies the elements to the new array when the array is full.
  - **get()**: Returns the element at the specified index.
  - **set()**: Sets the value of the element at the specified index.
  - **remove()**: Removes an element at a specific index and shifts all the subsequent elements to the left.
  - **size()**: Returns the current number of elements in the array.
  - **isEmpty()**: Checks whether the dynamic array is empty.
  - **display()**: Prints the elements of the dynamic array.

- **Main Class**: Demonstrates how to use the `DynamicArray` class, including adding elements, accessing, modifying, removing elements, and displaying the array.

### **Sample Output:**

```
Dynamic Array after adding elements:
10 20 30 40 50
Element at index 2: 30
Dynamic Array after setting value at index 2 to 35:
10 20 35 40 50
Dynamic Array after removing element at index 3:
10 20 35 50
Size of dynamic array: 4
Is dynamic array empty? false
```

### **Time Complexity:**
- **add()**: O(1) – Amortized constant time when adding an element. In case of resizing, it takes O(n) where n is the current number of elements, but this resizing happens less frequently.
- **get()**: O(1) – Constant time to access an element at a specific index.
- **set()**: O(1) – Constant time to update an element at a specific index.
- **remove()**: O(n) – Shifting elements after removal takes linear time.
- **resize()**: O(n) – Resizing and copying the elements to the new array takes linear time. However, this operation happens less frequently as the array grows.

### **Notes:**
- This dynamic array implementation grows in size by doubling the array's capacity each time it becomes full. This approach ensures that the amortized time complexity of adding an element remains O(1).
- If you need more advanced functionality, you could implement methods to shrink the array when many elements are removed or support dynamic resizing by a fixed percentage instead of doubling.

Let me know if you need any further modifications or additional features!

## **Singly Linked List Implementation in Java**

Here is a basic implementation of a **LinkedList** in Java. A linked list is a data structure in which each element (called a node) contains a reference to the next node in the sequence. This allows for dynamic memory allocation and flexible data management.

This implementation involves two classes:
1. **Node Class**: Represents each node in the linked list.
2. **LinkedList Class**: Handles the linked list operations, such as inserting, deleting, and displaying the list.

### 1. **Node Class** (Represents an element in the list)

```java
class Node {
    int data;  // Data of the node
    Node next; // Reference to the next node

    // Constructor to create a new node
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}
```

### 2. **LinkedList Class** (Manages the list operations)

```java
class LinkedList {
    Node head; // Head node of the linked list

    // Constructor to initialize the linked list
    public LinkedList() {
        head = null; // Initially the list is empty
    }

    // Method to add a node at the end of the list
    public void append(int data) {
        Node newNode = new Node(data);
        
        // If the list is empty, the new node becomes the head
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            // Traverse to the last node
            while (current.next != null) {
                current = current.next;
            }
            // Set the next reference of the last node to the new node
            current.next = newNode;
        }
    }

    // Method to insert a node at the beginning of the list
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode; // New node becomes the head
    }

    // Method to delete a node by its value
    public void deleteNode(int key) {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        // If the node to be deleted is the head node
        if (head.data == key) {
            head = head.next; // Move the head to the next node
            return;
        }

        Node current = head;
        Node previous = null;

        // Traverse the list to find the node to delete
        while (current != null && current.data != key) {
            previous = current;
            current = current.next;
        }

        // If the node is not found
        if (current == null) {
            System.out.println("Node with value " + key + " not found.");
            return;
        }

        // Unlink the node from the list
        previous.next = current.next;
    }

    // Method to display all nodes in the list
    public void display() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    // Method to search for a node by its value
    public boolean search(int key) {
        Node current = head;
        while (current != null) {
            if (current.data == key) {
                return true; // Key found
            }
            current = current.next;
        }
        return false; // Key not found
    }

    // Method to get the size of the linked list
    public int size() {
        int size = 0;
        Node current = head;
        while (current != null) {
            size++;
            current = current.next;
        }
        return size;
    }
}
```

### 3. **Main Class** (Demonstrates the usage of LinkedList)

```java
public class Main {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        // Adding elements to the list
        list.append(10);
        list.append(20);
        list.append(30);
        list.append(40);
        list.append(50);

        System.out.println("Linked List after appending elements:");
        list.display();  // Output: 10 -> 20 -> 30 -> 40 -> 50 -> null

        // Insert an element at the beginning
        list.insertAtBeginning(5);
        System.out.println("Linked List after inserting 5 at the beginning:");
        list.display();  // Output: 5 -> 10 -> 20 -> 30 -> 40 -> 50 -> null

        // Delete an element
        list.deleteNode(20);
        System.out.println("Linked List after deleting node with value 20:");
        list.display();  // Output: 5 -> 10 -> 30 -> 40 -> 50 -> null

        // Searching for a value in the list
        boolean found = list.search(10);
        System.out.println("Search result for 10: " + found);  // Output: true

        // Searching for a non-existent value
        found = list.search(100);
        System.out.println("Search result for 100: " + found);  // Output: false

        // Getting the size of the list
        System.out.println("Size of the list: " + list.size());  // Output: 5
    }
}
```

### Explanation:
- **Node Class**: Represents an individual element in the list. It contains the data (value) and a reference (link) to the next node.
- **LinkedList Class**: Manages the linked list with the following operations:
  - **append()**: Adds a new node at the end of the list.
  - **insertAtBeginning()**: Inserts a new node at the beginning of the list.
  - **deleteNode()**: Deletes a node by its value. If the node is found, it is unlinked from the list.
  - **display()**: Traverses and prints the linked list.
  - **search()**: Searches for a specific value in the list.
  - **size()**: Returns the number of elements in the list.
- **Main Class**: Demonstrates how to create and manipulate a linked list using the `LinkedList` class.

### Sample Output:
```
Linked List after appending elements:
10 -> 20 -> 30 -> 40 -> 50 -> null
Linked List after inserting 5 at the beginning:
5 -> 10 -> 20 -> 30 -> 40 -> 50 -> null
Linked List after deleting node with value 20:
5 -> 10 -> 30 -> 40 -> 50 -> null
Search result for 10: true
Search result for 100: false
Size of the list: 5
```

### Time Complexity:
- **append()**: O(n) – You must traverse the entire list to find the last node.
- **insertAtBeginning()**: O(1) – Constant time since you're inserting at the head.
- **deleteNode()**: O(n) – You need to search for the node to delete.
- **search()**: O(n) – You may need to traverse the entire list.
- **size()**: O(n) – Traversing the entire list to count the nodes.

This implementation uses a **singly linked list**, where each node only knows about the next node. You can extend this implementation to create a **doubly linked list**, where each node maintains references to both the next and previous nodes, allowing for traversal in both directions.

## **Doubly Linked List Implementation in Java**

A **doubly linked list** is a type of linked list in which each node contains three components:
1. **Data**: The value stored in the node.
2. **Next**: A reference to the next node in the sequence.
3. **Previous**: A reference to the previous node in the sequence.

This allows traversal in both directions (from head to tail and vice versa). Below is a basic implementation of a doubly linked list in Java.

Here, we will implement a `DoublyLinkedList` with the following operations:
1. **Append**: Adds a node at the end of the list.
2. **Insert at Beginning**: Inserts a node at the beginning of the list.
3. **Delete**: Deletes a node by its value.
4. **Display Forward**: Displays the list from head to tail.
5. **Display Backward**: Displays the list from tail to head.
6. **Search**: Searches for a value in the list.

### 1. **Node Class** (Represents each element in the doubly linked list)

```java
class Node {
    int data;       // Data of the node
    Node next;      // Reference to the next node
    Node prev;      // Reference to the previous node

    // Constructor to create a new node
    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}
```

### 2. **DoublyLinkedList Class** (Manages the operations of the list)

```java
class DoublyLinkedList {
    Node head;  // Head node of the doubly linked list

    // Constructor to initialize the doubly linked list
    public DoublyLinkedList() {
        head = null;  // Initially, the list is empty
    }

    // Method to append a node to the end of the list
    public void append(int data) {
        Node newNode = new Node(data);
        
        if (head == null) {
            head = newNode;  // If the list is empty, make the new node the head
        } else {
            Node current = head;
            // Traverse to the last node
            while (current.next != null) {
                current = current.next;
            }
            // Set the next of the last node to the new node
            current.next = newNode;
            newNode.prev = current;  // Set the previous reference of the new node
        }
    }

    // Method to insert a node at the beginning of the list
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);
        
        if (head != null) {
            newNode.next = head;  // Set the next of the new node to the current head
            head.prev = newNode;  // Set the previous of the current head to the new node
        }
        head = newNode;  // Make the new node the head of the list
    }

    // Method to delete a node by its value
    public void delete(int key) {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        Node current = head;

        // If the node to be deleted is the head node
        if (current.data == key) {
            head = current.next;  // Move head to the next node
            if (head != null) {
                head.prev = null;  // Make the previous of the new head null
            }
            return;
        }

        // Traverse the list to find the node to delete
        while (current != null && current.data != key) {
            current = current.next;
        }

        // If the node is not found
        if (current == null) {
            System.out.println("Node with value " + key + " not found.");
            return;
        }

        // Unlink the node from the list
        if (current.next != null) {
            current.next.prev = current.prev;  // Set the previous of the next node to the previous node
        }
        if (current.prev != null) {
            current.prev.next = current.next;  // Set the next of the previous node to the next node
        }
    }

    // Method to display the list from head to tail
    public void displayForward() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        Node current = head;
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.next;
        }
        System.out.println("null");
    }

    // Method to display the list from tail to head
    public void displayBackward() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }

        Node current = head;
        // Traverse to the last node
        while (current.next != null) {
            current = current.next;
        }

        // Display the list from tail to head
        while (current != null) {
            System.out.print(current.data + " <-> ");
            current = current.prev;
        }
        System.out.println("null");
    }

    // Method to search for a value in the list
    public boolean search(int key) {
        Node current = head;
        while (current != null) {
            if (current.data == key) {
                return true; // Key found
            }
            current = current.next;
        }
        return false; // Key not found
    }
}
```

### 3. **Main Class** (Demonstrates the usage of Doubly Linked List)

```java
public class Main {
    public static void main(String[] args) {
        DoublyLinkedList list = new DoublyLinkedList();

        // Adding elements to the doubly linked list
        list.append(10);
        list.append(20);
        list.append(30);
        list.append(40);
        list.append(50);

        System.out.println("Doubly Linked List after appending elements:");
        list.displayForward();  // Output: 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> null

        // Inserting an element at the beginning
        list.insertAtBeginning(5);
        System.out.println("Doubly Linked List after inserting 5 at the beginning:");
        list.displayForward();  // Output: 5 <-> 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> null

        // Deleting a node by its value
        list.delete(30);
        System.out.println("Doubly Linked List after deleting node with value 30:");
        list.displayForward();  // Output: 5 <-> 10 <-> 20 <-> 40 <-> 50 <-> null

        // Searching for a value in the list
        System.out.println("Is 20 in the list? " + list.search(20));  // Output: true
        System.out.println("Is 60 in the list? " + list.search(60));  // Output: false

        // Displaying the list in reverse order (backward)
        System.out.println("Doubly Linked List in reverse order:");
        list.displayBackward();  // Output: 50 <-> 40 <-> 20 <-> 10 <-> 5 <-> null
    }
}
```

### **Explanation:**

- **Node Class**:
  - Each node has three components: `data` (value stored in the node), `next` (link to the next node), and `prev` (link to the previous node).
  
- **DoublyLinkedList Class**:
  - **append()**: Adds a node to the end of the list. If the list is empty, it makes the new node the head.
  - **insertAtBeginning()**: Adds a node at the beginning of the list and updates the `prev` and `next` references.
  - **delete()**: Removes a node with a specified value by adjusting the `next` and `prev` references of adjacent nodes.
  - **displayForward()**: Displays the elements of the list from head to tail.
  - **displayBackward()**: Displays the elements of the list from tail to head.
  - **search()**: Searches for a node by its value and returns `true` if found, `false` otherwise.

### **Sample Output:**

```
Doubly Linked List after appending elements:
10 <-> 20 <-> 30 <-> 40 <-> 50 <-> null
Doubly Linked List after inserting 5 at the beginning:
5 <-> 10 <-> 20 <-> 30 <-> 40 <-> 50 <-> null
Doubly Linked List after deleting node with value 30:
5 <-> 10 <-> 20 <-> 40 <-> 50 <-> null
Is 20 in the list? true
Is 60 in the list? false
Doubly Linked List in reverse order:
50 <-> 40 <-> 20 <-> 10 <-> 5 <-> null
```

### **Time Complexity**:
- **append()**: O(n) – You need to traverse to the end of the list.
- **insertAtBeginning()**: O(1) – Constant time to insert at the head.
- **delete()**: O(n) – You may need to traverse the list to find the node to delete.
- **displayForward()**: O(n) – You need to traverse the entire list.
- **displayBackward()**: O(n) – You need to traverse the entire list backward.

This doubly linked list implementation supports both forward and backward traversal, providing more flexibility than a singly linked list. You can extend it further to handle additional operations as needed.