class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        i = 0
        n = len(nums)
        while i<n and nums[i]<0:
            neg+=1
            i+=1
        while i<n and nums[i]==0:
            i+=1
        pos = n-i
        return max(neg, pos)
        