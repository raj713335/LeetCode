# https://leetcode.com/problems/valid-number/description/

class Solution:
    def isNumber(self, s: str) -> bool:

        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            before, after = s.split('.', 1)
            if not before and not after:
                return False
            if before and not before.isdigit():
                return False
            if after and not after.isdigit():
                return False
            return True

        s = s.strip()
        if 'e' in s or 'E' in s:
            base, _, exp = s.partition('e') if 'e' in s else s.partition('E')
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        return isInteger(s) or isDecimal(s)
        
