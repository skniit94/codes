import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def is_bst(node, l, u):

    if not node:
        return True
    if node.data > l and node.data < u:
        return is_bst(node.left, l, node.data) and is_bst(node.right, node.data, u)
    return False


def check_bst(root):

    if is_bst(root, -sys.maxsize - 1, sys.maxsize):
        return 1
    return 0


def main():
    root = Node(5)
    root.left = Node(7)
    root.right = Node(3)

    print (check_bst(root))


if __name__ == "__main__":
    main()