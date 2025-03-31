# Searching Algorithms

## What is Searching?
Searching algorithms are used to find the position of a target value within a data structure, typically an array or list. These algorithms help efficiently retrieve information based on specific conditions.

## When to Use Different Searching Algorithms

1. **Linear Search**: When the dataset is small or unsorted.
2. **Binary Search**: When the dataset is sorted.
3. **Jump Search**: When searching in a large sorted dataset.
4. **Interpolation Search**: When the dataset is sorted and uniformly distributed.

---

## Types of Searching Algorithms

### 1. Linear Search
**Definition:** A simple search algorithm that checks every element sequentially until the target is found.

**Algorithm:**
1. Start from the first element.
2. Compare each element with the target.
3. If a match is found, return the index.
4. If the list ends without a match, return -1.

**Mathematical Example:**
Search for `7` in `[1, 3, 5, 7, 9]`:
```
Index:   0  1  2  3  4
Array:   1  3  5  7  9
Target:       ✓ (found at index 3)
```

**Time Complexity:**
- Worst Case: O(n)
- Best Case: O(1)

---

### 2. Binary Search
**Definition:** A more efficient search algorithm that divides the sorted list into halves until the target is found.

**Algorithm:**
1. Set low and high pointers to the start and end of the array.
2. Compute the middle index.
3. If the middle element is the target, return its index.
4. If the middle element is greater, search in the left half.
5. If the middle element is smaller, search in the right half.

**Mathematical Example:**
Search for `7` in `[1, 3, 5, 7, 9]`:
```
Middle: 5 (index 2), 7 > 5 → Search right
Middle: 7 (index 3), Target found!
```

**Time Complexity:**
- Worst Case: O(log n)
- Best Case: O(1)

---

### 3. Jump Search
**Definition:** A search algorithm that jumps ahead by a fixed step to locate the block containing the target and then performs a linear search within that block.

**Algorithm:**
1. Choose a step size `m = sqrt(n)`.
2. Jump `m` steps until an element is greater than or equal to the target.
3. Perform linear search within the previous block.

**Mathematical Example:**
Search for `7` in `[1, 3, 5, 7, 9]` (step size = `sqrt(5) ≈ 2`):
```
Jump to index 2 → 5 (less than 7)
Jump to index 4 → 9 (greater than 7)
Linear search in block [5, 7] → Found at index 3
```

**Time Complexity:**
- Worst Case: O(√n)
- Best Case: O(1)

---

### 4. Interpolation Search
**Definition:** An improved binary search that estimates the position using interpolation formula rather than dividing the list into halves.

**Algorithm:**
1. Use the formula:
   ```
   pos = low + [(target - arr[low]) * (high - low) / (arr[high] - arr[low])]
   ```
2. If `arr[pos]` is the target, return `pos`.
3. If `arr[pos]` is greater, search the left.
4. If `arr[pos]` is smaller, search the right.

**Mathematical Example:**
Search for `7` in `[1, 3, 5, 7, 9]`:
```
pos = 0 + [(7 - 1) * (4 - 0) / (9 - 1)] ≈ 3
arr[3] = 7 → Found!
```

**Time Complexity:**
- Worst Case: O(n)
- Best Case: O(1)

---

## Conclusion
Each search algorithm has its strengths and weaknesses. The best choice depends on data size, order, and access speed. Understanding these algorithms ensures optimal performance in different scenarios.

