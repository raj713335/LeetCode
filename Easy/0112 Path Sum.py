# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def target(root, sumx=0):

            if not root:
                return 0

            sumx += root.val

            if not root.left and not root.right:
                return sumx == targetSum

            return target(root.left, sumx) or target(root.right, sumx)

        return target(root)


        
