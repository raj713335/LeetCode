# https://leetcode.com/problems/library-late-fee-calculator/description/

class Solution:
    def lateFee(self, daysLate: List[int]) -> int:

        penalty = 0

        for i in range(0, len(daysLate)):
            if daysLate[i] == 1:
                penalty += 1
            elif daysLate[i] >= 2 and daysLate[i] <= 5:
                penalty += 2 * daysLate[i]
            else:
                penalty += 3 * daysLate[i]

        return penalty
        
