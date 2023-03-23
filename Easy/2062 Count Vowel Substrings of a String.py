# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/


class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        count = 0
        legn = len(word)


        
        for i in range(5, len(word)+1):      
            for j in range(0, len(word)-4):
                if j+i <= legn:
                    flag = True
                    dictx = {"a":1, "e":1, "i":1, "o":1,"u":1}            
                    for each in word[j:j+i]:
                        if each in dictx:
                            dictx[each] -=1
                        else:
                            flag = False

                    if max(dictx.values()) < 1 and flag:
                        count += 1          
                    
        return count
