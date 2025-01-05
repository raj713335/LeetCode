# https://leetcode.com/problems/substring-matching-pattern/description/


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        return bool(search(p.replace('*', '.*'), s))
