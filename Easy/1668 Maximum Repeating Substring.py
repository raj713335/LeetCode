# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        k = 0
		
        while True:
		
            if k*word not in sequence:
                return k-1
				
            k+=1
            
        
