class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        k = len(nums)
        heap = []
        cur_max = -10 ** 5

        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cur_max = max(cur_max, nums[i][0])
        win = [-10**5, 10**5]

        while heap:
            cur_min, list_i, i = heapq.heappop(heap)
            if cur_max - cur_min < win[1] - win[0]:
                win = [cur_min, cur_max]
            if i == len(nums[list_i]) - 1:
                break
            heapq.heappush(heap, (nums[list_i][i + 1], list_i, i + 1))
            cur_max = max(cur_max, nums[list_i][i + 1])
        return win
            

