# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        nodes = [root]

        while nodes[0] != None:
            temp = nodes.pop(0)
            nodes.append(temp.left)
            nodes.append(temp.right)

        for each in nodes:
            if each != None:
                return False
        
        return True

