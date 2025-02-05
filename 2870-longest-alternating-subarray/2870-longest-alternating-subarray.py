class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_len = 1
        cur_len = 1
        i=0
        while i<len(nums)-1:
            if nums[i+1] - nums[i] == 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
                i+=1
                if i<len(nums)-1 and nums[i+1] - nums[i] == -1:
                    cur_len += 1
                    max_len = max(max_len, cur_len)
                    i+=1
                else:
                    cur_len = 1
            else:
                cur_len = 1
                i+=1
        return max_len if max_len > 1 else -1

        