# https://leetcode.com/problems/check-distances-between-same-letters/description/


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        dictx = { "a": [-1, 0],"b": [-1, 1],"c": [-1, 2],"d": [-1, 3],"e": [-1, 4],"f": [-1, 5],"g": [-1, 6],"h": [-1, 7],
        "i": [-1, 8],"j": [-1,9],"k": [-1, 10],"l": [-1, 11],"m": [-1, 12],"n": [-1, 13],"o": [-1, 14],"p": [-1, 15],
        "q": [-1, 16],"r": [-1, 17],"s": [-1, 18],"t": [-1, 19],"u": [-1, 20],"v": [-1, 21],"w": [-1, 22],"x": [-1, 23],
        "y": [-1, 24],"z": [-1, 25]}


        for i in range(0, len(s)):
            
            if dictx[s[i]][0] == -1:
                dictx[s[i]][0] = i
            else:
                if i - dictx[s[i]][0]-1 == distance[dictx[s[i]][1]]:
                    dictx[s[i]][0] = i
                else:
                    return False

        return True

        
