# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, curr_sum):

            if not root:
                return 0

            curr_sum = curr_sum * 10 + root.val

            if not root.left and not root.right:
                return curr_sum
            
            return dfs(root.left, curr_sum) + dfs(root.right, curr_sum)

        return dfs(root, 0)
