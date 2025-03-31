# Stack Data Structure

## What is a Stack?
A stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle. This means the last element inserted is the first one to be removed, similar to a stack of plates.

## When to Use Stacks
- When managing function calls (recursion, backtracking).
- When implementing undo/redo functionality.
- When evaluating expressions (postfix, prefix notation).
- When solving problems like depth-first search (DFS).

---

## Types of Stacks

### 1. Simple Stack
- Follows LIFO.
- Uses `push()` to add elements and `pop()` to remove elements.

### 2. Doubly Ended Stack
- Allows pushing and popping from both ends.
- Useful for optimizing specific algorithms.

### 3. Fixed Size Stack
- Has a predefined maximum size.
- Implemented using arrays.

### 4. Dynamic Stack
- Can grow and shrink as needed.
- Implemented using linked lists.

---

## Basic Operations on Stacks

### 1. Push (Insertion)
**Definition:** Adding an element to the top of the stack.

**Algorithm:**
1. Check if the stack is full.
2. Insert the element at the top.
3. Update the top pointer.

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
```

**Time Complexity:** O(1)

---

### 2. Pop (Deletion)
**Definition:** Removing an element from the top of the stack.

**Algorithm:**
1. Check if the stack is empty.
2. Remove the top element.
3. Update the top pointer.

```python
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Stack is empty")
```

**Time Complexity:** O(1)

---

### 3. Peek (Top Element)
**Definition:** Getting the top element without removing it.

**Algorithm:**
1. Check if the stack is empty.
2. Return the top element.

```python
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
```

**Time Complexity:** O(1)

---

### 4. Checking if the Stack is Empty
```python
    def is_empty(self):
        return len(self.stack) == 0
```

**Time Complexity:** O(1)

---

## Example of Stack Operations
Consider a stack with elements `[10, 20, 30]`:

```
Top → [30, 20, 10]
```
1. **Push(40)** → `[40, 30, 20, 10]`
2. **Pop()** → `[30, 20, 10]`
3. **Peek()** → `30`

---

## Advantages of Stacks
- Simple and efficient (O(1) operations).
- Ideal for problems requiring backtracking.
- Used in memory management (function call stack).

## Disadvantages of Stacks
- Limited size in static array implementation.
- Accessing elements other than the top is inefficient (O(n)).

---

## Conclusion
Stacks are a crucial data structure for handling LIFO-based operations efficiently. They are widely used in recursion, expression evaluation, and algorithm implementation.