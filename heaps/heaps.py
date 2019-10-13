class maxheap(object):

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def heapify(self, i, n):
        l = 2*i + 1
        r = 2*i + 2
        m = i
        if l < n and self.arr[l] > self.arr[m]:
            m = l
        if r < n and self.arr[r] > self.arr[m]:
            m = r
        if m != i:
            self.arr[m], self.arr[i] = self.arr[i], self.arr[m]
            self.heapify(m, n)

    def build(self):
        for i in range(int(self.n/2)-1, -1, -1):
            self.heapify(i, self.n)

    def sort(self):
        self.build()
        for i in range(self.n-1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.heapify(0, i)


class priorityqueue(maxheap):

    def __init__(self):
        super().__init__([])

    def maximum(self):
        if not self.n:
            return
        return self.arr[0]

    def ext_max(self):
        if not self.n:
            return
        m = self.arr[0]
        self.arr[0] = self.arr[self.n-1]
        self.n-= 1
        self.heapify(0, self.n)
        return m

    def increase_val(self, i, val):
        if val < self.arr[i]:
            return
        self.arr[i] = val
        p = int((i-1)/2)
        while p >= 0 and self.arr[i] > self.arr[p]:
            self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            i = p
            p = int((i-1)/2)


    def insert_val(self, val):

        self.arr.append(val)
        self.n +=1
        self.increase_val(self.n - 1, val)



def main():
    # heap = maxheap([8, 3, 7, 9, 6, 5, 4, 2, 1])
    # print (heap.arr)
    # heap.build()
    # print (heap.arr)
    # heap.sort()
    # print (heap.arr)

    q = priorityqueue()
    print (q.maximum())
    print (q.ext_max())

    q.insert_val(4)
    print (q.arr)
    q.insert_val(8)
    print (q.arr)
    q.insert_val(1)
    print (q.arr)
    q.insert_val(7)
    print (q.arr)
    q.insert_val(3)
    print (q.arr)
    q.increase_val(3, 9)
    print (q.arr)


if __name__ == "__main__":
    main()