# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        s1 = [root]
        s2 = []
        
        while len(s1) > 0:
            
            curr = s1.pop()
            s2.append(curr.val)
            
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)
            
        return s2[::-1]
            
        
        
