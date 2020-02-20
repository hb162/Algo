class BST:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def add_node(node, value):
    if node is None:
        return BST(value)
    if value < node.value:
        node.left = add_node(node.left, value)
    else:
        node.right = add_node(node.right, value)
    return node


def left_most_child(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def remove_node(root, value):
    if root is None:
        return root
    if root.value > value:
        root.left = remove_node(root.left, value)
    elif root.value < value:
        root.right = remove_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = left_most_child(root.right)
        root.value = temp.value
        root.right = remove_node(root.right, temp.value)
    return root


def preorder(root):
    if root is not None:
        print(root.value)
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value)


def lca(root, n1, n2):  # tìm gốc chung gần nhất
    if root is None:
        return None
    if root.value == n1 or root.value == n2:
        return root
    tree_left = lca(root.left, n1, n2)
    tree_right = lca(root.right, n1, n2)
    if tree_left is not None and tree_right is not None:
        return root
    if tree_left is not None:
        return tree_left
    else:
        return tree_right


def find_level(root, value, distance, level):
    if root is None:
        return None
    if root.value == value:
        distance.append(level)
        return level
    find_level(root.left, value, distance, level + 1)
    find_level(root.right, value, distance, level + 1)


def find_length(root, n1, n2):
    ancestor = lca(root, n1, n2)
    distance1 = []
    distance2 = []
    if ancestor is not None:
        find_level(ancestor, n1, distance1, 0)
        find_level(ancestor, n2, distance2, 0)
        return distance1[0] + distance2[0]
    else:
        return None


b = BST(10)
b = add_node(b, 5)
b = add_node(b, 9)
b = add_node(b, 0)
b = add_node(b, 3)
b = add_node(b, 7)
b = add_node(b, 6)
b = add_node(b, 20)
print('before:')
preorder(b)
b = remove_node(b, 5)
print('after:')
preorder(b)
print('length:', find_length(b, 0, 9))
