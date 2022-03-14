# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        count = 0
        
        for i in range(0, len(patterns)):
            for j in range(0, len(word)-len(patterns[i])+1):
                if patterns[i] == word[j:j+len(patterns[i])]:
                    count += 1
                    break
        return count
        
