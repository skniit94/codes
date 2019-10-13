def sol(n):
    l = len(n)
    pos = []
    neg = []

    for i in range(l):
        pos.append(0)
        neg.append(0)
        for j in range(i + 1, l):
            if n[i] - n[j] > 0:
                pos[-1] += 1
            else:
                neg[-1] += 1
    print (pos, neg)
    ans = 0
    for i in range(l):
        for j in range(i+1, l):
            if n[i] - n[j] > 0:
                ans += pos[j]
            else:
                ans += neg[j]

    return ans


if __name__ == "__main__":
    n = [5, 2, 3, 1, 4, 7]
    print(sol(n))