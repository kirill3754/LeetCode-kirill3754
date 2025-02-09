from collections import deque

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        left_queries = []
        for i in range(len(queries)):
            if queries[i][0] == queries[i][1]:
                ans[i] = queries[i][0]
            elif queries[i][0] > queries[i][1] and heights[queries[i][0]] > heights[queries[i][1]]:
                ans[i] = queries[i][0]
            elif queries[i][1] > queries[i][0] and heights[queries[i][1]] > heights[queries[i][0]]:
                ans[i] = queries[i][1]
            elif queries[i][0] > queries[i][1]:
                left_queries.append([queries[i][1], queries[i][0], i])
            else:
                left_queries.append([queries[i][0], queries[i][1], i])
        #print(left_queries)

        left_queries.sort(key=lambda x:x[1], reverse=True)
        #print('ans=',ans)
        #print(left_queries)

        stack = deque([heights[-1]])
        stack_i = deque([len(heights)-1])
        prev_y = len(heights)-2
        for x, y, i in left_queries:
            #print('x, y, i', x, y, i)
            #print('stack', stack)
            #print('stack_i', stack_i)
            for j in range(prev_y, y, -1):

                while stack and heights[j]>=stack[0]:
                    stack.popleft()
                    stack_i.popleft()
                stack.appendleft(heights[j])
                stack_i.appendleft(j)
                #print('stack', stack)
                #print('stack_i', stack_i)
                #print('__________')
            prev_y = y

            j = bisect_right(stack, heights[x])
            #print('j, heights[x]', j, heights[x])
            if j < len(stack):
                ans[i] = stack_i[j]
                #print('ans[i] = stack_i[j]', stack_i[j])
            #else:
                #print('ans[i] = -1')
            
            #print('--------')
            #print('------')
        return ans


        