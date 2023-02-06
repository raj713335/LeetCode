# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:


        while k > 0:

            maxi = 0
            index = -1
            for i in range(0, len(gifts)):
                if gifts[i] > maxi:
                    maxi = gifts[i]
                    index = i
            gifts[index] = int(gifts[index]**0.5)

            k -= 1
        return sum(gifts)
