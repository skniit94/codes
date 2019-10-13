'''Soumika has a string S and its starting index is 1. The string S consists of characters from 1-9 . As she is very intelligent, she wants to test his brother Vinay Tendulkar. She asked her brother Vinay Tendulkar to count the number of even numbered characters ( i.e  ) for every index i . For an index i, the result should be calculated from i to the end of the string. As Vinay doesn't know about programming, he wants you to help him find the solution.

Input:
First line contains a string S.

Output:
Print |S| space-separated integers,the result of every index.

Constraints:
1 ≤ |S| ≤ 4

SAMPLE INPUT
574674546476
SAMPLE OUTPUT
7 7 7 6 5 5 4 4 3 2 1 1
'''


def main():
    n = int(input())
    ans = []
    e = 0
    while n:
        print (n)
        r = n % 10
        print (r)
        if not r % 2:
            e += 1
        ans.append(e)
        n = int(n/10)

    s = ''
    for i in range(len(ans) -1 , -1, -1):
        s += f'{ans[i]} '

    print (s)

if __name__ == '__main__':
    main()