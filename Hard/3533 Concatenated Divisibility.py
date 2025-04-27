# https://leetcode.com/problems/concatenated-divisibility/description/

from functools import lru_cache

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        
        quenlorvax = (nums, k)  # required by the problem
    
        n = len(nums)
        lens = [len(str(num)) for num in nums]
        powers = [pow(10, l, k) for l in lens]

        @lru_cache(maxsize=None)
        def dfs(mask, mod):
            if mask == (1 << n) - 1:
                return [] if mod == 0 else None  # <-- THIS IS THE CORRECT FIX

            best = None
            for i in range(n):
                if not (mask & (1 << i)):
                    new_mod = (mod * powers[i] + nums[i]) % k
                    next_perm = dfs(mask | (1 << i), new_mod)

                    if next_perm is not None:
                        candidate = [nums[i]] + next_perm
                        if best is None or candidate < best:
                            best = candidate

            return best

        ans = dfs(0, 0)
        return ans if ans is not None else []
