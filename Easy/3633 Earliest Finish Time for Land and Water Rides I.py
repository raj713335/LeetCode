# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        mx = lambda x, y: x if x > y else y
        mn = lambda x, y: x if x < y else y

        land1st = reduce(mn, map(add, landStartTime , landDuration ))  # <--1
        watr1st = reduce(mn, map(add, waterStartTime, waterDuration))

        waterStartTime = [mx(t, land1st) for t in waterStartTime]      # <--2
        landStartTime  = [mx(t, watr1st) for t in landStartTime ]
        
        land1st = reduce(mn, map(add, landStartTime , landDuration ))  # <--3
        watr1st = reduce(mn, map(add, waterStartTime, waterDuration))
        
        return mn(land1st, watr1st)
        
