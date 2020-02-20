



def print_dags(mat):
    r = len(mat)
    if not r:
        return
    c = len(mat[0])

    # print (r, c)

    for i in range(c-1, -1, -1):
        t = i
        for j in range(r):
            # print (t, j)
            print (mat[j][t])
            t += 1
            if t >= c:
                break

    for i in range(1, r):
        t = i
        for j in range(c):
            print(mat[t][j])
            t+=1
            if t >= r:
                break



if __name__ == "__main__":
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    mat = [[1, 2, 3]]
    print_dags(mat)
