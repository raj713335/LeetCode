# https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetricTree(p, q):
            if p is None and q is None:
                return True
            elif p is None and q is not None:
                return False
            elif p is not None and q is None:
                return False
            else:
                return symmetricTree(p.left, q.right) and symmetricTree(p.right, q.left) and p.val == q.val

        return symmetricTree(root.left, root.right)

        
