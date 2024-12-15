# https://leetcode.com/problems/button-with-longest-push-time/description/

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:

        prev = events[0][1] 
        max_time = events[0][1] 
        max_value = events[0][0] 

        for i in range(1, len(events)):

            time = events[i][1] - prev
            prev = events[i][1]

            if time > max_time:
                max_time = time
                max_value = events[i][0]

            if time == max_time:
                max_value = min(max_value, events[i][0])

        return max_value

        
