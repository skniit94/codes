def main():
    t = int(input())
    while t:
        t -= 1
        n, m, q = list(map(int, input().split(' ')))
        hmr = {i: 0 for i in range(1, n+1)}
        hmc = {i: 0 for i in range(1, m+1)}
        while q:
            q -= 1
            r, c = list(map(int, input().split(' ')))
            hmr[r] = hmr.get(r, 0) + 1
            hmc[c] = hmc.get(c, 0) + 1
        rodd = reven = codd = ceven = 0
        # print (hmr, hmc)
        for val in hmr.values():
            if val % 2:
                rodd += 1
            else:
                reven += 1

        for val in hmc.values():
            if val % 2:
                codd += 1
            else:
                ceven += 1

        print (rodd*ceven + reven*codd)


if __name__ == '__main__':
    main()