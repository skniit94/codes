import math
import numpy as np
from statistics import mean
from sklearn.linear_model import LinearRegression


def hurst_exponent(S):

    theta = 100
    q = 2
    K = []

    T_max = [i for i in range(1, 20)]
    for i in T_max:
        T = 1000 - i
        alpha = 0.01

        w0 = (1 - math.exp(-alpha))/(1 - math.exp(-alpha*T))

        # print (w0)

        Wt = [w0 * math.exp(-i/theta) for i in range(0, T)]

        Nt = [abs(S[t + i]-S[t])**q for t in range(0, T)]

        Dt = [abs(S[t])**q for t in range(0, T)]

        Wt.reverse()

        # print (Wt, Nt, Dt)

        Navg = 0
        Davg = 0

        for i in range(0, T):
            Navg += Wt[i] * Nt[i]
            Davg += Wt[i] * Dt[i]

        K.append(Navg/Davg)

        # print (Navg, Davg, K)

    # print (K)
    b = []
    for j in range(5, 20):
        KJ = K[0:j]
        TJ = T_max[0:j]

        lnKJ = np.log(KJ)
        lnTJ = np.log(TJ)

        x = np.array(lnTJ).reshape((-1, 1))
        y = np.array(lnKJ)

        model = LinearRegression()
        model.fit(x, y)
        b.append(model.coef_[0])


    b_avg = mean(b)
    return b_avg/q


def main():

    input_files = ['GHE_1.txt', 'GHE_2.txt', 'GHE_3.txt', 'GHE_4.txt']

    for file in input_files:
        inp_file = open(file, 'r')

        data = list(inp_file.read().split('\n'))
        data.pop()
        S = list(map(float, data))

        # print (type(S), len(S), S)
        h = hurst_exponent(S)
        print (f"Input file --> {file} Output --> {h}")


if __name__ == "__main__":
    main()


