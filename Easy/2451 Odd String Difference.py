# https://leetcode.com/problems/odd-string-difference/description/


class Solution:
    def oddString(self, words: List[str]) -> str:

        dictx = { "a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7,
        "i": 8,"j": 9,"k": 10,"l": 11,"m": 12,"n": 13,"o": 14,"p": 15,
        "q": 16,"r": 17,"s": 18,"t": 19,"u": 20,"v": 21,"w": 22,"x": 23,
        "y": 24,"z": 25}

        value = {}

        for each in words:
            temp = []
            index = ""
            for i in range(0, len(each)-1):
                index +=  str(dictx[each[i+1]] - dictx[each[i]]) 
                temp.append(index)
            temp =  "".join(temp)
            if temp not in value:
                value[temp] = [each]
            else:
                value[temp].append(each)

        for key, value in value.items():
            if len(value) == 1:
                return value[0]
