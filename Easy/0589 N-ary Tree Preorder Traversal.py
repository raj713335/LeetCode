# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def order(root):
            if root is None: return None
            arr.append(root.val)
            for i in root.children:
                order(i)    
        order(root)
        return arr
        
