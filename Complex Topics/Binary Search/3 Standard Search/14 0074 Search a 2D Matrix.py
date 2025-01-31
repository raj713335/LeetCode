# https://leetcode.com/problems/search-a-2d-matrix/description/


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            row = (top + bottom ) // 2

            if matrix[row][0] > target:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        if top > bottom:
            return False

        l, r = 0, len(matrix[0])

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
