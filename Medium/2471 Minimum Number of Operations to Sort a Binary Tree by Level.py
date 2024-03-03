# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def minSwaps(arr): 
            n = len(arr) 
            arrpos = [*enumerate(arr)] 
            arrpos.sort(key=lambda it: it[1]) 
            vis = {k: False for k in range(n)} 
            ans = 0
            for i in range(n): 
                if vis[i] or arrpos[i][0] == i: 
                    continue
                cycle_size = 0
                j = i 
                while not vis[j]: 
                    vis[j] = True
                    j = arrpos[j][0] 
                    cycle_size += 1
                if cycle_size > 0: 
                    ans += (cycle_size - 1) 
            return ans 

        count = 0

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
                count += minSwaps(temp)

        return count
        
