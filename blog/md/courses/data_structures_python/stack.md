# Stack

A **stack** is a data structure that follows the **Last In First Out (LIFO)** principle, where the last element inserted is the first one to be removed. In Python, a stack can be implemented using a simple **array** (or **list**).

### Stack Operations:

- **push(item)**: Adds an item to the top of the stack.
- **pop()**: Removes and returns the item from the top of the stack.
- **peek()**: Returns the top item without removing it.
- **is_empty()**: Checks whether the stack is empty.
- **size()**: Returns the number of elements in the stack.

## Stack using list

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
    def is_empty(self):
        return len(self.stack) == 0
```

or write it like the following,

```python
class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack

    # Push item onto the stack
    def push(self, item):
        self.stack.append(item)

    # Pop item from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    # Peek at the top item of the stack
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return the size of the stack
    def size(self):
        return len(self.stack)

    # Print the stack
    def display(self):
        return self.stack


# Example usage
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushes:", stack.display())  # Output: [10, 20, 30]

    # Peek the top element
    print("Top element:", stack.peek())  # Output: 30

    # Pop elements from the stack
    print("Popped element:", stack.pop())  # Output: 30
    print("Stack after pop:", stack.display())  # Output: [10, 20]

    # Check if the stack is empty
    print("Is the stack empty?", stack.is_empty())  # Output: False

    # Get the size of the stack
    print("Size of the stack:", stack.size())  # Output: 2
```

### Explanation:

1. **`__init__()`**: Initializes the stack as an empty list `[]`.
2. **`push(item)`**: Appends an item to the end of the list, which represents the top of the stack.
3. **`pop()`**: Removes and returns the last element in the list (top of the stack) using the `pop()` method.
4. **`peek()`**: Returns the last item in the list without removing it (top of the stack) by accessing the last index `[-1]`.
5. **`is_empty()`**: Checks whether the stack is empty by verifying if the length of the list is zero.
6. **`size()`**: Returns the number of elements in the stack by returning the length of the list.
7. **`display()`**: Returns the current state of the stack.

### Example Output:

```
Stack after pushes: [10, 20, 30]
Top element: 30
Popped element: 30
Stack after pop: [10, 20]
Is the stack empty? False
Size of the stack: 2
```

### Notes:

- **Time Complexity**:
  - **Push** and **Pop** operations take \(O(1)\) time because appending and removing elements from the end of a list are constant-time operations in Python.
  - **Peek**, **is_empty**, and **size** also take \(O(1)\) time.
  
- This implementation uses a Python **list**, which is dynamic and handles resizing internally, so you don't need to worry about resizing the array as the stack grows or shrinks.
