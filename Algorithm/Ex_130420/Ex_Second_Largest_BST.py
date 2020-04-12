"""
Given the root to a binary search tree,
find the second largest node in the tree.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root


def find_max(root):
    while root.right is not None:
        root = root.right
    return root.data


def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        return None
    if root.left and not root.right:
        return find_max(root.left)
    if (root.right and
            not root.right.left and
            not root.right.right):
        return root.value
    return find_second_largest(root.right)


root = None
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
# print(find_max(root))
print(find_second_largest(root))

"""
Độ phức tạp: O(h), h là chiều cao của cây.
"""



