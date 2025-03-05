# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        res = []
        index = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):

                heapq.heappush(res, -matrix[i][j])
                index += 1

                if index > k:
                    heapq.heappop(res)

        return -res[0]
        
