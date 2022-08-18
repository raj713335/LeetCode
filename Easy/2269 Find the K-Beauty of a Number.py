# https://leetcode.com/problems/find-the-k-beauty-of-a-number/


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        count = 0
        
        for i in range(0, len(str(num))-k+1):
            try:
                if num % int(str(num)[i:i+k]) == 0:
                    count += 1
            except:
                pass
                
        return count
        
