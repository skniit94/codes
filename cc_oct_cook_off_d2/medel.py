
t = int(input())

while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split(' ')))
    ma = a[0]
    mi = a[0]
    mai = mii =  0
    for i in range(1, n):
        if a[i] > ma:
            ma = a[i]
            mai = i

        if a[i] < mi:
            mi = a[i]
            mii = i

    gi = max(mai, mii)
    li = min(mai, mii)

    print('\n')
    print (a[li], end = ' ')
    print (a[gi])

