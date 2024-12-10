# https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150

import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dictx = {}
        temp_dictx = {}

        for each in t:
            if each not in dictx.keys():
                dictx[each] = 1
                temp_dictx[each] = 0
            else:
                dictx[each] += 1

        have, need = 0, len(dictx.values())

        min_length, j = math.inf, 0
        res_string = ""
        res = ""
        flag = False

        for i in range(0, len(s)):
            if have != need:
                res_string += s[i]
                if s[i] in temp_dictx:
                    temp_dictx[s[i]] += 1
                    if temp_dictx[s[i]] == dictx[s[i]]:
                        have += 1

            while have == need and j <= i:
                if s[j] in temp_dictx:
                    temp_dictx[s[j]] -= 1
                    if temp_dictx[s[j]] < dictx[s[j]]:
                        have -= 1
                res_string = res_string[1:]
                j += 1
                flag = True


            if flag:
                temp = s[j-1] + res_string
                if min_length > len(temp) and s[j - 1] in temp_dictx.keys() and temp_dictx[s[j - 1]] + 1 == dictx[s[j - 1]]:
                    min_length = len(temp)
                    res = temp

            flag = False

        return res
                
