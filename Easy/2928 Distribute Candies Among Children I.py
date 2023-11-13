# https://leetcode.com/problems/distribute-candies-among-children-i/description/


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        count = 0

        for i in range(0, limit+1):
            for j in range(0, limit+1):
                for k in range(0, limit+1):
                    if (i + j + k) == n:
                        count += 1

        return count 
        
