# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr.left:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                q.append(curr.left)
                q.append(curr.right)

        return root

        # cur, nxt = root, root.left if root else None


        # while cur and nxt:
        #     cur.left.next = cur.right
        #     if cur.next:
        #         cur.right.next = cur.next.left

        #     cur = cur.next
        #     if not cur:
        #         cur = nxt
        #         nxt = cur.left

        # return root
        
