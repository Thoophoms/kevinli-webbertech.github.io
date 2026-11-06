# Huffman Tree

A **Huffman Tree** is a **binary tree** used for **lossless data compression**. It is part of the **Huffman Coding** algorithm, which is a widely used method for encoding data efficiently. The purpose of a Huffman tree is to represent symbols (characters or data values) in a way that minimizes the overall size of the data when transmitted or stored.

### What is Huffman Coding?

**Huffman Coding** is a **variable-length prefix encoding** scheme. The idea is to assign shorter codes to more frequent symbols and longer codes to less frequent symbols. This reduces the overall number of bits needed to represent the data. 

### Huffman Tree Construction

To construct a Huffman tree, follow these steps:

1. **Count the Frequency**: Start by counting the frequency of each symbol (or character) in the data you wish to compress.
   
   Example (for a string "ABRACADABRA"):
   ```
   A: 5
   B: 2
   R: 2
   C: 1
   D: 1
   ```

2. **Create a Priority Queue (Min-Heap)**: Each symbol is represented by a node with the symbol and its frequency. These nodes are inserted into a **min-heap** or **priority queue** based on their frequencies. The node with the lowest frequency has the highest priority.

3. **Build the Huffman Tree**:
   - While there is more than one node in the heap:
     1. Remove the two nodes with the lowest frequencies.
     2. Create a new node with the sum of their frequencies. This new node becomes the parent of the two nodes.
     3. Insert the new node back into the heap.
   - Repeat the process until there is only one node left, which becomes the root of the Huffman tree.

4. **Assign Binary Codes**: Once the Huffman tree is built, assign binary codes to the symbols:
   - Assign `0` to the left child and `1` to the right child at each step of the traversal from the root to the leaves.
   - The resulting code for each symbol is the path from the root to the symbol’s leaf node.

### Example: Huffman Tree Construction

Let's use the example string "ABRACADABRA" with the following frequencies:

```
A: 5
B: 2
R: 2
C: 1
D: 1
```

1. **Step 1 - Create Initial Nodes**:
   Each symbol is a node with its frequency:
   ```
   A: 5, B: 2, R: 2, C: 1, D: 1
   ```

2. **Step 2 - Build the Tree**:
   - Combine `C` and `D` (the two lowest frequencies): 
     New node: `CD: 2`, which becomes the parent of `C` and `D`.
   
   - New list of nodes: `A: 5, B: 2, R: 2, CD: 2`
   
   - Combine `B` and `R`: 
     New node: `BR: 4`, which becomes the parent of `B` and `R`.
   
   - New list of nodes: `A: 5, BR: 4, CD: 2`
   
   - Combine `CD` and `BR`: 
     New node: `CD-BR: 6`, which becomes the parent of `CD` and `BR`.
   
   - New list of nodes: `A: 5, CD-BR: 6`
   
   - Combine `A` and `CD-BR`: 
     New node: `A-CD-BR: 11`, which becomes the root of the tree.

   Now, the Huffman tree looks like this:
   ```
            (11)
           /    \
        (5)      (6)
        /  \    /    \
      (A)  (B) (R)   (CD)
                          /  \
                        (C)  (D)
   ```

3. **Step 3 - Assign Binary Codes**:
   - `A: 0` (left child of the root)
   - `B: 10` (left child of node `(BR)`)
   - `R: 11` (right child of node `(BR)`)
   - `C: 110` (left child of node `(CD)`)
   - `D: 111` (right child of node `(CD)`)

   Final Huffman codes:
   ```
   A: 0
   B: 10
   R: 11
   C: 110
   D: 111
   ```

### Uses of Huffman Trees

1. **Data Compression**:
   The primary use of Huffman trees is in **lossless data compression** algorithms. The idea is to reduce the size of data by encoding more frequent symbols with shorter codes and less frequent symbols with longer codes.
   
   **Example**: Huffman coding is used in formats like:
   - **ZIP** files (compression).
   - **JPEG** (image compression).
   - **MP3** (audio compression).
   - **PDF** (document compression).

2. **Efficient Encoding**:
   Huffman trees allow data to be represented using **variable-length** codes, unlike traditional fixed-length encoding (like ASCII, where each character is represented by 8 bits). This results in a more compact representation of the data.

3. **Canonical Huffman Coding**:
   Huffman coding can be used in situations where it's necessary to transmit or store both the encoded data and the decoding tree. In practice, **Canonical Huffman Coding** is used, which ensures that the tree structure can be reconstructed without needing to transmit the full tree structure (e.g., in image or video encoding).

4. **Applications in Networking**:
   Huffman coding is used in various **network protocols** to compress the data being transmitted. This helps reduce the amount of bandwidth required for data transmission, thus improving speed and reducing costs.

5. **Dictionary Compression**:
   Huffman coding is useful in **dictionary compression** methods, where frequently used words or phrases are given shorter codes, and less frequent ones are given longer codes.

---

### Advantages of Huffman Coding:
- **Optimal**: Huffman coding is optimal for prefix codes, meaning it results in the smallest possible encoding for a given set of symbol frequencies.
- **Lossless**: Huffman coding is a **lossless compression** algorithm, meaning that the original data can be perfectly reconstructed from the compressed data.

### Disadvantages of Huffman Coding:
- **Overhead**: While Huffman coding minimizes the size of the compressed data, the process of building the Huffman tree and maintaining the binary codes can add some overhead, especially for smaller datasets.
- **Complexity**: Constructing the Huffman tree requires sorting and repeated merging of nodes, making the algorithm a bit more complex than simple compression schemes like Run-Length Encoding (RLE).

### Summary:

A **Huffman Tree** is a binary tree used for **data compression** by assigning variable-length binary codes to input characters based on their frequencies. The **Huffman Coding** algorithm is widely used in applications such as file compression (ZIP), image encoding (JPEG), and audio compression (MP3), among others. The goal is to reduce the amount of data needed to represent the original data, leading to more efficient storage and transmission.


## Python Implementation

```python

import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)
    return codes

def huffman_encoding(text):
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    root = build_huffman_tree(char_freq)
    huffman_codes = generate_huffman_codes(root)
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, root

def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            decoded_text += current.char
            current = root
    return decoded_text

# Testing Huffman Encoding and Decoding
if __name__ == "__main__":
    text = "hello huffman"
    encoded_text, tree = huffman_encoding(text)
    decoded_text = huffman_decoding(encoded_text, tree)
    print("Original Text:", text)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)
```