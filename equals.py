hm = {}


def __key__(arr): return ''.join(map(str, sorted(arr)))


def __equal__(arr): return all(i == arr[0] for i in arr)


def __hm_min__(hm):

    m = -1

    for i in hm.values():
        if i < m:
            m = i

    return m


def util(arr, val, step):

    global hm
    print (hm)
    print (arr, "array")
    print (step, "step")
    key = __key__(arr)

    if __equal__(arr):
        hm[key] = step
        print (key, "returned array equal")
        return

    if hm.get(key):
        print (key, "returned key found")
        return

    hm[key] = -1

    for i in range(len(arr)):
        print (arr[i], "array elem")
        for j in val:
            print (j, "val elem")
            new_arr = [arr[t]+j if t != i else arr[t] for t in range(len(arr))]
            util(new_arr, val, step + 1)


def main():

    global hm
    arr = [1, 1, 5]
    val = [1, 2, 5]
    step = 0

    util(arr, val, step)

    print (__hm_min__(hm))


if __name__ == "__main__":
    main()
