# https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = [0]
        max_right = [0]

        max_left_height = 0
        max_right_height = 0

        sum_water = 0

        for i in range(1, len(height)):
            if height[i-1] > max_left_height:
                max_left.append(height[i-1])
                max_left_height = height[i-1]
            else:
                max_left.append(max_left_height)

        for i in range(len(height)-2, -1, -1):
            if height[i+1] > max_right_height:
                max_right.append(height[i+1])
                max_right_height = height[i+1]
            else:
                max_right.append(max_right_height)

        max_right = max_right[::-1]

        for i in range(0, len(height)):
            water_stored = min(max_left[i], max_right[i]) - height[i]

            if water_stored > 0:
                sum_water += water_stored

        return sum_water
