## `__` function and variables

In Python, a variable or method name prefixed with double underscores (`__`) is known as a **name-mangled** or **private** variable/method. 

This is a way to make attributes or methods "private" to a class, meaning they cannot be easily accessed or modified from outside the class. 
However, this is not true privacy (as in some other languages like Java) but rather a mechanism to avoid name clashes in subclasses.

---

### Key Points About `__` Variables:
1. **Name Mangling**:
   - When a variable or method name starts with `__`, Python internally changes its name to `_ClassName__variableName` to avoid conflicts in subclasses.
   - This is called **name mangling**.

2. **Not Truly Private**:
   - The variable or method is still accessible, but its name is modified to make it harder to accidentally override or access.

3. **Purpose**:
   - It is primarily used to avoid naming conflicts in inheritance hierarchies.
   - It is not intended for strict access control (use a single underscore `_` for convention-based "private" attributes).

---

### Example: Using `__` Variables
```python
class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self.__private_var = "I am private"

    def display(self):
        print(self.public_var)
        print(self.__private_var)

# Create an object
obj = MyClass()

# Access public variable
print(obj.public_var)  # Works fine

# Access private variable directly (will raise an error)
try:
    print(obj.__private_var)
except AttributeError as e:
    print(f"Error: {e}")

# Access private variable using name mangling
print(obj._MyClass__private_var)  # Works, but not recommended

# Call the display method (accesses private variable internally)
obj.display()
```

---

### Output:
```
I am public
Error: 'MyClass' object has no attribute '__private_var'
I am private
I am public
I am private
```

---

### Explanation:
1. **`self.public_var`**:
   - This is a public variable and can be accessed directly from outside the class.

2. **`self.__private_var`**:
   - This is a private variable due to the `__` prefix.
   - Direct access (`obj.__private_var`) raises an `AttributeError`.
   - However, it can still be accessed using the mangled name (`obj._MyClass__private_var`).

3. **`display` Method**:
   - The private variable is accessible within the class methods, so `obj.display()` works fine.

---

### When to Use `__` Variables:
- Use `__` variables when you want to avoid name clashes in subclasses.
- Use a single underscore `_` for convention-based private attributes (e.g., `self._private_var`), which indicates that the attribute is intended for internal use but does not enforce any access restrictions.

---

### Example: Name Mangling in Inheritance
```python
class Parent:
    def __init__(self):
        self.__private_var = "Parent's private"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private_var = "Child's private"

    def display(self):
        print(self.__private_var)  # Accesses Child's private variable
        print(self._Parent__private_var)  # Accesses Parent's private variable

# Create an object
obj = Child()
obj.display()
```

---

### Output:
```
Child's private
Parent's private
```

---

### Explanation:
- The `__private_var` in the `Parent` class is mangled to `_Parent__private_var`.
- The `__private_var` in the `Child` class is mangled to `_Child__private_var`.
- This avoids naming conflicts between the parent and child classes.

---

### Summary:
- `__` variables are name-mangled to avoid conflicts in inheritance.
- They are not truly private but are harder to access directly.
- Use them sparingly and prefer a single underscore `_` for convention-based private attributes.