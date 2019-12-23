def get_uneaten_trees(n, k, a):

    t = [0]*n
    for i in a:
        m = 1
        j =  i * m
        while j <= n:
            t[j-1] = 1
            m += 1
            j = i * m

    c = 0
    for i in t:
        if t[i] == 0:
            c += 1
    return c

def main():

    n = int(input())
    k = int(input())
    a = []
    while k:
        a.append(int(input()))
        k -=1

    print(get_uneaten_trees(n, k, a))


if __name__ == "__main__":
    main()