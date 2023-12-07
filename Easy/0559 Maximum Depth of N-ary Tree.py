# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        maxi = 0

        for each in root.children:
            maxi = max(maxi, self.maxDepth(each))

        return maxi+1
