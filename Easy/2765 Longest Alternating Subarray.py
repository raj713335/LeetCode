# https://leetcode.com/problems/longest-alternating-subarray/description/


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:

        max_count = 0
        flag = True
        count = 0

        for i in range(1, len(nums)):

            temp = nums[i] - nums[i-1]

            if flag and temp == 1:
                count += 1
                flag = False
            elif flag!= True and temp == -1:
                count += 1
                flag = True
            else:
                max_count = max(count, max_count)
                if temp == 1:
                    count = 1
                    flag = False
                else:
                    count = 0
                    flag = True
                    
        max_count = max(count, max_count)

        if max_count == 0:
            return -1
        else:
            return max_count+1




