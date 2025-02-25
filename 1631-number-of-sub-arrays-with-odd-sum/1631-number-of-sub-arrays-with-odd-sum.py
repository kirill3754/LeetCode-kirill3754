class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_n, ev_n = 0, 0
        ans = 0
        mod = 10**9 + 7
        for num in arr:
            if num % 2:
                odd_n, ev_n = ev_n, odd_n
                odd_n += 1
            else:
                ev_n += 1
            ans = (ans + odd_n) % mod
        return ans
            
        