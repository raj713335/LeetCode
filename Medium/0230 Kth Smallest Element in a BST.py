# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack =[]
        
        def printInorder(root):
            
            if root:
                printInorder(root.left)
                stack.append(root.val)
                printInorder(root.right)
                
            return stack    

        return sorted(printInorder(root))[k-1]
        
        
        
        
        
