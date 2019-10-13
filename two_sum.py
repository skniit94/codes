
class Solution(object):
    def twoSum(self, nums, tar):
        d = {}
        for i in range(len(nums)):
            diff = tar - nums[i]
            if d.get(diff, -1) > -1:
                return [d.get(diff), i]
            d[nums[i]] = i


def main():
    nums = [3, 3]
    tar = 6
    print (Solution().twoSum(nums, tar))


if __name__ == "__main__":
    main()