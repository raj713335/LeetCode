# https://leetcode.com/problems/minimum-moves-to-reach-target-score/description/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        s = target
        count = 0
        doubles = maxDoubles

        if maxDoubles  == 0:
            return s-1

        while s != 1:
            if s % 2 == 0:
                if doubles > 0:
                    s = s//2
                    count += 1
                    doubles -= 1
                else:
                    count += (s-1)
                    return count
                    
            else:
                s -= 1
                count += 1

        return count
        
