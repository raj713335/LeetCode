# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack =[]
        def printPostorder(root):
 
            if root:
                # Then recur on left child
                printPostorder(root.left)
        
                # Finally recur on right child
                printPostorder(root.right)
            
                # First print the data of node
                stack.append(root.val)

            return stack
        return printPostorder(root)
            
