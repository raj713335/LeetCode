# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        res = []
        stack = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        res = sorted(res)

        
        for i in range(0, len(res)-1):
            res[i] = abs(res[i] - res[i+1])

        return min(res)
