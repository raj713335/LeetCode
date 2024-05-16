# https://leetcode.com/problems/closest-binary-search-tree-value/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        nearest = float("inf")

        while root:
            if root.val == target: return root.val
            if abs(root.val-target) < abs(nearest-target): nearest = root.val
            if abs(root.val-target) == abs(nearest-target): nearest = min(root.val,nearest)

            if root.val > target:
                root = root.left
            else:
                root = root.right
        
        return nearest
