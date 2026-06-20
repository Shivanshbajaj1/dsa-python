# 03. Stacks & Queues

## Stack — LIFO (Last In, First Out)

Think: a stack of plates. You add/remove from the top only.

| Operation | Complexity |
|---|---|
| push (add to top) | O(1) |
| pop (remove from top) | O(1) |
| peek (look at top) | O(1) |

Used for: undo/redo, function call stacks, expression evaluation, DFS, matching brackets.

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

- `01_stack.py` — stack implementation + balanced-brackets checker
- `02_queue.py` — queue implementation + a simple task scheduler example
