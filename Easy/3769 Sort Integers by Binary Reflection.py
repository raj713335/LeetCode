# https://leetcode.com/problems/sort-integers-by-binary-reflection/description/

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:

        res = []

        for each in nums:
            temp = bin(each)
            temp = temp[2:][::-1]
            temp = int(temp, 2)

            res.append([each, temp])

        res = sorted(res, key=lambda x: (x[1], x[0]))

        output = []

        for key, val in res:
            output.append(key)

        return output
        
