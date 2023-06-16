# https://leetcode.com/problems/minimize-string-length/description/


class Solution:
    def minimizedStringLength(self, s: str) -> int:

        s = set(s)

        return len(s)
