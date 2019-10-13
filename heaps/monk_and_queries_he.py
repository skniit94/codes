'''
Monk was asked to answer some queries in an interview. He is given an empty array A. Queries are of 4 types:-
1. 1 X - Add number X to the array A.
2. 2 X - Remove a single instance of number X from the array A. If not possible, print "-1" without the quotes.
3. 3 - Find the maximum element in the array A.
4. 4 - Find the minimum element in the array A.

Input:
The first line contains the integer Q.
The next Q lines will each contain a query like the ones mentioned above.

Output:
For queries 3 and 4, print the answer in a new line. If the array is empty for query 3 and 4, then print "-1" without the quotes.

Constraints:
1 <= Q <= 100000
1 <= X <= 100000

SAMPLE INPUT
5
1 5
1 9
1 6
3
2 1
SAMPLE OUTPUT
9
-1
Explanation
There are 5 queries.
Query 1 - 5 is added to the array.
Query 2 - 9 is added to the array.
Query 3 - 6 is added to the array.
Query 4 - The maximum element in the array is 9.
Query 5 - Since there is no element in the array with value 1, so the output is -1.
'''


class Solution(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_length = 0
        self.max_length = 0
        self.hm_min = {}
        self.hm_max = {}

    def update_hm(self, hm, val, prev, i):
        # print (hm, val, prev, i)
        val_index_map = hm.get(val, {})
        if prev != -1:
            val_index_map.pop(prev)
        if i != -1:
            val_index_map[i] = True
        hm[val] = val_index_map
        # print (hm)

    def insert(self, val):
        self.insert_min(val)
        self.insert_max(val)

    def insert_max(self, val):
        self.max_heap.append(val)
        self.max_length += 1
        i = self.max_length - 1
        par = int((i - 1)/2)
        while par >= 0 and self.max_heap[par] < self.max_heap[i]:
            self.update_hm(self.hm_max, self.max_heap[par], par, i)
            self.max_heap[i], self.max_heap[par] = self.max_heap[par], self.max_heap[i]
            i = par
            par = int((i - 1)/2)
        self.update_hm(self.hm_max, val, -1,  i)

    def insert_min(self, val):
        self.min_heap.append(val)
        self.min_length += 1
        i = self.min_length - 1
        par = int((i - 1)/2)
        while par >= 0 and self.min_heap[par] > self.min_heap[i]:
            self.update_hm(self.hm_min, self.min_heap[par], par, i)
            self.min_heap[i], self.min_heap[par] = self.min_heap[par], self.min_heap[i]
            i = par
            par = int((i - 1)/2)
        self.update_hm(self.hm_min, val, -1, i)

    def remove(self, val):
        if self.remove_from_min(val) == -1:
            return -1
        if self.remove_from_max(val) == -1:
            return -1
        return 1

    @staticmethod
    def search(hm, val):
        val_index_list = list(hm.get(val, {}).keys())
        if len(val_index_list):
            return val_index_list[0]
        return -1

    def min_heapify(self, i):
        m = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.min_length and self.min_heap[l] < self.min_heap[m]:
            m = l
        if r < self.min_length and self.min_heap[r] < self.min_heap[m]:
            m = r
        if m != i:
            self.update_hm(self.hm_min, self.min_heap[m], m, i)
            self.update_hm(self.hm_min, self.min_heap[i], i, m)
            self.min_heap[i], self.min_heap[m] = self.min_heap[m], self.min_heap[i]
            self.min_heapify(m)

    def max_heapify(self, i):
        m = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.max_length and self.max_heap[l] > self.max_heap[m]:
            m = l
        if r < self.max_length and self.max_heap[r] > self.max_heap[m]:
            m = r
        if m != i:
            self.update_hm(self.hm_max, self.max_heap[m], m, i)
            self.update_hm(self.hm_max, self.max_heap[i], i, m)
            self.max_heap[i], self.max_heap[m] = self.max_heap[m], self.max_heap[i]
            self.max_heapify(m)

    def remove_from_min(self, val):
        i = self.search(self.hm_min, val)
        if i == -1:
            return i
        l = self.min_length - 1

        if i == l:
            self.update_hm(self.hm_min, self.min_heap[i], i, -1)
            self.min_heap.pop()
            self.min_length -= 1
            return 1

        self.update_hm(self.hm_min, self.min_heap[i], i, -1)
        self.update_hm(self.hm_min, self.min_heap[l], l, i)
        self.min_heap[i], self.min_heap[l] = self.min_heap[l], self.min_heap[i]
        self.min_heap.pop()
        self.min_length -= 1
        self.min_heapify(i)
        return 1

    def remove_from_max(self, val):
        i = self.search(self.hm_max, val)
        if i == -1:
            return i
        l = self.max_length - 1

        if i == l:
            self.update_hm(self.hm_max, self.max_heap[i], i, -1)
            self.max_heap.pop()
            self.max_length -= 1
            return 1

        self.update_hm(self.hm_max, self.max_heap[i], i, -1)
        self.update_hm(self.hm_max, self.max_heap[l], l, i)
        self.max_heap[i], self.max_heap[l] = self.max_heap[l], self.max_heap[i]
        self.max_heap.pop()
        self.max_length -= 1
        self.max_heapify(i)
        return 1

    def get_max(self):
        if self.max_length == 0:
            return -1
        else:
            return self.max_heap[0]

    def get_min(self):
        if self.min_length == 0:
            return -1
        else:
            return self.min_heap[0]


def main():
    n = list(map(int, input().split(' ')))
    s = Solution()
    for i in range(n[0]):
        a = list(map(int, input().split(' ')))
        if len(a) == 1:
            if a[0] == 3:
                print (s.get_max())
            if a[0] == 4:
                print (s.get_min())
        if len(a) == 2:
            if a[0] == 1:
                s.insert(a[1])
            if a[0] == 2:
                if s.remove(a[1]) == -1:
                    print (-1)
        # print (s.hm_max)
        # print (s.hm_min)


if __name__ == "__main__":
    main()
