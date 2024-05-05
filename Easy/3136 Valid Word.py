# https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:

        if len(word)>=3 and word.isalnum():
            word = word.lower()
            c, v = 0, 0
            for i in word:
                if i in "aeiou":
                    v = 1
                elif i in "bcdfghjklmnpqrstvwxyz":
                    c = 1
                
                if c and v:
                    return True

        return False

        
