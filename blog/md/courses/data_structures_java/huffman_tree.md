# **Huffman Tree**

A **Huffman Tree** is a type of **binary tree** used for **data compression**. It is constructed using a **greedy algorithm** and is widely used in applications such as file compression (e.g., in **ZIP files** and **JPEG images**). The Huffman Tree is used to build **Huffman codes**, which assign variable-length codes to each input character based on their frequencies, with more frequent characters receiving shorter codes and less frequent characters receiving longer codes.

### **How Huffman Tree Works:**
The idea behind the Huffman coding algorithm is to:
1. **Assign shorter codes** to more frequent characters.
2. **Assign longer codes** to less frequent characters.

The construction of the Huffman Tree follows these steps:

1. **Count the frequency** of each character in the given data.
2. **Create a priority queue (min-heap)** where each element is a node representing a character and its frequency.
3. **Build the Huffman Tree**:
   - Extract the two nodes with the lowest frequencies from the priority queue.
   - Create a new internal node with a frequency equal to the sum of the two nodes' frequencies. This node becomes the parent of the two nodes.
   - Insert the new internal node back into the priority queue.
   - Repeat this process until there is only one node left in the priority queue, which becomes the root of the Huffman Tree.

4. **Generate the Huffman codes**: Starting from the root, assign a **0** for left edges and a **1** for right edges. Each leaf node will have a unique code based on the path from the root to the leaf.

### **Huffman Tree Characteristics:**
- **Optimal**: The Huffman Tree produces the most efficient prefix-free encoding, minimizing the total number of bits required to represent the data.
- **Prefix-Free Codes**: No code is a prefix of another, which is a property that allows the encoded data to be uniquely decoded.

### **Example of Huffman Coding:**

For the string "AAABBBCC", the frequency of characters is:
- `A: 3`
- `B: 3`
- `C: 2`

#### **Steps to Build the Huffman Tree:**

1. **Count frequencies** and create nodes:
   - `A: 3`, `B: 3`, `C: 2`
   - Create nodes for each character and insert them into the priority queue (min-heap).

2. **Combine two nodes with the smallest frequencies**:
   - Combine `C` (2) and one of the `B` nodes (3) to create a new node with frequency 5.
   - The remaining nodes are `A` (3) and the newly created node with frequency 5 (`C + B`).

3. **Repeat until one node remains**:
   - Combine `A` (3) and the node with frequency 5 (`C + B`) to create the final tree node with frequency 8 (`A + (C + B)`).

4. **Generate the Huffman codes** by traversing the tree.

#### **Huffman Tree for "AAABBBCC":**
```
          8
         / \
        3   5
       / \  / \
      A   B C   B
```

- Code for `A`: `0`
- Code for `B`: `10`
- Code for `C`: `11`

Thus, the Huffman code for the string "AAABBBCC" would be:
- A → `0`
- B → `10`
- C → `11`

### **Java Implementation of Huffman Tree**

Here’s a simple Java implementation of the **Huffman Coding** algorithm:

