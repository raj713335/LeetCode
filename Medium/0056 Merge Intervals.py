# https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        ptr = 1
        output = []
        
        temp = intervals[0]
        
        while ptr < len(intervals):
            if intervals[ptr][0] <= temp[1]:
                if intervals[ptr][1] <= temp[1]:
                    ptr += 1
                else:
                    temp = [temp[0], intervals[ptr][1]]
                    ptr += 1
            else:
                output.append(temp)
                temp = intervals[ptr]
                ptr += 1
                
        output.append(temp)
        
        return output
                    
