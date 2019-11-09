def lcs(x, y):

    x, y = list(x), list(y)
    n, m = len(x), len(y)

    # mat = [[0]* (n+1)] * (m+1)
    # above matrix will not work
    # as change in one row will reflect
    # in all others.

    mat = []
    for i in range(0, m+1):
        mat.append([0]*(n+1))
    print (mat)
    # mat[5][5] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            print (i, j)
            if x[j] == y[i]:
                mat[i][j] = mat[i+1][j+1] + 1
            else:
                mat[i][j] = max(mat[i+1][j], mat[i][j+1])
            print (mat)

    print (mat)
    return mat[0][0]


def main():
    x = 'abcbdab'
    y = 'bdcaba'
    print (lcs(x, y))


if __name__ == "__main__":
    main()