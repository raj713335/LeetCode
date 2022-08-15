# https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        
        def right_view(root, level):
            if root == None:
                return
            
            if level == len(stack):
                stack.append(root.val)
                
            
            right_view(root.right, level+1)
            right_view(root.left, level+1)
        
        right_view(root, 0)
        return stack
