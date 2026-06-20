"""
02. Linked Lists — Exercises
Fill in each TODO using the Node class below (don't import from 01_*).
Run this file to check your work.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_list(values):
    """Helper: build a linked list from a Python list. Already implemented for you."""
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_python_list(head):
    """Helper: convert a linked list back to a Python list for easy comparison."""
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def remove_duplicates(head):
    """
    Remove duplicate values from a linked list (keep first occurrence),
    return the new head. O(n) time using a set.
    e.g. 1->2->2->3->1  =>  1->2->3
    """
    # TODO: implement
    pass


def merge_two_sorted_lists(head1, head2):
    """
    Merge two already-sorted linked lists into one sorted linked list.
    Return the new head. O(n + m) time.
    """
    # TODO: implement
    pass


def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end of the list (1-indexed) and return
    the new head. Do it in a single pass using two pointers.
    e.g. 1->2->3->4->5, n=2  =>  1->2->3->5
    """
    # TODO: implement
    pass


def run_tests():
    tests = [
        ("remove_duplicates", remove_duplicates, build_list([1, 2, 2, 3, 1]), [1, 2, 3]),
        ("merge_two_sorted_lists", lambda: merge_two_sorted_lists(build_list([1, 3, 5]), build_list([2, 4, 6])), None, [1, 2, 3, 4, 5, 6]),
        ("remove_nth_from_end", lambda: remove_nth_from_end(build_list([1, 2, 3, 4, 5]), 2), None, [1, 2, 3, 5]),
    ]

    for name, func, arg, expected in tests:
        try:
            result_head = func(arg) if arg is not None else func()
            result = to_python_list(result_head)
            status = "PASS" if result == expected else f"FAIL (got {result})"
        except Exception as e:
            status = f"ERROR ({e})"
        print(f"{name:30s} -> {status}")


if __name__ == "__main__":
    run_tests()
