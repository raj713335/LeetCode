# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        
        for i in range(0, len(nums)-k+1):
            start = nums[i]
            flag = True
            for j in range(i+1, i+k):
                if start + 1 != nums[j]:
                    res.append(-1)
                    flag = False
                    break
                else:
                    start = nums[j]
                    
            if flag:
                res.append(start)
            
        return res
        
