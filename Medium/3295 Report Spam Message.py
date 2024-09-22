# https://leetcode.com/problems/report-spam-message/

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        
        banned_words = {}
        
        for each in bannedWords:
            if each not in banned_words.keys():
                banned_words[each] = 1
                
        count = 0
        
        for each in message:
            if each in banned_words.keys():
                count += 1
                
                
        if count >= 2:
            return True
        else:
            return False
        
