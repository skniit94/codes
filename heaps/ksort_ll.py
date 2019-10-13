class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):

    def ksort(self, a):

        self.build_heap(a)
        self.print_arr(a)
        head = a[0]
        temp = head
        while a:
            if a[0].next:
                a[0] = a[0].next
                self.heapify(0, a)
                temp.next = a[0]
            else:
                a.pop(0)
                if a:
                    self.heapify(0, a)
                    temp.next = a[0]

            temp = temp.next
            self.print_ll(head)
            self.print_arr(a)
        return head

    def heapify(self, i, a):

        l = 2*i + 1
        r = 2*i + 2
        al = len(a)
        m = i
        if l < al and a[m].val > a[l].val:
            m = l

        if (r < al and a[m].val > a[r].val):
            m = r

        if (m != i):
            a[m], a[i] = a[i], a[m]
            self.heapify(m, a)

    def build_heap(self, a):

        for i in range(int(len(a)/2)-1, -1, -1):
            self.heapify(i, a)

    @staticmethod
    def print_ll(h):
        print('ll')
        while h:
            print (h.val, end = ' ')
            h = h.next
        print()

    @staticmethod
    def print_arr(a):
        print ('arr')
        for i in a:
            print (i.val, end = ' ')
        print()


def main():
    h1 = Node(1)
    h1.next = Node(4)
    h1.next.next = Node(7)

    h2 = Node(2)
    h2.next = Node(5)
    h2.next.next = Node(8)

    h3 = Node(6)
    h3.next = Node(9)
    h3.next.next = Node(11)

    s = Solution()
    head = s.ksort([h2])
    s.print_ll(head)


if __name__ == "__main__":
    main()



