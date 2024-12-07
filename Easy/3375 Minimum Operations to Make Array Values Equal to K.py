https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        min_value = min(nums)
        
        if min_value < k:
            return -1
        
        count = 0
        
        nums_set = list(set(nums))
        
        for i in range(0, len(nums_set)):
            if nums_set[i] > k:
                count += 1
                
        return count
        
