# https://leetcode.com/problems/minimum-time-to-complete-trips/description/

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        right = min(time) * totalTrips + 1
        left = 0
        answer = 0

        def trips(mid):
            nonlocal answer
            count = 0    
            for each in time:
                count += (mid//each)
          
            if count < totalTrips:
                return -1
            elif count >= totalTrips:
                answer = mid
                return 1


        
        while left < right-1:
            mid = (left+right) //2

            res = trips(mid)

            if res == -1:
                left = mid
            else:
                right = mid

        return answer

