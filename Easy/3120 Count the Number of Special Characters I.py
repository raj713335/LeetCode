# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        word = set(list(word))

        dictx = {}
        count = 0

        for each in word:
            if each.lower() not in dictx.keys():
                dictx[each.lower()] = 1
            else:
                count += 1

        return count 
        
