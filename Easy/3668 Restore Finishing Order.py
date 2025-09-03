# https://leetcode.com/problems/restore-finishing-order/description/

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        dictx = {}

        for each in friends:
            dictx[each] = 1

        res = []

        for each in order:
            if each in dictx.keys():
                res.append(each)

        return res


        
