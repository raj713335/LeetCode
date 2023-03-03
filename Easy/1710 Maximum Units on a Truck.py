# https://leetcode.com/problems/maximum-units-on-a-truck/description/


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        res = 0

        boxTypes = sorted(boxTypes, key= lambda x: x[1], reverse = True)

        while truckSize > 0 and boxTypes:

            if truckSize >= boxTypes[0][0]:
                res += (boxTypes[0][0] * boxTypes[0][1])
                truckSize -= boxTypes[0][0]
            else:
                res += (truckSize * boxTypes[0][1])
                truckSize -= boxTypes[0][0]

            boxTypes.pop(0)


        return res
        
