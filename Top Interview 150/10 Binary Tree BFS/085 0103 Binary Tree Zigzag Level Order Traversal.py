# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        if not root:
            return []

        stack = collections.deque([root])

        res = []

        count = 0

        while stack:
            temp = []
            count += 1
            for _ in range(0, len(stack)):
                
                curr = stack.popleft()
                temp.append(curr.val)


                if curr.left:
                    stack.append(curr.left)
                
                if curr.right:
                    stack.append(curr.right)
            if count % 2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)

        return res
        
