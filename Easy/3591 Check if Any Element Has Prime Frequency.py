# https://leetcode.com/problems/check-if-any-element-has-prime-frequency/description/

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        dictx = {}

        for i in range(0, len(nums)):
            if nums[i] not in dictx:
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1

        values = list(set(dictx.values()))


        for i in range(0, len(values)):
            if values[i] == 2:
                return True

            if values[i] == 1:
                continue

            flag = True

            for j in range(2, values[i]):
                if values[i] % j == 0:
                    flag = False

            if flag == True:
                return True

        
        return False
        
        
