def sol(mat):

    hm = {}
    n = len(mat[0])
    m = len(mat)
    for i in range(m):
        xmi = xma = (i, 0)
        mi = ma = mat[i][0]
        for j in range(1, n):
            if mat[i][j] > ma:
                ma = mat[i][j]
                xma = (i, j)
            if mat[i][j] < mi:
                mi = mat[i][j]
                xmi = (i, j)

        hm[str(xma[0]) + '_' + str(xma[1])] = True
        hm[str(xmi[0]) + '_' + str(xmi[1])] = True

    for j in range(n):
        xmi = xma = (0, j)
        mi = ma = mat[0][j]
        for i in range(1, m):
            if mat[i][j] > ma:
                ma = mat[i][j]
                xma = (i, j)
            if mat[i][j] < mi:
                mi = mat[i][j]
                xmi = (i, j)

        hm[str(xma[0]) + '_' + str(xma[1])] = True
        hm[str(xmi[0]) + '_' + str(xmi[1])] = True

    return len(hm.values())


if __name__ == "__main__":
    m = [[1], [2], [3]]
    print (sol(m))