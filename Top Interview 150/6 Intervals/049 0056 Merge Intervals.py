# https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        res = []
        
        i = 0

        while i < len(intervals):
            
            start = intervals[i]

            while i + 1 < len(intervals) and intervals[i+1][0] <= start[1]:
                if start[1] < intervals[i + 1][1]:
                    start[1] = intervals[i + 1][1]
                i += 1

            if i + 1 < len(intervals) and intervals[i+1][0] <= start[1]:
                res.append([start[0], intervals[i+1][1]])
                i += 1
            else:
                res.append([start[0], start[1]]) 

            i += 1
        
        return res
                    
