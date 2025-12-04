# https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:

        res = []

        while root:
            res.append(root.val)
            root = root.next

        return res
        
