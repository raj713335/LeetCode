# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums = sorted(nums)

        n = len(nums)

        for k in range(0, n-2):
            i = k + 1
            j = n - 1

            temp = - nums[k]

            while i < j:
                temp_inner = nums[i] + nums[j]
                
                if temp_inner > temp:
                    j -= 1
                elif temp_inner < temp:
                    i += 1
                else:
                    res.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1

        return list(res)

