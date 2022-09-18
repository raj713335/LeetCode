# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        stack =[]
        
        def printInorder(root):
            
            if root:
                printInorder(root.left)
                stack.append(root.val)
                printInorder(root.right)
                
            return stack    

        arr = printInorder(root)
        
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i]+arr[j] == k:
                    return True
                
        return False
        
