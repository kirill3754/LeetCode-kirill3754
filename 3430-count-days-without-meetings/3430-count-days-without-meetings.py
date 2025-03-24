class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # print(meetings)
        n = len(meetings)
        ans = meetings[0][0] - 1
        cur_max = 0
        for i in range(n-1):
            cur_max = max(cur_max, meetings[i][1])
            val = meetings[i+1][0] - cur_max - 1
            # print(meetings[i], val)
            ans += max(0, val)
        cur_max = max(cur_max, meetings[n-1][1])
        ans += days - cur_max

        return ans
        