

def create_weight_set(s, char_weights):

    pr_str = ''
    pr_weight = 0
    weight_set = set()
    for i in s:
        char_weight = char_weights.get(i)
        weight_set.add(char_weight)
        if pr_str and pr_str[-1] == i:
            pr_str += i
            pr_weight += char_weight
            weight_set.add(pr_weight)
        else:
            pr_str = i
            pr_weight = char_weight

    return weight_set


def main():

    s = input()

    c = int(input())

    q = []

    for _ in range(c):
        q.append(int(input()))

    char_weights = {chr(i + 97): i + 1 for i in range(26)}
    weight_set = create_weight_set(s, char_weights)

    for i in q:
        if i in weight_set:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
