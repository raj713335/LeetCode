# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dictx = {}

        for i in range(0, len(nums)):
            if nums[i] not in dictx:
                dictx[nums[i]] = i
            else:
                if i - dictx[nums[i]] <= k:
                    return True
                else:
                    dictx[nums[i]] = i

        return False
        
