# https://leetcode.com/problems/last-stone-weight-ii/description/

# partition the array into two groups with minimum difference" problem


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        total = sum(stones)
        memo = {}

        def dfs(i, curr_sum):
            if i == len(stones):
                return abs((total - curr_sum) - curr_sum)
            
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            # Two choices: pick or not pick current stone
            pick = dfs(i + 1, curr_sum + stones[i])
            not_pick = dfs(i + 1, curr_sum)
            
            memo[(i, curr_sum)] = min(pick, not_pick)
            return memo[(i, curr_sum)]
        
        return dfs(0, 0)
            
