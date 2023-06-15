# https://leetcode.com/problems/find-the-losers-of-the-circular-game/description/

import math

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        nn = []
        for i in range(0, n):
            nn.append(i+1)

        n = nn

        friends_recived = [1]
        initial = 0
        length = len(n)
        loosers = []

        for i in range(1, 1000):
            print(friends_recived)
            initial = (initial + k*i) % length
            if n[initial] not in friends_recived:
                friends_recived.append(n[initial])
            else:
                break


        for i in range(0, len(n)):
            if n[i] not in friends_recived:
                loosers.append(n[i])

        return loosers

        
            
