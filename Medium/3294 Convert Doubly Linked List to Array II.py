# https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:

        res = []

        root = node

        while root:
            res.append(root.val)
            root = root.prev

        res = res[::-1]

        root = node
        root = root.next

        while root:
            res.append(root.val)
            root = root.next

        return res
        
        
