# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.msum = float('-inf')
        self.get_sum(root)
        return self.msum
    
    def get_sum(self, node):
        if not node:
            return 0
        
        ls, rs = self.get_sum(node.left), self.get_sum(node.right)
        max_single_path = max(node.val+max(ls,rs), node.val)
        self.msum = max(self.msum, max_single_path , node.val+ls+rs)
        return max_single_path
