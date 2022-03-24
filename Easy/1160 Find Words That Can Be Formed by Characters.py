# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        dictx = {}
        count = 0
        
        for each in chars:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        for char in words:
            wx = dictx.copy()
            flag = True
            for each in char:
                if each in wx:
                    if wx[each] > 0:
                        wx[each] -= 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                count += len(char)
                
        return count
                
                
        
