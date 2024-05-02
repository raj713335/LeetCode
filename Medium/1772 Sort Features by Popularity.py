# https://leetcode.com/problems/sort-features-by-popularity/description/

class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:

        dictx = {}

        for each in features:
            dictx[each] = 0

        for each in responses:
            for val in set(list(map(str, each.split(" ")))):
                if val in dictx:
                    dictx[val] += 1

        dictx = sorted(dictx.items(), key = lambda x: x[1], reverse=True)

        ans = []

        for each in dictx:
            ans.append(each[0])

        return ans

        
