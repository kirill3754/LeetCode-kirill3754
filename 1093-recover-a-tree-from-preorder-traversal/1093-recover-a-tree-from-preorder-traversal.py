# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        val = []
        d = []
        cur_d = 0
        cur_val = 0
        i = 0
        n = len(traversal)
        while i < n:
            while i < n and traversal[i] == '-':
                cur_d += 1
                i += 1
            while i < n and traversal[i] != '-':
                cur_val = cur_val * 10 + int(traversal[i])
                i += 1
            d.append(cur_d)
            val.append(cur_val)
            cur_d = 0
            cur_val = 0
        m = len(val)
        def add_node(node, level):
            nonlocal i, m
            if i < m and d[i] > level and not node.left:
                node.left = TreeNode(val[i])
                i += 1
                add_node(node.left, level+1)
            if i < m and d[i] > level:
                node.right = TreeNode(val[i])
                i += 1
                add_node(node.right, level+1)
            return
        root = TreeNode(val[0])
        i = 1
        add_node(root, 0)
        return root
        
        