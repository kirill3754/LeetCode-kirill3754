class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        oprs = 0
        while(True):
            a = heapq.heappop(nums)
            if a >= k:
                return oprs
            b = heapq.heappop(nums)
            heapq.heappush(nums, a*2 + b)
            oprs += 1
        return -1
        