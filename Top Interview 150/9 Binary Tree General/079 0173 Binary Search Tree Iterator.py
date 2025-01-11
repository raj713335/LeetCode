# https://leetcode.com/problems/binary-search-tree-iterator/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

        self.root = root

        self.stack = []
        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            self.stack.append(root.val)
            dfs(root.right)

        dfs(self.root)

        self.stack[:] = self.stack[::-1]
        

    def next(self) -> int:
        return self.stack.pop()
        

    def hasNext(self) -> bool:
        if self.stack != []:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
