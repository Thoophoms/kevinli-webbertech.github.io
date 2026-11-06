# **Greedy Algorithm**

A **greedy algorithm** is a problem-solving approach that builds a solution incrementally by making the **locally optimal choice** at each step, with the hope that these local choices will lead to a globally optimal solution. In other words, the algorithm makes the best possible decision at each step, without worrying about the future consequences, assuming that local optimal choices lead to the overall best solution.

### **Key Characteristics of Greedy Algorithms**:
1. **Greedy Choice Property**: A global optimum can be arrived at by selecting a local optimum. In other words, choosing the best option at each step should lead to the overall best solution.
2. **Optimal Substructure**: The optimal solution to the problem can be constructed from optimal solutions to its subproblems.
3. **No Backtracking**: Once a decision is made, it is not revisited or changed, and the algorithm does not backtrack to make alternate choices.

### **Common Greedy Algorithm Problems**:
1. **Fractional Knapsack Problem**: Maximize the total value in a knapsack with a weight limit, where items can be taken fractionally.
2. **0/1 Knapsack Problem**: A similar problem but the items must either be completely included or excluded.
3. **Activity Selection Problem**: Select the maximum number of activities that do not overlap in time.
4. **Huffman Coding**: Data compression technique where the most frequent characters are assigned shorter codes.
5. **Prim’s and Kruskal’s Algorithms**: Used to find the **Minimum Spanning Tree (MST)** in a graph.

### **Steps to Design a Greedy Algorithm**:
1. **Problem Analysis**: Understand the problem and determine if a greedy approach is applicable.
2. **Greedy Choice Property**: Identify the greedy choice that will lead to a solution.
3. **Optimal Substructure**: Ensure that solving subproblems optimally will lead to the solution of the original problem.
4. **Algorithm Construction**: Build the greedy algorithm by selecting the best possible choice at each step and updating the state.
5. **Proof of Optimality**: Ensure that the greedy choice leads to an optimal solution.

### **Examples of Greedy Algorithms**:

---

### **1. Activity Selection Problem**:
**Problem Statement**: Given a set of activities with their start and end times, select the maximum number of activities that can be performed by a single person, such that no two activities overlap.

#### **Greedy Approach**:
1. **Sort** the activities by their finish time (earliest finish time first).
2. Select the activity with the earliest finish time.
3. For each subsequent activity, if its start time is greater than or equal to the finish time of the last selected activity, select it.

#### **Java Implementation**:

```java
import java.util.*;

class Activity {
    int start, finish;

    public Activity(int start, int finish) {
        this.start = start;
        this.finish = finish;
    }
}

public class GreedyAlgorithm {

    // Method to select the maximum number of activities
    public static void selectActivities(Activity[] activities) {
        // Sort activities by finish time
        Arrays.sort(activities, Comparator.comparingInt(a -> a.finish));

        System.out.println("Selected activities:");

        // The first activity always gets selected
        int lastSelectedActivityIndex = 0;
        System.out.println("Activity: (" + activities[lastSelectedActivityIndex].start + ", " + activities[lastSelectedActivityIndex].finish + ")");
        
        // Consider the rest of the activities
        for (int i = 1; i < activities.length; i++) {
            // If this activity starts after the last selected activity finishes, select it
            if (activities[i].start >= activities[lastSelectedActivityIndex].finish) {
                System.out.println("Activity: (" + activities[i].start + ", " + activities[i].finish + ")");
                lastSelectedActivityIndex = i;
            }
        }
    }

    public static void main(String[] args) {
        // Example input
        Activity[] activities = new Activity[] {
            new Activity(1, 4),
            new Activity(2, 6),
            new Activity(5, 7),
            new Activity(6, 8),
            new Activity(8, 9)
        };
        
        selectActivities(activities);
    }
}
```

#### **Explanation**:
1. **Sorting**: We first sort the activities based on their finish time in increasing order.
2. **Greedy Choice**: Select the first activity, then for each subsequent activity, check if its start time is after the finish time of the last selected activity. If true, select it.

#### **Sample Output**:

```
Selected activities:
Activity: (1, 4)
Activity: (5, 7)
Activity: (8, 9)
```

#### **Time Complexity**:
- Sorting the activities takes **O(n log n)**, and iterating over the activities takes **O(n)**. So, the overall time complexity is **O(n log n)**.

---

### **2. Fractional Knapsack Problem**:
**Problem Statement**: Given a set of items, each with a weight and value, determine the maximum value that can be obtained by filling a knapsack of capacity `W`. The twist is that you can take fractional parts of the items.

#### **Greedy Approach**:
1. **Compute the value-to-weight ratio** for each item.
2. **Sort** the items in decreasing order of value-to-weight ratio.
3. **Take the item** with the highest value-to-weight ratio first and fill the knapsack. If the item cannot fully fit, take the fractional part of it.
4. **Repeat** the process until the knapsack is full or all items are processed.

#### **Java Implementation**:

```java
import java.util.*;

class Item {
    int weight;
    int value;

    // Constructor
    public Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}

public class GreedyKnapsack {

    // Method to solve the Fractional Knapsack problem
    public static double getMaxValue(Item[] items, int capacity) {
        // Calculate value-to-weight ratio for each item
        Arrays.sort(items, (a, b) -> Double.compare(b.value / (double) b.weight, a.value / (double) a.weight));

        double maxValue = 0;
        for (Item item : items) {
            if (capacity == 0) break;

            // If the item can be fully taken
            if (item.weight <= capacity) {
                maxValue += item.value;
                capacity -= item.weight;
            }
            // If the item cannot be fully taken, take the fraction
            else {
                maxValue += item.value * ((double) capacity / item.weight);
                break;
            }
        }
        return maxValue;
    }

    public static void main(String[] args) {
        Item[] items = new Item[] {
            new Item(10, 60),
            new Item(20, 100),
            new Item(30, 120)
        };

        int capacity = 50;

        double maxValue = getMaxValue(items, capacity);
        System.out.println("Maximum value in knapsack = " + maxValue);
    }
}
```

#### **Explanation**:
1. **Sort Items by Value-to-Weight Ratio**: We sort the items based on their value-to-weight ratio in descending order.
2. **Greedy Choice**: Select the item with the highest ratio first. If the entire item can't fit, take a fraction of it until the knapsack is full.

#### **Sample Output**:
```
Maximum value in knapsack = 240.0
```

#### **Time Complexity**:
- Sorting the items takes **O(n log n)**, and iterating over the items takes **O(n)**. So, the overall time complexity is **O(n log n)**.

---

### **Advantages of Greedy Algorithms**:
1. **Efficiency**: Greedy algorithms are often more efficient than exhaustive algorithms, especially for problems with a large input size.
2. **Simplicity**: Greedy algorithms are often easy to understand and implement.
3. **Fast Solution**: Many greedy algorithms run in polynomial time and provide a solution quickly.

### **Disadvantages of Greedy Algorithms**:
1. **Not Always Optimal**: Greedy algorithms do not always produce the optimal solution, especially when the problem does not have the greedy choice property or optimal substructure.
2. **Local Optimality**: Greedy choices focus only on the current step and do not consider future consequences, which can lead to suboptimal solutions.

### **Conclusion**:
Greedy algorithms are a powerful and efficient approach for solving a variety of problems, especially those that can be broken down into smaller subproblems where the greedy choice leads to an optimal solution. However, they may not always produce the best solution for all problems, so it’s important to verify that a greedy approach works for the specific problem at hand.