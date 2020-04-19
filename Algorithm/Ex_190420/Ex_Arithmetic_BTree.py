"""
You are given a binary tree representation of an arithmetic expression.
In this tree, each leaf is an integer value, and a non-leaf node is of one of the four operations '+', '-', '*' or '/'

Write a function that takes this tree and evaluates the expression
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def evaluate(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.val)

    left = evaluate(root.left)
    right = evaluate(root.right)

    if root.val == PLUS:
        return left + right
    elif root.val == MINUS:
        return left - right
    elif root.val == TIMES:
        return left * right
    else:
        return left / right


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))

"""
Độ phức tạp: O(1)
"""
