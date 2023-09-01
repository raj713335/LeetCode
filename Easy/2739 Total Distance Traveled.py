# https://leetcode.com/problems/total-distance-traveled/


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        distance = 0

        while mainTank > 0:
            if mainTank >= 5:
                mainTank -= 5
                distance += 5
                if additionalTank >= 1:
                    additionalTank -= 1
                    mainTank += 1
            if mainTank < 5:
                distance += mainTank
                mainTank = 0

        return distance*10
        
