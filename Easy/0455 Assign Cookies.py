# https://leetcode.com/problems/assign-cookies/description/


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g = sorted(g)

        s = sorted(s)

        count = 0

        for each in g:        
            for i in range(0, len(s)):
                if s[i] >= each:
                    count += 1
                    del s[i]
                    break

        return count
        
