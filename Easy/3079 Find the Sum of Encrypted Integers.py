# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        sumx = 0

        for i in range(0, len(nums)):
            length = len(str(nums[i]))
            maxi = 0
            for each in str(nums[i]):
                if int(each) > maxi:
                    maxi = int(each)

            nums[i] = int(str(maxi) * length)
            sumx += nums[i]

        return sumx
