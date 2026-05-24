# https://leetcode.com/problems/limit-occurrences-in-sorted-array/description/

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:

        length = len(nums)

        res = []

        new_element = nums[0]
        count = 0

        for i in range(0, length):
            if nums[i] == new_element:
                count += 1

                if count > k:
                    count -= 1
            
            else:
                res += [nums[i-1]] * count
                new_element = nums[i]
                count = 1

        res += [new_element] * count
        
        return res
        
