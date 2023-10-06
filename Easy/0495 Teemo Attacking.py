# https://leetcode.com/problems/teemo-attacking/description/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        count = 0 

        for i in range(0, len(timeSeries)-1):
            temp = timeSeries[i] + duration 
            if temp >= timeSeries[i+1]:
                count += timeSeries[i+1] - timeSeries[i]
            else:
                count += temp - timeSeries[i]
        
        return count + duration

        
