# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        curr = [root]
        order = []
        max_height = []
        max_height_val = []
        parent = [root.val]
        valord = {}
        height = 1
        ordern = 0
        while curr:
            next_row = []
            for node in curr:
                order.append(node.val)
                valord[node.val] = ordern
                ordern += 1
                max_height.append(height)
                if len(max_height_val) < node.val:
                    max_height_val.extend([0] * (node.val - len(max_height_val)))
                max_height_val[node.val - 1] = height
                if node.left:
                    next_row.append(node.left)
                    parent.append(node.val)
                if node.right:
                    next_row.append(node.right)
                    parent.append(node.val)
            curr = list(next_row)
            height += 1
        #print(f'     order = {order}\nmax_height = {max_height}\nmax_he_val = {max_height_val}\n    parent = {parent}\n    valord = {valord}\n')
        n = len(order)
        for i in range(n-1, -1, -1):
            p = parent[i]
            o = valord[p]
            max_height[o] = max(max_height[o], max_height[i])

        #print(f'     order = {order}\nmax_height = {max_height}\n')

        highest = [0] * n
        sec_highest = [0] * n

        curr = [root]
        ordern = 0
        height = 1
        while curr:
            next_row = []
            lev_max = height - 1
            lev_sec_max = height - 1
            for node in curr:
                #print(max_height[ordern])
                if max_height[ordern] > lev_max:
                    lev_sec_max = lev_max
                    lev_max = max_height[ordern]
                elif max_height[ordern] > lev_sec_max:
                    lev_sec_max = max_height[ordern]
                ordern += 1
            #print(lev_max, lev_sec_max, '\n')
            for node in curr:
                highest[node.val - 1] = lev_max
                sec_highest[node.val - 1] = lev_sec_max
                if node.left:
                    next_row.append(node.left)
                if node.right:
                    next_row.append(node.right)
            curr = list(next_row)
            height += 1        
        #print(f'    highest = {highest}\nsec_highest = {sec_highest}\n')
        ans = []
        for q in queries:
            h = max_height[valord[q]]
            if h == highest[q-1]:
                ans.append(sec_highest[q-1]-1)
            else:
                ans.append(highest[q-1]-1)
            #print(valord[q], h, highest[q-1], sec_highest[q-1])








        return ans