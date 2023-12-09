# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        dictx = {}

        def dfs(root):

            if not root:
                return

            temp = root.val

            if temp not in dictx:
                dictx[temp] = 1
            else:
                dictx[temp] += 1

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        res = []

        maxi = max(dictx.values())

        for key, val in dictx.items():
            if val == maxi:
                res.append(key)

        return res
