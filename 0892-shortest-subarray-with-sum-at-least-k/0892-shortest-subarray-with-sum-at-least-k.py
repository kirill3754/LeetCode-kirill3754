class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = n + 1
        s = list(accumulate(nums, initial=0))
        q = deque()

        for i, v in enumerate(s):
            while q and v - s[q[0]] >= k:
                min_len = min(min_len, i - q.popleft())
            while q and s[q[-1]] >= v:
                q.pop()
            q.append(i)

        return -1 if min_len == n + 1 else min_len
        