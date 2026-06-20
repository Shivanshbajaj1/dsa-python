# 02. Linked Lists

## Concepts

A **linked list** is a chain of nodes, each holding a value and a pointer to the next node.
Unlike arrays, elements are *not* contiguous in memory.

| Operation | Array | Linked List |
|---|---|---|
| Access by index | O(1) | O(n) |
| Insert/delete at front | O(n) | O(1) |
| Insert/delete at known node | O(n) | O(1) |
| Search | O(n) | O(n) |

## Why use one?

Cheap insert/delete at the front or middle (once you have a reference to the node),
no need to pre-allocate size. Used to build stacks, queues, hash map buckets, and
LRU caches.

## Key technique: fast & slow pointers

Two pointers moving at different speeds through the list. Used to:
- detect a cycle (Floyd's algorithm)
- find the middle node in one pass
- find the Nth node from the end

## Files

- `01_singly_linked_list.py` — Node/LinkedList classes + the patterns above
- `02_exercises.py` — practice problems
