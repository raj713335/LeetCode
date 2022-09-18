# https://leetcode.com/problems/time-needed-to-buy-tickets/


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        num_seconds = 0
        
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0 and tickets[k] > 0:
                    tickets[i] -= 1
                    num_seconds += 1

        return num_seconds
        
