# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

import math 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        val = -1
        L, R = 0, len(nums)
        while (L != R):
            index = math.ceil((L + R) // 2)

            if nums[index] == target:
                val = index
                break
            elif nums[index] > target:
                R -= 1
            else:
                L += 1

        val_left = val
        val_right = val

        while val_left > 0:
            try:
                val_left -= 1
                if nums[val_left] == target:
                    continue

                else:
                    val_left += 1
                    break
            except:
                val_left += 1
                break

        while val_right < len(nums):
            try:
                val_right += 1

                if nums[val_right] == target:
                    continue

                else:
                    val_right -= 1
                    break
            except:
                val_right-=1
                break
        return [val_left, val_right]
            
