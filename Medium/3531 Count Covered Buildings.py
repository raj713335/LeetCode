# https://leetcode.com/problems/count-covered-buildings/description/

from collections import defaultdict
import bisect

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        row_map = defaultdict(list)
        col_map = defaultdict(list)

        for x, y in buildings:
            row_map[x].append(y)
            col_map[y].append(x)

        # Sort each row and column list
        for key in row_map:
            row_map[key].sort()
        for key in col_map:
            col_map[key].sort()

        count = 0
        for x, y in buildings:
            # Find left and right in row
            y_list = row_map[x]
            idx = bisect.bisect_left(y_list, y)
            has_left = idx > 0
            has_right = idx < len(y_list) - 1

            # Find above and below in column
            x_list = col_map[y]
            idx2 = bisect.bisect_left(x_list, x)
            has_above = idx2 > 0
            has_below = idx2 < len(x_list) - 1

            if has_left and has_right and has_above and has_below:
                count += 1

        return count
