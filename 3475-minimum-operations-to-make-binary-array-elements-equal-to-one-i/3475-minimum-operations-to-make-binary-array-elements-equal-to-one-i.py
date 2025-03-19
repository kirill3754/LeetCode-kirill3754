class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            if not nums[i]:
                ans += 1
                for j in range(i, i+3):
                    nums[j] = 1 - nums[j]
        if nums[n-1] and nums[n-2]:
            return ans
        else:
            return -1


        