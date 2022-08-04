# https://leetcode.com/problems/add-to-array-form-of-integer/


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        numx = ""
        
        for each in num:
            numx += str(each)
        numx = int(numx)
        
        return list(str(numx+k))
        
