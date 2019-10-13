class Window(object):

    def __init__(self, max_size):
        self.store = []
        self.store_info = {}
        self.values = []
        self.max_size = max_size
        self.curr_size = 0

    def add(self, val):
        rem = None
        if self.curr_size == self.max_size:
            rem = self.values.pop(0)
            self.values.append(val)
        else:
            self.values.append(val)
            self.curr_size += 1

        if rem:
            # i = self.store_info[rem]
            for i in range(0, self.max_size):
                if self.store[i] == rem:
                    break
            # self.store_info[val] = i
            if self.store[i] > val:
                self.store[i] = val
                p = int((i - 1) / 2)
                while p >= 0 and self.store[i] < self.store[p]:
                    # self.store_info[self.store[i]], self.store_info[self.store[p]] = self.store_info[self.store[p]], \
                    #                                                                  self.store_info[self.store[i]]
                    self.store[i], self.store[p] = self.store[p], self.store[i]
                    i = p
                    p = int((i - 1) / 2)
            else:
                self.store[i] = val
                self.heapify(i)
        else:
            self.store.append(val)
            i = self.curr_size - 1
            # self.store_info[val] = i
            p = int((i - 1) / 2)
            while p >= 0 and self.store[i] < self.store[p]:
                # self.store_info[self.store[i]], self.store_info[self.store[p]] = self.store_info[self.store[p]], \
                #                                                                  self.store_info[self.store[i]]
                self.store[i], self.store[p] = self.store[p], self.store[i]
                i = p
                p = int((i - 1) / 2)

    def heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        m = i
        if l < self.curr_size and self.store[m] > self.store[l]:
            m = l
        if r < self.curr_size and self.store[m] > self.store[r]:
            m = r
        if m != i:
            # self.store_info[self.store[i]], self.store_info[self.store[m]] = self.store_info[self.store[m]], \
            #                                                                  self.store_info[self.store[i]]
            self.store[i], self.store[m] = self.store[m], self.store[i]
            self.heapify(m)

    def is_good(self, val):
        if self.curr_size == 0:
            return 1
        if val < self.store[0]:
            return 1
        return 0

    def print_info(self):
        print (self.values)
        print (self.store)
        print (self.store_info)
        print (self.curr_size)


def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        w = Window(5)
        c = 0
        a = list(map(int, input().split(' ')))
        for i in range(0, n):
            c += w.is_good(a[i])
            # print (w.is_good(a[i]))
            w.add(a[i])
            # w.print_info()
            # print()
        print(c)


if __name__ == '__main__':
    main()