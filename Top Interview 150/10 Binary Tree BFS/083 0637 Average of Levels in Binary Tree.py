# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if not root:
            return []

        stack = collections.deque([root])

        res = []

        while stack:
            sumx = 0
            count = 0
            for _ in range(0, len(stack)):
                
                curr = stack.popleft()
                sumx += curr.val
                count += 1

                if curr.left:
                    stack.append(curr.left)
                
                if curr.right:
                    stack.append(curr.right)
            
            res.append(sumx/count)

        return res
