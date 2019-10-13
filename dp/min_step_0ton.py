import sys
sys.setrecursionlimit(10**6)


class Solution(object):
    def __init__(self, n):
        self.n = n
        self.hm = {}

    def get(self, sum, x):
        if sum > self.n:
            return self.n+1
        if sum == self.n:
            return 0

        ans = self.hm.get(sum)
        if ans:
            l = len(ans)
            if l > x - 1:
                return ans[x-1]

        if x == 1:
            sum += 1
        else:
            sum *= 2

        a = self.get(sum, 1)
        self.hm[sum] = [a]
        b = self.get(sum, 2)
        self.hm[sum].append(b)

        return 1 + min(a, b)


def main():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        print (Solution(n).get(0, 1))


if __name__ == '__main__':
    main()