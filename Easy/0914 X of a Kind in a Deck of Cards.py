# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/


import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        dictx = {}

        for i in range(0, len(deck)):
            if deck[i] not in dictx.keys():
                dictx[deck[i]] = 1
            else:
                dictx[deck[i]] += 1

        set_dictx = list(dictx.values())

        if math.gcd(*set_dictx) > 1:
            return True
        else:
            return False
        
