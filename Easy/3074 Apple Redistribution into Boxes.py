# https://leetcode.com/problems/apple-redistribution-into-boxes/description/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        count = 0
        apple_sumx = sum(apple)

        capacity = sorted(capacity, reverse=True)

        for i in range(0, len(capacity)):
            if apple_sumx <= 0:
                return count
            else:
                apple_sumx -= capacity[i]
                count += 1

        return count
        
