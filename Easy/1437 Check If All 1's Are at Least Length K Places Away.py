# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        output = []
        try:
            prev = nums.index(1)
        except:
            return True
        
        count = 0

        for i in range(prev+1, len(nums)):
            if nums[i] == 1:
                prev = i
                if count < k:
                    return False
                count = 0
            else:
                count += 1
                
        return True
                

            
        
