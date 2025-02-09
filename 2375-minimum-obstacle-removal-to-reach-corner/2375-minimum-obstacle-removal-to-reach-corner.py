class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        p = [[inf] * m for i in range(n)]
        '''for row in grid:
            print(row)
        for row in p:
            print(row)'''
        p[0][0] = 0
        cur = [[0, 0]]
        while cur:
            new_cur = []
            for i, j in cur:
                if i > 0:
                    score = p[i][j] + grid[i-1][j]
                    if score < p[i-1][j]:
                        p[i-1][j] = score
                        new_cur.append([i-1, j])
                if i < n-1:
                    score = p[i][j] + grid[i+1][j]
                    if score < p[i+1][j]:
                        p[i+1][j] = score
                        new_cur.append([i+1, j])
                if j > 0:
                    score = p[i][j] + grid[i][j-1]
                    if score < p[i][j-1]:
                        p[i][j-1] = score
                        new_cur.append([i, j-1])
                if j < m-1:
                    score = p[i][j] + grid[i][j+1]
                    if score < p[i][j+1]:
                        p[i][j+1] = score
                        new_cur.append([i, j+1])
            cur = new_cur
        '''for row in p:
            print(row)'''
        return p[n-1][m-1]
        