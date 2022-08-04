# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = list(map(str, sentence.split(" ")))
        
        word_len = len(searchWord)
        
        for i in range(0, len(sentence)):
            if len(sentence[i]) >= word_len:
                if sentence[i][0:word_len] == searchWord:
                    return i+1
                
        return -1
            
        
