# https://leetcode.com/problems/find-right-interval/description/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)

        mapping = {}
        res = [-1] * n

        for idx, value in enumerate(intervals):
            mapping[(value[0], value[1])] = idx

        
        intervals = sorted(intervals)

        for i in range(0, n):
            l = 0
            r = n - 1

            while l <= r:
                mid = (l+r)//2

                if intervals[mid][0] < intervals[i][1]:
                    l = mid + 1
                elif intervals[mid][0] >= intervals[i][1]:
                    r = mid - 1

            try:
                res[mapping[(intervals[i][0], intervals[i][1])]] = mapping[(intervals[l][0], intervals[l][1])]
            except:
                res[mapping[(intervals[i][0], intervals[i][1])]] = -1

            
        return res
            
