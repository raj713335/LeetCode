# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        dictx = {}

        def dfs(root, level):
            if not root:
                return 
            
            dfs(root.left, level+1)
            if level in dictx:
                dictx[level].append(root.val)
            else:
                dictx[level] = [root.val]
            dfs(root.right, level+1)

        dfs(root, 0)

        res = []
        for each in sorted(dictx.keys()):
            res.append(max(dictx[each]))

        return res
        
