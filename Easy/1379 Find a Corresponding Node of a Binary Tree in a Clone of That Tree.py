# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        node = None
        
        if original.val == target.val:
            node = cloned
            
        if node is None and original.left:
            node = self.getTargetCopy(original.left, cloned.left, target)
        if node is None and original.right:
            node = self.getTargetCopy(original.right, cloned.right, target)
        
        return node
        
