class Solution(object):

    def __init__(self):
        self.p = self.get_primes()
        # print (self.p)

    def get_primes(self):
        r = 1000005
        p = [i for i in range(1, r)]
        for i in range(1, r-1):
            if p[i] == 0:
                continue
            j = i
            while True:
                j += p[i]
                if j > r - 2:
                    break
                p[j] = 0
        p = [i for i in p if i != 0]
        return p

    def get_star(self, a):
        l = len(a)
        hm = {a[i]: i for i in range(l)}
        hm2 = {}
        # print (hm)
        p = self.p
        star = 0
        ma = a[0]
        for i in range(l):
            # print (f'a[i] {a[i]}')
            if hm.get(a[i]) > i or hm.get(1, -1) > i:
                hm2[a[i]] = hm2.get(a[i], 0) + 1
                ma = max(ma, a[i])
                continue
            temp = a[i]
            c = 1
            prod = 1
            while temp:
                b = False
                while not temp % p[c]:
                    prod *= p[c]
                    # print (f'prod {prod}')
                    if hm.get(prod, -1) > i:
                        # print('break 1')
                        b = True
                        # print ('cb1')
                        break
                    temp = int(temp/p[c])
                    # print (f'temp {temp}')
                    if hm.get(temp, -1) > i:
                        # print('break 2')
                        b = True
                        # print ('cb2')
                        break
                c += 1
                # print('y')
                if b:
                    # print ('cb3')
                    break

                # print (f'p[c] {p[c]}')
                if not temp % p[c] and hm.get(p[c], -1) > i:
                    # print('break 3')
                    b = True
                    # print ('cb4')
                    break

                if p[c] > temp:
                    # print ('cb5')
                    break

            # print ('x')
            if not b:
                count = 0
                x = 1
                temp = a[i] * x
                # print (f'ma {ma} hm2 {hm2} temp {temp}')
                while (temp <= ma):
                    count += hm2.get(temp, 0)
                    x += 1
                    temp = a[i]* x
                star = max(star, count)

            hm2[a[i]] = hm2.get(a[i], 0) + 1
            ma = max(ma, a[i])
            # print (f'hm2 {hm2} a[i] {a[i]} ma {ma}')

        return star


def main():
    t = int(input())
    s = Solution()
    while t:
        t -= 1
        l = int(input())
        a = list(map(int, input().split(' ')))
        print (s.get_star(a))

if __name__ == '__main__':
    main()