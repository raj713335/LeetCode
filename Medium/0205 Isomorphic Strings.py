# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map1 = []
        map2 = []

        for idx in s:
            map1.append(s.index(idx))

        for idx in t:
            map2.append(t.index(idx))

        if map1 == map2:
            return True
            
        return False
        
