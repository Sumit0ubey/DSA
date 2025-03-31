# Linked List Data Structure

## What is a Linked List?
A linked list is a linear data structure where elements (nodes) are linked using pointers. Unlike arrays, linked lists do not require contiguous memory allocation.

## When to Use Linked Lists
- When memory allocation is dynamic.
- When frequent insertions and deletions are required.
- When implementing stacks, queues, or graphs.
- When the size of the data is unknown.

---

## Types of Linked Lists
1. **Singly Linked List**: Each node has a data field and a pointer to the next node.
2. **Doubly Linked List**: Each node has a pointer to both the next and previous nodes.
3. **Circular Linked List**: The last node points back to the first node.

---

## Basic Operations on Linked Lists

### 1. Insertion
**Definition:** Adding a new node at the beginning, end, or a specific position.

**Algorithm:**
1. Create a new node.
2. Adjust pointers to insert the node at the desired position.

**Mathematical Example:**
Insert `30` into a linked list:
```
Before: 10 → 20 → 40
After:  10 → 20 → 30 → 40
```

**Time Complexity:**
- O(1) for inserting at the beginning.
- O(n) for inserting at a specific position.

---

### 2. Deletion
**Definition:** Removing a node from the linked list.

**Algorithm:**
1. Find the node to delete.
2. Adjust the pointers to bypass it.
3. Free the memory.

**Mathematical Example:**
Delete `20` from `10 → 20 → 30 → 40`:
```
Before: 10 → 20 → 30 → 40
After:  10 → 30 → 40
```

**Time Complexity:**
- O(1) for deleting the first node.
- O(n) for deleting a specific node.

---

### 3. Searching
**Definition:** Finding an element in the linked list.

**Algorithm:**
1. Start from the head.
2. Traverse the list until the target is found.

**Example:** Search for `30` in `10 → 20 → 30 → 40`:
```
Element found at position 3
```

**Time Complexity:** O(n)

---

### 4. Traversal
**Definition:** Accessing each element of the linked list.

**Algorithm:**
1. Start from the head.
2. Move through each node using a loop.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

current = head
while current:
    print(current.data)
    current = current.next
```

**Time Complexity:** O(n)

---

## Advantages of Linked Lists
- Dynamic memory allocation (no fixed size).
- Efficient insertions and deletions.
- Can easily implement other data structures like stacks and queues.

## Disadvantages of Linked Lists
- Higher memory usage due to pointers.
- Slower access time compared to arrays (O(n) vs. O(1)).
- Complex pointer handling.

---

## Conclusion
Linked lists are essential for dynamic data storage and efficient insertions/deletions. Understanding their structure and operations is crucial for optimizing memory usage and flexibility in programming.

