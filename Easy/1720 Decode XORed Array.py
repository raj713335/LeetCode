# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        
        for i in range(0, len(encoded)):
            res.append(res[-1]^encoded[i])
            
        return res
        
