# https://leetcode.com/problems/minimum-operations-to-collect-elements/description/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        numsx = [x for x in range(1, k+1)]

        count = k

        for i in range(len(nums)-k, -1, -1):
            num1 = sorted(list(set(nums[i:])))[:k]

            if num1 == numsx:
                return count 
            else:
                count += 1


        
