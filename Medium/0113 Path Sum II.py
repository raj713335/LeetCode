# https://leetcode.com/problems/path-sum-ii/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:


        def dfs(root, curr_sum, local_stack, stack):

            if not root:
                return
            
            curr_sum += root.val
            local_stack.append(root.val)

            if not root.left and not root.right:
                if curr_sum == targetSum:
                    stack.append(local_stack[::])

            
            dfs(root.left, curr_sum, local_stack, stack) 
            dfs(root.right, curr_sum, local_stack, stack)
            local_stack.pop()
        
        stack = []
        dfs(root, 0, [], stack)
        return stack
        
