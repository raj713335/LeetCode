# https://leetcode.com/problems/elevator-requests-i/description/

class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:

        sumx = abs(0 - requests[0])

        for i in range(1, len(requests)):
            sumx += abs(requests[i-1] - requests[i])

        return sumx


        
