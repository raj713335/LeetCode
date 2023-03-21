# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        count = 0
        
        flag = False
        temp = 0 

        for i in range(0, len(nums)):
            
            if nums[i] == 0:
                flag = True
                temp += 1
            else:
                if flag:
                    flag = False

            if flag == False:
                while temp > 0:
                    count += temp
                    temp -= 1

        while temp > 0:
            count += temp
            temp -= 1


        return count
        
