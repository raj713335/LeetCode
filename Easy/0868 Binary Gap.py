# https://leetcode.com/problems/binary-gap/


class Solution:
    def binaryGap(self, n: int) -> int:
        
        n = bin(n)[2:]
        
        max_gap = 0
        temp = 0
        
        prev = n.index("1")
        
        for i in range(prev+1, len(n)):
            if n[i] == "0":
                temp += 1
            else:
                temp += 1
                prev = i
                if temp > max_gap:
                    max_gap = temp
                temp = 0
                
        return max_gap
        
