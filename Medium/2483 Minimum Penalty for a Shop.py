# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:

        penalty = customers.count("Y")
        global_penalty = penalty
        close_index = 0

        for i in range(1, len(customers)+1):
            if customers[i-1] == "Y":
                penalty -= 1
                if global_penalty > penalty:
                    global_penalty = penalty
                    close_index = i
            else:
                penalty += 1
                if global_penalty > penalty:
                    global_penalty = penalty
                    close_index = i

        return close_index
