# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        list1 = nums[:n]
        list2 = nums[n:]
        
        res = []
        
        for i in range(0, n):
            res.append(list1[i])
            res.append(list2[i])
            
        return res
            
        
