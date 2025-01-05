# https://leetcode.com/problems/convert-bst-to-greater-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tally = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return

        self.convertBST(root.right)
        self.tally += root.val
        root.val = self.tally
        self.convertBST(root.left)
        return root
