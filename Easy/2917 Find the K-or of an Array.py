# https://leetcode.com/problems/find-the-k-or-of-an-array/description/

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:

        res=0
        for i in range(32):
            count=0
            for num in nums:
                if(num&2**i):
                    count+=1
            if(count>=k):
                res+=2**i
        return res
        
