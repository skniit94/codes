def main():
    t = int(input())
    while t:
        t -= 1
        n, k = list(map(int, input().split(' ')))
        a = list(map(int, input().split(' ')))

        q = int(k / n)
        r = k % n

        if q > 0:

            r3 = int(q % 3)

            if r3 == 0:
                r3 = 3

            for i in range(r3):
                for j in range(n):
                    a[j] = a[j] ^ a[n-j-1]

        for i in range(r):
            a[i] = a[i] ^ a[n - i - 1]

        for i in a:
            print (i, end = ' ')
        print()

if __name__ == '__main__':
    main()