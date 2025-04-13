# https://leetcode.com/problems/maximum-length-of-pair-chain/description/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()
        
        n = len(pairs)

        dp = {}

        def LIS(index, prev):

            if index == n:
                return 0
            elif (index, prev) in dp:
                return dp[(index, prev)]

            take = 0


            if  pairs[index][0] > prev:
                take = 1 + LIS(index + 1, pairs[index][1])
            
            skip = LIS(index +  1, prev)
                
            dp[(index, prev)] = max(take, skip)
            return dp[(index, prev)] 

        return LIS(0, float("-inf"))
        
