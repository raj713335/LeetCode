# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/


class Solution:
    def getSmallestString(self, s: str) -> str:
        
        res = [s]

        for i in range(0, len(s)-1):
            temp = list(s)
            if int(temp[i]) % 2 == 0 and int(temp[i+1]) % 2 == 0:
                temp[i], temp[i+1] = temp[i+1], temp[i]
                res.append("".join(temp))
            elif int(temp[i]) % 2 != 0 and int(temp[i+1]) % 2 != 0:
                temp[i], temp[i+1] = temp[i+1], temp[i]
                res.append("".join(temp))

        return sorted(res)[0]
