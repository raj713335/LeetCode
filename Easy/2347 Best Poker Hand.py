# https://leetcode.com/problems/best-poker-hand/description/


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        setx = set(suits)
        if len(setx) == 1:
            return "Flush"
        
        dictx = {}

        for i in range(0, len(ranks)):
            if ranks[i] not in dictx:
                dictx[ranks[i]] = 1
            else:
                dictx[ranks[i]] += 1

        flag_three = False
        flag_pair = False

        for key, val in dictx.items():
            if val >= 3:
                flag_three = True
                break
            elif val == 2:
                flag_pair = True

        if flag_three:
            return "Three of a Kind"
        if  flag_pair:
            return "Pair"

        return "High Card"
        
