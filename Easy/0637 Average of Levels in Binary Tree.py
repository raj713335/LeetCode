# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        dictx = {}
        res = []

        level = 0

        def dfs(root, level):

            if not root:
                return 
            
            if level not in dictx:
                dictx[level] = [root.val]
            else:
                dictx[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, level)

        for key, val in dictx.items():
            temp = sum(val)/len(val)
            res.append(temp)

        return res
        