```java
import java.util.*;

class HuffmanTree {
    // Node class for the Huffman tree
    static class Node {
        int freq;
        char ch;
        Node left, right;

        public Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
            left = right = null;
        }
    }

    // Comparator class to compare two nodes based on their frequencies
    static class NodeComparator implements Comparator<Node> {
        public int compare(Node n1, Node n2) {
            return n1.freq - n2.freq;
        }
    }

    // Method to build the Huffman tree
    public static Node buildHuffmanTree(Map<Character, Integer> freqMap) {
        PriorityQueue<Node> pq = new PriorityQueue<>(new NodeComparator());

        // Add all nodes to the priority queue
        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }

        // Build the tree
        while (pq.size() > 1) {
            // Remove two nodes with the smallest frequencies
            Node left = pq.poll();
            Node right = pq.poll();

            // Create a new internal node with the sum of frequencies
            Node newNode = new Node('\0', left.freq + right.freq);
            newNode.left = left;
            newNode.right = right;

            // Add the new node back to the priority queue
            pq.add(newNode);
        }

        // The remaining node is the root of the Huffman Tree
        return pq.poll();
    }

    // Method to generate Huffman codes from the tree
    public static void generateHuffmanCodes(Node root, StringBuilder prefix, Map<Character, String> huffmanCodes) {
        // Base case: if the node is null, return
        if (root == null) return;

        // If the node is a leaf node, it contains a character
        if (root.left == null && root.right == null) {
            huffmanCodes.put(root.ch, prefix.toString());
        }

        // Recursively traverse the left and right subtrees
        prefix.append('0');
        generateHuffmanCodes(root.left, prefix, huffmanCodes);
        prefix.deleteCharAt(prefix.length() - 1);

        prefix.append('1');
        generateHuffmanCodes(root.right, prefix, huffmanCodes);
        prefix.deleteCharAt(prefix.length() - 1);
    }

    // Method to print the Huffman codes
    public static void printHuffmanCodes(Map<Character, String> huffmanCodes) {
        System.out.println("Character | Huffman Code");
        System.out.println("------------------------");
        for (Map.Entry<Character, String> entry : huffmanCodes.entrySet()) {
            System.out.println(entry.getKey() + " \t\t " + entry.getValue());
        }
    }

    // Method to perform Huffman encoding
    public static String encode(String input, Map<Character, String> huffmanCodes) {
        StringBuilder encodedString = new StringBuilder();
        for (char ch : input.toCharArray()) {
            encodedString.append(huffmanCodes.get(ch));
        }
        return encodedString.toString();
    }

    public static void main(String[] args) {
        // Sample input string
        String input = "AAABBBCC";

        // Step 1: Calculate frequency of each character
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char ch : input.toCharArray()) {
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }

        // Step 2: Build Huffman Tree
        Node root = buildHuffmanTree(freqMap);

        // Step 3: Generate Huffman Codes
        Map<Character, String> huffmanCodes = new HashMap<>();
        generateHuffmanCodes(root, new StringBuilder(), huffmanCodes);

        // Step 4: Print Huffman Codes
        printHuffmanCodes(huffmanCodes);

        // Step 5: Encode the input string
        String encodedString = encode(input, huffmanCodes);
        System.out.println("\nEncoded String: " + encodedString);
    }
}
```

### **Explanation of the Code**:

1. **Node Class**: This represents a node in the Huffman tree. Each node has:
   - A frequency (`freq`), which stores the number of occurrences of a character.
   - A character (`ch`), which stores the character (used for leaf nodes).
   - Left and right child nodes (`left` and `right`).

2. **NodeComparator Class**: This comparator is used to order nodes in a **priority queue** (min-heap) based on their frequency values.

3. **buildHuffmanTree()**: This method constructs the Huffman tree using a priority queue (min-heap). It repeatedly combines the two nodes with the lowest frequencies until only one node remains.

4. **generateHuffmanCodes()**: This method recursively generates the Huffman codes by traversing the Huffman tree. It uses the prefix `0` for left edges and `1` for right edges.

5. **printHuffmanCodes()**: This method prints the Huffman codes for each character.

6. **encode()**: This method encodes the input string using the generated Huffman codes.

7. **main()**:
   - The main method performs the steps: 
     - It calculates the frequency of each character in the input string.
     - It builds the Huffman tree.
     - It generates the Huffman codes and prints them.
     - It encodes the input string using the Huffman codes and prints the encoded result.

### **Sample Output:**

```
Character | Huffman Code
------------------------
A 	     0
B 	     10
C 	     11

Encoded String: 000010101011
```

### **Time Complexity of Huffman Coding**:
- **Building the frequency map**: O(n), where **n** is the number of characters in the input.
- **Building the Huffman tree**: O(n log n), where **n** is the number of distinct characters in the input.
- **Generating Huffman codes**: O(n), as each character is processed once in the tree.

Thus, the overall time complexity is **O(n log n)**, which is efficient for compression.

### **Space Complexity**:
- **O(n)**: Space is used to store the frequency map, the Huffman tree, and the Huffman codes.

### **Advantages of Huffman Coding**:
1. **Optimality**: Huffman coding produces the most efficient encoding scheme for any given input in terms of the total number of bits used.
2. **Lossless Compression**: Huffman coding is a lossless data compression algorithm, meaning the original data can be perfectly reconstructed from the compressed data.

### **Disadvantages of Huffman Coding**:
1. **Overhead**: The frequency table and tree must be stored along with the encoded data, which adds overhead.
2. **Not Adaptive**: In its basic form, Huffman coding requires the entire input to be known in advance.

### **Conclusion**:
Huffman coding is a widely used and efficient algorithm for lossless data compression. It is the basis for compression standards such as **ZIP**, **JPEG**, and **MP3**. However, it is more suitable for scenarios where the frequencies of characters are known or can be computed ahead of time.

Let me know if you need further clarification or additional enhancements!