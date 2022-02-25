# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dictx = {"X++":1,"++X":1,"--X":-1,"X--":-1}
        x = 0
        
        for i in range(0, len(operations)):
            x = x+dictx[operations[i]]
            
        return x
        
