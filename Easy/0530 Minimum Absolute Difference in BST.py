# https://leetcode.com/problems/minimum-absolute-difference-in-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        stack =[]
        
        def printInorder(root):
            
            if root:
                printInorder(root.left)
                stack.append(root.val)
                printInorder(root.right)
                
            return sorted(stack)    

        arr = sorted(printInorder(root))
        
        
        minx = math.inf
        
        for i in range(0, len(arr)-1):
            if arr[i+1] - arr[i] < minx:
                minx = arr[i+1] - arr[i]
                
        return minx
        
