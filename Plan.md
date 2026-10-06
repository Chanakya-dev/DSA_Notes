```text
DATA STRUCTURE
      ↓
Understand the DS
      ↓
Operations
      ↓
Techniques applicable to that DS
      ↓
Algorithms using those techniques
      ↓
Problems
```

# The DSA Learning Architecture

For every Data Structure, we follow the same learning cycle:

```text
1. Understand the Data Structure
          ↓
2. Understand its operations
          ↓
3. Understand its strengths / weaknesses
          ↓
4. Learn techniques used with it
          ↓
5. Learn algorithms built around it
          ↓
6. Solve problems
          ↓
7. Learn how to recognize when to use it
```

For example:

```text
ARRAY
 │
 ├── Basic operations
 │
 ├── Techniques
 │      ├── Two Pointers
 │      ├── Sliding Window
 │      ├── Prefix Sum
 │      ├── Difference Array
 │      ├── Kadane
 │      └── etc.
 │
 ├── Algorithms
 │      ├── Binary Search
 │      ├── Merge Sort
 │      ├── Quick Sort
 │      └── etc.
 │
 └── Problems
```

That's much more natural.

---

# Our DSA Roadmap

## 1. Arrays

First master:

### Data Structure

```text
Array
```

Learn:

- memory representation
- indexing
- traversal
- insertion
- deletion
- searching
- updating
- fixed size
- time/space complexity

### Techniques

Then:

```text
Traversal
Frequency Counting
Two Pointers
Sliding Window
Prefix Sum
Difference Array
Sorting + Array
Binary Search
Kadane's Algorithm
Dutch National Flag
Cyclic Sort
Boyer-Moore Voting
```

### Algorithms

Then:

```text
Linear Search
Binary Search
Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
Counting Sort
```

### Problems

Finally:

```text
Easy
→ Medium
→ Hard
```

But while solving, the focus is:

> **Why did I choose this technique?**

---

# 2. Strings

Then move to:

```text
STRING
```

### Data Structure concepts

```text
String
Character array
StringBuilder
StringBuffer
immutability
```

### Techniques

```text
Two Pointers
Sliding Window
Frequency Counting
Hashing
String Traversal
Palindrome techniques
```

### Algorithms

```text
String Matching
KMP
Rabin-Karp
Z Algorithm
Manacher's Algorithm
```

You don't need KMP/Manacher immediately.

We'll divide them into:

```text
Core
Intermediate
Advanced
```

---

# 3. Hashing

Then:

```text
HASHING
```

Learn:

```text
HashMap
HashSet
Hash Function
Collision concept
Frequency Map
Lookup
Grouping
Counting
```

Techniques:

```text
Frequency Counting
Seen Before
Complement Lookup
Prefix Sum + HashMap
Hashing + Sliding Window
Hashing + Two Pointers
```

Algorithms/problems:

```text
Two Sum
Longest Consecutive Sequence
Group Anagrams
Subarray Sum
Longest Subarray
```

Now you start seeing something important:

> A data structure doesn't necessarily have only one technique.

For example:

```text
HashMap
   ↓
Frequency Counting
   ↓
Prefix Sum + HashMap
   ↓
Sliding Window + HashMap
   ↓
Many different algorithms
```

---

# 4. Linked List

Then:

```text
LINKED LIST
```

### Data structure

```text
Node
Head
Tail
Next
Traversal
Insertion
Deletion
```

### Techniques

```text
Two Pointers
Fast & Slow Pointer
Dummy Node
Reverse Traversal
In-place manipulation
```

### Algorithms

```text
Reverse Linked List
Cycle Detection
Merge Two Lists
Find Middle
Find Nth From End
Intersection
Merge Sort on Linked List
```

Notice how **Two Pointers comes back**.

That's important.

We don't learn:

> "Two Pointers chapter is finished forever."

Instead:

> "I learned Two Pointers, and now I recognize where it applies."

---

# 5. Stack

```text
STACK
```

### Data Structure

```text
push
pop
peek
isEmpty
```

### Techniques

```text
Monotonic Stack
Previous Element
Next Element
Expression Processing
```

### Algorithms

```text
Next Greater Element
Previous Greater Element
Next Smaller Element
Stock Span
Largest Rectangle in Histogram
```

---

# 6. Queue / Deque

```text
QUEUE
   ↓
DEQUE
```

Learn:

```text
FIFO
enqueue
dequeue
front
rear
```

Techniques:

```text
BFS
Sliding Window Maximum
Monotonic Queue
```

