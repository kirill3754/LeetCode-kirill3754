class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotation_i = -1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if rotation_i == -1:
                    rotation_i = i
                else:
                    return False
        if rotation_i == -1:
            return True
        if nums[0] >= nums[-1]:
            return True
        return False
        
            
        