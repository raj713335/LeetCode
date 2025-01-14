# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = collections.deque([root])
        res = []
        depth = 0

        while q:
            temp = []
            depth += 1
            for _ in range(0, len(q)):

                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            if depth % 2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)

        return res
