class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_cnt = 0
        ten_cnt = 0
        for bill in bills:
            if bill == 5:
                five_cnt += 1
            elif bill == 10:
                five_cnt -= 1
                ten_cnt += 1
            else:
                five_cnt -= 1
                ten_cnt -= 1
            while ten_cnt < 0:
                ten_cnt += 1
                five_cnt -= 2
            if five_cnt < 0 or ten_cnt < 0:
                return False
        return True
        