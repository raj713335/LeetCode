# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def function(node):
            if node is None:
                return 0 

            total = 0

            if node.left and node.left.left:
                if node.val%2 == 0:
                    total += node.left.left.val

            if node.left and node.left.right:
                if node.val%2 == 0:
                    total += node.left.right.val

            if node.right and node.right.left:
                if node.val%2 == 0:
                    total += node.right.left.val

            if node.right and node.right.right:
                if node.val%2 == 0:
                    total += node.right.right.val

            return total + function(node.left) + function(node.right)

        return function(root)
        
