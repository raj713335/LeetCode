# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        dictx = {}

        for each in arr1:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        for each in arr2:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        for each in arr3:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        ans = []

        for key, value in dictx.items():
            if value == 3:
                ans.append(key)

        return ans
        
