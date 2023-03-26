# https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        listx = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes

        return sum(listx[:k])
        
