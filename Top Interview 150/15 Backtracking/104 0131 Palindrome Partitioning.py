# https://leetcode.com/problems/palindrome-partitioning/description/


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        res = []

        def isPalindrome(s, l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(part[:])
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

        
        
