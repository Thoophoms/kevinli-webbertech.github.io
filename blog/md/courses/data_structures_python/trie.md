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

### Python Code for Trie Implementation

Here’s an implementation of a **Trie** in Python with the basic operations: `insert`, `search`, and `starts_with` (prefix search).

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Stores the children nodes (each character has a node)
        self.is_end_of_word = False  # Marks if the current node is the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the trie with a root node
    
    # Insert a word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            # If the character is not present, create a new TrieNode
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word
    
    # Search for a word in the trie
    def search(self, word):
        node = self.root
        for char in word:
            # If the character is not found, return False
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # Check if the end of the word is marked
    
    # Check if there is any word in the trie that starts with the given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            # If the character is not found, return False
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # Prefix exists
    
# Example Usage
if __name__ == "__main__":
    trie = Trie()
    
    # Insert words into the trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("bat")
    trie.insert("ball")
    
    # Search for words in the trie
    print("Search 'apple':", trie.search("apple"))  # Output: True
    print("Search 'app':", trie.search("app"))      # Output: True
    print("Search 'bat':", trie.search("bat"))      # Output: True
    print("Search 'bake':", trie.search("bake"))    # Output: False
    
    # Check for words starting with a given prefix
    print("Prefix 'ba':", trie.starts_with("ba"))  # Output: True
    print("Prefix 'bat':", trie.starts_with("bat")) # Output: True
    print("Prefix 'balloon':", trie.starts_with("balloon")) # Output: False
```

### Explanation:

1. **TrieNode Class**:
   - `children`: A dictionary that maps a character (key) to a **TrieNode** (value). This is where the child nodes are stored.
   - `is_end_of_word`: A boolean that indicates whether the current node is the end of a word. This is necessary to differentiate between prefixes and complete words.

2. **Trie Class**:
   - **`insert(word)`**: This method inserts a word into the trie by iterating through each character in the word and creating new nodes as needed. Once the last character of the word is reached, the `is_end_of_word` flag is set to `True`.
   - **`search(word)`**: This method checks whether a word exists in the trie. It traverses through the nodes according to the characters in the word and checks if the last node has `is_end_of_word` set to `True`.
   - **`starts_with(prefix)`**: This method checks if there is any word in the trie that starts with the given prefix. It traverses the trie based on the prefix characters. If all characters in the prefix are found, it returns `True`; otherwise, `False`.

### Example Output


```
Search 'apple': True
Search 'app': True
Search 'bat': True
Search 'bake': False
Prefix 'ba': True
Prefix 'bat': True
Prefix 'balloon': False
```

### Time Complexity

- **Insert**: O(m), where `m` is the length of the word being inserted.
- **Search**: O(m), where `m` is the length of the word being searched.
- **Starts With**: O(p), where `p` is the length of the prefix.

The space complexity depends on the number of words and the average length of the words inserted into the trie.

### Summary:
- A **Trie** is an efficient tree-like data structure used for storing and searching strings or prefixes.
- Tries allow for fast prefix searches and can be used in applications like autocomplete and dictionary lookups.
- The **insert**, **search**, and **prefix search** operations all run in linear time relative to the length of the word or prefix.