# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        index = 0
        
        for i in range(0, len(word)):
            if word[i] == ch:
                index = i
                break
                
        return word[:index+1][::-1]+word[index+1:]
        
