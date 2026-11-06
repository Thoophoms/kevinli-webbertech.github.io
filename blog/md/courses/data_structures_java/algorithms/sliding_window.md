# **sliding window**

The **sliding window** algorithm is a commonly used technique for solving problems involving sequences (arrays or lists). The main idea is to maintain a "window" over a sequence, which slides through the sequence one element at a time while keeping track of some value (such as a sum, maximum, minimum, or other relevant information) within that window. This technique can optimize problems that would otherwise have a **brute force O(n²)** solution to **O(n)**, making it highly efficient.

### **Key Concepts of Sliding Window Algorithms:**
1. **Window Size**: A window can have a fixed or variable size.
   - **Fixed-size sliding window**: The window has a predetermined size, and the algorithm moves the window by one position at a time.
   - **Variable-size sliding window**: The window size can change based on some condition, and the window adjusts dynamically as it slides.
   
2. **Efficient Computation**: As the window slides over the array, only the elements entering and exiting the window are considered, making the algorithm more efficient than recalculating from scratch at every step.

### **Common Applications of Sliding Window:**
1. **Maximum/Minimum of Subarrays**: Find the maximum or minimum value in every subarray of size `k`.
2. **Sum of Subarrays**: Compute the sum of elements in every subarray of size `k`.
3. **String Matching**: Find substrings within a given string that match a pattern (e.g., finding anagrams).
4. **Longest Substring without Repeating Characters**: Track the longest substring with no repeated characters.

### **Types of Sliding Window Algorithms:**
1. **Fixed-size sliding window**: The window size is fixed.
2. **Variable-size sliding window**: The window size changes dynamically.

### **Sliding Window Algorithm Examples:**

#### 1. **Fixed-size Sliding Window: Maximum Sum of Subarray of Size `k`**
Given an array, find the maximum sum of a subarray with a fixed size `k`.

**Problem Statement:**
Given an array `arr[]` of size `n`, find the maximum sum of a subarray of size `k`.

#### **Algorithm**:
- Iterate over the array and calculate the sum of the first `k` elements.
- Then slide the window by removing the first element of the previous window and adding the next element of the array.
- Track the maximum sum during the sliding process.

#### **Java Implementation:**

```java
public class SlidingWindow {
    // Method to find the maximum sum of a subarray of size k
    public static int maxSumSubarray(int[] arr, int k) {
        int n = arr.length;
        if (n < k) return -1; // Return -1 if k is greater than array size

        // Compute the sum of the first window
        int windowSum = 0;
        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }

        int maxSum = windowSum;

        // Slide the window and compute the sum for each subsequent window
        for (int i = k; i < n; i++) {
            windowSum += arr[i] - arr[i - k]; // Add the next element, remove the first element of the previous window
            maxSum = Math.max(maxSum, windowSum); // Update the max sum if the current sum is greater
        }

        return maxSum;
    }

    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};
        int k = 3;

        int maxSum = maxSumSubarray(arr, k);
        System.out.println("Maximum sum of subarray of size " + k + ": " + maxSum);
    }
}
```

#### **Explanation**:
1. The first for-loop calculates the sum of the first `k` elements.
2. The sliding window is implemented by adding the next element and removing the element that goes out of the window.
3. The maximum sum is updated during the window sliding process.

#### **Output:**
```
Maximum sum of subarray of size 3: 9
```

#### **Time Complexity**:
- **O(n)**: The sliding window technique ensures that the sum is computed in constant time for each window, so the algorithm runs in linear time.

---

#### 2. **Variable-size Sliding Window: Longest Substring Without Repeating Characters**

**Problem Statement**:
Given a string, find the length of the longest substring without repeating characters.

#### **Algorithm**:
- Use two pointers (`start` and `end`) to represent the window. 
- As `end` expands to the right, check if the character at `end` is in the window (i.e., between `start` and `end`). 
- If it is, move the `start` pointer to the right of the last occurrence of the repeating character.
- Track the length of the window (substring) during the process.

#### **Java Implementation**:

```java
import java.util.HashSet;

public class SlidingWindow {
    // Method to find the longest substring without repeating characters
    public static int longestSubstringWithoutRepeating(String s) {
        HashSet<Character> set = new HashSet<>();
        int maxLength = 0;
        int start = 0;

        for (int end = 0; end < s.length(); end++) {
            // If the character is in the set, shrink the window from the start
            while (set.contains(s.charAt(end))) {
                set.remove(s.charAt(start));
                start++;
            }

            // Add the current character to the set
            set.add(s.charAt(end));

            // Update the maximum length
            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        String s = "abcabcbb";

        int result = longestSubstringWithoutRepeating(s);
        System.out.println("Length of the longest substring without repeating characters: " + result);
    }
}
```

#### **Explanation**:
1. **start** and **end** represent the current window's boundaries.
2. We use a **HashSet** to track the characters in the current window.
3. If a character at `end` is already in the set (indicating a repeat), we move the `start` pointer to the right of the previous occurrence of the character.
4. The window size (`end - start + 1`) is updated at each step to find the maximum length.

#### **Output:**
```
Length of the longest substring without repeating characters: 3
```

#### **Time Complexity**:
- **O(n)**: The sliding window ensures that each character is processed at most twice, once when expanding the window and once when shrinking it, resulting in linear time complexity.

---

### **Common Sliding Window Problems:**

1. **Maximum/Minimum Sum of Subarrays of Size k**: 
   - Given an array, find the maximum/minimum sum of any subarray of size `k`.

2. **Longest Substring with K Distinct Characters**: 
   - Given a string, find the length of the longest substring that contains at most `K` distinct characters.

3. **Smallest Subarray with Sum Greater Than or Equal to k**: 
   - Given an array, find the smallest contiguous subarray whose sum is greater than or equal to `k`.

4. **Longest Substring with At Most K Distinct Characters**:
   - Given a string, find the longest substring that contains at most `k` distinct characters.

---

### **Conclusion:**

The **sliding window technique** is a highly efficient approach to solving problems related to subarrays or substrings. By maintaining a window that either has a fixed size or a variable size (based on conditions), we can reduce time complexity from **O(n²)** to **O(n)** in many cases.

- **Fixed-size sliding window** is used when the size of the window is known in advance.
- **Variable-size sliding window** is used when the window size can change dynamically based on some condition (e.g., maximizing or minimizing the sum, length, or other properties).

The sliding window is especially useful in problems that require processing contiguous elements in an array or string.