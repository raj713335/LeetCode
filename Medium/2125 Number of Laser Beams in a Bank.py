# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        count = 0
        prev = bank[0].count("1")
        
        for each in bank[1:]:
            temp = each.count("1")
            if temp > 0:
                count += (prev*temp)
                prev = temp
        return count
            
        
