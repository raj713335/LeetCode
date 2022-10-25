# https://leetcode.com/problems/calculate-digit-sum-of-a-string/submissions/


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        
        while len(s) > k:
            
            temp = ""
            for i in range(0, len(s), k):
                var = sum(list(map(int, s[i:i+k])))  
                temp += str(var)

            s = temp
            
        return s
                    
        
