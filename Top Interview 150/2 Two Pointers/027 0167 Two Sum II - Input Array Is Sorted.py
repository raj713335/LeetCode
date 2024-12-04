# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i, j = 0, len(numbers)-1

        while i < j:
            temp = numbers[i] + numbers[j]
            if temp < target:
                i += 1
            elif temp > target:
                j -= 1
            else:
                return [i+1, j+1]
