# https://leetcode.com/problems/sort-the-people/


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        dictx = {}
        
        for i in range(0, len(names)):
            dictx[heights[i]] = names[i]
            
            
        dictx = sorted(dictx.items(), key=lambda x: x[0], reverse = True)
        
        people = []
        
        for each in dictx:
            people.append(each[1])
            
        return people
        
