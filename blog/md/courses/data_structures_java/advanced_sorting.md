# Merge Sort and Quick Sort

## **Merge Sort**

**Merge Sort** is a comparison-based, divide-and-conquer sorting algorithm that divides the array into two halves, recursively sorts the two halves, and then merges the sorted halves back together. It is one of the most efficient algorithms for sorting large datasets, with a time complexity of **O(n log n)** in all cases.

### **Merge Sort Algorithm Overview:**
1. **Divide**: Split the array into two halves until each sub-array contains only one element.
2. **Conquer**: Recursively sort each sub-array.
3. **Combine**: Merge the two sorted sub-arrays back together.

### **Merge Sort Time Complexity:**
- **Best case**: O(n log n)
- **Worst case**: O(n log n)
- **Average case**: O(n log n)

Merge sort consistently performs at O(n log n) time complexity, regardless of the input data's initial order.

### **Merge Sort Space Complexity:**
- O(n) – Merge Sort is not an in-place sorting algorithm. It requires additional space to merge the sub-arrays.

### **Merge Sort Implementation in Java**

Here’s how you can implement the **Merge Sort** algorithm in Java:

```java
class MergeSort {
    // Method to perform merge sort
    public static void mergeSort(int[] arr) {
        if (arr.length < 2) {
            return; // Base case: an array of length 1 is already sorted
        }

        int mid = arr.length / 2;  // Find the middle index
        int[] left = new int[mid];  // Left half of the array
        int[] right = new int[arr.length - mid];  // Right half of the array

        // Copy data into left and right sub-arrays
        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);

        // Recursively sort the two halves
        mergeSort(left);
        mergeSort(right);

        // Merge the sorted halves back together
        merge(arr, left, right);
    }

    // Helper method to merge two sorted arrays
    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        // Merge the two sub-arrays into the original array
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        // Copy the remaining elements of left array, if any
        while (i < left.length) {
            arr[k++] = left[i++];
        }

        // Copy the remaining elements of right array, if any
        while (j < right.length) {
            arr[k++] = right[j++];
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

        // Perform merge sort
        mergeSort(arr);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation:**
1. **mergeSort()**:
   - This is the main recursive function that splits the array into two halves until the base case (arrays of length 1) is reached. It then recursively sorts each half.
   
2. **merge()**:
   - This function merges two sorted arrays (left and right) into the original array. It compares elements from both arrays and places the smaller element in the original array. If one of the arrays is exhausted, the remaining elements from the other array are copied over.

3. **printArray()**:
   - A utility method to print the array.

4. **main()**:
   - The main method demonstrates how to create an array, perform merge sort on it, and print the sorted array.

### **Sample Output:**

```
Original array:
64 34 25 12 22 11 90 
Sorted array:
11 12 22 25 34 64 90 
```

### **Time Complexity of Merge Sort:**
- **Divide Step**: The array is divided into two halves, which takes O(log n) steps.
- **Conquer Step**: In each level of recursion, all elements are compared and merged, taking O(n) time.
  
Thus, the overall time complexity of Merge Sort is O(n log n) for all cases (best, worst, and average).

### **Space Complexity:**
- **O(n)**: Merge Sort uses additional space for the left and right sub-arrays to merge the elements. This requires O(n) additional space where **n** is the number of elements in the array.

### **Advantages of Merge Sort:**
1. **Consistent Performance**: Merge Sort guarantees O(n log n) time complexity, making it highly efficient for large datasets.
2. **Stable Sorting**: Merge Sort is a stable algorithm, meaning that equal elements maintain their relative order after sorting.
3. **Works Well for Linked Lists**: Merge Sort works efficiently on linked lists, unlike QuickSort and HeapSort, which require random access.

### **Disadvantages of Merge Sort:**
1. **Space Complexity**: Merge Sort requires O(n) additional space, making it less space-efficient compared to in-place algorithms like QuickSort or HeapSort.
2. **Not In-Place**: Unlike algorithms like QuickSort, Merge Sort is not an in-place algorithm and needs additional space for the left and right sub-arrays.

### **Conclusion:**
Merge Sort is a highly efficient, stable sorting algorithm with **O(n log n)** time complexity. It is particularly useful for large datasets and cases where stability (maintaining the relative order of equal elements) is important. However, its **O(n)** space complexity can make it less ideal when memory usage is a concern.

Let me know if you'd like further details or enhancements!

## **QuickSort**

**QuickSort** is a comparison-based sorting algorithm that follows the **divide-and-conquer** approach. It is generally faster than other O(n log n) algorithms like **MergeSort** and **HeapSort** for average-sized datasets.

### **QuickSort Algorithm:**
1. **Choose a Pivot**: Select an element from the array to act as the pivot. Different pivot selection strategies exist (e.g., first element, last element, random element, or the median).
2. **Partitioning**: Reorder the array so that elements smaller than the pivot come before it, and elements larger than the pivot come after it. After this step, the pivot is in its correct sorted position.
3. **Recursively Apply**: Apply the same process to the sub-arrays formed by dividing the array into two halves around the pivot.
4. **Base Case**: If the array has one or zero elements, it is already sorted.

### **QuickSort Time Complexity:**
- **Best Case**: O(n log n) – When the pivot divides the array into two roughly equal halves.
- **Worst Case**: O(n²) – When the pivot is the smallest or largest element, and the array is not balanced.
- **Average Case**: O(n log n) – On average, the pivot divides the array into fairly equal sub-arrays.

### **QuickSort Space Complexity:**
- O(log n) – The space complexity is due to the recursion stack. The algorithm works in-place and does not require additional storage for sorting.

### **Java Implementation of QuickSort**

Here’s the implementation of the **QuickSort** algorithm in Java:

```java
class QuickSort {
    // Method to perform QuickSort
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            // Find the pivot element such that elements smaller than the pivot are on the left
            // and elements greater than the pivot are on the right
            int pivotIndex = partition(arr, low, high);

