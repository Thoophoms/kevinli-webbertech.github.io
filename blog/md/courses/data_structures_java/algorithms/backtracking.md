# **Backtracking**

**Backtracking** is a general algorithmic technique for solving problems recursively by trying out different possibilities and abandoning (or "backtracking") as soon as it determines that the current solution cannot possibly lead to a valid solution. It is particularly useful for solving **combinatorial problems**, such as puzzles, pathfinding problems, and optimization problems.

### **Key Concepts of Backtracking:**
1. **Recursive Exploration**: The idea is to build a solution incrementally, one step at a time. If the current solution violates the problem's constraints, we backtrack to the previous step and try a different path.
2. **Pruning**: If at any point, the solution violates the constraints, we abandon that solution and backtrack. This step helps to reduce the number of potential solutions to explore.

### **Common Backtracking Problems:**
1. **N-Queens Problem**: Place `n` queens on an `n x n` chessboard such that no two queens attack each other.
2. **Sudoku Solver**: Fill a partially filled 9x9 grid of Sudoku with valid numbers.
3. **Subset Sum**: Find subsets of numbers that add up to a given sum.
4. **Permutations and Combinations**: Find all possible permutations or combinations of a set of numbers or characters.
5. **Graph Traversal Problems**: Like finding Hamiltonian paths or cycles in a graph.

### **Backtracking Algorithm Structure:**
1. **Choose**: Select an option to explore.
2. **Explore**: Recursively explore further by calling the backtracking function.
3. **Un-choose**: If a solution doesn't work, undo the choice (backtrack) and try the next option.

### **Example Problems and Solutions:**

---

### **1. N-Queens Problem:**

**Problem Statement:**
Place `n` queens on an `n x n` chessboard such that no two queens attack each other. This means no two queens should share the same row, column, or diagonal.

#### **Backtracking Approach:**
1. Place a queen in a row.
2. For each row, try placing a queen in every column.
3. If the placement is safe, recursively try to place queens in the next rows.
4. If the placement leads to a conflict, backtrack and try the next position.

#### **Java Implementation:**

```java
public class NQueens {
    // Method to print the chessboard
    public static void printSolution(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Method to check if a queen can be placed at board[row][col]
    public static boolean isSafe(int[][] board, int row, int col) {
        // Check the column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1) {
                return false;
            }
        }

        // Check the upper left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        // Check the upper right diagonal
        for (int i = row, j = col; i >= 0 && j < board.length; i--, j++) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    // Recursive method to solve the N-Queens problem
    public static boolean solveNQueens(int[][] board, int row) {
        // If all queens are placed, return true
        if (row >= board.length) {
            return true;
        }

        // Try placing a queen in all columns one by one
        for (int col = 0; col < board.length; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 1; // Place queen

                // Recursively place the rest of the queens
                if (solveNQueens(board, row + 1)) {
                    return true;
                }

                // If placing queen in board[row][col] doesn't lead to a solution, backtrack
                board[row][col] = 0; // Backtrack
            }
        }

        // If the queen cannot be placed in any column of this row, return false
        return false;
    }

    public static void main(String[] args) {
        int n = 4; // You can change n to any value
        int[][] board = new int[n][n];

        if (solveNQueens(board, 0)) {
            printSolution(board);
        } else {
            System.out.println("Solution does not exist.");
        }
    }
}
```

#### **Explanation:**
1. **isSafe()**: Checks if a queen can be safely placed at a given position by ensuring there are no other queens in the same column or diagonals.
2. **solveNQueens()**: Recursively tries to place queens in each row. If placing a queen in the current row leads to a solution, it proceeds to the next row. If no valid placement exists, it backtracks by removing the queen and trying the next possible position.
3. **printSolution()**: Prints the chessboard, where `1` represents a queen and `0` represents an empty space.

#### **Sample Output for `n=4`:**
```
1 0 0 0 
0 0 1 0 
0 1 0 0 
0 0 0 1 
```

---

### **2. Sudoku Solver:**

**Problem Statement:**
Solve a 9x9 Sudoku puzzle. The puzzle consists of a partially filled grid, and the goal is to fill the remaining cells with numbers from 1 to 9, such that each row, column, and 3x3 subgrid contains all the digits from 1 to 9.

#### **Backtracking Approach:**
1. Try placing a number from 1 to 9 in each empty cell.
2. If placing the number leads to a valid solution, continue to the next empty cell.
3. If placing the number violates the Sudoku constraints, backtrack by removing the number and trying the next one.

#### **Java Implementation:**

```java
public class SudokuSolver {
    // Method to check if a number can be placed at grid[row][col]
    public static boolean isSafe(int[][] grid, int row, int col, int num) {
        // Check if the number is already in the row or column
        for (int x = 0; x < 9; x++) {
            if (grid[row][x] == num || grid[x][col] == num) {
                return false;
            }
        }

        // Check if the number is in the 3x3 subgrid
        int startRow = row - row % 3, startCol = col - col % 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i + startRow][j + startCol] == num) {
                    return false;
                }
            }
        }

        return true;
    }

    // Recursive method to solve the Sudoku
    public static boolean solveSudoku(int[][] grid) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                // If the cell is empty (contains 0), try placing a number
                if (grid[row][col] == 0) {
                    for (int num = 1; num <= 9; num++) {
                        if (isSafe(grid, row, col, num)) {
                            grid[row][col] = num; // Place the number

                            // Recursively try to solve the rest of the grid
                            if (solveSudoku(grid)) {
                                return true;
                            }

                            // If placing num doesn't lead to a solution, backtrack
                            grid[row][col] = 0;
                        }
                    }

                    return false; // If no number can be placed, return false
                }
            }
        }

        return true; // If the grid is completely filled
    }

    // Method to print the Sudoku grid
    public static void printGrid(int[][] grid) {
        for (int r = 0; r < 9; r++) {
            for (int d = 0; d < 9; d++) {
                System.out.print(grid[r][d]);
                System.out.print(" ");
            }
            System.out.print("\n");

            if ((r + 1) % 3 == 0) {
                System.out.print("");
            }
        }
    }

    public static void main(String[] args) {
        int[][] board = new int[][] {
            {5, 3, 0, 0, 7, 0, 0, 0, 0},
            {6, 0, 0, 1, 9, 5, 0, 0, 0},
            {0, 9, 8, 0, 0, 0, 0, 6, 0},
            {8, 0, 0, 0, 6, 0, 0, 0, 3},
            {4, 0, 0, 8, 0, 3, 0, 0, 1},
            {7, 0, 0, 0, 2, 0, 0, 0, 6},
            {0, 6, 0, 0, 0, 0, 2, 8, 0},
            {0, 0, 0, 4, 1, 