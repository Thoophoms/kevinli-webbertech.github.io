# N^2 Sorting Algorithms

## **Bubble Sort**

**Bubble Sort** is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent items, and swapping them if they are in the wrong order. The process is repeated until the list is sorted.

### **Bubble Sort Algorithm:**
1. Start from the first element of the array.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Continue this process for all elements in the array. After one complete pass, the largest element will be at the end of the array.
5. Repeat the process for the rest of the array (ignoring the last sorted element).
6. Continue until the array is sorted.

### **Bubble Sort Time Complexity:**
- **Best case**: O(n) (if the array is already sorted, the algorithm can detect this after one pass).
- **Worst case**: O(n²) (if the array is sorted in reverse order).
- **Average case**: O(n²).

### **Bubble Sort Space Complexity:**
- O(1), since it is an **in-place sorting algorithm** and uses only a constant amount of extra space.

### **Java Implementation of Bubble Sort**

Here’s how you can implement the Bubble Sort algorithm in Java:

```java
class BubbleSort {
    // Method to perform bubble sort
    public static void bubbleSort(int[] arr) {
        int n = arr.length;

        // Traverse through all elements in the array
        for (int i = 0; i < n - 1; i++) {
            // Last i elements are already sorted
            for (int j = 0; j < n - i - 1; j++) {
                // Compare adjacent elements
                if (arr[j] > arr[j + 1]) {
                    // Swap if the element found is greater than the next element
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    // Utility method to print the array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};

        System.out.println("Original array:");
        printArray(arr);

        // Perform bubble sort
        bubbleSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation:**
1. **bubbleSort()**: 
   - This method implements the bubble sort algorithm.
   - It has two nested loops:
     - The outer loop ensures that the sorting process is repeated for all elements.
     - The inner loop performs the actual comparison and swapping of adjacent elements.
   
2. **printArray()**:
   - A utility method to print the elements of the array.

3. **main()**:
   - An array is created and initialized with unsorted integers.
   - The original array is printed.
   - The `bubbleSort()` method is called to sort the array.
   - Finally, the sorted array is printed.

### **Sample Output:**

```
Original array:
64 34 25 12 22 11 90 
Sorted array:
11 12 22 25 34 64 90 
```

### **Optimized Bubble Sort**:
One common optimization to the Bubble Sort algorithm is to add a flag to check whether a swap was made during the inner loop. If no swaps are made during a pass, then the array is already sorted, and we can stop early.

Here's the optimized version:

```java
class BubbleSort {
    // Optimized Bubble Sort
    public static void bubbleSort(int[] arr) {
        int n = arr.length;

        // Traverse through all elements in the array
        for (int i = 0; i < n - 1; i++) {
            boolean swapped = false;

            // Compare adjacent elements
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap if the element found is greater than the next element
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no two elements were swapped, then the array is sorted
            if (!swapped) {
                break;
            }
        }
    }

    // Utility method to print the array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};

        System.out.println("Original array:");
        printArray(arr);

