# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.max_len = 0
        
        def dfs(node, is_left, length):
            if not node:
                return
            self.max_len = max(self.max_len, length)
            if is_left:
                dfs(node.right, False, length + 1)  # change direction
                dfs(node.left, True, 1)             # restart from left
            else:
                dfs(node.left, True, length + 1)    # change direction
                dfs(node.right, False, 1)           # restart from right
        
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return self.max_len
        
