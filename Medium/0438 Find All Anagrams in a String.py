# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/


import copy

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        dictx = {}

        res = []

        len_p = len(p)

        if len(s) < len_p:
            return []

        for each in p:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        temp_dictx = {}

        for i in range(0, len_p):
            if s[i] not in temp_dictx:
                temp_dictx[s[i]] = 1
            else:
                temp_dictx[s[i]] += 1

        flag = True
        for each in dictx.keys():
            try:
                if dictx[each] != temp_dictx[each]:
                    flag = False
            except:
                flag = False

        if flag:
            res.append(0)


        for i in range(1, len(s)-len_p+1):
            temp_dictx[s[i-1]] -= 1
            if s[i+len(p)-1] not in temp_dictx:
                temp_dictx[s[i+len_p-1]] = 1
            else:
                temp_dictx[s[i+len_p-1]] += 1

            flag = True
            for each in dictx.keys():
                try:
                    if dictx[each] != temp_dictx[each]:
                        flag = False
                except:
                    flag = False

            if flag:
                res.append(i)

        return res
        
