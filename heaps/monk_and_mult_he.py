'''
The Monk learned about priority queues recently and asked his teacher for an interesting problem. So his teacher came up with a simple problem. He now has an integer array A. For each index i, he wants to find the product of the largest, second largest and the third largest integer in the range [1,i].
Note: Two numbers can be the same value-wise but they should be distinct index-wise.

Input:
The first line contains an integer N, denoting the number of elements in the array A.
The next line contains N space separated integers, each denoting the ith integer of the array A.

Output:
Print the answer for each index in each line. If there is no second largest or third largest number in the array A upto that index, then print "-1", without the quotes.

Constraints:
1 <= N <= 100000
0 <= A[i] <= 1000000

SAMPLE INPUT
5
1 2 3 4 5
SAMPLE OUTPUT
-1
-1
6
24
60
Explanation
There are 5 integers 1,2,3,4 and 5.
For the first two indexes, since the number of elements is less than 3, so -1 is printed.
For the third index, the top 3 numbers are 3,2 and 1 whose product is 6.
For the fourth index, the top 3 numbers are 4,3, and 2 whose product is 24.
For the fifth index, the top 3 numbers are 5,4 and 3 whose product is 60.

'''


def prod(a):
    if len(a) < 3:
        return -1
    return a[0]*a[1]*a[2]


def min_heapify(a, i):
    n = len(a)
    m = i
    l = 2*i+1
    r = 2*i+2

    if (l < n and a[l] < a[m]):
        m = l
    if (r < n and a[r] < a[m]):
        m = r
    if (m != i):
        a[m], a[i] = a[i], a[m]
        min_heapify(a, m)


def print_prod(a, n):
    h = []
    for i in range(n):
        if len(h) < 3:
            h.append(a[i])
        elif h[0] < a[i]:
            h[0] = a[i]
        min_heapify(h, 0)
        print(prod(h))


def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    print_prod(a, n)


if __name__ == '__main__':
    main()