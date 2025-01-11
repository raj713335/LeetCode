# https://leetcode.com/problems/binary-search-tree-iterator/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.root = root
        self.stack = collections.deque()

        def dfs(root):
            if not root:
                return 
            
            dfs(root.left)
            self.stack.append(root.val)
            dfs(root.right)

        dfs(self.root)


    def next(self) -> int:
        return self.stack.popleft()

    def hasNext(self) -> bool:
        
        if len(self.stack) > 0:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

