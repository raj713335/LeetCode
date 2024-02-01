# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()

        res = []
        index = 0

        for i in range(1, len(nums)):
            if abs(nums[index] - nums[i]) <= k:
                continue
            else:
                res.append(nums[index:i])
                index = i

        
        res.append(nums[index:])
        print(res)
        return len(res)
                
        
