# https://leetcode.com/problems/count-valid-prefixes/description/

class Solution:
    def countValidPrefixes(self, s: str) -> int:

        count = 0

        count_1 = 0
        count_0 = 0

        for i in range(0, len(s)):
            if s[i] == "0":
                count_0 += 1
            else:
                count_1 += 1

            if count_0 == count_1 - 1:
                count += 1
            elif count_0 - 1 == count_1:
                count += 1
            elif count_0 == count_1:
                count += 1

        return count
        
