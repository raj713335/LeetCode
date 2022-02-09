# https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = set()
        
        nums = sorted(nums)
        
        for l in range(0, len(nums)-3):
            for k in range(l+1, len(nums)-2):
                
                i, j = k+1, len(nums)-1
                
                while (i<j):
                    four_sum = nums[l]+nums[k]+nums[i]+nums[j]
                    
                    if four_sum > target:
                        j -= 1
                    elif four_sum < target:
                        i += 1
                    else:
                        result.add((nums[l],nums[k],nums[i],nums[j]))
                        i += 1
                        j -= 1
                        
        return result
        
