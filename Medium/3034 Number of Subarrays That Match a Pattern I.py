# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/description/

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        pattern_length = len(pattern)
        count = 0

        for i in range(0, len(nums)-pattern_length):
                temp = nums[i:i+pattern_length+1]
                flag = True
                for j in range(0, pattern_length):
                    if pattern[j] == 0:
                        if temp[j] != temp[j+1]:
                            flag = False
                            break
                    if pattern[j] == 1:
                        if temp[j] >= temp[j+1]:
                            flag = False
                            break
                    if pattern[j] == -1:
                        if temp[j] <= temp[j+1]:
                            flag = False
                            break
                if flag:
                    count += 1
                       
        return count
        
