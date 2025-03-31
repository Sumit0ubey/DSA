# Sorting Algorithms

## What is Sorting?
Sorting is the process of arranging elements in a specific order, typically in ascending or descending order. Sorting is widely used in searching, databases, and optimizing algorithms.

## When to Use Sorting Algorithms
- When searching for elements efficiently.
- When organizing large datasets.
- When preparing data for further processing (e.g., removing duplicates).
- When optimizing algorithms that require sorted input.

---

## Types of Sorting Algorithms

### 1. Bubble Sort
- **Concept:** Repeatedly swaps adjacent elements if they are in the wrong order.
- **Time Complexity:** O(n²) (worst & average case), O(n) (best case if already sorted).
- **Best Used When:** Small datasets or nearly sorted arrays.

**Algorithm:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

### 2. Selection Sort
- **Concept:** Repeatedly selects the smallest element and places it at the beginning.
- **Time Complexity:** O(n²) for all cases.
- **Best Used When:** Small datasets.

**Algorithm:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

---

### 3. Insertion Sort
- **Concept:** Builds the sorted array one element at a time by inserting elements into their correct position.
- **Time Complexity:** O(n²) (worst case), O(n) (best case if already sorted).
- **Best Used When:** Small datasets or nearly sorted arrays.

**Algorithm:**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

---

### 4. Merge Sort (Divide and Conquer)
- **Concept:** Splits the array into halves, sorts them, and merges them back.
- **Time Complexity:** O(n log n) for all cases.
- **Best Used When:** Large datasets requiring stable sorting.

**Algorithm:**
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```

---

### 5. Quick Sort (Divide and Conquer)
- **Concept:** Selects a pivot and partitions the array around it.
- **Time Complexity:** O(n log n) (average case), O(n²) (worst case when poorly chosen pivot).
- **Best Used When:** Large datasets with random order.

**Algorithm:**
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

### 6. Heap Sort
- **Concept:** Uses a binary heap structure to sort elements.
- **Time Complexity:** O(n log n) for all cases.
- **Best Used When:** Priority queues and large datasets.

**Algorithm:**
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

---

## Comparison of Sorting Algorithms
| Algorithm       | Best Case | Average Case | Worst Case | Stable | In-Place |
|----------------|-----------|-------------|------------|--------|----------|
| Bubble Sort    | O(n)      | O(n²)       | O(n²)      | Yes    | Yes      |
| Selection Sort | O(n²)     | O(n²)       | O(n²)      | No     | Yes      |
| Insertion Sort | O(n)      | O(n²)       | O(n²)      | Yes    | Yes      |
| Merge Sort     | O(n log n)| O(n log n)  | O(n log n) | Yes    | No       |
| Quick Sort     | O(n log n)| O(n log n)  | O(n²)      | No     | Yes      |
| Heap Sort      | O(n log n)| O(n log n)  | O(n log n) | No     | Yes      |

---

## Conclusion
Sorting algorithms are essential in computer science, each with unique strengths and weaknesses. Choosing the right algorithm depends on the dataset size, stability requirements, and performance considerations.
