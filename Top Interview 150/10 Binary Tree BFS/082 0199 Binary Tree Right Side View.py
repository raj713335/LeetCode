# https://leetcode.com/problems/binary-tree-right-side-view/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        if not root:
            return []

        stack = collections.deque([root])

        res = []

        while stack:
            prev = None
            for _ in range(0, len(stack)):
                
                curr = stack.popleft()
                prev = curr

                if curr.left:
                    stack.append(curr.left)
                
                if curr.right:
                    stack.append(curr.right)
            
            res.append(prev.val)

        return res