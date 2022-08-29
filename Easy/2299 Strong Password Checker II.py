# https://leetcode.com/problems/strong-password-checker-ii/


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False
        
        lower = False
        upper = False
        digit = False
        special = False
        special_charcters = "!@#$%^&*()-+"
        
        prev = ""
        
        for i in range(0, len(password)):
            if prev == password[i]:
                return False
            elif password[i].isnumeric():
                digit = True
            elif password[i].isupper():
                upper = True
            elif password[i].islower():
                lower = True
            elif password[i] in special_charcters:
                special = True
            prev = password[i]
            
        
        if lower and upper and digit and special:
            return True
        return False
        
