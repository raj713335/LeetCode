# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        node = root
        ds = []
        
        def depth(node, level):
            if node == None:
                return
            
            if (level == len(ds)):
                ds.append(node.val)
                
            depth(node.right, level+1)
            depth(node.left, level+1)
        
        depth(node, 0)
        
        return len(ds)
            
        