            // Recursively apply the same logic to the left and right sub-arrays
            quickSort(arr, low, pivotIndex - 1);  // Left sub-array
            quickSort(arr, pivotIndex + 1, high); // Right sub-array
        }
    }

    // Method to partition the array around a pivot
    private static int partition(int[] arr, int low, int high) {
        // Select the pivot (here we choose the last element)
        int pivot = arr[high];
        int i = (low - 1);  // Index of the smaller element

        // Traverse the array and rearrange elements around the pivot
        for (int j = low; j < high; j++) {
            // If current element is smaller than or equal to the pivot
            if (arr[j] <= pivot) {
                i++;
                // Swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Swap the pivot element with the element at index i + 1
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        // Return the partition index (pivot position)
        return i + 1;
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

        // Perform quick sort
        quickSort(arr, 0, arr.length - 1);

        System.out.println("Sorted array:");
        printArray(arr);
    }
}
```

### **Explanation:**
1. **quickSort()**:
   - This is the main recursive function that performs the QuickSort algorithm. It splits the array into sub-arrays around a pivot, and recursively sorts them.
   
2. **partition()**:
   - This function takes the array, the low and high indices, and partitions the array around the pivot. It places the pivot in its correct position and rearranges the array so that all elements smaller than the pivot are on the left, and all elements greater than the pivot are on the right.
   
3. **printArray()**:
   - A utility method to print the elements of the array.

4. **main()**:
   - The main method demonstrates how to create an array, perform QuickSort on it, and print the sorted array.

### **Sample Output:**

```
Original array:
64 34 25 12 22 11 90 
Sorted array:
11 12 22 25 34 64 90 
```

### **Time Complexity of QuickSort:**
- **Best Case (Balanced Partitioning)**: O(n log n) – When the pivot divides the array into two equal halves.
- **Worst Case (Unbalanced Partitioning)**: O(n²) – This happens when the pivot always ends up being the smallest or largest element, leading to unbalanced partitions (e.g., sorted or reverse-sorted data).
- **Average Case**: O(n log n) – On average, the pivot will divide the array into reasonably balanced sub-arrays.

### **Space Complexity:**
- **O(log n)** – This is the space used by the recursion stack. In the worst case (when the array is already sorted or reverse-sorted), the recursion depth can be O(n), but on average it is O(log n).

### **Advantages of QuickSort:**
1. **Efficient**: On average, QuickSort has O(n log n) time complexity, which is very efficient compared to algorithms like Bubble Sort or Insertion Sort (O(n²)).
2. **In-place Sorting**: QuickSort doesn’t require extra space for sorting, as it works in-place.
3. **Divide and Conquer**: It works well on large datasets, especially when the array is large.

### **Disadvantages of QuickSort:**
1. **Worst-case performance**: The worst-case time complexity is O(n²) when the pivot selection is poor (e.g., when the array is already sorted or nearly sorted). This can be mitigated by choosing a good pivot (like using **randomized** QuickSort).
2. **Not Stable**: QuickSort is not a stable sorting algorithm, which means that it may change the relative order of equal elements.

### **Optimizations for QuickSort:**
1. **Randomized QuickSort**: Randomly selecting the pivot to avoid the worst-case scenario.
2. **Three-way QuickSort**: A variation that handles duplicate elements efficiently.

### **Conclusion:**

QuickSort is a fast and efficient sorting algorithm for large datasets with a time complexity of **O(n log n)** in most cases. It is widely used due to its in-place sorting and overall efficiency. However, care should be taken to choose a good pivot, or else the worst-case time complexity of **O(n²)** can occur.

Let me know if you'd like further explanations or enhancements!