# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        arr = []

        def post(root):
            
            if root:
            
                post(root.left)
                arr.append(root.val)
                post(root.right)
            
            return arr
        
        post(root1)
        post(root2)
        
        return sorted(arr)
        
