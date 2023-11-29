# https://leetcode.com/problems/1-bit-and-2-bit-characters/


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ret = True
        for bit in bits[-2::-1]:
            if bit: 
                ret = not ret
            else: 
                break
        return ret
        
