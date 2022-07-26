# https://leetcode.com/problems/count-prefixes-of-a-given-string/


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        
        count = 0
        
        for each in words:
            if each == s[0:len(each)]:
                count += 1
                
        return count
        
