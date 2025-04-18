# https://leetcode.com/problems/binary-tree-cameras/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        self.camera_count = 0

        def dfs(node):
            if not node:
                return 1  # Null nodes are considered covered

            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                self.camera_count += 1
                return 0  # Place camera here

            if left == 0 or right == 0:
                return 1  # This node is covered by child’s camera

            return -1  # This node needs camera

        if dfs(root) == -1:
            self.camera_count += 1  # Place camera at root if needed

        return self.camera_count
        
