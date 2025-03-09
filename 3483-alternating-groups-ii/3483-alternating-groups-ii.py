class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        #check if the colors are circled or find a new start
        n = len(colors)
        start = 0
        for i in range(n-1):
            if colors[i] == colors[i+1]:
                start = i+1
                break
        else:
            if colors[n-1] != colors[0]:
                return n
        colors = colors[start:] + colors[:start]

        #calculate alternating subsections length
        ans = 0
        cnt = 1
        for i in range(n-1):
            if colors[i] != colors[i+1]:
                cnt += 1
            else:
                ans += max(cnt-k+1, 0)
                cnt = 1
        ans += max(cnt-k+1, 0)
        return ans


        