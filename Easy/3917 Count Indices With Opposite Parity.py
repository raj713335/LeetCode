# https://leetcode.com/problems/count-indices-with-opposite-parity/description/

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:

        length = len(nums)
        output = [[0, 0]] * length


        for i in range(length-1, 0, -1):
            if nums[i] % 2 == 0:
                output[i-1] = [output[i][0] + 1, output[i][1]]
            else:
                output[i-1] = [output[i][0], output[i][1] + 1]

        res = []

        for i in range(0, length):
            if nums[i] % 2 == 0:
                res.append(output[i][1])
            else:
                res.append(output[i][0])

        return res
        
