# **Dynamic Programming (DP)**

**Dynamic Programming (DP)** is a technique used to solve problems by breaking them down into smaller subproblems and solving each subproblem just once, storing the solutions to subproblems in a table (often an array or matrix), and reusing these solutions when needed. This helps to avoid redundant calculations, improving the time complexity of problems that have overlapping subproblems.

### **Key Characteristics of Dynamic Programming:**
1. **Overlapping Subproblems**: The problem can be broken down into smaller subproblems, and these subproblems are solved multiple times.
2. **Optimal Substructure**: The optimal solution to the problem can be constructed efficiently from optimal solutions to its subproblems.

### **Dynamic Programming Approach**:
1. **Divide the problem into smaller subproblems**.
2. **Solve each subproblem** only once and store its solution (memoization or tabulation).
3. **Combine the results** of the subproblems to find the solution to the original problem.

### **Key Techniques in Dynamic Programming**:
1. **Memoization** (Top-Down DP): Store the results of subproblems in a cache (usually a dictionary or array) to avoid recomputation. The function is called recursively, and results are cached as they are computed.
2. **Tabulation** (Bottom-Up DP): Solve the problem iteratively by solving all subproblems and storing their results in a table (often an array or matrix), starting from the smallest subproblems and moving up to the original problem.

### **Steps for Solving Problems Using Dynamic Programming**:
1. **Characterize the Structure of an Optimal Solution**: Break down the problem into simpler subproblems.
2. **Define the State**: Identify the variables or parameters that represent the state of the subproblem.
3. **Write the Recurrence Relation**: Determine how the solution to a subproblem depends on the solutions to smaller subproblems.
4. **Compute the Value of the Optimal Solution**: Use memoization or tabulation to compute the value of the optimal solution.
5. **Reconstruct the Optimal Solution**: If required, reconstruct the solution by tracing back through the computed values.

### **Common Dynamic Programming Problems**:

1. **Fibonacci Sequence**: Calculate the nth Fibonacci number.
2. **0/1 Knapsack Problem**: Given a set of items, each with a weight and value, determine the maximum value that can be obtained by filling a knapsack of capacity `W` with the given items, where each item can either be included or excluded.
3. **Longest Common Subsequence**: Given two sequences, find the longest subsequence common to both sequences.
4. **Coin Change Problem**: Find the minimum number of coins needed to make up a given sum using coins of specific denominations.
5. **Matrix Chain Multiplication**: Find the most efficient way to multiply a sequence of matrices.
6. **Shortest Path Problems** (e.g., Floyd-Warshall Algorithm).

### **Example 1: Fibonacci Sequence**

The **Fibonacci Sequence** is a classic example of dynamic programming. It is defined as:
- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) for n > 1

#### **Naive Recursion (Brute Force)**:
Without dynamic programming, the recursive approach will recompute the same values multiple times, leading to an exponential time complexity.

#### **Dynamic Programming Solution**:
We can solve this efficiently by storing the results of subproblems.

#### **Java Implementation** (Memoization and Tabulation):

```java
public class Fibonacci {

    // Memoization (Top-Down Approach)
    public static int fibonacciMemo(int n, int[] memo) {
        if (n <= 1) {
            return n;
        }
        if (memo[n] != -1) {
            return memo[n]; // Return the cached result
        }
        memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo); // Cache the result
        return memo[n];
    }

    // Tabulation (Bottom-Up Approach)
    public static int fibonacciTabulation(int n) {
        if (n <= 1) {
            return n;
        }
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2]; // Bottom-up approach
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int n = 10;

        // Using Memoization
        int[] memo = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            memo[i] = -1; // Initialize memoization array
        }
        System.out.println("Fibonacci (Memoization) of " + n + ": " + fibonacciMemo(n, memo));

        // Using Tabulation
        System.out.println("Fibonacci (Tabulation) of " + n + ": " + fibonacciTabulation(n));
    }
}
```

#### **Explanation**:
1. **Memoization (Top-Down)**: The `fibonacciMemo()` function computes Fibonacci numbers recursively but stores each result in an array (`memo`) to avoid recalculating the same value multiple times.
2. **Tabulation (Bottom-Up)**: The `fibonacciTabulation()` function builds the solution iteratively from the base case, storing results in a table (array).

#### **Sample Output**:
```
Fibonacci (Memoization) of 10: 55
Fibonacci (Tabulation) of 10: 55
```

#### **Time Complexity**:
- **Memoization**: O(n), as each Fibonacci number is computed once and stored.
- **Tabulation**: O(n), as it fills the table iteratively from bottom to top.

---

### **Example 2: 0/1 Knapsack Problem**

**Problem Statement**: Given `n` items, each with a weight and a value, determine the maximum value that can be achieved with a knapsack of capacity `W`. Each item can either be included or excluded from the knapsack.

#### **Dynamic Programming Solution**:
1. **State**: Define `dp[i][w]` as the maximum value that can be obtained using the first `i` items with a knapsack capacity of `w`.
2. **Recurrence Relation**:
   - If the item `i` is not included: `dp[i][w] = dp[i-1][w]`
   - If the item `i` is included: `dp[i][w] = dp[i-1][w - weight[i]] + value[i]`
   - The transition is `dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])`.

#### **Java Implementation**:

```java
public class Knapsack {

    // Method to solve the 0/1 Knapsack Problem using DP
    public static int knapsack(int W, int[] weights, int[] values, int n) {
        int[][] dp = new int[n + 1][W + 1];

        // Fill the DP table
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (weights[i - 1] <= w) {
                    // If the item can be included in the knapsack
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    // If the item cannot be included in the knapsack
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[n][W]; // The last cell contains the maximum value
    }

    public static void main(String[] args) {
        int[] values = {60, 100, 120};
        int[] weights = {10, 20, 30};
        int W = 50; // Knapsack capacity
        int n = values.length;

        System.out.println("Maximum value in Knapsack = " + knapsack(W, weights, values, n));
    }
}
```

#### **Explanation**:
- We use a 2D array `dp[i][w]` where `i` represents the number of items considered and `w` represents the current capacity of the knapsack. 
- We iterate over all items and capacities, updating the `dp` table based on whether we include or exclude each item.

#### **Sample Output**:
```
Maximum value in Knapsack = 220
```

#### **Time Complexity**:
- **O(n * W)**, where `n` is the number of items and `W` is the capacity of the knapsack.
- The space complexity is also **O(n * W)** due to the 2D array used for memoization.

---

### **Conclusion:**

Dynamic Programming is a powerful algorithmic technique for solving optimization problems, especially those involving overlapping subproblems. By storing and reusing solutions to subproblems, DP optimizes the computation process and avoids redundant work.

- **Memoization** (top-down) is typically easier to implement but can have more space overhead due to recursion.
- **Tabulation** (bottom-up) is more efficient in terms of space and avoids recursion overhead but may require additional effort to structure the problem iteratively.