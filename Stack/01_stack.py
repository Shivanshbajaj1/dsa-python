"""
03. Stacks — implementation + a real use case.
Run directly: python 01_stack.py
"""


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


def is_balanced(expression):
    """
    Classic stack use case: check that every bracket in `expression`
    is properly opened and closed in the right order.
    e.g. "{[()]}" -> True, "{[(])}" -> False
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


def evaluate_postfix(tokens):
    """
    Evaluate a postfix (Reverse Polish Notation) expression using a stack.
    e.g. ["2", "1", "+", "3", "*"] means (2 + 1) * 3 = 9
    """
    stack = Stack()
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    for token in tokens:
        if token in ops:
            b = stack.pop()  # note: pop order matters for - and /
            a = stack.pop()
            stack.push(ops[token](a, b))
        else:
            stack.push(float(token))

    return stack.pop()


if __name__ == "__main__":
    print("is_balanced('{[()]}'):", is_balanced("{[()]}"))
    print("is_balanced('{[(])}'):", is_balanced("{[(])}"))
    print("evaluate_postfix:", evaluate_postfix(["2", "1", "+", "3", "*"]))
