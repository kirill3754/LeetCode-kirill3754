class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        def max_sum_finder(nums):
            cur_sum = 0
            max_sum = 0
            for n in nums:
                cur_sum += n
                if cur_sum < 0:
                    cur_sum = 0
                else:
                    max_sum = max(max_sum, cur_sum)
            return max_sum
        
        return max(max_sum_finder(nums), max_sum_finder([-n for n in nums]))
        
        
        