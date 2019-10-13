
def __equal__(a, b, c):
    
    if a == b and b == c:
        return True
    return False


def __max__(a, b, c):

    return max(max(a, b), c)


def equal_stacks(s1, s2, s3):

    h1, h2, h3 = sum(s1), sum(s2), sum(s3)

    while s1 and s2 and s3:
        print (h1, h2, h3)
        if __equal__(h1, h2, h3):
            return h1

        max_height = __max__(h1, h2, h3)

        if max_height == h1:
            h1 -= s1.pop(-len(s1))
        elif max_height == h2:
            h2 -= s2.pop(-len(s2))
        elif max_height == h3:
            h3 -= s3.pop(-len(s3))

    return 0


def main():
    s1 = [3, 2, 1, 1, 1]
    s2 = [4, 3, 2]
    s3 = [1, 1, 4, 1]
    print (equal_stacks(s1, s2, s3))


if __name__ == "__main__":
    main()