        // Perform bubble sort
        bubbleSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation of Optimized Version:**
- The **`swapped`** flag is introduced to detect whether any swaps were made during the inner loop. If no swaps were made, the array is already sorted, and the algorithm terminates early, improving the best-case time complexity to **O(n)** for already sorted arrays.

### **Sample Output (Optimized Version):**

```
Original array:
64 34 25 12 22 11 90 
Sorted array:
11 12 22 25 34 64 90 
```

### **Conclusion:**
- **Bubble Sort** is a simple sorting algorithm that works by repeatedly comparing adjacent elements and swapping them if they are in the wrong order.
- Although it is easy to implement and understand, its time complexity is poor in practice, especially for large datasets (O(n²) in the worst case).
- **Optimized Bubble Sort** improves the best case to O(n) when the array is already sorted.

## **Selection Sort**

**Selection Sort** is another simple comparison-based sorting algorithm. It works by repeatedly finding the smallest (or largest, depending on the sorting order) element from the unsorted portion of the array and swapping it with the first unsorted element. This process is repeated for all elements until the array is sorted.

### **Selection Sort Algorithm:**
1. **Find the Minimum**: Find the smallest element in the unsorted part of the array.
2. **Swap**: Swap this smallest element with the first element of the unsorted part of the array.
3. **Repeat**: Move the boundary of the unsorted portion by one element and repeat the process for the remaining elements.

### **Selection Sort Time Complexity:**
- **Best Case**: O(n²)
- **Worst Case**: O(n²)
- **Average Case**: O(n²)
  
Selection sort always performs O(n²) comparisons, regardless of the order of the elements. Hence, it is not suitable for large datasets.

### **Selection Sort Space Complexity:**
- O(1), as it is an in-place sorting algorithm and does not require extra space.

### **Java Implementation of Selection Sort**

Here’s how you can implement the **Selection Sort** algorithm in Java:

```java
class SelectionSort {
    // Method to perform selection sort
    public static void selectionSort(int[] arr) {
        int n = arr.length;

        // Traverse through all elements in the array
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in the unsorted portion
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // Swap the found minimum element with the first element of the unsorted portion
            if (minIndex != i) {
                int temp = arr[minIndex];
                arr[minIndex] = arr[i];
                arr[i] = temp;
            }
        }
    }

    // Utility method to print the array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};

        System.out.println("Original array:");
        printArray(arr);

        // Perform selection sort
        selectionSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation:**
1. **selectionSort()**:
   - This method implements the selection sort algorithm.
   - It iterates through the array, finds the minimum element in the unsorted portion of the array, and swaps it with the first element of the unsorted part.
   
2. **printArray()**:
   - A utility method to print the elements of the array.

3. **main()**:
   - The main method demonstrates how to create an array, perform the sorting, and print the sorted array.

### **Sample Output:**

```
Original array:
64 25 12 22 11 
Sorted array:
11 12 22 25 64 
```

### **Time Complexity:**
- **Best Case**: O(n²) – Even if the array is already sorted, selection sort still performs O(n²) comparisons.
- **Worst Case**: O(n²) – This happens when the array is in reverse order, requiring the maximum number of comparisons.
- **Average Case**: O(n²) – On average, selection sort will require O(n²) comparisons, regardless of the order of the elements.

### **Space Complexity:**
- **O(1)** – Selection sort is an in-place sorting algorithm, meaning it does not require extra memory for sorting. It only swaps elements within the given array.

### **Advantages of Selection Sort:**
1. **Simple**: Easy to implement and understand.
2. **In-Place**: Requires only a constant amount of extra space (O(1)).

### **Disadvantages of Selection Sort:**
1. **Inefficient**: Its time complexity of O(n²) makes it impractical for large datasets compared to more efficient algorithms like QuickSort or MergeSort.
2. **Not Stable**: Selection Sort is not a stable sorting algorithm. It may change the relative order of equal elements in the array.

### **Conclusion:**
Selection Sort is a simple, in-place sorting algorithm that is easy to understand and implement but is inefficient for large datasets due to its O(n²) time complexity. It is most suitable for educational purposes or for small datasets where its simplicity can be an advantage.

## **Insertion Sort**

**Insertion Sort** is a simple sorting algorithm that builds the final sorted array one element at a time. It is much like sorting a hand of playing cards, where you pick up the cards one by one and insert them in the correct position in your hand.

### **Insertion Sort Algorithm:**
1. **Start with the second element** (since a single-element list is trivially sorted).
2. **Compare it to the elements before it** and insert it into the correct position, shifting all larger elements to the right.
3. **Repeat** this process for each subsequent element in the array until the entire array is sorted.

### **Properties of Insertion Sort:**
1. **Time Complexity**:
   - **Best case**: O(n) (when the array is already sorted).
   - **Worst case**: O(n²) (when the array is sorted in reverse order).
   - **Average case**: O(n²).
   
2. **Space Complexity**: O(1), since it's an in-place sorting algorithm.
3. **Stable**: If two elements are equal, their relative order will not change.
4. **Adaptive**: It performs well when the array is nearly sorted.

### **Insertion Sort Time Complexity:**
- **Best Case**: O(n), occurs when the input is already sorted.
- **Worst Case**: O(n²), occurs when the input is sorted in reverse order.
- **Average Case**: O(n²).

### **Java Implementation of Insertion Sort**

Here's how you can implement the **Insertion Sort** algorithm in Java:

```java
class InsertionSort {
    // Method to perform insertion sort
    public static void insertionSort(int[] arr) {
        int n = arr.length;

        // Traverse through elements from the second element to the last
        for (int i = 1; i < n; i++) {
            int key = arr[i]; // The current element to be inserted
            int j = i - 1;

            // Move elements of arr[0..i-1] that are greater than key
            // to one position ahead of their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key; // Insert the key at its correct position
        }
    }

