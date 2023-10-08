# https://leetcode.com/problems/path-crossing/description/

class Solution:
    def isPathCrossing(self, path: str) -> bool:

        path=list(path)
        i,j=0,0
        k=[]
        k.append([i,j])
        for l in path:
            if l=='N':
                j+=1
            if l=='S':
                j-=1
            if l=='E':
                i+=1
            if l=='W':
                i-=1
            k.append([i,j])

        for m in k:
            if k.count(m)>1:
                return True
        return False

        
