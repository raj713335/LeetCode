# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        res = []

        def dfs(root):

            if not root:
                return 

            res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        res = sorted(set(res))

        try:
            return res[1]
        except:
            return -1
        