Algorithms:

```text
BFS
Shortest path in unweighted graph
Sliding Window Maximum
```

---

# 7. Heap / Priority Queue

```text
HEAP
```

Learn:

```text
Min Heap
Max Heap
Heapify
Insert
Delete
Peek
```

Techniques:

```text
Top K
K-way merge
Repeated min/max
Two heaps
```

Algorithms:

```text
Heap Sort
Kth Largest
Kth Smallest
Median of Stream
Merge K Sorted Lists
```

---

# 8. Trees

Now we enter hierarchical data.

```text
TREE
```

### Data Structure

```text
Node
Root
Leaf
Parent
Child
Height
Depth
Subtree
```

### Techniques

```text
DFS
BFS
Recursion
Backtracking
Two Pointers-style traversal
```

### Algorithms

```text
Preorder
Inorder
Postorder
Level Order
Height
Diameter
LCA
Path Sum
Tree Views
Serialization
```

Then:

```text
BINARY SEARCH TREE
```

Techniques:

```text
Inorder property
Binary Search
DFS
```

Algorithms:

```text
Search
Insert
Delete
Successor
Predecessor
LCA
```

---

# 9. Graph

Then:

```text
GRAPH
```

### Data Structure

```text
Vertex
Edge
Directed
Undirected
Weighted
Unweighted
Adjacency List
Adjacency Matrix
```

### Techniques

```text
DFS
BFS
Visited tracking
Topological reasoning
Union-Find
Relaxation
```

### Algorithms

```text
BFS
DFS
Dijkstra
Bellman-Ford
Floyd-Warshall
Kruskal
Prim
Kahn's Algorithm
Kosaraju
Tarjan
```

This is where the distinction between **technique** and **algorithm** becomes very useful.

For example:

```text
Graph
  ↓
BFS technique
  ↓
Shortest Path in Unweighted Graph
```

or:

```text
Graph
  ↓
DFS
  ↓
Cycle Detection
```

or:

```text
Graph
  ↓
Union-Find
  ↓
Kruskal
  ↓
Minimum Spanning Tree
```

---

# 10. Trie

```text
TRIE
```

Learn:

```text
Node
Children
End-of-word
Insertion
Search
Prefix Search
```

Techniques:

```text
Prefix-based traversal
DFS
Backtracking
```

Algorithms/problems:

```text
Autocomplete
Word Search
Prefix Matching
Word Dictionary
```

---

# 11. Disjoint Set / Union-Find

```text
DISJOINT SET
```

Learn:

```text
Parent
Find
Union
Path Compression
Union by Rank
Union by Size
```

Then algorithms:

```text
Cycle Detection
Connected Components
Kruskal MST
Dynamic Connectivity
```

---

# 12. Advanced Data Structures

After the core structures:

```text
Segment Tree
Fenwick Tree / BIT
Sparse Table
Ordered Set / Tree
```

These are much later.

---

# Where Does Recursion / Backtracking / Greedy / DP Go?

This is the only modification I'd make to your idea.

They aren't really data structures.

They're **problem-solving techniques/paradigms**.

So we keep a separate final section:

```text
DATA STRUCTURES
        +
TECHNIQUES
        +
ALGORITHMIC PARADIGMS
```

The paradigms are:

```text
Recursion
Divide & Conquer
Backtracking
Greedy
Dynamic Programming
Bit Manipulation
```

But we learn them **after we have enough data structures to make them meaningful**.

---

# So Your Complete Structure Becomes

```text
                    DSA
                     │
          ┌──────────┴──────────┐
          │                     │
    DATA STRUCTURES       ALGORITHMIC PARADIGMS
          │                     │
          │              Recursion
          │              Divide & Conquer
          │              Backtracking
          │              Greedy
          │              Dynamic Programming
          │
          ├── Array
          │    ├── Techniques
          │    ├── Algorithms
          │    └── Problems
          │
          ├── String
          │    ├── Techniques
          │    ├── Algorithms
          │    └── Problems
          │
          ├── Hashing
          │    ├── Techniques
          │    ├── Algorithms
          │    └── Problems
          │
          ├── Linked List
          │    ├── Techniques
          │    ├── Algorithms
          │    └── Problems
          │
          ├── Stack
          │    ├── Techniques
          │    ├── Algorithms
          │    └── Problems
          │
          ├── Queue / Deque
          │
          ├── Heap
          │
          ├── Tree
          │
          ├── BST
          │
          ├── Graph
          │
          ├── Trie
          │
          └── Union-Find
```
