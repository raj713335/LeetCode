# https://leetcode.com/problems/faulty-sensor/description/


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:

        ans = -1

        for i in range(0, len(sensor1)-1):
            if sensor1[i] == sensor2[i]:
                continue
            elif sensor1[i] == sensor2[i+1] and sensor1[i+1] != sensor2[i]:
                return 1
            elif sensor1[i+1] == sensor2[i] and sensor1[i] != sensor2[i+1]:
                return 2
        
        return ans
        
