# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        result = 0 
        mapping = defaultdict(int)
        for t in time:
            key = t % 60
            if key == 0:
                result += mapping[0]
            else:
                result += mapping[60 - key]
            mapping[key] += 1
        return result
        
