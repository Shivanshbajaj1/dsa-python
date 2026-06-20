# 07. Trees

## Concept

A hierarchical structure: each node has a value and references to child nodes.
A **binary tree** restricts each node to at most two children (left, right).

A **binary search tree (BST)** adds an ordering rule: left subtree < node < right
subtree, which makes search/insert/delete O(log n) on average (O(n) worst case
if the tree becomes a straight line — "unbalanced").

## Traversal types

| Traversal | Order | Use case |
|---|---|---|
| In-order | left, node, right | Gives sorted order for a BST |
| Pre-order | node, left, right | Copying/serializing a tree |
| Post-order | left, right, node | Deleting a tree, evaluating expression trees |
| Level-order (BFS) | level by level | Shortest path in unweighted tree, level-based logic |

## Files

- `01_binary_tree.py` — BST implementation: insert, search, all four traversals,
  height, and a balance check
