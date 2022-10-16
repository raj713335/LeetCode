# https://leetcode.com/problems/find-players-with-zero-or-one-losses/submissions/


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        dictx = {}
        
        for match in matches:
            if match[0] not in dictx:
                dictx[match[0]] = [1, 0]
            else:
                dictx[match[0]][0] += 1
                
            if match[1] not in dictx:
                dictx[match[1]] = [0, -1]
            else:
                dictx[match[1]][1] -= 1
                
        result = [[], []]
        
        
        for each in dictx.items():
            if each[1][1] == 0:
                result[0].append(each[0])
            if each[1][1] == -1:
                result[1].append(each[0])
        
        result[0] = sorted(result[0])
        result[1] = sorted(result[1])
      
        return result
                
        
