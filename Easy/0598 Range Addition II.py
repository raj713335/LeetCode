# https://leetcode.com/problems/range-addition-ii/description/


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        if ops == []:
            return m*n   

        max_m = math.inf
        max_n = math.inf

        for each in ops:
            max_m = min(max_m, each[0])
            max_n = min(max_n, each[1])


        return max_m * max_n
        
