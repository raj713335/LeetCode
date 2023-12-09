# https://leetcode.com/problems/univalued-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        res = []

        def dfs(root):

            if not root:
                return 
            
            res.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        if len(set(res)) == 1:
            return True
        else:
            return False
        
