# https://leetcode.com/problems/count-substrings-without-repeating-character/description/


class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:

        length = len(s)

        count = length

        for i in range(0, length):
            j = i + 1
            dictx = {}
            dictx[s[i]] = 1
            while j < length:
                if s[j] not in dictx:
                    count += 1
                    dictx[s[j]] = 1
                    j += 1
                else:
                    break

        return count
        
