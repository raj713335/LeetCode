# https://leetcode.com/problems/minimum-cost-to-merge-stones/description/

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:

        n = len(stones)
    
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]
        

        memo = {}
        
        def dp(i, j, piles):
            if i == j:
                return 0 if piles == 1 else float('inf')
            
            if (i, j, piles) in memo:
                return memo[(i, j, piles)]
            
            # If we want 1 pile, first merge into k piles, then combine
            if piles == 1:
                cost = dp(i, j, k) + prefix[j+1] - prefix[i]
                return cost
            
            min_cost = float('inf')
            # Try splitting at every valid mid point
            for mid in range(i, j, k-1):
                left = dp(i, mid, 1)
                right = dp(mid+1, j, piles-1)
                min_cost = min(min_cost, left + right)
            
            memo[(i, j, piles)] = min_cost
            return memo[(i, j, piles)]
        
        return dp(0, n-1, 1)
        
