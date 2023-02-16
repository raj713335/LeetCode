# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        dictx = {}

        for i in range(0, len(numbers)):
            dictx[numbers[i]] = i+1

        for i in range(0, len(numbers)):
            if numbers[i] == target:
                return sorted([i+1, dictx[0]])
            temp = target - numbers[i]
            if temp in dictx:
                if numbers[i] != temp:
                    return [i+1, dictx[temp]]
                elif numbers[i] == numbers[i+1]:
                    return [i+1, i+2]

            