    // Utility method to print the array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};

        System.out.println("Original array:");
        printArray(arr);

        // Perform insertion sort
        insertionSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation:**
1. **insertionSort()**:
   - This method implements the Insertion Sort algorithm.
   - It starts with the second element, compares it to the previous elements, and inserts it in the correct position in the sorted portion of the array.
   
2. **printArray()**:
   - A utility method to print the elements of the array.

3. **main()**:
   - The main method demonstrates how to create an array, perform the sorting, and print the sorted array.

### **Sample Output:**

```
Original array:
64 34 25 12 22 11 90 
Sorted array:
11 12 22 25 34 64 90 
```

### **Time Complexity:**
- **Best Case (Already Sorted Array)**: O(n) – If the array is already sorted, only the outer loop runs, and the inner loop doesn't do any shifting.
- **Worst Case (Reversed Array)**: O(n²) – If the array is in reverse order, for each element, we will have to shift all the previous elements.
- **Average Case**: O(n²) – On average, for each element, the inner loop performs O(n) comparisons.

### **Space Complexity:**
- **O(1)** – Insertion sort is an in-place sorting algorithm. It does not require additional storage beyond the input array.

### **Advantages of Insertion Sort:**
1. **Simple and Easy to Implement**: It is a simple algorithm and easy to understand.
2. **Efficient for Small Data**: Works well for small datasets or nearly sorted data.
3. **Stable**: If two elements are equal, their relative order remains unchanged.
4. **Adaptive**: Performs well when the array is nearly sorted.

### **Disadvantages of Insertion Sort:**
1. **Inefficient for Large Datasets**: Its time complexity is O(n²), making it inefficient for large datasets compared to more efficient algorithms like QuickSort or MergeSort.
2. **Not Suitable for Sorting Large Collections**: Insertion sort becomes inefficient as the dataset grows, especially when the array is in reverse order.

### **Conclusion:**
Insertion Sort is a simple, stable, and efficient sorting algorithm for small datasets or nearly sorted data. It has a time complexity of O(n²) in the worst case, which makes it impractical for larger datasets. However, its simplicity and adaptive nature make it useful for educational purposes and small-scale applications.

## **Heap Sort**

**Heap Sort** is a comparison-based sorting algorithm that works by utilizing a **heap** data structure. It first builds a heap from the input data, and then repeatedly extracts the largest element (in the case of a max-heap) or the smallest element (in the case of a min-heap) from the heap and places it in the sorted order.

### **Heap Sort Algorithm Overview:**

1. **Build a Max-Heap**: Transform the input array into a max-heap, where the parent node is greater than its children.
2. **Swap Root with Last Element**: Swap the root (maximum element) with the last element of the heap.
3. **Reduce Heap Size**: After the swap, the heap size is reduced by 1 (excluding the last element).
4. **Heapify the Root**: Reheapify the heap by calling the heapify function to restore the max-heap property.
5. **Repeat**: Repeat steps 2–4 until the heap size is reduced to 1.

### **Heap Sort Time Complexity:**
- **Best, Average, and Worst Case**: O(n log n), since building the heap takes O(n) and the subsequent heapify operations take O(log n).
- **Space Complexity**: O(1) because the algorithm is done in-place.

### **Heap Sort Example (Max-Heap):**
In a **Max-Heap**, the largest element is always at the root. After the heap is built, the root (largest element) is swapped with the last element of the heap, and the heap size is reduced by 1. The heapify operation ensures that the heap property is restored.

### **Java Implementation of Heap Sort**

```java
class HeapSort {
    // Method to perform heap sort
    public static void heapSort(int[] arr) {
        int n = arr.length;

        // Build a max heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }

        // Extract elements one by one from the heap
        for (int i = n - 1; i > 0; i--) {
            // Swap the current root with the last element
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // Heapify the root element to restore the heap property
            heapify(arr, i, 0);
        }
    }

    // To maintain the heap property
    private static void heapify(int[] arr, int n, int i) {
        int largest = i; // Initialize largest as root
        int left = 2 * i + 1; // Left child
        int right = 2 * i + 2; // Right child

        // If left child is larger than root
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }

        // If right child is larger than the largest so far
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }

        // If largest is not root
        if (largest != i) {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }

    // Utility method to print the array
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};

        System.out.println("Original array:");
        printArray(arr);

        // Perform heap sort
        heapSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation:**
1. **heapSort()**:
   - The method first builds the max-heap by calling `heapify()` on all non-leaf nodes (from bottom to top).
   - Then, it repeatedly extracts the maximum element (root) from the heap, swaps it with the last element, and reduces the heap size. After each extraction, `heapify()` is called to restore the heap property.

2. **heapify()**:
   - This method ensures that the subtree rooted at index `i` satisfies the heap property. If the subtree violates the property (i.e., the root is smaller than one of its children), the method swaps the root with the largest of the two children and recursively heapifies the affected subtree.

3. **printArray()**:
   - A utility method to print the elements of the array.

4. **main()**:
   - The main method creates an array, performs heap sort on it, and prints the sorted array.

### **Sample Output:**

```
Original array:
12 11 13 5 6 7 
Sorted array:
5 6 7 11 12 13 
```

### **Time Complexity:**
- **Building the Max-Heap**: O(n) – Building the max-heap involves heapifying each node, which takes O(log n) time. Since there are n/2 non-leaf nodes, the total time for building the heap is O(n).
- **Heapify**: O(log n) – Heapifying a node takes O(log n) time.
- **Extracting the Elements**: O(n log n) – For each of the n elements, we swap the root with the last element (O(1)) and heapify the remaining tree (O(log n)).
  
Thus, the overall time complexity of Heap Sort is **O(n log n)** for all cases (best, worst, and average).

### **Space Complexity:**
- **O(1)** – Heap Sort is an in-place sorting algorithm. It does not require extra space apart from the input array.

### **Advantages of Heap Sort:**
1. **Efficient Sorting**: It has O(n log n) time complexity for all cases, making it more efficient than O(n²) algorithms like Bubble Sort or Insertion Sort.
2. **In-Place Sorting**: Heap Sort is an in-place algorithm and does not require additional storage apart from the input array.
3. **Not Recursive**: Unlike Merge Sort, Heap Sort doesn't require additional memory for recursion, making it more memory-efficient.

### **Disadvantages of Heap Sort:**
1. **Not Stable**: Heap Sort is not a stable sorting algorithm. It might change the relative order of elements with equal values.
2. **Less Efficient for Small Arrays**: For small arrays, algorithms like QuickSort or Insertion Sort may be faster in practice due to lower constant factors.

### **Conclusion:**
Heap Sort is a very efficient and reliable sorting algorithm with O(n log n) time complexity. It is useful for large datasets and applications where sorting in place is required. However, its lack of stability and slightly slower performance on smaller datasets compared to algorithms like MergeSort or QuickSort might make it less suitable in some cases.
