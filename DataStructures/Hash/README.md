# Hash Data Structure

## What is a Hash Table?
A **hash table** (or hash map) is a data structure that stores key-value pairs. It uses a **hash function** to compute an index (or hash code) where the value is stored, allowing for fast insertion, deletion, and lookup operations.

## When to Use Hash Tables
- When quick lookups, insertions, and deletions are required.
- When implementing associative arrays (dictionaries, symbol tables).
- When solving problems that require counting occurrences (frequency tables).
- When handling large datasets efficiently.

---

## Key Concepts of Hash Tables

### 1. Hash Function
A function that maps a given key to an index in the table.

**Example Hash Function:**
```python
hash_index = key % table_size
```
If `table_size = 10` and `key = 25`:
```
index = 25 % 10 = 5
```

### 2. Collision Handling
When two keys hash to the same index, a collision occurs. There are several ways to handle this:
- **Chaining:** Use a linked list at each index.
- **Open Addressing:** Find the next available slot (linear probing, quadratic probing, double hashing).

---

## Types of Hashing Techniques

### 1. **Direct Hashing**
- Uses the key itself as the index.
- Works when keys are small and sequential.

### 2. **Modulo-Division Hashing**
- Uses `key % table_size` to determine the index.
- Effective for distributing keys uniformly.

### 3. **Multiplication Hashing**
- Uses a multiplication constant to generate a hash.

### 4. **Universal Hashing**
- Uses a randomly chosen hash function to minimize collisions.

---

## Basic Operations on Hash Tables

### 1. Insertion
**Definition:** Adds a key-value pair.

**Algorithm:**
1. Compute the hash index using a hash function.
2. If no collision, insert the value.
3. If a collision occurs, handle it using chaining or open addressing.

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = key % self.size
        self.table[index].append((key, value))
```

**Time Complexity:** O(1) (average case), O(n) (worst case with collisions).

---

### 2. Deletion
**Definition:** Removes a key-value pair.

**Algorithm:**
1. Compute the hash index.
2. Find the key in the index and remove it.

```python
    def delete(self, key):
        index = key % self.size
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
```

**Time Complexity:** O(1) (average case), O(n) (worst case).

---

### 3. Search
**Definition:** Finds the value for a given key.

**Algorithm:**
1. Compute the hash index.
2. Check if the key exists at that index.

```python
    def search(self, key):
        index = key % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
```

**Time Complexity:** O(1) (average case), O(n) (worst case with collisions).

---

## Example of Hash Table Operations

Consider a hash table of size `10` and inserting keys `[15, 25, 35]`:

```
Index  | Data
-----------------
  5    | [(15, value1), (25, value2), (35, value3)]
```
1. **Insert(45, value4)** → Collision at index `5`, stored using chaining.
2. **Search(25)** → Returns `value2`.
3. **Delete(15)** → Removes `value1` from index `5`.

---

## Advantages of Hash Tables
- Fast O(1) average time complexity for insert, delete, and search.
- Efficient memory usage when well-designed.
- Ideal for large datasets and associative arrays.

## Disadvantages of Hash Tables
- Performance degrades with excessive collisions.
- Requires a good hash function to avoid clustering.
- Inefficient for ordered data retrieval.

---

## Conclusion
Hash tables provide efficient key-value storage, making them a fundamental data structure in computer science. Choosing an appropriate hash function and collision handling technique is crucial for optimal performance.