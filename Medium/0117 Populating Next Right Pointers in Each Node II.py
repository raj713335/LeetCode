# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:
            l = len(q)
            prev = None

            for _ in range(l):

                curr = q.popleft()

                if prev:
                    prev.next = curr
                
                prev = curr

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return root
