class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if (num>9 and num<100) or (num>999 and num<10000) or num == 100000:
                ans +=1
        return ans
        