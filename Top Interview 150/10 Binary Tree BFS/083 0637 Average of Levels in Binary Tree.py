# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []

        q = collections.deque([root])
        res = []

        while q:
            sumx = 0
            count = 0

            for _ in range(0, len(q)):
                curr = q.popleft()
                sumx += curr.val
                count += 1

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

            res.append(sumx/count)

        return res
