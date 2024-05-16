# https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/description/


# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        while root.len:
            length = max(root.left.len, len(root.left.val)) if root.left else 0
            if length >= k:
                root = root.left
            else:
                root = root.right
                k -= length
        return root.val[k - 1]
        
