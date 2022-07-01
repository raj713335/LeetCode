# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        opx = []
        
        
        for i in range(1, n+1):
            if i in target:
                opx.append("Push")
            else:
                opx.extend(["Push", "Pop"])
            if i == target[-1]:
                break
                
        return opx
        
