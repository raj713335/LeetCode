# https://leetcode.com/problems/sum-of-left-leaves/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        # does this node have a left child which is a leaf?
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        # no it does not have a left child or it's not a leaf
        else:
			# bummer
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
