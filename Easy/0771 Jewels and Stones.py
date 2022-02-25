# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count = 0
        
        for i in range(0, len(jewels)):
            for j in range(0, len(stones)):
                if jewels[i] == stones[j]:
                    count += 1
                    
        return count
        
