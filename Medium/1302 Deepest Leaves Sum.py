# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        a = []
        
        h = self.height(root)
        self.traverse(root, a, h, 0)
        return sum(a)
        
    def height(self, root):
        
        if not root:
            return -1
        
        hleft = self.height(root.left)+1
        hright = self.height(root.right)+1
        
        return max(hleft, hright)
    
    def traverse(self, root, a , h, c):
        
        if not root:
            return
        
        self.traverse(root.left, a, h, c+1)
        self.traverse(root.right, a, h, c+1)
        
        if not root.left and not root.right and c==h:
            a.append(root.val)
        
        
