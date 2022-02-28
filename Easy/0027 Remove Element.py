# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums.sort(key=lambda x: int(x == val))

        return len(nums) - nums.count(val)
        
