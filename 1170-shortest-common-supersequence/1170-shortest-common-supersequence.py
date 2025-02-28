class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)+1
        m = len(str2)+1
        path = [[0] * m for i in range(n)]
        for i in range(n):
            path[i][0] = i
        for j in range(m):
            path[0][j] = j
        for i in range(1, n):
            for j in range(1, m):
                if str1[i-1] == str2[j-1]:
                    path[i][j] = 1 + path[i-1][j-1]
                else:
                    path[i][j] = 1 + min(path[i-1][j], path[i][j-1])
        ans = []
        i = n - 1
        j = m - 1
        while i > 0 or j > 0:
            if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
                ans.append(str1[i-1])
                i -= 1
                j -= 1
            elif i > 0 and path[i][j] - path[i-1][j] == 1:
                ans.append(str1[i-1])
                i -= 1
            elif j > 0 and path[i][j] - path[i][j-1] == 1:
                ans.append(str2[j-1])
                j -= 1
        ans.reverse()
        return ''.join(ans)
        