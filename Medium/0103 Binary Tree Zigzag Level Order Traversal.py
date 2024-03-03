# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        flag = True
        res = []

        q = deque([root])

        while q:

            temp = []

            for _ in range(0, len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if len(temp) > 0:
                if flag:
                    res.append(temp)
                else:
                    res.append(temp[::-1])

                flag = not flag

        return res
        
