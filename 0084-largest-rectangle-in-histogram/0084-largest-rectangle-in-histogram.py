class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_h = max(heights)
        ans = 0
        stack = []
        stack_i = []
        for i, h in enumerate(heights):
            #print('i,h',i,h)
            if not stack or h > stack[-1]:
                stack.append(h)
                stack_i.append(i)
                #print('stack,stack_i',stack,stack_i,'---')
            elif h < stack[-1]:
                while stack and h < stack[-1]:
                    common_height = stack.pop()
                    i0 = stack_i.pop()
                    width = i-i0
                    #print('common_height,i0,width',common_height,i0,width)
                    ans = max(ans, width * common_height)
                stack.append(h)
                stack_i.append(i0)                
        while stack:
            common_height = stack.pop()
            i0 = stack_i.pop()
            width = n-i0
            #print('common_height,i0,width',common_height,i0,width)
            ans = max(ans, width * common_height)
        return ans





        

        