# https://leetcode.com/problems/increasing-order-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        stack = collections.deque()

        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)

        dfs(root)

        new_root = None
        while stack:
            curr = stack.popleft()

            if not new_root:
                new_root = TreeNode(curr)
                node = new_root
            else:
                node.left = None
                node.right = TreeNode(curr)
                node = node.right

        return new_root
