# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        subtreeSums = set()
        
        def getSum(node):
            if not node:
                return 0
            elif not node.left and not node.right:
                subtreeSums.add(node.val)
                return node.val
            else:
                result = getSum(node.left) + getSum(node.right) + node.val
                subtreeSums.add(result)
                return result
            
        rootSum = getSum(root)
        idealSplit = rootSum/2
        closestToIdeal = 0
        
        for possibleSum in subtreeSums:
            if math.fabs(possibleSum - idealSplit) < math.fabs(closestToIdeal - idealSplit):
                closestToIdeal = possibleSum        
        
        return (((rootSum - closestToIdeal) % (10**9 + 7)) * (closestToIdeal % (10**9 + 7)))  % (10**9 + 7)
