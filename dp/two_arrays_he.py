hm1 = {}
hm2 = {}


def pre_compute(n, a, b):

    s1 = s2 = 0
    for i in range(n):

        if not i % 2:
            s1 += a[i]
            s2 += b[i]
        else:
            s1 += b[i]
            s2 += a[i]
        key = '0_' + str(i)
        hm1[key] = s1
        hm2[key] = s2


def main():

    n, q = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pre_compute(n, a, b)

    # print (hm1, hm2)
    for i in range(q):
        p, x, y = list(map(int, input().split()))
        x -= 1
        y -= 1
        k1 = '0_'+ str(y)
        k2 = '0_' + str(x-1)
        if p == 1 and not x % 2:
            print (hm1.get(k1, 0) - hm1.get(k2, 0))
        elif p == 1 and x % 2:
            print (hm2.get(k1, 0) - hm2.get(k2, 0))
        elif p == 2 and not x % 2:
            print (hm2.get(k1, 0) - hm2.get(k2, 0))
        else:
            print (hm1.get(k1, 0) - hm1.get(k2, 0))


if __name__ == '__main__':
    main()