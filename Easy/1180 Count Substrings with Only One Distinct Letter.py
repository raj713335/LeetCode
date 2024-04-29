# https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/description/


class Solution:
    def countLetters(self, s: str) -> int:

        count = 0

        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                if len(set(s[i:j])) == 1:
                    count += 1

        return count
        
