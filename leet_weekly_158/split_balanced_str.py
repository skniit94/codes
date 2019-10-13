
class Solution(object):
    def balancedStringSplit(self, s):

        s = list(s)
        r = l = 0
        c = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r += 1
            else:
                l += 1

            if r == l:
                c += 1
                r = 0
                l = 0

        return c



s = Solution()

print (s.balancedStringSplit('RRLRRLLL'))
