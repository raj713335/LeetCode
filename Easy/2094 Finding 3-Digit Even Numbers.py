# https://leetcode.com/problems/finding-3-digit-even-numbers/


from itertools import permutations 

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        
        ans = set()
        for x, y, z in permutations(digits, 3): 
            if x != 0 and z & 1 == 0: 
                ans.add(100*x + 10*y + z) 
        return sorted(ans)
            
        

        
