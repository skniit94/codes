
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_str = self.find_smallest_str(strs)

        for st in strs:
            min_str = self.compare(st, min_str)
            if not min_str:
                return min_str
        return min_str

    def compare(self, s1, s2):
        s1 = list(s1)
        s2 = list(s2)
        l1 = len(s1)
        l2 = len(s2)
        i = 0
        new_str = ''

        while i < l1 and i < l2:
            if s1[i] == s2[i]:
                new_str += s1[i]
            else:
                break
            i += 1
        return new_str

    def find_smallest_str(self, strs):

        min_str = strs[0]
        minl = len(min_str)

        for st in strs:
            l = len(st)
            if l < minl:
                minl = l
                min_str = st
        return min_str


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))