# https://leetcode.com/problems/valid-elements-in-an-array/description/


class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:

        output = []

        for i in range(1, len(nums)-1):
            flag = False

            for j in range(i-1, -1, -1):
                flag = True
                if nums[i] <= nums[j]:
                    flag = False
                    break
            
            if flag:

                output.append(nums[i])
                flag = False

            else:
                for j in range(i+1, len(nums)):
                    flag = True
                    if nums[i] <= nums[j]:
                        flag = False
                        break

                if flag:
                    output.append(nums[i])

        output.insert(0, nums[0])

        if len(nums) != 1:
            output.append(nums[-1])

        return output
        
