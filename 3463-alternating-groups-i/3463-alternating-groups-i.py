class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)
        colors.append(colors[0])
        colors.append(colors[1])
        for i in range(n):
            if abs(colors[i]-colors[i+1]) == 1 and abs(colors[i+1]-colors[i+2]) == 1:
                res += 1
        return res
        