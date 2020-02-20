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
b1 = add_node(b1, 5)
b1 = add_node(b1, 9)
b1 = add_node(b1, 0)
b1 = add_node(b1, 3)
b1 = add_node(b1, 7)
b1 = add_node(b1, 6)
b1 = add_node(b1, 20)

b2 = BST(10)
b2 = add_node(b2, 5)
b2 = add_node(b2, 9)
b2 = add_node(b2, 0)
b2 = add_node(b2, 3)
b2 = add_node(b2, 7)
b2 = add_node(b2, 6)
b2 = add_node(b2, 20)
print('Equal?', check(b1, b2))

