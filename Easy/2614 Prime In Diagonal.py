# https://leetcode.com/problems/prime-in-diagonal/

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        m = len(nums)
        n = len(nums[0])
        l = 0
        r = 0
        dictx = {}

        prime = 0

        while (l < m and r < n):

            temp = nums[l][r]
            flag = True

            if temp not in dictx:
                for i in range(2, int(temp**0.5)+1):
                    if temp % i == 0:
                        flag = False
                        break
                dictx[temp] = 1
            
                if flag and temp > prime:
                    prime = temp

            l += 1
            r += 1

        l = 0
        r = n-1

        while (l < m and r > -1):

            temp = nums[l][r]
            flag = True

            if temp not in dictx:
                for i in range(2, int(temp**0.5)+1):
                    if temp % i == 0:
                        flag = False
                        break
                dictx[temp] = 1
            
                if flag and temp > prime:
                    prime = temp

            l += 1
            r -= 1
        if prime == 1:
            return 0
        return prime

