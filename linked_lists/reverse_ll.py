
class node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class llist(object):
    def __init__(self, node):
        self.head = node
        self.end = node

    def add(self, node):
        self.end.next = node
        self.end = node

    def printll(self):
        head = self.head

        while(head):
            print(head.data),
            head = head.next
        print

    def reverse_util(self, prev, curr):

        if not curr.next:
            curr.next = prev
            prev.next = None
            return curr

        head = self.reverse_util(curr, curr.next)
        curr.next = prev
        prev.next = None
        return head

    def reversell1(self):

        if not self.head or not self.head.next:
            return
        self.head = self.reverse_util(self.head, self.head.next)

    def reversell2(self):
        t1 = None

        while self.head:
            t2 = self.head.next
            self.head.next = t1
            t1 = self.head
            self.head = t2

        self.head = t1


def main():
    head = node(1)
    ll = llist(head)
    # ll.add(node(2))
    # ll.add(node(3))
    # ll.add(node(4))
    # ll.add(node(5))

    ll.printll()
    ll.reversell1()
    ll.printll()


if __name__ == "__main__":
    main()