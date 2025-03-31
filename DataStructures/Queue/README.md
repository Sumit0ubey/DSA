# Queue Data Structure

## What is a Queue?
A queue is a linear data structure that follows the **FIFO (First In, First Out)** principle. It means that the element inserted first is the first one to be removed, similar to a real-life queue (e.g., a line at a ticket counter).

## When to Use Queues
- When elements need to be processed in order.
- When managing tasks in scheduling systems (CPU scheduling, print queue).
- When implementing breadth-first search (BFS) algorithms.
- When handling requests in a server (task queues).

---

## Types of Queues

### 1. Simple Queue
- Follows FIFO.
- Elements are inserted at the **rear** and removed from the **front**.

### 2. Circular Queue
- The last position is connected back to the first, forming a circle.
- Prevents wastage of space in a fixed-size array implementation.

### 3. Double-Ended Queue (Deque)
- Elements can be added or removed from both ends (front and rear).
- Two types:
  - **Input-Restricted Deque**: Insertion allowed only at one end.
  - **Output-Restricted Deque**: Deletion allowed only at one end.

### 4. Priority Queue
- Elements are dequeued based on priority instead of FIFO.
- Higher priority elements are dequeued before lower priority ones.

---

## Basic Operations on Queues

### 1. Enqueue (Insertion)
**Definition:** Adding an element to the rear of the queue.

**Algorithm:**
1. Check if the queue is full.
2. Insert the element at the rear.
3. Update the rear pointer.

```python
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            print("Queue is full")
```

**Time Complexity:** O(1)

---

### 2. Dequeue (Deletion)
**Definition:** Removing an element from the front of the queue.

**Algorithm:**
1. Check if the queue is empty.
2. Remove the front element.
3. Update the front pointer.

```python
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Queue is empty")
```

**Time Complexity:** O(1) (linked list) or O(n) (array-based)

---

### 3. Peek (Front Element)
**Definition:** Getting the front element without removing it.

**Algorithm:**
1. Check if the queue is empty.
2. Return the front element.

```python
    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None
```

**Time Complexity:** O(1)

---

### 4. Checking if the Queue is Empty
```python
    def is_empty(self):
        return len(self.queue) == 0
```

**Time Complexity:** O(1)

---

## Example of Queue Operations
Consider a queue where elements `[10, 20, 30]` exist:

```
Front → [10, 20, 30] ← Rear
```
1. **Enqueue(40)** → `[10, 20, 30, 40]`
2. **Dequeue()** → `[20, 30, 40]`
3. **Peek()** → `20`

---

## Advantages of Queues
- Maintains order of processing.
- Efficient O(1) insertion and deletion (linked list implementation).
- Used in various real-world applications like task scheduling.

## Disadvantages of Queues
- Fixed size in array-based implementation.
- Dequeue operation in array-based queues is O(n) due to shifting.
- Accessing elements randomly is inefficient (O(n)).

---

## Conclusion
Queues are a crucial data structure for managing tasks in an orderly fashion. Different types of queues serve different needs, making them widely applicable in various computing problems like scheduling and data streaming.

