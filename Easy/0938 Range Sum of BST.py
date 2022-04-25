# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        def dfs(node):
            if not node:
                return 0
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            else:
                self.sum += node.val
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.sum
        

        
