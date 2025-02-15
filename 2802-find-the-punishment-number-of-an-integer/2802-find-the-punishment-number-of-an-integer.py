class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check_split(num, idx, target):
            if idx == len(num):
                return target == 0
            cur_sum = 0
            for i in range(idx, len(num)):
                cur_sum = cur_sum*10 + int(num[i])
                if cur_sum > target:
                    return False
                if check_split(num, i+1, target - cur_sum):
                    return True
            return False

        ans = 0
        for i in range(1, n+1):
            i_sq = i*i
            i_sq_str = str(i_sq)
            if check_split(i_sq_str, 0, i):
                ans += i_sq
        return ans


                
        