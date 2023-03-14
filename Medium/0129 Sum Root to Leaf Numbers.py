# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:


        def rootToLeaf(root, items=0):

            if not root:
                return 0

            items = items * 10 + root.val
            if not root.left and not root.right:
                return items

            return rootToLeaf(root.left, items) + rootToLeaf(root.right, items)

            

        return rootToLeaf(root)





