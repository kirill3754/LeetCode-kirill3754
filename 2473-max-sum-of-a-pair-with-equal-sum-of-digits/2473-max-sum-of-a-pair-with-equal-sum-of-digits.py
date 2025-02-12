class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_num = [-1]*82
        second_max_num = [-1]*82
        for n in nums:
            dig_sum = 0
            for digit in str(n):
                dig_sum += int(digit)
            if n > max_num[dig_sum]:
                second_max_num[dig_sum] = max_num[dig_sum]
                max_num[dig_sum] = n
            elif n > second_max_num[dig_sum]:
                second_max_num[dig_sum] = n
            print(n, dig_sum)
        ans = -1
        for i in range(len(max_num)):
            if max_num[i] >= 0 and second_max_num[i] >= 0:
                ans = max(ans, max_num[i] + second_max_num[i])
        return ans if ans >= 0 else -1
        