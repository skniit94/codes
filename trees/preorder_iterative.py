class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.stack = []

    def preorder_iterative(self, root):
        s = self.stack
        while True:
            while root:
                s.append(root)
                print (root.data, end = ' ')
                root = root.left
            if not s:
                return
            root = s.pop(-1).right

    def preorder(self, root):
        if not root:
            return
        print (root.data, end= ' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder_iterative(self, root):
        s = self.stack
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                return
            root = s.pop(-1)
            print (root.data, end = ' ')
            root = root.right

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print (root.data, end= ' ')
        self.inorder(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.left.right.left = Node(10)
    root.left.left.right.left.right = Node(11)
    s = Solution()
    s.inorder(root)
    print()
    s.inorder_iterative(root)
    print()


if __name__ == '__main__':
    main()