# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        res = [] # res[i] = height of LIS ending at i & including nums[i]
        dp = [float("inf")] * (len(obstacles)+1) #dp[i], where i = length of LIS, is the smallest ending value
        for obs in obstacles:
            index = bisect.bisect(dp, obs)
            res.append(index+1)
            dp[index] = obs

        return res
        
