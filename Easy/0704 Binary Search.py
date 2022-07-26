# https://leetcode.com/problems/binary-search/

import sys
sys.setrecursionlimit(1500)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
                
        low = 0
        high = len(nums)-1
        
        def binary_search(nums, target, low, high):
            
            if high >= low:
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(nums, target, low, mid-1)
                else:
                    return binary_search(nums, target, mid+1, high)
            else:
                return -1

            
        result = binary_search(nums, target, low, high)

        return result
        

        
