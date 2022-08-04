# https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n = list(str(n))[::-1]
        count = 0
        for i in range(3, len(n), 3):
            n.insert(i+count , ".")
            count += 1
            
        return "".join(n[::-1])
        
