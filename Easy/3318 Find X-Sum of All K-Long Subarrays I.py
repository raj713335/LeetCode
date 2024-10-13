# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        res = []

        for i in range(0, len(nums)-k+1):

            dictx = {}
            
            for each in sorted(nums[i:i+k], reverse=True):
                if each not in dictx.keys():
                    dictx[each] = 1
                else:
                    dictx[each] += 1

            keys = sorted(list(dictx.items()), key = lambda x: x[1], reverse=True)

            temp = 0

            for j in range(0, x):
                try:
                    temp += keys[j][0]*keys[j][1]
                except:
                    temp += 0
            
            res.append(temp)

        return res
