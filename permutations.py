def find_perm(s):
    s = list(s)
    if len(s) == 1:
        return 1
    p = 0
    for i in range(len(s)):
        s[0], s[i] = s[i], s[0]
        p += find_perm(s[1:])
        s[0], s[i] = s[i], s[0]
    return p


if __name__ == "__main__":
    print(find_perm('abcd'))