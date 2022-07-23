# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        dictx = {}
        words = 0
        
        for each in brokenLetters:
            dictx[each] = 1
            
        text = text.split(" ")
            
        for word in text:
            flag = True
            for each in word:
                if each in dictx:
                    flag = False
            if flag:
                words += 1
                
        return words
        
