class BST:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def add_node(root, node):
    if root is None:
        root = node
    if root.value < node.value:
        if root.right is None:
            root.right = node
        else:
            add_node(root.right, node)
    elif root.value > node.value:
        if root.left is None:
            root.left = node
        else:
            add_node(root.left, node)


def check(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is not None and tree2 is not None:
        if tree1.value == tree2.value and check(tree1.left, tree2.left) and check(tree1.right, tree2.right):
            return True
    return False


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


b1 = BST(10)
add_node(b1, BST(1))
add_node(b1, BST(4))
add_node(b1, BST(6))
add_node(b1, BST(7))
add_node(b1, BST(3))
add_node(b1, BST(8))
add_node(b1, BST(20))

b2 = BST(10)
add_node(b2, BST(1))
add_node(b2, BST(4))
add_node(b2, BST(6))
add_node(b2, BST(7))
add_node(b2, BST(3))
add_node(b2, BST(8))
add_node(b2, BST(20))
print('Equal?', check(b1, b2))

