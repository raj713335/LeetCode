# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

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

        res = sorted(res)

        try:
            return res[-k]
        except:
            return -1
        
