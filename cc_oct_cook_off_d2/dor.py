
x = [1]
hm = {1: 0}
for i in range(1, 64):
    x.append(x[i - 1] * 2)
    hm[x[i]] = i

t = int(input())

while t:
    t -= 1
    a, b = list(map(int, input().split(' ')))

    l = min(a, b)
    r = max(a, b)

    for i in range(63, -1, -1):
        # print(i,r & x[i], l & x[i] )
        if not (r & x[i]):
            if not (l & x[i]):
                temp = l | x[i]
                # print (temp, i)
                if temp <= r:
                    l = temp

    print (l | r)










