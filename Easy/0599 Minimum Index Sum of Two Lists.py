# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dictx = {}

        output = []

        for i in range(0, len(list1)):
            for j in range(0, len(list2)):
                if list1[i] == list2[j]:
                    dictx[list1[i]] = i+j

        minx = min(dictx.values())

        for key, val in dictx.items():
            if val == minx:
                output.append(key)
        
        return output
