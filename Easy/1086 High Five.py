# https://leetcode.com/problems/high-five/description/

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        dictx = {}

        for each in items:
            if each[0] not in dictx:
                dictx[each[0]] = [each[1]]
            else:
                dictx[each[0]].append(each[1])

        print(dictx)

        ans = []

        for key, value in dictx.items():
            scores = sorted(value, reverse=True)[:5]
            scores = sum(scores)//5
        
            ans.append([key, scores])

        return sorted(ans)
        
