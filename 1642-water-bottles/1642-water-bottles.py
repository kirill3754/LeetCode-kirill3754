class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            left = numBottles % numExchange
            exchanged = numBottles // numExchange
            ans = ans + numBottles - left
            numBottles = left + exchanged
        ans += numBottles
        return ans
        