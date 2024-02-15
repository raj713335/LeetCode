# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        valid_peri = 0
        count = 2
        valid_count = 0
        nums = sorted(nums)
        local_peri = nums[0] + nums[1]

        for i in range(2, len(nums)):
            if local_peri > nums[i]:
                local_peri += nums[i]
                count += 1
                valid_peri = local_peri
                valid_count = count
            else:
                local_peri += nums[i]
                count += 1

        if valid_count >= 3:
            return valid_peri
        else:
            return -1
            
        
