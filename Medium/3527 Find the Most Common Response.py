# https://leetcode.com/problems/find-the-most-common-response/description/

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        dictx = {}
        res = []

        for words in responses:
            values = set()
            for each in words:
                if each not in dictx:
                    values.add(each)
                    dictx[each] = 1
                elif each not in values:
                    dictx[each] += 1
                    values.add(each)

        mx_length = 0
        for key, value in dictx.items():
            if value > mx_length:
                mx_length = value
                res = []
                res.append(key)
            elif value == mx_length:
                res.append(key)

        res = sorted(res)
        return res[0]
                
        
