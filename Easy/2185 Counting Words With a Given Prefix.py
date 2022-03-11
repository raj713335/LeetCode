# https://leetcode.com/problems/counting-words-with-a-given-prefix/

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        res = 0
        
        for each in words:
            if len(each) >= len(pref):
                if each[:len(pref)] == pref:
                    res += 1
        return res
                
