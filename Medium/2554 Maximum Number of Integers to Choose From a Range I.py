# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned = sorted(set(banned))

        i = 0
        k = 0
        sumx = 0

        for j in range(1, n+1):
            try:
                if j != banned[i]:
                    sumx += j
                    if sumx <= maxSum:
                        k += 1
                    else:
                        return k 
                else:
                    i += 1
            except:
                sumx += j
                if sumx <= maxSum:
                    k += 1
                else:
                    return k 

        return k

        
