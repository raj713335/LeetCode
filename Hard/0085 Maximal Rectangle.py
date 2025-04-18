# https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        n_cols = len(matrix[0])
        heights = [0] * n_cols
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  # Sentinel
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            heights.pop()
            return max_area

        for row in matrix:
            for i in range(n_cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
        
