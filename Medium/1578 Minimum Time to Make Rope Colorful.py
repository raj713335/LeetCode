# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        i = 0
        total_time = 0
        colors = list(colors)

        while (i < len(colors)-1):
            if colors[i] == colors[i+1]:
                if neededTime[i] < neededTime[i+1]:
                    total_time += neededTime[i]
                    del colors[i]
                    del neededTime[i]
                else:
                    total_time += neededTime[i+1]
                    del colors[i+1]
                    del neededTime[i+1]
            else:
                i += 1

        return total_time

        
