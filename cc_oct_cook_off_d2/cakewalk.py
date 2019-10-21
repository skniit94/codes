
a = [1]
hm = {1: 0}
for i in range(1, 64):
    a.append(a[i - 1] * 2)
    hm[a[i]] = i

# print (a)
# print (hm)

t = int(input())

while t:
    t -= 1
    n = int(input())
    c = 0
    while n % 10 == 0:
        n = int(n/10)
        c += 1

    # print (n, c)
    # print (hm.get(n))
    if hm.get(n, -1) > -1 and c >= hm.get(n):
        print ('Yes')
    else:
        print ('No')




