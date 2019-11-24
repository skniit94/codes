import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def NP_moving_block_bootstrap(mat):

    random.seed(5000)
    B = 16
    sub_mat_set = []
    for i in range(B):
        sub_mat = []
        start = random.randint(0, 1470)
        # print (start)
        for j in range(100):
            sub_mat.append(mat[j][start:start+30])
        # print (sub_mat)
        sub_mat_set.append(sub_mat)
    # print (sub_mat_set, sub_mat_set[0], sub_mat_set[0][0])
    lr_mat = []
    for i in range(B):
        lr = []
        for j in range(100):
            l1 = math.log(sub_mat_set[i][j][0])
            l2 = math.log(sub_mat_set[i][j][-1])
            lr.append(l2 - l1)
        lr_mat.append(lr)

    M = []
    for i in range(100):
        sum = 0
        for j in range(B):
            sum += lr_mat[j][i]
        M.append(sum)

    M_REV = []
    for i in range(len(M)):
        M_REV.append(((math.exp(M[i]) - 1), i))

    # step 7 says repeat 2 to 5 1000
    # times but the seed value is not changed
    # due to which in every iteration M_REV will
    # be same, finally the mean value will be same as
    # M_REV values hence I have not iterated 1000 times.

    M_REV.sort(key=lambda x: x[0])

    TOP_ASSETS = M_REV[-5:]
    TOP_ASSETS.reverse()

    return TOP_ASSETS


def main():

    input_files = ['Input_Data_Non_Param_BootStrap.txt']

    for file in input_files:
        inp_file = open(file, 'r')

        data = list(inp_file.read().split('\n'))
        data.pop()
        # print (data)
        mat = []
        for i in range(1, len(data)):
            row = data[i].split('\t')
            row.pop(0)
            row = list(map(float, row))
            mat.append(row)

        # print (mat)
    top_assets = NP_moving_block_bootstrap(mat)

    d = []
    col = []
    print('Top assets are')
    for i in top_assets:
        d.append(mat[i[1]])
        col.append(i[1])
        print (f'Asset {i[1]}')

    d = np.matrix(d).T

    df = pd.DataFrame(d, columns=col)
    df.boxplot(column=col)
    plt.show()


if __name__ == "__main__":
    main()
