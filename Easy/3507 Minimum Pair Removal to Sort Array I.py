# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        count = 0

        flag = True

        while flag:
            flag = False
            min_sum = float('inf')
            index = -1
            for i in range(0, len(nums)-1):
                if nums[i] > nums[i+1]:
                    flag = True

                temp_sum = nums[i] + nums[i+1]

                if temp_sum < min_sum:
                    min_sum = temp_sum
                    index = i
            
            if flag:
                count += 1
                nums[index] = min_sum
                del nums[index+1]

        return count
        
