class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) // 2
        for i in range(n):
            if nums[i*2] != nums[i*2+1]:
                return False
        return True
        