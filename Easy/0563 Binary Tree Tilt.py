# https://leetcode.com/problems/binary-tree-tilt/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0
        
        def calculate_tilt(node):
            if not node:
                return 0
            
            left_sum = calculate_tilt(node.left)
            right_sum = calculate_tilt(node.right)
            tilt = abs(left_sum - right_sum)
            
            self.total_tilt += tilt
            
            return left_sum + right_sum + node.val
        
        calculate_tilt(root)
        return self.total_tilt
        
