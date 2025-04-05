from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        ans = 0
        l = len(nums)
        for i in range(1, l + 1):
            for subset in combinations(nums, i):
                print(subset)
                x = subset[0]
                for j in range(1, len(subset)):
                    x = x ^ subset[j]
                ans += x


        return ans
        