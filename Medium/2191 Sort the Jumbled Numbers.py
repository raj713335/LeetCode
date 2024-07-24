# https://leetcode.com/problems/sort-the-jumbled-numbers/description/?envType=daily-question&envId=2024-07-24


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        dictx = {}

        for i in range(0, 10):
            dictx[str(i)] = str(mapping[i])

        res = []

        for each in nums:
            temp = ""
            for k in str(each):
                temp += dictx[k]
            res.append([int(temp), each])

        res = sorted(res, key= lambda x: x[0])

        output = []

        for each in res:
            output.append(each[1])

        return output

        
