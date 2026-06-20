"""
07. Trees — Binary Search Tree implementation + traversals.
Run directly: python 01_binary_tree.py
"""
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """O(log n) average, O(n) worst case (unbalanced tree)."""
        if not self.root:
            self.root = TreeNode(value)
            return
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Return True if value exists in the tree. O(log n) average."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def in_order(self):
        """Left, node, right. For a BST this yields sorted order."""
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)

    def pre_order(self):
        """Node, left, right."""
        result = []
        self._pre_order(self.root, result)
        return result

    def _pre_order(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)

    def post_order(self):
        """Left, right, node."""
        result = []
        self._post_order(self.root, result)
        return result

    def _post_order(self, node, result):
        if node:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.value)

    def level_order(self):
        """Breadth-first: level by level, using a queue."""
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self):
        """Number of edges on the longest root-to-leaf path. Empty tree = -1."""
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))


if __name__ == "__main__":
    bst = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)

    print("in_order (sorted):", bst.in_order())
    print("pre_order:", bst.pre_order())
    print("post_order:", bst.post_order())
    print("level_order (BFS):", bst.level_order())
    print("search(60):", bst.search(60))
    print("search(99):", bst.search(99))
    print("height:", bst.height())
