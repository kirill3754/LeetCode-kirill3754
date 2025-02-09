class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        rise = [1] * n
        fall = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    rise[i] = max(rise[i], 1 + rise[j])
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                if nums[i] > nums[j]:
                    fall[i] = max(fall[i], fall[j] + 1)
        
        return n - max(a + b - 1 for a, b in zip(rise, fall) if a > 1 and b > 1)

        
        