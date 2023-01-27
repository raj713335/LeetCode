# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        dictx = {}
        res = []
        prev = ""

        for each in words:
            temp = "".join(sorted(each))
            if temp not in dictx or prev !=temp:
                dictx[temp] = 1
                res.append(each)
                prev = temp

        return res
            
        
