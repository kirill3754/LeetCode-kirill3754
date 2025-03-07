class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        all_nums = [1] * (right + 1)
        for i in range(2, right + 1):
            if all_nums[i] == 0:
                continue
            val = i * 2
            while val <= right:
                all_nums[val] = 0
                val += i
        min_diff = right - left + 2
        prev = -right
        num1 = 0
        start = max(2, left)
        for i in range(start, right + 1):
            if all_nums[i]:
                diff = i - prev
                if diff < min_diff:
                    min_diff = diff
                    num1 = prev
                    num2 = i
                prev = i
        return [num1, num2] if num1 else [-1, -1]

        