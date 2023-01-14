# https://leetcode.com/problems/license-key-formatting/description/


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.split("-")

        rem = ""
        res = ""

        i = len(s)-1
        while i > -1 or len(rem) >= k:

            if len(rem) >= k:
                res = rem[-k:].upper() + "-" + res
                rem = rem[:-k]
                continue
            else:
                rem = s[i] + rem
                i -= 1

        print(res)

        res =  rem.upper() +"-" + res

        try:
            if res[0] == "-":
                res = res[1:]
            if res[-1] == "-":
                res = res[:-1]
        except:
            pass

        return res

        


        
