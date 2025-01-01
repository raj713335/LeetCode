# https://leetcode.com/problems/cousins-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        dictx = {}
        stack = []
        level = 0
        curr = root
        head = None

        while curr or stack:
            while curr:
                stack.append([curr, level, head])
                head = curr.val
                curr = curr.left
                level += 1
            
            curr, level, headx = stack.pop()
            dictx[curr.val] = [level, headx]

            head = curr.val
            curr = curr.right
            level += 1


        if dictx[x][0] == dictx[y][0] and dictx[x][1] != dictx[y][1]:
            return True
        
        return False
