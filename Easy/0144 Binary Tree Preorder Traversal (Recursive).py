# https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        nodes = []
        
        if not root:
            return nodes
        
        curr = root
        stack = [root]
        
        while len(stack) > 0:
            curr = stack.pop()
            nodes.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                 
            
        return nodes
        
