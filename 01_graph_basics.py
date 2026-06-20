# 08. Graphs

## Concept

A set of **nodes (vertices)** connected by **edges**. Generalizes trees — a graph
can have cycles, disconnected parts, and edges can be directed or weighted.

## Representations

- **Adjacency list** (most common): `{node: [neighbors]}` — space-efficient for
  sparse graphs, what we use here.
- **Adjacency matrix**: 2D grid of 0/1 (or weights) — O(1) edge lookup but O(V²) space.

## BFS vs DFS

| | Data structure | Use case |
|---|---|---|
| BFS (Breadth-First Search) | Queue | Shortest path in an unweighted graph |
| DFS (Depth-First Search) | Stack (or recursion) | Path existence, cycle detection, topological sort |

## Files

- `01_graph_basics.py` — adjacency-list Graph class with BFS, DFS, shortest path,
  and cycle detection
