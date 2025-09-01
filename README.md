# Data Structures in Python

A complete, well-tested collection of inicial, basic and advanced **data structures implemented in Python**.  

This repository focuses on clear, understandable Python implementations with:
- short focused modules, each defining one data structure,
- a top-of-file description explaining **what the structure is** and **when is it recommended to use it** 

---

## Goals
- Offer readable, tested implementations that teach core ideas.
- Provide a foundation you can extend (balanced trees, optimized graph algorithms, persistent structures, etc.).

---

## At-a-glance: Structures & When to use them

### Basic
- **Stack (LIFO)**  
  *What it is:* Simple Last-In-First-Out container.  
  *When to use:* Undo systems, recursion elimination, expression evaluation (postfix), DFS helper.  
  *Complexity:* push/pop O(1), peek O(1).

- **Queue (FIFO)**  
  *What it is:* First-In-First-Out container.  
  *When to use:* Task scheduling, BFS, producer-consumer patterns.  
  *Complexity:* enqueue/dequeue O(1).

- **Singly Linked List**  
  *What it is:* Nodes linked forward only.  
  *When to use:* When you need O(1) insertion/removal at head and you don't require random access. Good for streaming-style structures.  
  *Complexity:* insert/delete at head O(1), search/access O(n).

- **Doubly Linked List**  
  *What it is:* Nodes linked both forward and backward.  
  *When to use:* LRU caches, efficient removals when you have node references, deque-like implementations.  
  *Complexity:* removal/insertion O(1) with node reference, search O(n).

- **Hash Table (simple chaining)**  
  *What it is:* Key → bucket mapping using hashing.  
  *When to use:* Fast associative arrays / dictionaries. Use the builtin `dict` for production, but this shows principles.  
  *Complexity:* average insert/search/delete O(1), worst-case O(n) if many collisions.

- **Binary Search Tree (BST)**  
  *What it is:* Ordered binary tree for efficient search.  
  *When to use:* Ordered sets/maps, sorted iteration. Prefer balanced variants (AVL/Red-Black) for guaranteed log-time ops.  
  *Complexity:* average search/insert/delete O(log n), worst-case O(n) (unbalanced).

### Advanced
- **Graph (adjacency list)**  
  *What it is:* Nodes and edges; adjacency list representation.  
  *When to use:* Model networks, relationships, route finding. Implement BFS/DFS, Dijkstra, topological sort, etc.  
  *Complexity:* Traversals O(V + E).

- **Trie (prefix tree)**  
  *What it is:* Tree keyed by characters/parts of keys.  
  *When to use:* Autocomplete, prefix searches, dictionary of strings.  
  *Complexity:* insert/search O(L) where L is key length.

- **Heap (binary heap)**  
  *What it is:* Priority queue backed by a binary heap.  
  *When to use:* Priority scheduling, Dijkstra, heap sort. Use `heapq` in production; this is educational.  
  *Complexity:* push/pop O(log n), peek O(1).

- **Segment Tree (range queries)**  
  *What it is:* Tree to answer range queries and point/range updates efficiently.  
  *When to use:* Range sum/min/max, competitive programming, offline/online queries on arrays.  
  *Complexity:* query/update O(log n).

- **Disjoint Set (Union-Find)**  
  *What it is:* Keeps track of disjoint sets with union and find operations.  
  *When to use:* Kruskal's MST, connectivity queries, grouping problems. Use path compression + union by rank.  
  *Complexity:* amortized almost O(1) per operation (inverse-Ackermann α(n)).

- **Skip List**  
  *What it is:* Probabilistic alternative to balanced trees using layered linked lists.  
  *When to use:* Ordered map/set with probabilistic balancing; good educational comparison to trees.  
  *Complexity:* average O(log n) for search/insert/delete; worst O(n).

---

**Top-of-file template** (copy into each `.py`):
```python
"""
Stack — Last-In-First-Out container.

What it is:
    A simple container with push/pop behavior.

When to use:
    Use when you need LIFO semantics: undo stacks, DFS auxiliary stack, expression evaluation.

Complexities:
    push: O(1)
    pop:  O(1)
    peek: O(1)
"""


