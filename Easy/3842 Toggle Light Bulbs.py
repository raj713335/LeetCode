# https://leetcode.com/problems/toggle-light-bulbs/description/

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:

        bulbs_list = [False] * 100

        for each in bulbs:
            if bulbs_list[each-1] == False:
                bulbs_list[each-1] = True
            else:
                bulbs_list[each-1] = False

        result = []

        for i in range(0, 100):
            if bulbs_list[i] == True:
                result.append(i+1)

        return result

        
