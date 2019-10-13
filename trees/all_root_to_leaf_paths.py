class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.stack = []

    def print_paths(self, root):
        s = self.stack
        if not root:
            return
        s.append(root)
        self.print_paths(root.left)
        self.print_paths(root.right)

        if not root.left and not root.right:
            self.print_stack()

        s.pop(-1)

    def print_stack(self):
        for i in self.stack:
            print (i.data, end = ' ')
        print()

    def preorder(self, root):
        if not root:
            return
        print (root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

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
    # s.preorder(root)
    # print()
    s.print_paths(root)


if __name__ == '__main__':
    main()