# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      
        stack =[]
        def printPreorder(root):
 
            if root:

                # First print the data of node
                stack.append(root.val)

                # Then recur on left child
                printPreorder(root.left)

                # Finally recur on right child
                printPreorder(root.right)
                
            return stack
        return printPreorder(root)
