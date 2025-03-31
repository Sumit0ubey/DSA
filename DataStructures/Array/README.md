# Array Data Structure

## What is an Array?
An array is a data structure that stores a fixed-size sequential collection of elements of the same type. It is one of the simplest and most widely used data structures in programming.

## When to Use Arrays
- When you need fast access to elements using an index.
- When the number of elements is known in advance.
- When performing operations like sorting and searching efficiently.
- When memory needs to be allocated contiguously.

---

## Types of Arrays
1. **One-Dimensional Array**: A simple list of elements.
2. **Multi-Dimensional Array**: Arrays with multiple indices (e.g., 2D matrices).
3. **Jagged Array**: Arrays containing arrays of varying lengths.

---

## Basic Operations on Arrays

### 1. Traversal
**Definition:** Accessing each element of an array one by one.

**Algorithm:**
1. Start from the first element.
2. Move through each element using a loop.
3. Print or process each element.

```python
arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    print(arr[i])
```

**Time Complexity:** O(n)

---

### 2. Insertion
**Definition:** Adding an element at a specific index.

**Algorithm:**
1. Shift elements to the right from the given index.
2. Insert the new element.
3. Increase the array size.

**Mathematical Example:**
Insert `25` at index `2` in `[10, 20, 30, 40, 50]`:
```
[10, 20, __, 30, 40, 50]
[10, 20, 25, 30, 40, 50]
```

**Time Complexity:**
- Best Case: O(1) (inserting at the end)
- Worst Case: O(n) (shifting elements)

---

### 3. Deletion
**Definition:** Removing an element from an array.

**Algorithm:**
1. Find the element index.
2. Shift remaining elements left.
3. Reduce the array size.

**Mathematical Example:**
Delete `30` from `[10, 20, 30, 40, 50]`:
```
[10, 20, __, 40, 50]
[10, 20, 40, 50]
```

**Time Complexity:**
- Best Case: O(1) (deleting the last element)
- Worst Case: O(n) (shifting elements)

---

### 4. Searching
**Definition:** Finding an element in an array.

#### **Linear Search**
- Works on unsorted arrays.
- Time Complexity: O(n)

#### **Binary Search**
- Works on sorted arrays.
- Time Complexity: O(log n)

**Example:** Search for `30` in `[10, 20, 30, 40, 50]`:
```
Element found at index 2
```

---

### 5. Sorting
Sorting arranges elements in a specific order (ascending/descending).

#### **Bubble Sort**
- Repeatedly swaps adjacent elements if they are in the wrong order.
- Time Complexity: O(n²)

#### **Quick Sort**
- Uses divide-and-conquer to sort efficiently.
- Time Complexity: O(n log n)

#### **Example:** Sorting `[30, 10, 50, 20, 40]`:
```
Before: [30, 10, 50, 20, 40]
After:  [10, 20, 30, 40, 50]
```

---

## Advantages of Arrays
- Fast access using an index (O(1)).
- Efficient for storing multiple elements of the same type.
- Memory is allocated contiguously.

## Disadvantages of Arrays
- Fixed size (cannot dynamically resize without reallocation).
- Insertion and deletion can be slow (O(n) in worst case).
- Requires contiguous memory allocation.

---

## Conclusion
Arrays are fundamental data structures useful for storing and processing collections of elements efficiently. They serve as the foundation for many other data structures like stacks, queues, and matrices.