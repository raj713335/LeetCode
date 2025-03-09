# https://leetcode.com/problems/fruits-into-baskets-ii/description/

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        dictx = {basket: False for basket in range(0, len(baskets))}

        for fruit in fruits:
            for basket in range(0, len(baskets)):
                if fruit <= baskets[basket] and dictx[basket] == False:
                    dictx[basket] = True
                    break

        count = 0

        for key, value in dictx.items():
            if value == False:
                count += 1

        return count
        
