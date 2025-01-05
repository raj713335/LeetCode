# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tally = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return

        self.bstToGst(root.right)
        self.tally += root.val
        root.val = self.tally
        self.bstToGst(root.left)

        return root
