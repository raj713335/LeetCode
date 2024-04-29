# https://leetcode.com/problems/diet-plan-performance/description/


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        points = 0

        calori =  sum(calories[0:0+k])
        if calori < lower:
                points -= 1
        elif calori > upper:
            points += 1

        for i in range(1, len(calories)-k+1):
            calori -=  calories[i-1]
            calori +=  calories[i+k-1]
            if calori < lower:
                points -= 1
            elif calori > upper:
                points += 1

        return points
        
