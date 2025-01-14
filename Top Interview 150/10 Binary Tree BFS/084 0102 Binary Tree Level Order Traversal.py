# https://leetcode.com/problems/binary-tree-level-order-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        stack = collections.deque([root])

        res = []

        while stack:
            temp = []
            for _ in range(0, len(stack)):
                
                curr = stack.popleft()
                temp.append(curr.val)


                if curr.left:
                    stack.append(curr.left)
                
                if curr.right:
                    stack.append(curr.right)
            
            res.append(temp)

        return res
        
