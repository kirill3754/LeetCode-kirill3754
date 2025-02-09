class Solution:
    def trap(self, height: List[int]) -> int:
        #print(height)
        ans = 0
        cur = height[0]
        n = len(height)
        integating = False
        for i in range(1, n):
            if integating:
                if height[i] < start_height:
                    cur_vol += start_height - height[i]
                else:
                    integating = False
                    ans += cur_vol
                    for j in range(start_i, i):
                        height[j] = start_height
            else:
                if height[i] < height[i - 1]:
                    integating = True
                    start_height = height[i - 1]
                    cur_vol = start_height - height[i]
                    start_i = i
        #print(height)
        integating = False
        for i in range(n-2, -1, -1):
            if integating:
                if height[i] < start_height:
                    cur_vol += start_height - height[i]
                else:
                    integating = False
                    ans += cur_vol
            else:
                if height[i] < height[i + 1]:
                    integating = True
                    start_height = height[i + 1]
                    cur_vol = start_height - height[i]
                    start_i = i        
        return(ans)

        