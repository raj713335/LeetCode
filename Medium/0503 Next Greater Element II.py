# https://leetcode.com/problems/next-greater-element-ii/description/


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []

        for j in range(0, len(nums)):
            flag = True
            index = j
            val = -1
            for i in range(index+1, len(nums)):
                if nums[i] > nums[j]:
                    val = nums[i]
                    flag = False
                    break

            if flag:
                for i in range(0, index+1):
                    if nums[i] > nums[j]:
                        val = nums[i]

                        break
            output.append(val)

        return output
        
