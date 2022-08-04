# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) == 1:
            return True
        
        if word[0].isupper():
            if word[1].isupper():
                for each in word[2:]:
                    if each.islower():
                        return False
            else:
                for each in word[1:]:
                    if each.isupper():
                        return False
                    
        else:
            for each in word[1:]:
                if each.isupper():
                    return False
        return True
        
