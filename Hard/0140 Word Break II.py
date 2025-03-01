# https://leetcode.com/problems/word-break-ii/description/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)  # Convert list to set for quick lookup
        res = []  # Store all possible segmentations

        def dfs(start, path):
            if start == len(s):
                res.append(" ".join(path))  # Join words with spaces
                return

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    dfs(end, path + [s[start:end]])  # Recur with new word added

        dfs(0, [])
        return res
        
