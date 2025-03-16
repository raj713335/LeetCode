# https://leetcode.com/problems/word-break/description/


# Time Complexity: O(n * m * k) (where n is the length of string `s`, m is the number of words in `wordDict`, and k is the average length of words in `wordDict`)
# Space Complexity: O(n) (due to the `dp` array of size `n + 1`)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        n = len(s)

        dp = [0] * (n+1)
        dp[-1] = 1

        for i in range(n-1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if i + word_len <= n and s[ i : i + word_len ] == word:
                    dp[i] = dp[ i + word_len]
                if dp[i]:
                    break

        return bool(dp[0])
