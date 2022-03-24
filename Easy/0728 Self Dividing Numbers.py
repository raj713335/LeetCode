# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        
        for i in range(left, right+1):
            flag = True
            for each in str(i):
                if each =="0":
                    flag = False
                    break
                if i%int(each)!=0:
                    flag = False
                    break
                    
            if flag:
                res.append(i)
                
        return res
                
        
