# https://leetcode.com/problems/find-the-least-frequent-digit/description/

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        dictx = {}

        for di in str(n):
            if di in dictx.keys():
                dictx[di] += 1
            else:
                dictx[di] = 1

        smallest_digit = []
        frequency = math.inf

        for key, value in dictx.items():
            if value < frequency:
                smallest_digit = [key]
                frequency = value
            elif value == frequency:
                smallest_digit.append(key)

        return int(sorted(smallest_digit)[0])
        
