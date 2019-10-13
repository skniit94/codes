class Solution(object):
    def __init__(self, *args):
        self.height = args
        self.n = len(args)

    def max_area(self):
        """
        :type height: List[int]
        :rtype: int
        """
        print (self.height)
        print (self.n)
        height = self.height
        n = self.n
        max_indexes = []
        max = 0
        for i in range(n):
            if max < height[i]:
                max = height[i]
                max_indexes = [i]
            elif max == height[i]:
                max_indexes.append(i)
        print (max, max_indexes)
        max_water = 0
        for i in range(n):
            for j in range(len(max_indexes)):
                water = abs(max_indexes[j] - i)*height[i]
                print ("###", max_indexes[j], i, water, max_water)
                if water > max_water:
                    print (max_indexes[j], i, height[i])
                    max_water = water

        return max_water


if __name__ == '__main__':

    print (Solution(1,5,4,3,3,2,2).max_area())


