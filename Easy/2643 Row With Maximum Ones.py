# https://leetcode.com/problems/row-with-maximum-ones/description/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        max_count = 0
        row_index = 0


        for i in range(0, len(mat)):
            temp = mat[i].count(1)
            if temp > max_count:
                max_count = temp
                row_index = i

        return [row_index, max_count]
