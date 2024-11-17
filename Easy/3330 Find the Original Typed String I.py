# https://leetcode.com/problems/find-the-original-typed-string-i/description/

class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        count = 1

        for i in range(1, len(word)):
            if word[i-1] == word[i]:
                count += 1

        return count

