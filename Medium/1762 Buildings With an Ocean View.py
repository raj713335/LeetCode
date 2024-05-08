# https://leetcode.com/problems/buildings-with-an-ocean-view/description/

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        maxi = 0

        res = []


        for i in range(len(heights)-1, -1, -1):
            print(heights[i], maxi, i)
            if heights[i] > maxi:
                res.append(i)
                maxi = heights[i]

        return res[::-1]

        
