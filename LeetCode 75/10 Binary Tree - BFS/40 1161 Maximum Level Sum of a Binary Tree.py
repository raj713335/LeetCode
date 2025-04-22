# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

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
            res.append(sum(dictx[each]))

        return res.index(max(res)) + 1
