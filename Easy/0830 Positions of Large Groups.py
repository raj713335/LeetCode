# https://leetcode.com/problems/positions-of-large-groups/description/


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        res = []

        last = 0

        prev = ""
        count = 0

        for i in range(0, len(s)):
            if s[i] != prev:
                if count >= 3:
                    res.append([last, i-1])
                last = i
                prev = s[i]
                count = 1
            else:
                count += 1

        if count >= 3:
            res.append([last, i])


        return res


