# https://leetcode.com/problems/simplified-fractions/


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        dictx = {}
        output = []
        
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i/j not in dictx:
                    dictx[i/j] = 1
                    output.append(str(i)+"/"+str(j))
                    
        return output
                    
        
