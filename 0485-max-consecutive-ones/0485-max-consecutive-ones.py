class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        cur_con = 0
        for n in nums:
            if n:
                cur_con += 1
            else:
                max_con = max(max_con, cur_con)
                cur_con = 0
        max_con = max(max_con, cur_con)
        return max_con
        