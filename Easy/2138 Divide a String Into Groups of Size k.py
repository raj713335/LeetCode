# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        res = []

        for i in range(0, len(s), k): 
            temp = s[i:i+k]
            if len(temp) != k:
                temp += (fill * k)

            res.append(temp[:k])

        return res
