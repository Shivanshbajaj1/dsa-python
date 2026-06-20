"""
02. Linked Lists — implementation + classic patterns.
Run directly: python 01_singly_linked_list.py
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add to the end. O(n) for a singly linked list without a tail pointer."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """Add to the front. O(1)."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        """Reverse the list in place. O(n) time, O(1) space."""
        prev = None
        current = self.head
        while current:
            next_node = current.next   # save before overwriting
            current.next = prev        # flip the pointer
            prev = current
            current = next_node
        self.head = prev
        return self

    def find_middle(self):
        """Fast/slow pointers: when fast hits the end, slow is at the middle."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def has_cycle(self):
        """Floyd's cycle detection. If fast ever equals slow, there's a cycle."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def nth_from_end(self, n):
        """Two pointers, n apart. When the lead pointer hits the end, the
        trailing pointer is at the nth node from the end."""
        lead = self.head
        for _ in range(n):
            if not lead:
                return None
            lead = lead.next

        trail = self.head
        while lead:
            lead = lead.next
            trail = trail.next
        return trail.value if trail else None


if __name__ == "__main__":
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)

    print("list:", ll.to_list())
    print("middle:", ll.find_middle())
    print("2nd from end:", ll.nth_from_end(2))
    print("reversed:", ll.reverse().to_list())
    print("has_cycle:", ll.has_cycle())
