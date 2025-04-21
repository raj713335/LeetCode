
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        
        def helper(node):
            if not node:
                return 0
            
            # Recursively get the max sum from left and right subtrees
            left = max(helper(node.left), 0)  # Ignore negative paths
            right = max(helper(node.right), 0)  # Ignore negative paths
            
            # Current path sum including the current node and both children
            current_sum = node.data + left + right
            
            # Update the global max_sum
            nonlocal max_sum
            max_sum = max(max_sum, current_sum)
            
            # Return the maximum path sum for the current node to its parent
            return node.data + max(left, right)
    
        max_sum = float('-inf')
        helper(root)
        return max_sum
