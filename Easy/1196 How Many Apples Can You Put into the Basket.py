# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/description/

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        weight = sorted(weight)

        length = len(weight)
        index = 0
        maxi = 5000

        while maxi > 0 and index < length:
            maxi -= weight[index]
            if maxi >= 0:
                index += 1

        return index 
        
