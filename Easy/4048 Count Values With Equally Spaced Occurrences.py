# https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/description/


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:

        dictx = {}
        count = 0

        for i in range(0, len(nums)):
            if nums[i] not in dictx.keys():
                dictx[nums[i]] = [[i],1]
            else:
                dictx[nums[i]][0].append(i)
                dictx[nums[i]][1] += 1
        
        for key, value in dictx.items():
            res_pos = []
            if value[1] == 3:
                temp = value[0]
                for i in range(0, 2):
                    res_pos.append(temp[i+1] - temp[i])

            if len(set(res_pos)) == 1:
                count += 1

        return count
