# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return []

        q = collections.deque([root])
        res = []
        min_difference = math.inf

        while q:
            temp = []
            for _ in range(0, len(q)):

                curr = q.popleft()
                res.append(curr.val)

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

        res = sorted(res)

        return res[k-1]
