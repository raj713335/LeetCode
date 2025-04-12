# https://leetcode.com/problems/number-of-matching-subsequences/description/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        length = len(s)
        count = 0

        dp = {}

        def match_sequence(s1, s2, n, m):

            while n > -1 and m > -1:
                if s1[n] == s2[m]:
                    n -= 1
                    m -= 1
                else:
                    n -= 1

            return m

        for i in range(0, len(words)):

            if words[i] not in dp:
                res = match_sequence(s, words[i], length - 1, len(words[i]) - 1)
                dp[words[i]] = res 
            else:
                res = dp[words[i]]

            if res == -1:
                count += 1

        return count
                
        
