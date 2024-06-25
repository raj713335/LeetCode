# https://leetcode.com/problems/grumpy-bookstore-owner/description/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        base_sum = 0

        for i in range(0, len(grumpy)):
            if grumpy[i] == 0:
                base_sum += customers[i]

        max_sum = 0
        count = 0

        for i in range(0, minutes):
            if grumpy[i] == 1:
                count += customers[i]

        if count > max_sum:
            max_sum = count

        for i in range(minutes, len(grumpy)):
            if grumpy[i-minutes] == 1:
                count -= customers[i-minutes]
            if grumpy[i] == 1:
                count += customers[i]

            if count > max_sum:
                max_sum = count

        return base_sum + max_sum


        
