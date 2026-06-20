# Queues


## Queue — FIFO (First In, First Out)

Think: a line at a checkout. First person in line is served first.

| Operation | Complexity |
|---|---|
| enqueue (add to back) | O(1) |
| dequeue (remove from front) | O(1) (with the right data structure) |

Used for: BFS, task scheduling, buffering/streaming data.

> ⚠️ A Python `list` makes a fine stack (`append`/`pop`), but a **bad** queue —
> `list.pop(0)` is O(n). Use `collections.deque` for queues instead.

## Files
- `02_queue.py` — queue implementation + a simple task scheduler example
