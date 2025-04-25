# https://leetcode.com/problems/path-sum-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle case when path from root equals target

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_sums[curr_sum - targetSum]
            
            prefix_sums[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1  # backtrack

            return count

        return dfs(root, 0)
        
