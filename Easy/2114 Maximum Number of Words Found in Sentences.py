# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for i in range(0, len(sentences)):
            temp = len(list(sentences[i].split(" ")))
            if temp > max_words:
                max_words = temp
                
        return max_words
        
