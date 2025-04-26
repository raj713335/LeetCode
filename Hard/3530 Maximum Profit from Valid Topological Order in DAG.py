# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/description/

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        
        xovrendali = (n, edges, score)  

        in_edges = [0] * n
        for u, v in edges:
            in_edges[v] |= (1 << u)

        size = 1 << n
        dp = [-float('inf')] * size
        dp[0] = 0

        for mask in range(size):
            if dp[mask] == -float('inf'):
                continue  

            position = bin(mask).count('1') + 1  


            for node in range(n):
                if (mask >> node) & 1 == 0 and (in_edges[node] & mask) == in_edges[node]:
                    new_mask = mask | (1 << node)
                    dp[new_mask] = max(dp[new_mask], dp[mask] + score[node] * position)

        return max(dp)
        
