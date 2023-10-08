# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/


class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        hill_valley = 0
        length = len(nums)

        mexa = [0, 0, 0]

        for i in range(1, length-1):
            l, r = i - 1, i + 1

            while nums[i] == nums[l]:
                l -= 1
                if l <= 0:
                    l = 0
                    break

            while nums[i] == nums[r]:
                r += 1
                if r >= (length-1):
                    r = (length-1)
                    break

            if nums[i] > nums[l] and nums[i] > nums[r]:
                temp = [nums[l], nums[i], nums[r]]
                if mexa != temp:
                    #print(i, nums[l], nums[i], nums[r], "hill", l , r)
                    hill_valley += 1
                    mexa = temp
            elif nums[i] < nums[l] and nums[i] < nums[r]:
                temp = [nums[l], nums[i], nums[r]]
                if mexa != temp:
                    #print(i, nums[l], nums[i], nums[r], "valley", l ,r)
                    hill_valley += 1
                    mexa = temp

        return hill_valley
        
