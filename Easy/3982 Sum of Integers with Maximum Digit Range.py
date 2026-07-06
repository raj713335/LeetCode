# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/description/


class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:

        dictx = {}

        max_range = 0

        for numbers in nums:
            num = str(numbers)
            maxi = max(num)
            mini = min(num)

            rangeo = int(maxi) - int(mini)

            if rangeo > max_range:
                max_range = rangeo

            if numbers not in dictx.keys():

                dictx[int(numbers)] = [rangeo, 1]
            else:
                dictx[int(numbers)][1] += 1

        
        result = 0

        for key, value in dictx.items():
            if value[0] == max_range:
                result += (key * value[1])

        return result
        
