# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        res = []

        q = deque([root])

        while q:

            temp = []

            for _ in range(0, len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    if node.children:
                        for each in node.children:
                            q.append(each)
            
            if len(temp) > 0:
                res.append(temp)

        return res
        
