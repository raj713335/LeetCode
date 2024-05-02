# https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/description/


class Solution:
    def isDecomposable(self, s: str) -> bool:

        prev = s[0]
        count = 1
        flag = True
        
        for i in range(1, len(s)):
            if s[i] == prev:
                count += 1
                if count > 3:
                    count = 1
                    prev = s[i]
            else:
                if count == 1:
                    return False
                elif count == 2:
                    if flag:
                        flag = False
                    else:
                        return False

                count = 1
                prev = s[i]

        if count == 2:
            if flag:
                flag = False
            else:
                return False
        elif count > 3:
            count = count % 3
            if count == 2:
                if flag:
                    flag = False
                else:
                    return False
            else:
                return False
        elif count == 1:
            return False

        if flag:
            return False
        else:
            return True


        
