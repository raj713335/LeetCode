# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        counter = 0

        for each in nums:
            if each != val:
                nums[counter] = each
                counter += 1

        return counter 

        
