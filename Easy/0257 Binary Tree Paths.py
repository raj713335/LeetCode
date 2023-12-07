# https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        ans = []

        def dfs(root: Optional[TreeNode], path: List[str]) -> None:
          if not root:
            return
          if not root.left and not root.right:
            ans.append(''.join(path) + str(root.val))
            return

          path.append(str(root.val) + '->')
          dfs(root.left, path)
          dfs(root.right, path)
          path.pop()

        dfs(root, [])
        return ans
