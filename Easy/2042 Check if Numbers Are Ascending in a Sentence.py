# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/


import math

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        s = s.split(" ")
        
        prev = -math.inf
        
        for each in s:
            try:
                if int(each) > prev:
                    prev = int(each)
                else:
                    return False
            except:
                pass
            
        return True
        
        
