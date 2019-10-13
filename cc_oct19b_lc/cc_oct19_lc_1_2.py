class Node(object):
    def __init__(self, val, ind):
        self.val = val
        self.ind = ind
        self.prev = None
        self.next = None


class Queue(object):
    def __init__(self):
        self.start = None
        self.end = None

    def push(self, node):
        if not self.end:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node

    def pop_front(self):
        if self.start:
            self.start = self.start.next

    def pop_back(self):
        if self.end:
            self.end = self.end.prev

    def print_queue(self):
        temp = self.start
        while temp:
            print (temp.val,end=' ')
            temp = temp.next
        print()

    def __bool__(self):
        if self.start:
            return True
        return False

class Solution(object):
    def __init__(self, arr, length):
        self.arr = arr
        self.n = length

    def get_good_numbers(self):
        a = self.arr
        q = Queue()
        c = 0
        for i in range(0, self.n):
            if not q:
                q.push(Node(a[i], i))
                c += 1
            elif  a[i] < q.start.val:
                q.start = q.end = Node(a[i], i)
                c+=1
            else:
                while a[i] < q.end.val:
                    q.pop_back()
                q.push(Node(a[i], i))

            if i - q.start.ind == 5:
                q.pop_front()

        return c


def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        a = list(map(int, input().split(' ')))
        print( Solution(a, n).get_good_numbers())

if __name__ == '__main__':
    main()