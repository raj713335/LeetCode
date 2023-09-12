# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/


class Solution:
    def minDeletions(self, s: str) -> int:

        dictx = {}
        listx = []
        count = 0

        for i in range(0, len(s)):
            if s[i] not in dictx:
                dictx[s[i]] =  1
            else:
                dictx[s[i]] += 1

        for key, values in dictx.items():
            listx.append([key, values])
        
        listx = sorted(listx, key = lambda x : x[1], reverse = True)

        for i in range(1, len(listx)):
            if listx[i][1] >= listx[i-1][1]:
                diff = abs(listx[i-1][1] - listx[i][1])

                if listx[i][1] - (diff + 1) >= 0:
                    listx[i][1] -= diff + 1
                    count += diff + 1
                else:
                    count += listx[i][1]
                    listx[i][1] = 0

        return count
