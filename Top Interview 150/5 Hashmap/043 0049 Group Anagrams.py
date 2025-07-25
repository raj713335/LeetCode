# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictx = {}
        
        for each in strs:
            temp = "".join(sorted(each))
            if temp not in dictx:
                dictx[temp] = [each]
            else:
                dictx[temp].append(each)
                
        return list(dictx.values())
