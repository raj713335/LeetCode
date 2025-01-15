# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
import math

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

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

        for i in range(0, len(res)-1):
            temp_diff = res[i+1] - res[i]
            if temp_diff < min_difference:
                min_difference = temp_diff



        return min_difference
        