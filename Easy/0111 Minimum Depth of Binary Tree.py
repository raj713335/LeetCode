# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        max_depth = math.inf
        def mindepth(root, depth=1):
            nonlocal max_depth


            if not root:
                return 0

            if not root.left and not root.right:
                if depth < max_depth:
                    max_depth = depth


            mindepth(root.left, depth+1)
            mindepth(root.right, depth+1)

        mindepth(root)

        if max_depth == math.inf:
            return 0
        return max_depth

        
