# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        res = []
        strx = ""
        sumx = 0

        def binaryToDecimal(binary):
            decimal, i = 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1

            return decimal

        def dfs(root, strx):

            if not root:
                return
            
            if not root.left and not root.right:
                strx += str(root.val)
                res.append(strx)
                strx = ""

            strx += str(root.val)
            dfs(root.left, strx)
            dfs(root.right, strx)

        dfs(root, strx)

        for each in res:
            sumx += binaryToDecimal(int(each))
        
        return sumx

        
