# https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/description/


class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        ans = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            counts[s[r]]+=1
            ans+=counts[s[r]]
        return ans
        
