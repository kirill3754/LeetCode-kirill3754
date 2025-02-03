class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_incr = 1
        max_decr = 1
        cur_incr = 1
        cur_decr = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cur_incr += 1
                max_incr = max(max_incr, cur_incr)
            else:
                cur_incr = 1
            if nums[i+1] < nums[i]:
                cur_decr += 1
                max_decr = max(max_decr, cur_decr)
            else:
                cur_decr = 1
        return max(max_incr, max_decr)

        