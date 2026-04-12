# https://leetcode.com/problems/find-the-degree-of-each-vertex/description/

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:

        res = []

        for each in matrix:
            res.append(sum(each))

        return res
        
