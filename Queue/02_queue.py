"""
03. Queues — implementation + a real use case.
Run directly: python 02_queue.py
"""

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()  # O(1) append/popleft, unlike a plain list

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


def round_robin_scheduler(tasks, time_slice):
    """
    Simulate a round-robin CPU scheduler: each task in the queue gets
    `time_slice` units of work; if not finished, it goes to the back
    of the queue. Returns the order tasks complete in.
    tasks: list of (name, total_time) tuples.
    """
    q = Queue()
    for task in tasks:
        q.enqueue(list(task))  # [name, remaining_time]

    completion_order = []
    while not q.is_empty():
        name, remaining = q.dequeue()
        worked = min(time_slice, remaining)
        remaining -= worked
        if remaining > 0:
            q.enqueue([name, remaining])
        else:
            completion_order.append(name)

    return completion_order


if __name__ == "__main__":
    q = Queue()
    for v in [1, 2, 3]:
        q.enqueue(v)
    print("dequeue order:", [q.dequeue() for _ in range(3)])

    tasks = [("A", 5), ("B", 3), ("C", 8)]
    print("scheduler completion order:", round_robin_scheduler(tasks, time_slice=2))
