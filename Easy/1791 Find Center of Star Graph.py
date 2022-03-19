# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dictx = {}
        for each in edges:
            if each[0] not in dictx:
                dictx[each[0]] = 1
            else:
                dictx[each[0]] += 1
            if each[1] not in dictx:
                dictx[each[1]] = 1
            else:
                dictx[each[1]] += 1
        star = 0
        value = 0
        for key,val in dictx.items():
            if value < val:
                star = key
                value = val

        return star
                
