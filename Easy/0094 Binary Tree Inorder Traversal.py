# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack =[]
        def printInorder(root):
 
            if root:
                # Then recur on left child
                printInorder(root.left)
        
                # First print the data of node
                stack.append(root.val)

                # Finally recur on right child
                printInorder(root.right)
            return stack
          
        return printInorder(root)
        
        
