def main():

    t = int(input())
    while t:
        t -= 1
        n = int(input())
        x = 0
        while n:
            n -= 1
            l = input()
            x = x ^ int(l, 2)

        b = bin(x)
        s = [i for i in b[2:] if i == '1']
        print (len(s))


if __name__ == "__main__":
    main()