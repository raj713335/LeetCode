# https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        val = list(words[0])
        
        for i in range(1, len(words)):
            
            count = 0 
            temp = []
            word = list(words[i])
            while(count< len(val)):
                if val[count] in word:
                    word.remove(val[count])
                else:
                    temp.append(count)
                count += 1
            
            iterx = 0
            for each in temp:
                del val[each - iterx]
                iterx += 1
                
                
        return val
        
