# https://leetcode.com/problems/check-if-n-and-its-double-exist/


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for each in arr:
            
            if each*2 in arr:
                if each == 0:
                    if arr.count(0) > 1:
                        return True
                else:
                    return True
        return False
        
