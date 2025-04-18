# https://leetcode.com/problems/scramble-string/description/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        memo = {}

        def helper(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            if a == b:
                memo[(a, b)] = True
                return True

            if sorted(a) != sorted(b):  # pruning optimization
                memo[(a, b)] = False
                return False

            n = len(a)
            for i in range(1, n):
                # Check without swapping
                if helper(a[:i], b[:i]) and helper(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Check with swapping
                if helper(a[:i], b[-i:]) and helper(a[i:], b[:-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return helper(s1, s2)
        
