# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_vol = 0
        
        i, j = 0, len(height) - 1

        while i < j:

            temp_vol = min(height[i], height[j]) * (j-i)

            if temp_vol > max_vol:
                max_vol = temp_vol

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return max_vol
