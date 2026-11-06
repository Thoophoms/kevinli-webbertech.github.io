
# Trie

A **Trie** (pronounced "try") is a **tree-like data structure** that is used to store a dynamic set of strings, typically for **prefix matching**. It is primarily used for applications like **autocomplete**, **spell checking**, and **IP routing**, among others. Tries are sometimes called **prefix trees** because they allow efficient retrieval of keys that share common prefixes.

### Key Properties of a Trie

1. **Nodes Represent Prefixes**: Each node represents a character or part of a key, and paths from the root to the leaf represent complete words or strings.
2. **No Redundancy**: Common prefixes are stored only once. For example, the strings "bat" and "ball" share the prefix "ba", so "ba" would appear only once in the trie.
3. **Efficient Search**: Searching for a word or prefix is efficient, typically **O(m)**, where `m` is the length of the string being searched. In contrast to searching through a list of strings, tries can offer faster lookups.

### Trie Operations

- **Insert**: Insert a word into the trie.
- **Search**: Check if a word exists in the trie.
- **Prefix Search**: Check if there is any word in the trie that starts with a given prefix.
- **Delete**: Remove a word from the trie.

### Use Cases of Tries

1. **Autocomplete**: Tries are frequently used in search engines to provide suggestions based on typed prefixes.
2. **Spell Checkers**: For checking if a word exists in a dictionary.
3. **IP Routing**: Tries are used in networking algorithms, where IP addresses are matched based on prefixes.
4. **Dictionary Implementations**: To implement dictionary data structures with fast prefix matching.

### Trie Node Structure

Each **TrieNode** contains:
- **Children**: A dictionary or list that maps characters to child nodes.
- **End of Word Flag**: A boolean flag that indicates whether a node represents the end of a word.

### **Java Implementation of Trie**

Below is a Java implementation of a Trie that supports:
1. **Insert**: Add a string to the Trie.
2. **Search**: Search for a string in the Trie.
3. **StartsWith**: Check if there is any string in the Trie that starts with a given prefix.

### 1. **Trie Node Class**

```java
class TrieNode {
    TrieNode[] children; // Array of children (for each letter of the alphabet)
    boolean isEndOfWord; // Flag to indicate if this is the end of a word

    // Constructor for TrieNode
    public TrieNode() {
        children = new TrieNode[26]; // 26 letters in the alphabet
        isEndOfWord = false;
    }
}
```

### 2. **Trie Class**

```java
class Trie {
    private TrieNode root; // Root node of the Trie

    // Constructor to initialize the Trie
    public Trie() {
        root = new TrieNode();
    }

    // Insert a word into the Trie
    public void insert(String word) {
        TrieNode current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a'; // Calculate index (assuming lowercase letters)
            if (current.children[index] == null) {
                current.children[index] = new TrieNode(); // Create a new node if not present
            }
            current = current.children[index]; // Move to the next node
        }
        current.isEndOfWord = true; // Mark the end of the word
    }

    // Search for a word in the Trie
    public boolean search(String word) {
        TrieNode current = root;

        for (char c : word.toCharArray()) {
            int index = c - 'a'; // Calculate index
            if (current.children[index] == null) {
                return false; // Word not found
            }
            current = current.children[index]; // Move to the next node
        }
        return current.isEndOfWord; // Return true if it's the end of a word
    }

    // Check if there's any word in the Trie that starts with the given prefix
    public boolean startsWith(String prefix) {
        TrieNode current = root;

        for (char c : prefix.toCharArray()) {
            int index = c - 'a'; // Calculate index
            if (current.children[index] == null) {
                return false; // No word starts with the given prefix
            }
            current = current.children[index]; // Move to the next node
        }
        return true; // Prefix exists
    }
}
```

### 3. **Main Class to Demonstrate Trie Operations**

```java
public class Main {
    public static void main(String[] args) {
        Trie trie = new Trie();

        // Insert words into the Trie
        trie.insert("apple");
        trie.insert("app");
        trie.insert("bat");
        trie.insert("ball");

        // Search for words in the Trie
        System.out.println("Searching for 'apple': " + trie.search("apple")); // Output: true
        System.out.println("Searching for 'app': " + trie.search("app")); // Output: true
        System.out.println("Searching for 'bat': " + trie.search("bat")); // Output: true
        System.out.println("Searching for 'ball': " + trie.search("ball")); // Output: true
        System.out.println("Searching for 'bake': " + trie.search("bake")); // Output: false

        // Check if a prefix exists in the Trie
        System.out.println("Prefix 'ba' exists: " + trie.startsWith("ba")); // Output: true
        System.out.println("Prefix 'ban' exists: " + trie.startsWith("ban")); // Output: false
    }
}
```

### **Explanation:**
1. **TrieNode Class**: 
   - Represents each node in the Trie. It has an array `children` where each index represents a letter of the alphabet (from 'a' to 'z').
   - The `isEndOfWord` flag is used to mark the end of a valid word in the Trie.
   
2. **Trie Class**:
   - **insert()**: Inserts a word into the Trie by iterating through its characters and creating new nodes as necessary. The `isEndOfWord` flag is set to `true` when the word is completely inserted.
   - **search()**: Searches for a word in the Trie. It returns `true` if the word exists and ends at a node with `isEndOfWord` as `true`.
   - **startsWith()**: Checks if any word in the Trie starts with the given prefix. It returns `true` if the prefix exists, even if the prefix is not a complete word in the Trie.

### **Sample Output:**

```
Searching for 'apple': true
Searching for 'app': true
Searching for 'bat': true
Searching for 'ball': true
Searching for 'bake': false
Prefix 'ba' exists: true
Prefix 'ban' exists: false
```

### **Time Complexity:**
- **insert()**: O(m) – Where m is the length of the word. We need to traverse each character of the word and insert nodes if necessary.
- **search()**: O(m) – Searching for a word requires traversing each character of the word.
- **startsWith()**: O(m) – Checking if a prefix exists requires traversing each character of the prefix.

### **Space Complexity:**
- The space complexity of the Trie is O(n * m), where:
  - **n** is the number of words inserted.
  - **m** is the maximum length of the words.

Each node contains an array of 26 elements (one for each letter), and for each character in the word, a new node might be created.

### **Advantages of Tries:**
- **Efficient Search**: Tries allow for fast search operations, especially when you need to search for prefixes or autocomplete suggestions.
- **Prefix Search**: Tries can efficiently check for the existence of any prefix in a set of words.
- **Memory Efficiency**: Though Tries use more memory than other data structures, they are efficient for storing a large number of strings with shared prefixes.